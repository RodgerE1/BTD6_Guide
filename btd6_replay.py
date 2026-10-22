"""
btd6_replay.py
Unified Replay Engine and Schema Validator for BTD6 Strategy Guides.
Enforces invariant satisfaction across Editor, Database Validator, Radar, and Generator:
1. Type & schema validation (rejecting malformed data gracefully).
2. Deterministic tower replay engine keyed by tower_id.
3. Canonical economic calculations, timing-aware cash curves, and 70% refund accounting.
4. Non-finite / boolean numeric rejection.
5. Strict tactical capability coverage (blimp tiers, ceramic CC, hero arrival tracking).
"""

import math
from btd6_economy import (
    ALL_VALID_TOWERS,
    CANONICAL_HEROES,
    CANONICAL_TOWERS,
    DIFF_MULTIPLIERS,
    get_action_canonical_cost,
    get_cash_available,
    get_cumulative_cash_ceiling,
    get_hero_level_at_round,
    get_starting_cash,
    get_tower_capabilities,
    get_transition_cost,
    is_legal_crosspath,
    is_valid_numeric_cost,
    parse_upgrade,
)


PHASE_ORDER = {
    "before_round": 0,
    "during_round": 1,
    "after_round": 2
}


class TowerInstance:
    """Represents an active or historical tower instance on the tactical board."""
    def __init__(self, tower_id, tower_name, upgrade_tuple, upg_str, placed_round, placement="Center", targeting="First", initial_cost=0, is_hero=False, placed_timing="before_round"):
        self.tower_id = tower_id
        self.tower_name = tower_name
        self.upgrade = upgrade_tuple or (0, 0, 0)
        self.upg_str = upg_str or "0-0-0"
        self.placed_round = placed_round
        self.placed_timing = placed_timing
        self.placement = placement
        self.targeting = targeting
        self.total_invested = initial_cost
        self.is_hero = is_hero
        self.is_active = True
        self.sold_round = None
        self.sold_timing = None
        self.upgrade_history = [(placed_round, placed_timing, self.upgrade, self.upg_str)]

    def get_upgrade_at_round(self, at_round, at_timing="during_round"):
        """Returns the upgrade tuple this tower possessed at or before (at_round, at_timing)."""
        target_phase = (at_round, PHASE_ORDER.get(at_timing, 1))
        effective_upg = (0, 0, 0)
        for r, timing, upg_tup, _ in self.upgrade_history:
            if (r, PHASE_ORDER.get(timing, 0)) <= target_phase:
                effective_upg = upg_tup
        return effective_upg

    def is_present_at_round(self, at_round, at_timing="during_round"):
        """Returns True if the tower was placed by (at_round, at_timing) and not sold by then."""
        target_phase = (at_round, PHASE_ORDER.get(at_timing, 1))
        placed_phase = (self.placed_round, PHASE_ORDER.get(self.placed_timing, 0))
        if placed_phase > target_phase:
            return False
        if self.sold_round is not None:
            sold_phase = (self.sold_round, PHASE_ORDER.get(self.sold_timing or "before_round", 0))
            if sold_phase <= target_phase:
                return False
        return True

    def __repr__(self):
        return f"<TowerInstance id={self.tower_id} name={self.tower_name} upg={self.upg_str} invested={self.total_invested}>"


class TowerReplayEngine:
    """
    Stateful replay engine simulating gameplay board transitions step-by-step.
    Tracks active towers keyed by tower_id, canonical expenditures, refunds, and tactical buffs.
    All transitions are strictly transactional: failed transitions leave board state untouched.
    """
    def __init__(self, difficulty="Medium", start_round=1, max_round=60, monkey_knowledge=False,
                 more_starting_cash=None, free_dart_monkey=None):
        self.difficulty = difficulty
        self.start_round = start_round
        self.max_round = max_round
        is_chimps = (difficulty == "CHIMPS")
        self.monkey_knowledge = bool(monkey_knowledge and not is_chimps)

        if more_starting_cash is not None:
            self.more_starting_cash = bool(more_starting_cash and not is_chimps)
        else:
            self.more_starting_cash = self.monkey_knowledge

        if free_dart_monkey is not None:
            self.free_dart_monkey = bool(free_dart_monkey and not is_chimps)
        else:
            self.free_dart_monkey = self.monkey_knowledge

        self.free_dart_used = False
        self.active_towers = {}         # tower_id -> TowerInstance
        self.all_towers = {}            # tower_id -> TowerInstance (includes sold)
        self.tower_counters = {}        # tower_name -> int count
        self.cumulative_cost_spent = 0
        self.cumulative_refunds = 0
        self.opening_cost = 0
        self.has_opening_defense = False
        self.last_round = start_round
        self.last_timing = "before_round"
        self.has_committed_step = False
        self.step_history = []
        self.errors = []
        self.warnings = []

    def _generate_tower_id(self, tower_name, explicit_id=None):
        if explicit_id:
            return str(explicit_id)
        clean_name = tower_name.lower().replace(" ", "_")
        cnt = self.tower_counters.get(tower_name, 0) + 1
        cand_id = f"{clean_name}_{cnt}"
        while cand_id in self.all_towers:
            cnt += 1
            cand_id = f"{clean_name}_{cnt}"
        self.tower_counters[tower_name] = cnt
        return cand_id

    def _find_tower_for_upgrade(self, tower_name, explicit_id=None, upg_tuple=None, placement=None):
        if explicit_id:
            if explicit_id not in self.active_towers:
                return None, f"references nonexistent or inactive tower_id '{explicit_id}'."
            cand = self.active_towers[explicit_id]
            if cand.tower_name != tower_name:
                return None, f"tower_id '{explicit_id}' is a '{cand.tower_name}', not a '{tower_name}'."
            return cand, None

        candidates = [t for t in self.active_towers.values() if t.tower_name == tower_name]
        if not candidates:
            return None, f"upgrading '{tower_name}' which was never placed on the board!"

        # If placement specified and matches uniquely
        if placement:
            placement_matches = [t for t in candidates if t.placement and t.placement.strip() == placement.strip()]
            if len(placement_matches) == 1:
                return placement_matches[0], None

        # Match candidate that is a valid upgrade progression (tiers >= existing)
        if upg_tuple:
            valid_prog = [t for t in candidates if all(u >= e for u, e in zip(upg_tuple, t.upgrade))]
            if valid_prog:
                # Sort descending by sum of existing tiers to upgrade the tower already furthest along this path
                valid_prog.sort(key=lambda t: sum(t.upgrade), reverse=True)
                return valid_prog[0], None

        return candidates[0], None

    def _find_tower_for_sale(self, tower_name, explicit_id=None):
        if explicit_id:
            if explicit_id not in self.active_towers:
                return None, f"references nonexistent or inactive tower_id '{explicit_id}'."
            cand = self.active_towers[explicit_id]
            if cand.tower_name != tower_name:
                return None, f"tower_id '{explicit_id}' is a '{cand.tower_name}', not a '{tower_name}'."
            return cand, None

        candidates = [t for t in self.active_towers.values() if t.tower_name == tower_name]
        if not candidates:
            return None, f"selling unplaced tower '{tower_name}'!"
        return candidates[0], None

    def apply_step(self, step, step_index=0):
        """
        Applies a single strategy step to the replay state.
        Returns: (success: bool, error_msg: str or None)
        """
        # 1. Container and Field Type Validation
        if not isinstance(step, dict):
            err = f"steps[{step_index}] must be a JSON dictionary object, found {type(step).__name__}."
            self.errors.append(err)
            return False, err

        s_num = step.get("step_number", step_index + 1)
        if not isinstance(s_num, int) or isinstance(s_num, bool):
            err = f"steps[{step_index}].step_number must be an integer, found {type(s_num).__name__}."
            self.errors.append(err)
            return False, err

        r = step.get("round")
        if not isinstance(r, int) or isinstance(r, bool):
            err = f"Step {s_num}: steps[{step_index}].round must be an integer, found {type(r).__name__}."
            self.errors.append(err)
            return False, err

        if not (self.start_round <= r <= self.max_round):
            err = f"Step {s_num}: round {r} outside legal range [{self.start_round}, {self.max_round}]."
            self.errors.append(err)
            return False, err

        timing = step.get("timing", "before_round")
        if timing not in ("before_round", "during_round", "after_round"):
            err = f"Step {s_num}: timing '{timing}' must be one of 'before_round', 'during_round', 'after_round'."
            self.errors.append(err)
            return False, err

        if self.has_committed_step:
            if r < self.last_round:
                err = f"Step {s_num}: round {r} regressed from previous round {self.last_round}."
                self.errors.append(err)
                return False, err
            if r == self.last_round and PHASE_ORDER.get(timing, 0) < PHASE_ORDER.get(self.last_timing, 0):
                err = f"Step {s_num}: timing '{timing}' regressed from previous timing '{self.last_timing}' in Round {r}."
                self.errors.append(err)
                return False, err

        act = step.get("action")
        if not isinstance(act, str) or act not in ("Place", "Upgrade", "Target", "Ability", "Sell"):
            err = f"Step {s_num}: invalid action '{act}'. Allowed: Place, Upgrade, Target, Ability, Sell."
            self.errors.append(err)
            return False, err

        tower_raw = step.get("tower")
        if not isinstance(tower_raw, str) or not tower_raw.strip():
            err = f"Step {s_num}: steps[{step_index}].tower must be a non-empty string, found {type(tower_raw).__name__}."
            self.errors.append(err)
            return False, err
        tower = tower_raw.strip()

        upg_raw = step.get("upgrade", "0-0-0")
        if not isinstance(upg_raw, str):
            err = f"Step {s_num}: steps[{step_index}].upgrade must be a string, found {type(upg_raw).__name__}."
            self.errors.append(err)
            return False, err
        upg_str = upg_raw.strip()
        upg_tuple = parse_upgrade(upg_str)

        cost_val = step.get("cost_estimate", 0)
        if not is_valid_numeric_cost(cost_val):
            err = f"Step {s_num}: cost_estimate '{cost_val}' must be a finite, non-negative numeric value."
            self.errors.append(err)
            return False, err

        # Detailed string field checks
        explicit_id = step.get("tower_id")
        if explicit_id is not None:
            if not isinstance(explicit_id, str) or not explicit_id.strip():
                err = f"Step {s_num}: tower_id must be a non-empty string, found {type(explicit_id).__name__}."
                self.errors.append(err)
                return False, err
            explicit_id = explicit_id.strip()

        step_id = step.get("step_id")
        if step_id is not None and (not isinstance(step_id, str) or not step_id.strip()):
            err = f"Step {s_num}: step_id must be a non-empty string, found {type(step_id).__name__}."
            self.errors.append(err)
            return False, err

        placement = step.get("placement", "")
        if placement is not None and not isinstance(placement, str):
            err = f"Step {s_num}: placement must be a string, found {type(placement).__name__}."
            self.errors.append(err)
            return False, err
        placement = (placement or "").strip()

        targeting = step.get("targeting", "First")
        if targeting is not None and not isinstance(targeting, str):
            err = f"Step {s_num}: targeting must be a string, found {type(targeting).__name__}."
            self.errors.append(err)
            return False, err
        targeting = (targeting or "First").strip()

        details = step.get("details")
        if details is not None and not isinstance(details, str):
            err = f"Step {s_num}: details must be a string, found {type(details).__name__}."
            self.errors.append(err)
            return False, err

        # 2. Crosspath & Action Upgrades Legality
        if act in ("Place", "Upgrade"):
            if upg_str in ("Various", "None") or upg_tuple is None:
                err = f"Step {s_num}: {act} action requires a concrete legal upgrade path (e.g. '0-0-0', '3-2-0'), found '{upg_str}'."
                self.errors.append(err)
                return False, err
            if not is_legal_crosspath(upg_tuple):
                err = f"Step {s_num}: illegal crosspath '{upg_str}' for {tower}."
                self.errors.append(err)
                return False, err

        # 3. Action Pre-Flight Verification & Transactional Execution
        action_cost = 0
        refund_amount = 0
        target_tower = None
        new_opening_cost = self.opening_cost

        if act == "Place":
            # Exact canonical hero validation (rejects invented heroes like 'Quincy Imaginary Cannon')
            is_hero = tower in CANONICAL_HEROES
            is_valid = tower in ALL_VALID_TOWERS or is_hero
            if not is_valid:
                err = f"Step {s_num}: unrecognized or invented tower '{tower}' cannot be placed."
                self.errors.append(err)
                return False, err

            if explicit_id and explicit_id in self.all_towers:
                err = f"Step {s_num}: duplicate tower_id '{explicit_id}' already placed on the board."
                self.errors.append(err)
                return False, err

            free_dart_eligible = (
                self.free_dart_monkey
                and not self.free_dart_used
                and tower == "Dart Monkey"
                and upg_tuple == (0, 0, 0)
            )
            canon_cost = 0 if free_dart_eligible else get_action_canonical_cost(tower, (0, 0, 0), upg_tuple, "Place", self.difficulty)
            action_cost = canon_cost

            starting_cash_limit = get_starting_cash(self.difficulty, more_starting_cash=self.more_starting_cash)
            if r == self.start_round:
                new_opening_cost += action_cost
                if new_opening_cost > starting_cash_limit:
                    err = f"Step {s_num}: opening cost ${new_opening_cost} exceeds ${starting_cash_limit} starting cash on Round {self.start_round}."
                    self.errors.append(err)
                    return False, err

        elif act == "Upgrade":
            matched, find_err = self._find_tower_for_upgrade(tower, explicit_id, upg_tuple, placement)
            if not matched:
                err = f"Step {s_num}: {find_err}"
                self.errors.append(err)
                return False, err

            if upg_tuple:
                # Check downgrade
                if any(u < e for u, e in zip(upg_tuple, matched.upgrade)):
                    err = f"Step {s_num}: upgrading '{tower}' to {upg_str} drops levels from {matched.upg_str}!"
                    self.errors.append(err)
                    return False, err

                canon_upg_cost = get_action_canonical_cost(tower, matched.upgrade, upg_tuple, "Upgrade", self.difficulty)
                action_cost = canon_upg_cost

            if r == self.start_round:
                new_opening_cost += action_cost
                starting_cash_limit = get_starting_cash(self.difficulty, more_starting_cash=self.more_starting_cash)
                if new_opening_cost > starting_cash_limit:
                    err = f"Step {s_num}: opening cost ${new_opening_cost} exceeds ${starting_cash_limit} starting cash on Round {self.start_round}."
                    self.errors.append(err)
                    return False, err
            target_tower = matched

        elif act == "Sell":
            matched, find_err = self._find_tower_for_sale(tower, explicit_id)
            if not matched:
                err = f"Step {s_num}: {find_err}"
                self.errors.append(err)
                return False, err

            refund_amount = int(round(matched.total_invested * 0.70))
            target_tower = matched

        elif act == "Target":
            if explicit_id:
                if explicit_id not in self.active_towers:
                    err = f"Step {s_num}: targeting command references nonexistent or inactive tower_id '{explicit_id}'."
                    self.errors.append(err)
                    return False, err
                if self.active_towers[explicit_id].tower_name != tower:
                    err = f"Step {s_num}: targeting command references tower_id '{explicit_id}' which is a '{self.active_towers[explicit_id].tower_name}', not a '{tower}'."
                    self.errors.append(err)
                    return False, err
            else:
                has_matching = any(t.tower_name == tower for t in self.active_towers.values())
                if not has_matching:
                    err = f"Step {s_num}: targeting command references unplaced tower '{tower}'."
                    self.errors.append(err)
                    return False, err

        elif act == "Ability":
            hero_on_board = any(t.is_hero for t in self.active_towers.values())
            has_exact = any(t.tower_name == tower for t in self.active_towers.values())

            composite_valid = False
            if "Hero" in tower and hero_on_board:
                sub_tower = tower.replace("& Hero", "").replace("Hero &", "").strip()
                if sub_tower in ("Defense Fleet", "Fleet", "Radar Scanner & Defense", "Crowd Control"):
                    composite_valid = True
                elif any(t.tower_name == sub_tower for t in self.active_towers.values()):
                    composite_valid = True

            if not has_exact and not composite_valid:
                err = f"Step {s_num}: ability command references unplaced or unavailable tower/hero '{tower}'."
                self.errors.append(err)
                return False, err

        # 4. Economic Accounting & Cash Ceilings
        starting_cash_limit = get_starting_cash(self.difficulty, more_starting_cash=self.more_starting_cash)
        if r == self.start_round and (action_cost > starting_cash_limit or int(cost_val) > starting_cash_limit):
            err = f"Step {s_num}: opening cost ${max(action_cost, int(cost_val))} exceeds ${starting_cash_limit} starting cash on Round {self.start_round}."
            self.errors.append(err)
            return False, err

        new_cum_spent = self.cumulative_cost_spent + action_cost
        new_cum_refunds = self.cumulative_refunds + refund_amount
        earned_cash = get_cash_available(self.difficulty, r, timing=timing, more_starting_cash=self.more_starting_cash)
        cash_avail = earned_cash + self.cumulative_refunds

        # Reject if either canonical cumulative spending or declared estimate exceeds available cash
        effective_check_cost = max(new_cum_spent, self.cumulative_cost_spent + int(cost_val))

        if effective_check_cost > cash_avail:
            earned_during = get_cash_available(self.difficulty, r, timing="during_round", more_starting_cash=self.more_starting_cash)
            cash_during = earned_during + self.cumulative_refunds
            if timing == "before_round" and effective_check_cost <= cash_during:
                err = (
                    f"Step {s_num}: cumulative cost ${effective_check_cost:,} exceeds cash available "
                    f"before Round {r} (${cash_avail:,}). Step depends on income earned during Round {r} and must specify timing: 'during_round'."
                )
            else:
                err = (
                    f"Step {s_num}: cumulative cost ${effective_check_cost:,} exceeds max available cash "
                    f"${cash_avail:,} at Round {r} ({timing})."
                )
            self.errors.append(err)
            return False, err

        # 5. Commit Transaction (Mutate board state ONLY after all checks succeed)
        self.has_committed_step = True
        self.last_round = r
        self.last_timing = timing
        self.cumulative_cost_spent = new_cum_spent
        self.cumulative_refunds = new_cum_refunds
        if r == self.start_round:
            self.has_opening_defense = True
            self.opening_cost = new_opening_cost

        if act == "Place":
            if free_dart_eligible:
                self.free_dart_used = True
            t_id = self._generate_tower_id(tower, explicit_id)
            inst = TowerInstance(
                tower_id=t_id,
                tower_name=tower,
                upgrade_tuple=upg_tuple,
                upg_str=upg_str,
                placed_round=r,
                placement=placement,
                targeting=targeting,
                initial_cost=action_cost,
                is_hero=is_hero,
                placed_timing=timing
            )
            self.active_towers[t_id] = inst
            self.all_towers[t_id] = inst

        elif act == "Upgrade":
            target_tower.upgrade = upg_tuple
            target_tower.upg_str = upg_str
            target_tower.total_invested += action_cost
            target_tower.upgrade_history.append((r, timing, upg_tuple, upg_str))

        elif act == "Sell":
            target_tower.sold_round = r
            target_tower.sold_timing = timing
            target_tower.is_active = False
            if target_tower.tower_id in self.active_towers:
                del self.active_towers[target_tower.tower_id]

        self.step_history.append({
            "step_number": s_num,
            "round": r,
            "action": act,
            "tower": tower,
            "upgrade": upg_str,
            "cost": action_cost,
            "refund": refund_amount,
            "timing": timing
        })
        return True, None

    def evaluate_threat_coverage(self, at_round, at_timing="during_round"):
        """
        Evaluates planned capability coverage up to (at_round, at_timing) using the historical replay board.
        Accurately queries the active board and tower upgrades as they existed at (at_round, at_timing).
        Returns: dict(camo, lead, moab, bfb, zomg, ceramic)
        """
        # Reconstruct active board up to at_round using historical presence
        board = [t for t in self.all_towers.values() if t.is_present_at_round(at_round, at_timing)]

        # Check support synergies at at_round
        has_village_camo = any(t.tower_name == "Monkey Village" and t.get_upgrade_at_round(at_round, at_timing)[1] >= 2 for t in board)
        has_sub_decamo = any(t.tower_name == "Monkey Sub" and t.get_upgrade_at_round(at_round, at_timing)[0] >= 3 for t in board)

        # Etienne UAV global camo buff at Level 8 (tracked based on arrival round!)
        etienne_towers = [t for t in board if t.tower_name == "Etienne"]
        etienne_global_camo = any(get_hero_level_at_round("Etienne", t.placed_round, at_round) >= 8 for t in etienne_towers)
        has_global_camo = has_village_camo or has_sub_decamo or etienne_global_camo

        has_alch_lead_buff = any(t.tower_name == "Alchemist" and t.get_upgrade_at_round(at_round, at_timing)[0] >= 2 for t in board)
        has_mib = any(t.tower_name == "Monkey Village" and t.get_upgrade_at_round(at_round, at_timing)[1] >= 3 for t in board)
        has_lead_buff = has_alch_lead_buff or has_mib

        camo = False
        lead = False
        moab = False
        bfb = False
        zomg = False
        ceramic = False

        for t in board:
            hero_lvl = get_hero_level_at_round(t.tower_name, t.placed_round, at_round) if t.is_hero else None
            curr_upg = t.get_upgrade_at_round(at_round, at_timing)
            caps = get_tower_capabilities(t.tower_name, curr_upg, hero_level=hero_lvl)

            if caps["camo"] or has_global_camo:
                camo = True
            if caps["lead"] or has_lead_buff:
                lead = True
            if caps["moab_damage"]:
                moab = True
            if caps.get("bfb_damage", False):
                bfb = True
            if caps.get("zomg_damage", False):
                zomg = True
            if caps.get("ceramic_cc", False):
                ceramic = True

        return {
            "camo": camo,
            "lead": lead,
            "moab": moab,
            "bfb": bfb,
            "zomg": zomg,
            "ceramic": ceramic
        }


def assign_explicit_tower_ids(strategy, map_id, diff):
    """
    Ensures every placed tower has an explicit, persistent tower_id and all
    subsequent upgrade, target, and sell actions reference that tower_id.
    """
    if not isinstance(strategy, dict):
        return
    steps = strategy.get("steps")
    if not isinstance(steps, list):
        return

    # Gather all existing tower_ids upfront to avoid any collisions
    existing_ids = set()
    for s in steps:
        if isinstance(s, dict):
            raw_id = s.get("tower_id")
            if isinstance(raw_id, str) and raw_id.strip():
                existing_ids.add(raw_id.strip())

    active_towers = {}  # tower_name -> list of dict(id, upgrade, placement)
    tower_counter = 0

    for idx, s in enumerate(steps):
        if not isinstance(s, dict):
            continue
        act = s.get("action")
        tow = s.get("tower")
        if not isinstance(tow, str) or not tow.strip():
            continue
        tow = tow.strip()

        if act == "Place":
            raw_id = s.get("tower_id")
            if not isinstance(raw_id, str) or not raw_id.strip():
                while True:
                    tower_counter += 1
                    cand = f"{map_id}_{diff.lower()}_t{tower_counter}"
                    if cand not in existing_ids:
                        s["tower_id"] = cand
                        existing_ids.add(cand)
                        break
            t_id = s["tower_id"]
            upg = parse_upgrade(s.get("upgrade", "0-0-0")) or (0, 0, 0)
            place = s.get("placement", "")
            active_towers.setdefault(tow, []).append({
                "id": t_id,
                "upgrade": upg,
                "placement": place if isinstance(place, str) else ""
            })
        elif act in ("Upgrade", "Target", "Sell"):
            if s.get("tower_id"):
                # Preserve state tracking for explicit tower IDs
                explicit_id = s.get("tower_id")
                matched = None
                for c in active_towers.get(tow, []):
                    if c["id"] == explicit_id:
                        matched = c
                        break
                if not matched:
                    for c_list in active_towers.values():
                        for c in c_list:
                            if c["id"] == explicit_id:
                                matched = c
                                break
                        if matched:
                            break
                if matched:
                    if act == "Upgrade":
                        upg_parsed = parse_upgrade(s.get("upgrade", "0-0-0"))
                        if upg_parsed:
                            matched["upgrade"] = upg_parsed
                    elif act == "Sell":
                        for c_list in active_towers.values():
                            if matched in c_list:
                                c_list.remove(matched)
                continue
            candidates = active_towers.get(tow, [])
            if candidates:
                matched = None
                place = s.get("placement", "")
                if place:
                    p_matches = [c for c in candidates if c["placement"] and c["placement"].strip() == place.strip()]
                    if len(p_matches) == 1:
                        matched = p_matches[0]
                if not matched and act == "Upgrade":
                    upg = parse_upgrade(s.get("upgrade", "0-0-0"))
                    valid_prog = [c for c in candidates if all(u >= e for u, e in zip(upg, c["upgrade"]))]
                    if valid_prog:
                        # Sort descending by sum of existing tiers to pick the tower furthest along this path
                        valid_prog.sort(key=lambda c: sum(c["upgrade"]), reverse=True)
                        matched = valid_prog[0]
                if not matched:
                    matched = candidates[0]

                s["tower_id"] = matched["id"]
                if act == "Upgrade":
                    matched["upgrade"] = parse_upgrade(s.get("upgrade", "0-0-0"))
                elif act == "Sell":
                    if matched in candidates:
                        candidates.remove(matched)


def validate_strategy_schema(strategy):
    """
    Validates structural schema and field types of a strategy object without
    requiring replay simulation. Returns clean diagnostic error list.
    """
    errors = []
    if not isinstance(strategy, dict):
        return False, ["Strategy object must be a JSON dictionary."]

    diff = strategy.get("difficulty", "Easy")
    if diff not in ("Easy", "Medium", "Hard", "Impoppable", "CHIMPS"):
        errors.append(f"Invalid strategy difficulty '{diff}'.")

    req_fields = [
        "difficulty", "mode", "rounds", "status", "recommended_hero",
        "starting_cash", "overview", "camo_handling", "lead_handling",
        "moab_handling", "why_it_works", "steps"
    ]
    for rf in req_fields:
        if rf not in strategy:
            errors.append(f"Strategy missing required field '{rf}'.")

    # Validate string metadata fields (reject None or non-string values)
    for text_field in [
        "difficulty", "mode", "rounds", "status", "recommended_hero",
        "overview", "camo_handling", "lead_handling", "moab_handling", "why_it_works"
    ]:
        if text_field in strategy:
            val = strategy.get(text_field)
            if not isinstance(val, str) or val is None:
                errors.append(f"Strategy field '{text_field}' must be a string, found {type(val).__name__}.")

    # Validate requirements object and subfields
    if "requirements" in strategy:
        req = strategy.get("requirements")
        if req is None or not isinstance(req, dict):
            errors.append(f"Strategy 'requirements' must be a dictionary, found {type(req).__name__}.")
        else:
            if "required_starting_cash" in req:
                req_cash = req.get("required_starting_cash")
                if not is_valid_numeric_cost(req_cash):
                    errors.append(f"requirements.required_starting_cash '{req_cash}' must be a finite, non-negative number.")
            for bool_field in ("more_starting_cash", "free_dart_monkey", "monkey_knowledge"):
                if bool_field in req:
                    val = req.get(bool_field)
                    if not isinstance(val, bool):
                        errors.append(f"requirements.{bool_field} must be a boolean, found {type(val).__name__}.")
            if "game_version" in req:
                gv = req.get("game_version")
                if not isinstance(gv, str) or not gv.strip():
                    errors.append("requirements.game_version must be a non-empty string.")

    status = strategy.get("status", "Needs Review")
    if status not in ("Playtested", "Structurally Validated", "Verified", "Needs Review", "Draft"):
        errors.append(f"Strategy has unrecognized status '{status}'.")

    sc = strategy.get("starting_cash", 650)
    if not isinstance(sc, (int, float)) or isinstance(sc, bool) or math.isnan(sc) or sc < 0:
        errors.append(f"Strategy starting_cash '{sc}' must be a non-negative number.")

    steps = strategy.get("steps")
    if not isinstance(steps, list):
        errors.append("Strategy 'steps' must be a JSON list.")
        return False, errors

    seen_step_ids = set()
    for idx, s in enumerate(steps):
        if not isinstance(s, dict):
            errors.append(f"steps[{idx}] must be a JSON dictionary object, found {type(s).__name__}.")
            continue

        s_num = s.get("step_number", idx + 1)
        if not isinstance(s_num, int) or isinstance(s_num, bool):
            errors.append(f"steps[{idx}].step_number must be an integer, found {type(s_num).__name__}.")

        r = s.get("round")
        if not isinstance(r, int) or isinstance(r, bool):
            errors.append(f"Step {s_num}: round must be an integer, found {type(r).__name__}.")

        timing = s.get("timing", "before_round")
        if timing not in ("before_round", "during_round", "after_round"):
            errors.append(f"Step {s_num}: timing '{timing}' must be one of 'before_round', 'during_round', 'after_round'.")

        act = s.get("action")
        if not isinstance(act, str) or act not in ("Place", "Upgrade", "Target", "Ability", "Sell"):
            errors.append(f"Step {s_num}: invalid action '{act}'. Allowed: Place, Upgrade, Target, Ability, Sell.")

        tow = s.get("tower")
        if not isinstance(tow, str) or not tow.strip():
            errors.append(f"Step {s_num}: tower must be a non-empty string, found {type(tow).__name__}.")

        upg = s.get("upgrade", "0-0-0")
        if not isinstance(upg, str):
            errors.append(f"Step {s_num}: upgrade must be a string, found {type(upg).__name__}.")
        elif act in ("Place", "Upgrade"):
            if upg.strip() in ("Various", "None") or parse_upgrade(upg.strip()) is None:
                errors.append(f"Step {s_num}: {act} action requires a concrete legal upgrade path, found '{upg}'.")
            elif not is_legal_crosspath(upg):
                errors.append(f"Step {s_num}: illegal crosspath '{upg}' for {tow}.")

        cost = s.get("cost_estimate", 0)
        if not is_valid_numeric_cost(cost):
            errors.append(f"Step {s_num}: cost_estimate '{cost}' must be a finite, non-negative numeric value.")

        t_id = s.get("tower_id")
        if t_id is not None and (not isinstance(t_id, str) or not t_id.strip()):
            errors.append(f"Step {s_num}: tower_id must be a non-empty string, found {type(t_id).__name__}.")

        s_id = s.get("step_id")
        if s_id is not None:
            if not isinstance(s_id, str) or not s_id.strip():
                errors.append(f"Step {s_num}: step_id must be a non-empty string, found {type(s_id).__name__}.")
            else:
                s_id_clean = s_id.strip()
                if s_id_clean in seen_step_ids:
                    errors.append(f"Step {s_num}: duplicate step_id '{s_id_clean}' found in strategy.")
                seen_step_ids.add(s_id_clean)

        for str_field in ("placement", "details", "targeting", "round_range"):
            val = s.get(str_field)
            if val is not None and not isinstance(val, str):
                errors.append(f"Step {s_num}: {str_field} must be a string, found {type(val).__name__}.")

    return (len(errors) == 0), errors


def resolve_strategy_perks(strategy, default_monkey_knowledge=False):
    """
    Authoritative helper to resolve independent Monkey Knowledge perks from a strategy.
    Preserves recorded requirements unless explicitly overridden.
    """
    req = strategy.get("requirements") if isinstance(strategy, dict) and isinstance(strategy.get("requirements"), dict) else {}
    more_starting_cash = req.get("more_starting_cash")
    free_dart_monkey = req.get("free_dart_monkey")
    mk = req.get("monkey_knowledge")
    
    if mk is None:
        if more_starting_cash is not None or free_dart_monkey is not None:
            mk = bool(more_starting_cash or free_dart_monkey)
        elif isinstance(strategy, dict):
            strat_mk = strategy.get("monkey_knowledge")
            if strat_mk is not None:
                mk = bool(strat_mk)
            elif strategy.get("starting_cash") == 850:
                mk = True
            else:
                mk = bool(default_monkey_knowledge)
        else:
            mk = bool(default_monkey_knowledge)

    if more_starting_cash is None:
        if isinstance(strategy, dict) and strategy.get("starting_cash") == 850:
            more_starting_cash = True
        else:
            more_starting_cash = bool(mk)
    if free_dart_monkey is None:
        free_dart_monkey = bool(mk)

    return {
        "monkey_knowledge": bool(mk),
        "more_starting_cash": bool(more_starting_cash),
        "free_dart_monkey": bool(free_dart_monkey)
    }


def validate_strategy(strategy, map_context=None, diff_name=None, strict_threats=True, monkey_knowledge=None,
                      more_starting_cash=None, free_dart_monkey=None):
    """
    Validates a complete strategy dictionary against all BTD6 structural, economic,
    and tactical replay invariants. Supports independent Monkey Knowledge perks
    (more_starting_cash and free_dart_monkey).
    Returns: (is_valid: bool, errors: list, warnings: list, stats: dict)
    """
    errors = []
    warnings = []
    stats = {}

    schema_valid, schema_errors = validate_strategy_schema(strategy)
    if not schema_valid:
        return False, schema_errors, warnings, stats

    diff = diff_name or strategy.get("difficulty", "Easy")
    start_round = 6 if diff in ("Impoppable", "CHIMPS") else (3 if diff == "Hard" else 1)
    max_round = 100 if diff in ("Impoppable", "CHIMPS") else (80 if diff == "Hard" else (60 if diff == "Medium" else 40))
    min_steps = 14 if diff in ("Impoppable", "CHIMPS") else (12 if diff == "Hard" else (8 if diff == "Medium" else 5))

    # Infer independent perks from strategy requirements if not explicitly supplied
    resolved = resolve_strategy_perks(strategy, default_monkey_knowledge=False)
    if more_starting_cash is None:
        more_starting_cash = resolved["more_starting_cash"]
    if free_dart_monkey is None:
        free_dart_monkey = resolved["free_dart_monkey"]
    if monkey_knowledge is None:
        monkey_knowledge = resolved["monkey_knowledge"]

    starting_cash = strategy.get("starting_cash", 650)
    expected_cash = get_starting_cash(diff, more_starting_cash=more_starting_cash)
    if more_starting_cash:
        if starting_cash not in (650, expected_cash):
            errors.append(f"Starting cash is {starting_cash}, expected 650 or {expected_cash}.")
    else:
        if starting_cash != 650:
            errors.append(f"Starting cash is {starting_cash}, expected 650.")

    steps = strategy.get("steps", [])
    status = strategy.get("status", "Needs Review")
    if len(steps) < min_steps and status not in ("Draft", "Needs Review"):
        errors.append(f"{diff} strategy requires at least {min_steps} steps (found {len(steps)}).")
    elif len(steps) < min_steps:
        warnings.append(f"{diff} strategy has {len(steps)} steps (recommended minimum: {min_steps}).")

    # Replay Simulation
    engine = TowerReplayEngine(
        difficulty=diff,
        start_round=start_round,
        max_round=max_round,
        monkey_knowledge=monkey_knowledge,
        more_starting_cash=more_starting_cash,
        free_dart_monkey=free_dart_monkey
    )
    for idx, s in enumerate(steps):
        success, err = engine.apply_step(s, step_index=idx)
        if not success and err:
            errors.append(err)

    if not engine.has_opening_defense:
        errors.append(f"No defensive placement on starting round {start_round}.")

    # Tactical Capability Verification
    threat_issues = []
    if max_round >= 24:
        cov24 = engine.evaluate_threat_coverage(24)
        if not cov24["camo"]:
            threat_issues.append("Defense lacks Camo detection before Round 24 Camo bloon arrival.")

    if max_round >= 28:
        cov28 = engine.evaluate_threat_coverage(28)
        if not cov28["lead"]:
            threat_issues.append("Defense lacks Lead popping power before Round 28 Lead arrival.")

    if max_round >= 40:
        cov40 = engine.evaluate_threat_coverage(40)
        if not cov40["moab"]:
            threat_issues.append("Defense lacks MOAB-class blimp damage for Round 40 MOAB.")

    if max_round >= 60:
        cov60 = engine.evaluate_threat_coverage(60)
        if not cov60["bfb"]:
            threat_issues.append("Defense lacks sufficient blimp damage for Round 60 BFB.")

    if max_round >= 80:
        cov63 = engine.evaluate_threat_coverage(63)
        if not cov63["ceramic"]:
            threat_issues.append("Defense lacks heavy AoE / crowd control for Round 63 Ceramic rush.")

        cov80 = engine.evaluate_threat_coverage(80)
        if not cov80["zomg"]:
            threat_issues.append("Defense lacks endgame blimp destruction for Round 80 ZOMG.")

    if max_round >= 100:
        cov90 = engine.evaluate_threat_coverage(90)
        if not (cov90["camo"] and (cov90["lead"] or cov90["zomg"])):
            threat_issues.append("Defense lacks Camo Lead / DDT popping power for Round 90 DDTs.")

        cov100 = engine.evaluate_threat_coverage(100)
        if not (cov100["zomg"] or cov100["moab"]):
            threat_issues.append("Defense lacks massive single-target damage for Round 100 BAD.")

    if threat_issues:
        if strict_threats:
            errors.extend(threat_issues)
        else:
            warnings.extend(threat_issues)

    stats["total_steps"] = len(steps)
    stats["cumulative_cost"] = engine.cumulative_cost_spent
    stats["cumulative_refunds"] = engine.cumulative_refunds
    stats["active_towers_count"] = len(engine.active_towers)

    return (len(errors) == 0), errors, warnings, stats


def prepare_and_validate_strategy(
    strategy,
    map_context=None,
    diff_name=None,
    map_id=None,
    monkey_knowledge=None,
    more_starting_cash=None,
    free_dart_monkey=None,
    strict_threats=None,
    sync_costs=True
):
    """
    Unified authoritative strategy preparation and validation pipeline.
    1. Runs schema validation first (rejects malformed types/costs/requirements before any mutations).
    2. Determines draft status and establishes consistent policy.
    3. Assigns stable step IDs and explicit tower IDs.
    4. Normalizes and preserves requirements without overwriting unedited perks.
    5. Optionally synchronizes step displayed costs with exact replay execution pricing.
    6. Runs full transactional replay simulation and tactical checks.
    Returns: (is_valid: bool, errors: list, warnings: list, prepared_strategy: dict)
    """
    if not isinstance(strategy, dict):
        return False, ["Strategy object must be a JSON dictionary."], [], {}

    # 1. Structural Schema Validation FIRST
    schema_ok, schema_errs = validate_strategy_schema(strategy)
    if not schema_ok:
        return False, schema_errs, [], strategy

    diff = diff_name or strategy.get("difficulty", "Easy")
    status = strategy.get("status", "Needs Review")
    is_draft = status in ("Draft", "Needs Review", "Unverified Draft")

    if strict_threats is None:
        strict_threats = not is_draft

    target_mid = map_id or (map_context.get("id") if isinstance(map_context, dict) else "custom_map")

    # 2. Assign step IDs and explicit tower IDs safely
    for idx, s in enumerate(strategy.get("steps", [])):
        if isinstance(s, dict):
            if "step_id" not in s:
                s["step_id"] = f"{target_mid}_{diff.lower()}_s{s.get('step_number', idx + 1)}"
            if "timing" not in s:
                s["timing"] = "before_round"

    assign_explicit_tower_ids(strategy, target_mid, diff)

    # 3. Resolve and preserve requirements
    perks = resolve_strategy_perks(strategy, default_monkey_knowledge=(monkey_knowledge if monkey_knowledge is not None else False))
    if monkey_knowledge is not None:
        perks["monkey_knowledge"] = bool(monkey_knowledge)
    if more_starting_cash is not None:
        perks["more_starting_cash"] = bool(more_starting_cash)
    if free_dart_monkey is not None:
        perks["free_dart_monkey"] = bool(free_dart_monkey)

    req = strategy.get("requirements") if isinstance(strategy.get("requirements"), dict) else {}
    req["monkey_knowledge"] = perks["monkey_knowledge"]
    req["more_starting_cash"] = perks["more_starting_cash"]
    req["free_dart_monkey"] = perks["free_dart_monkey"]
    req["required_starting_cash"] = strategy.get("starting_cash", 850 if perks["more_starting_cash"] else 650)
    req["game_version"] = req.get("game_version", "v45.0")
    strategy["requirements"] = req

    # 4. Synchronize costs if requested
    if sync_costs:
        start_round = 6 if diff in ("Impoppable", "CHIMPS") else (3 if diff == "Hard" else 1)
        max_round = 100 if diff in ("Impoppable", "CHIMPS") else (80 if diff == "Hard" else (60 if diff == "Medium" else 40))
        sync_engine = TowerReplayEngine(
            difficulty=diff,
            start_round=start_round,
            max_round=max_round,
            monkey_knowledge=perks["monkey_knowledge"],
            more_starting_cash=perks["more_starting_cash"],
            free_dart_monkey=perks["free_dart_monkey"]
        )
        for idx, s in enumerate(strategy.get("steps", [])):
            if isinstance(s, dict):
                s["cost_estimate"] = 0
                success, _ = sync_engine.apply_step(s, idx)
                if success and sync_engine.step_history:
                    exact_cost = sync_engine.step_history[-1].get("cost", 0)
                    s["cost_estimate"] = exact_cost

    # 5. Replay and Economic Validation
    is_valid, errs, warns, stats = validate_strategy(
        strategy,
        map_context=map_context,
        diff_name=diff,
        strict_threats=strict_threats,
        monkey_knowledge=perks["monkey_knowledge"],
        more_starting_cash=perks["more_starting_cash"],
        free_dart_monkey=perks["free_dart_monkey"]
    )
    return is_valid, errs, warns, strategy

def normalize_map_strategies(maps_dict):
    """
    Normalizes round timing and step progression for canonical economic compliance across all maps.
    Ensures stable step IDs, handles multi-tier transition pricing on early naval/sub builds,
    and adjusts step rounds and timing flags so strategies pass rigorous simulation.
    """
    for mid, mdata in maps_dict.items():
        if not isinstance(mdata, dict):
            continue
        strat = mdata.get("difficulties", {}).get("Easy")
        if not strat or not isinstance(strat, dict):
            continue
        steps = strat.get("steps", [])
        if not steps:
            continue

        # Fix any illegal 0-2-2 to 3-2-0 Buccaneer crosspath drops
        for s in steps:
            if s.get("tower") == "Monkey Buccaneer" and s.get("upgrade") == "0-2-2":
                s["upgrade"] = "0-2-0"
                s["cost_estimate"] = 425
                s["details"] = s.get("details", "").replace("Crow's Nest detects Camos.", "prepares path for Destroyer.")

        # Naval maps (Destroyer / Sub progression)
        if mid in ['lotus_island', 'spa_pits', 'downstream', 'water_park', 'luminous_cove', 'protect_the_yacht', 'off_the_coast', 'bazaar', 'cargo']:
            if len(steps) == 8:
                s1_5 = steps[:5]
                s1_5[4]["cost_estimate"] = 3485
                bomb_step = next((s for s in reversed(steps) if s.get("tower") == "Bomb Shooter"), None)
                bomb_upg = bomb_step.get("upgrade", "0-3-0") if bomb_step else "0-3-0"
                bomb_place = bomb_step.get("placement", "Along the track bend.") if bomb_step else "Along the track bend."
                bomb_cost = 1930 if bomb_upg == "0-3-0" else 2415
                new_s6 = {
                    "step_number": 6,
                    "round_range": "Rounds 21–30: Camo and Lead Preparation",
                    "round": 27,
                    "action": "Place",
                    "tower": "Monkey Sub",
                    "upgrade": "2-0-0",
                    "placement": steps[5].get("placement", "In the water near Buccaneer."),
                    "targeting": "First",
                    "cost_estimate": 810,
                    "details": "Advanced Intel provides global camo and dart coverage.",
                    "timing": "before_round"
                }
                new_s7 = {
                    "step_number": 7,
                    "round_range": "Rounds 31–39: Midgame Defense",
                    "round": 32,
                    "action": "Upgrade",
                    "tower": "Monkey Sub",
                    "upgrade": "2-0-3",
                    "placement": steps[5].get("placement", "In the water near Buccaneer."),
                    "targeting": "First",
                    "cost_estimate": 2165,
                    "details": "Triple Guns dramatically scales up fast-firing dart output.",
                    "timing": "before_round"
                }
                new_s8 = {
                    "step_number": 8,
                    "round_range": "Rounds 31–39: Midgame Defense",
                    "round": 36,
                    "action": "Place",
                    "tower": "Alchemist",
                    "upgrade": "3-0-0",
                    "placement": steps[6].get("placement", "Within range of Buccaneer."),
                    "targeting": "Close",
                    "cost_estimate": 2040,
                    "details": "Berserker Brew boosts the Destroyer's fire rate and damage.",
                    "timing": "before_round"
                }
                new_s9 = {
                    "step_number": 9,
                    "round_range": "Round 40: MOAB Battle",
                    "round": 38,
                    "action": "Place",
                    "tower": "Bomb Shooter",
                    "upgrade": bomb_upg,
                    "placement": bomb_place,
                    "targeting": "Strong",
                    "cost_estimate": bomb_cost,
                    "details": "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.",
                    "timing": "during_round" if (bomb_cost > 1930 or mid == "cargo") else "before_round"
                }
                strat["steps"] = s1_5 + [new_s6, new_s7, new_s8, new_s9]

        elif mid in ['cracked', 'spring_spring', 'erosion', 'sunken_columns', 'peninsula', 'high_finance', 'muddy_puddles', 'bloody_puddles', 'ouch', 'sanctuary', 'pat_s_pond', 'dark_castle', 'flooded_valley']:
            if len(steps) >= 3:
                steps[2]["round"] = 12
                steps[2]["timing"] = "before_round"

        elif mid == 'firing_range':
            if len(steps) >= 8:
                steps[4]["round"] = 24
                steps[4]["cost_estimate"] = 3740
                steps[5]["round"] = 28
                steps[5]["timing"] = "before_round"
                steps[5]["cost_estimate"] = 940
                steps[6]["round"] = 34
                steps[6]["timing"] = "during_round"
                steps[6]["cost_estimate"] = 2720
                steps[7]["round"] = 37
                steps[7]["timing"] = "during_round"
                steps[7]["cost_estimate"] = 2355

        elif mid == 'geared':
            if len(steps) >= 8:
                steps[4]["round"] = 24
                steps[4]["cost_estimate"] = 3740
                steps[5]["cost_estimate"] = 445
                steps[6]["cost_estimate"] = 1955
                steps[7]["cost_estimate"] = 2355

        elif mid in ['mesa', 'x_factor', 'quad', 'ravine', 'glacial_trail']:
            if len(steps) >= 8:
                steps[4]["round"] = 24
                steps[4]["cost_estimate"] = 3740
                steps[5]["round"] = 27
                steps[5]["timing"] = "during_round"
                steps[5]["cost_estimate"] = 970
                steps[6]["round"] = 34
                steps[6]["timing"] = "during_round"
                steps[6]["cost_estimate"] = 2400
                steps[7]["cost_estimate"] = 2355

        elif mid == 'infernal':
            if len(steps) >= 7:
                steps[5]["round"] = 30
                steps[6]["round"] = 35
                steps[6]["timing"] = "during_round"

        # Assign stable step_id to all steps in all difficulties
        for diff in ["Easy", "Medium", "Hard"]:
            diff_strat = mdata.get("difficulties", {}).get(diff)
            if not diff_strat or not isinstance(diff_strat, dict):
                continue
            for idx, s in enumerate(diff_strat.get("steps", [])):
                if isinstance(s, dict) and "step_id" not in s:
                    s["step_id"] = f"{mid}_{diff.lower()}_s{s.get('step_number', idx + 1)}"

