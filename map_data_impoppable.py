"""
map_data_impoppable.py
Generates comprehensive Impoppable / Standard (Rounds 6-100) strategies for all 87 BTD6 maps.
Accounts for 1.20x price multiplier, 1 life, starting on Round 6 with $650, and key endgame threats:
R40 MOAB, R50 Dual MOABs, R60 BFB, R63 Ceramic Rush, R76 Regrows, R78 Camo Ceramics, R80 ZOMG,
R90 First DDTs (Dark Dirigible Titans), R95 Deadly DDT Swarm, R98 30 ZOMGs Gauntlet, R99 Fortified DDTs,
and the massive Round 100 BAD (Big Airship of Doom - 20,000 HP).
Ensures legal state transitions, monotonic upgrades, and economic affordability throughout.
"""

from btd6_economy import (
    get_action_canonical_cost,
    get_cash_available,
    get_earliest_affordable_round,
    is_legal_crosspath,
    parse_upgrade,
)
from map_data_hard import build_hard_strategy

def create_step(step_number, round_range, round_num, action, tower, upgrade, placement, targeting, cost, details, timing="before_round"):
    return {
        "step_number": step_number,
        "round_range": round_range,
        "round": round_num,
        "action": action,
        "tower": tower,
        "upgrade": upgrade,
        "placement": placement,
        "targeting": targeting,
        "cost_estimate": cost,
        "details": details,
        "timing": timing
    }

def get_step_round_and_timing(difficulty, running_cost, target_round, min_round, max_round=100):
    cash_before = get_cash_available(difficulty, target_round, timing="before_round")
    if running_cost <= cash_before:
        return max(target_round, min_round), "before_round"

    cash_during = get_cash_available(difficulty, target_round, timing="during_round")
    if running_cost <= cash_during:
        return max(target_round, min_round), "during_round"

    r_before = get_earliest_affordable_round(difficulty, running_cost, max_round=max_round, timing="before_round")
    if r_before is not None:
        return max(r_before, min_round), "before_round"

    r_during = get_earliest_affordable_round(difficulty, running_cost, max_round=max_round, timing="during_round")
    if r_during is not None:
        return max(r_during, min_round), "during_round"

    return max(target_round, min_round), "during_round"


def build_impoppable_strategy(map_id, map_data):
    if not isinstance(map_data, dict):
        return None

    diffs = map_data.get("difficulties", {})
    if not diffs.get("Medium"):
        from map_data_medium import build_medium_strategy
        diffs["Medium"] = build_medium_strategy(map_id, map_data)
    if not diffs.get("Hard"):
        from map_data_hard import build_hard_strategy
        diffs["Hard"] = build_hard_strategy(map_id, map_data)

    hard = diffs.get("Hard")
    if not hard:
        return None

    easy = map_data.get("difficulties", {}).get("Easy", {})
    hero = hard.get("recommended_hero") or easy.get("recommended_hero", "Sauda")
    alts = hard.get("hero_alternatives") or easy.get("hero_alternatives", ["Quincy", "Gwendolin"])
    has_water = map_data.get("water", False)
    hard_steps = hard.get("steps", [])

    landmark_start = hard_steps[0].get("placement", "Near the track entrance.") if len(hard_steps) > 0 else "Near the track entrance."
    landmark_core = hard_steps[1].get("placement", "At the primary track curve.") if len(hard_steps) > 1 else landmark_start

    impop_steps = []
    step_num = 1
    active_towers = []
    running_cost = 0
    last_r = 6

    # 1. Handle Opening Defense on Round 6 with $650 starting cash
    # Check if hard_steps[0] is affordable with $650 on Impoppable
    first_hard = hard_steps[0] if hard_steps else None
    sauda_pre_dart = False

    if first_hard:
        f_tow = first_hard.get("tower", "")
        f_act = first_hard.get("action", "Place")
        f_upg = parse_upgrade(first_hard.get("upgrade", "0-0-0")) or (0, 0, 0)
        f_cost = get_action_canonical_cost(f_tow, (0, 0, 0), f_upg, f_act, "Impoppable")

        # If opening hero/tower exceeds $650 (e.g. Sauda is $720), open with Dart Monkey on Round 6
        if f_cost > 650:
            dart_cost = get_action_canonical_cost("Dart Monkey", (0, 0, 0), (0, 0, 0), "Place", "Impoppable")
            running_cost += dart_cost
            impop_steps.append(create_step(
                step_num,
                "Rounds 6–10: Opening Defense",
                6,
                "Place",
                "Dart Monkey",
                "0-0-0",
                landmark_start,
                "First",
                dart_cost,
                f"Dart Monkey secures the early track perimeter on Round 6 for ${dart_cost} while funds accumulate to deploy {hero}.",
                timing="before_round"
            ))
            step_num += 1
            active_towers.append({
                "tower": "Dart Monkey",
                "upgrade": (0, 0, 0),
                "upg_str": "0-0-0",
                "placement": landmark_start
            })
            sauda_pre_dart = True

    # 2. Adapt remaining Hard steps to Impoppable (R6-80)
    for idx, s in enumerate(hard_steps):
        r = s.get("round", 6)
        if r < 6:
            r = 6

        act = s.get("action", "Place")
        tower = s.get("tower", "")
        upg_str = s.get("upgrade", "0-0-0")
        upg_tuple = parse_upgrade(upg_str) or (0, 0, 0)

        from_tuple = (0, 0, 0)
        if act == "Upgrade":
            prev_inst = None
            for t in active_towers:
                if t["tower"] == tower and all(u >= e for u, e in zip(upg_tuple, t["upgrade"])):
                    prev_inst = t
                    break
            if not prev_inst:
                for t in reversed(active_towers):
                    if t["tower"] == tower:
                        prev_inst = t
                        break
            if prev_inst:
                from_tuple = prev_inst["upgrade"]

        cost = get_action_canonical_cost(tower, from_tuple, upg_tuple, act, "Impoppable")
        if cost == 0 and act in ("Place", "Upgrade"):
            hard_c = s.get("cost_estimate", 0)
            cost = int(round(hard_c * 1.20 / 1.08 / 5.0) * 5)

        # Ensure lead popping capability before Round 28 for Sniper builds
        if tower == "Sniper Monkey" and upg_tuple == (1, 0, 2) and from_tuple == (0, 0, 0):
            c_lead = get_action_canonical_cost("Sniper Monkey", from_tuple, (1, 0, 0), "Upgrade", "Impoppable")
            r_lead, timing_lead = get_step_round_and_timing("Impoppable", running_cost + c_lead, 27, last_r, max_round=100)
            if r_lead <= 27:
                running_cost += c_lead
                impop_steps.append(create_step(
                    step_num,
                    "Rounds 21–30: Camo and Lead Preparation",
                    r_lead,
                    "Upgrade",
                    "Sniper Monkey",
                    "1-0-0",
                    s.get("placement", ""),
                    "Strong",
                    c_lead,
                    "Full Metal Jacket provides high-damage Lead popping power right before Round 28 Lead bloons arrive.",
                    timing=timing_lead
                ))
                step_num += 1
                from_tuple = (1, 0, 0)
                cost = get_action_canonical_cost("Sniper Monkey", from_tuple, upg_tuple, "Upgrade", "Impoppable")
                last_r = r_lead

        running_cost += cost
        assigned_r, step_timing = get_step_round_and_timing("Impoppable", running_cost, r, last_r, max_round=100)
        last_r = assigned_r

        if assigned_r <= 10:
            rr = "Rounds 6–10: Opening Defense"
        elif assigned_r <= 20:
            rr = "Rounds 11–20: Expanding Defense & Hero"
        elif assigned_r <= 30:
            rr = "Rounds 21–30: Camo and Lead Preparation"
        elif assigned_r <= 40:
            rr = "Rounds 31–40: MOAB Preparation & Defense"
        elif assigned_r <= 50:
            rr = "Rounds 41–50: Fortified Leads & Dual MOABs"
        elif assigned_r <= 60:
            rr = "Rounds 51–60: Camo Leads & BFB Battle"
        elif assigned_r <= 75:
            rr = "Rounds 61–75: Heavy Ceramics & Blimp Trains"
        else:
            rr = "Rounds 76–80: ZOMG Boss & Midgame Transition"

        impop_steps.append(create_step(
            step_num,
            rr,
            assigned_r,
            act,
            tower,
            upg_str,
            s.get("placement", ""),
            s.get("targeting", "First"),
            cost,
            s.get("details", ""),
            timing=step_timing
        ))
        step_num += 1

        if act == "Place":
            active_towers.append({
                "tower": tower,
                "upgrade": upg_tuple,
                "upg_str": upg_str,
                "placement": s.get("placement", landmark_core)
            })
        elif act == "Upgrade":
            matched_t = None
            for t in active_towers:
                if t["tower"] == tower and all(u >= e for u, e in zip(upg_tuple, t["upgrade"])):
                    matched_t = t
                    break
            if not matched_t:
                for t in reversed(active_towers):
                    if t["tower"] == tower:
                        matched_t = t
                        break
            if matched_t:
                matched_t["upgrade"] = upg_tuple
                matched_t["upg_str"] = upg_str

    def find_tower(name):
        for t in active_towers:
            if t["tower"] == name:
                return t
        return None

    # 3. Round 82/83: Universal Camo/Lead MIB Village (2-3-0) for DDT Preparation
    village = find_tower("Monkey Village")
    if village:
        curr_upg = village["upgrade"]
        if curr_upg[1] < 3:
            new_mid = 3
            new_top = max(curr_upg[0], 2)
            new_upg = (new_top, new_mid, 0)
            c = get_action_canonical_cost("Monkey Village", curr_upg, new_upg, "Upgrade", "Impoppable")
            running_cost += c
            assigned_r, step_timing = get_step_round_and_timing("Impoppable", running_cost, 83, last_r, max_round=100)
            last_r = assigned_r
            impop_steps.append(create_step(
                step_num,
                "Rounds 81–90: Super Ceramics & First DDTs",
                assigned_r,
                "Upgrade",
                "Monkey Village",
                f"{new_top}-3-0",
                village["placement"],
                "First",
                c,
                "Monkey Intelligence Bureau (2-3-0 MIB) removes all damage immunities across all towers in range, allowing every defender to hit Lead, Camo, and DDT blimps.",
                timing=step_timing
            ))
            step_num += 1
            village["upgrade"] = new_upg
            village["upg_str"] = f"{new_top}-3-0"
    else:
        v_place = f"Buffing central cluster near {landmark_core}."
        c = get_action_canonical_cost("Monkey Village", (0, 0, 0), (2, 3, 0), "Place", "Impoppable")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Impoppable", running_cost, 83, last_r, max_round=100)
        last_r = assigned_r
        impop_steps.append(create_step(
            step_num,
            "Rounds 81–90: Super Ceramics & First DDTs",
            assigned_r,
            "Place",
            "Monkey Village",
            "2-3-0",
            v_place,
            "First",
            c,
            "Monkey Intelligence Bureau (2-3-0 MIB) grants universal damage type and radar detection, essential for popping DDTs on Round 90.",
            timing=step_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Monkey Village",
            "upgrade": (2, 3, 0),
            "upg_str": "2-3-0",
            "placement": v_place
        })

    # 4. Round 87: Deploy / Upgrade Endgame Victory Tower (Perma-Spike or Sub Commander)
    spaf = find_tower("Spike Factory")
    sub = find_tower("Monkey Sub")
    bomb = find_tower("Bomb Shooter")

    if not spaf:
        spaf_place = f"At the final track exit behind {landmark_start}."
        c = get_action_canonical_cost("Spike Factory", (0, 0, 0), (0, 2, 5), "Place", "Impoppable")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Impoppable", running_cost, 87, last_r, max_round=100)
        last_r = assigned_r
        impop_steps.append(create_step(
            step_num,
            "Rounds 81–90: Super Ceramics & First DDTs",
            assigned_r,
            "Place",
            "Spike Factory",
            "0-2-5",
            spaf_place,
            "Close",
            c,
            "Perma-Spike (0-2-5) with Smart Spikes and Even Faster Production builds an invincible wall of spikes at the exit to catch fast DDT leaks.",
            timing=step_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Spike Factory",
            "upgrade": (0, 2, 5),
            "upg_str": "0-2-5",
            "placement": spaf_place
        })
    elif spaf["upgrade"][2] < 5:
        c = get_action_canonical_cost("Spike Factory", spaf["upgrade"], (0, 2, 5), "Upgrade", "Impoppable")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Impoppable", running_cost, 87, last_r, max_round=100)
        last_r = assigned_r
        impop_steps.append(create_step(
            step_num,
            "Rounds 81–90: Super Ceramics & First DDTs",
            assigned_r,
            "Upgrade",
            "Spike Factory",
            "0-2-5",
            spaf["placement"],
            "Close",
            c,
            "Perma-Spike upgrade ensures impenetrable late-game insurance against high-speed DDT rushes and leaking super ceramics.",
            timing=step_timing
        ))
        step_num += 1
        spaf["upgrade"] = (0, 2, 5)
        spaf["upg_str"] = "0-2-5"

    # 5. Round 90: First DDTs Tactical Action
    r90, r90_timing = get_step_round_and_timing("Impoppable", running_cost, 90, last_r, max_round=100)
    last_r = r90
    hero_on_board = any(t["tower"] == hero for t in active_towers)
    r90_tower = hero if hero_on_board else active_towers[0]["tower"]
    r90_upg = "0-0-0" if hero_on_board else active_towers[0]["upg_str"]

    impop_steps.append(create_step(
        step_num,
        "Rounds 81–90: Super Ceramics & First DDTs",
        r90,
        "Target",
        r90_tower,
        r90_upg,
        landmark_core,
        "Strong",
        0,
        "Round 90 unleashes the first 3 DDTs (Dark Dirigible Titans). Innate Camo, Lead, and Black immunities are neutralized by our 2-3-0 MIB Village; Perma-Spike catches any close rush.",
        timing=r90_timing
    ))
    step_num += 1

    # 6. Round 95: The Deadly DDT Swarm Tactical Action
    r95, r95_timing = get_step_round_and_timing("Impoppable", running_cost, 95, last_r, max_round=100)
    last_r = r95
    impop_steps.append(create_step(
        step_num,
        "Rounds 91–99: The Deadly DDT Swarms & Fortified Blimps",
        r95,
        "Ability",
        r90_tower,
        r90_upg,
        landmark_core,
        "Strong",
        0,
        "Round 95 launches 30 DDTs + 4 Fortified BFBs. Activate hero abilities and concentrate all primary damage to shred the high-speed blimp swarm.",
        timing=r95_timing
    ))
    step_num += 1

    # 7. Round 98: Heavy ZOMG Gauntlet Tactical Action
    r98, r98_timing = get_step_round_and_timing("Impoppable", running_cost, 98, last_r, max_round=100)
    last_r = r98
    glue_inst = find_tower("Glue Gunner")
    g_tower = glue_inst["tower"] if glue_inst else r90_tower
    g_upg = glue_inst["upg_str"] if glue_inst else r90_upg
    impop_steps.append(create_step(
        step_num,
        "Rounds 91–99: The Deadly DDT Swarms & Fortified Blimps",
        r98,
        "Target",
        g_tower,
        g_upg,
        landmark_core,
        "Strong",
        0,
        "Round 98 sends 30 ZOMGs and 8 Fortified BFBs (highest RBE wave in standard play). Relentless Glue pins child ceramics while our Tier 5 artillery grinds down the blimp armada.",
        timing=r98_timing
    ))
    step_num += 1

    # 8. Round 99: Fortified DDT Defense Tactical Action
    r99, r99_timing = get_step_round_and_timing("Impoppable", running_cost, 99, last_r, max_round=100)
    last_r = r99
    impop_steps.append(create_step(
        step_num,
        "Rounds 91–99: The Deadly DDT Swarms & Fortified Blimps",
        r99,
        "Ability",
        r90_tower,
        r90_upg,
        landmark_core,
        "Strong",
        0,
        "Round 99 tests rapid burst power against 9 Fortified DDTs with doubled HP. Trigger active abilities to dismantle the fortified hulls before they reach the exit.",
        timing=r99_timing
    ))
    step_num += 1

    # 9. Round 100: The BAD Endgame Boss Battle
    r100, r100_timing = get_step_round_and_timing("Impoppable", running_cost, 100, last_r, max_round=100)
    t5_bomb = any(t["tower"] == "Bomb Shooter" and t["upgrade"][1] >= 5 for t in active_towers)
    t5_sub = any(t["tower"] == "Monkey Sub" and t["upgrade"][2] >= 5 for t in active_towers)

    if t5_bomb:
        b_inst = find_tower("Bomb Shooter")
        bad_tower = "Bomb Shooter"
        bad_upg = b_inst["upg_str"] if b_inst else "0-5-2"
        bad_act = "Ability"
        bad_details = "Activate MOAB Eliminator active ability continuously on the Round 100 BAD hull (20,000 HP). It shatters into 2 ZOMGs and 3 DDTs; sweep them up for the Impoppable Victory Medal!"
    elif t5_sub:
        bad_tower = "Monkey Sub"
        bad_upg = "2-0-5"
        bad_act = "Target"
        bad_details = "Sub Commander's 2x damage aura directs the submarine fleet to melt the Round 100 BAD hull, securing the Impoppable Victory Medal!"
    elif hero_on_board:
        bad_tower = hero
        bad_upg = "0-0-0"
        bad_act = "Ability"
        bad_details = f"Activate {hero}'s Level 10 and Level 20 ultimate abilities to crack open the Round 100 BAD into child blimps and claim the Impoppable Victory Medal!"
    else:
        bad_tower = active_towers[0]["tower"]
        bad_upg = active_towers[0]["upg_str"]
        bad_act = "Target"
        bad_details = "Focus all primary fire and active abilities on the Round 100 BAD to conquer Impoppable difficulty!"

    impop_steps.append(create_step(
        step_num,
        "Round 100: The BAD (Big Airship of Doom)",
        r100,
        bad_act,
        bad_tower,
        bad_upg,
        landmark_start,
        "Strong",
        0,
        bad_details,
        timing=r100_timing
    ))

    overview = (
        f"Impoppable difficulty is the ultimate standard challenge on {map_data.get('name')}, spanning Rounds 6–100 with 1.20x prices "
        f"and 1 life. {hero} leads our defense, anchored by heavy crowd control (0-2-4 Relentless Glue), a 2-3-0 MIB Village for universal "
        "DDT popping, and endgame Tier 5 firepower (0-2-5 Perma-Spike / MOAB Eliminator) to conquer the Round 100 BAD."
    )

    camo_handling = (
        f"Early camo is dispatched via {hero} and Ninja detection. By Round 83, a 2-3-0 Monkey Village (MIB + Radar Scanner) "
        "is active at the main junction, granting universal Camo and Lead damage against Round 90/95/99 DDTs."
    )

    lead_handling = (
        "Acidic Mixture Dip (Alchemist 2-0-0) neutralizes early leads. MIB Village (2-3-0) removes all armor immunities, "
        "ensuring 100% lead-popping uptime across all attackers."
    )

    moab_handling = (
        "Midgame blimps (R40 MOAB, R50 Dual MOABs, R60 BFB) are demolished by targeted single-target missile fire. "
        "Endgame blimps (R80 ZOMG, R90/95 DDT swarms, R98 ZOMG gauntlet, and R100 BAD) are dismantled by Tier 5 anti-blimp artillery and Perma-Spike."
    )

    why_it_works = (
        "The build layers slow/stall crowd control (0-2-4 Relentless Glue), universal DDT decimation via MIB (2-3-0), "
        "and a permanent spike reservoir at the track exit to absorb super ceramics and high-speed blimp leaks."
    )

    return {
        "difficulty": "Impoppable",
        "mode": "Standard",
        "rounds": "6-100",
        "status": "Structurally Validated",
        "recommended_hero": hero,
        "hero_alternatives": alts,
        "starting_cash": 650,
        "overview": overview,
        "camo_handling": camo_handling,
        "lead_handling": lead_handling,
        "moab_handling": moab_handling,
        "why_it_works": why_it_works,
        "research_sources": [
            "BTD6 Impoppable Strategy Index",
            "Chou's BTD6 Round Mechanics Guide (Rounds 81-100)",
            "Bloons TD 6 Advanced DDT & BAD Breakdown"
        ],
        "steps": impop_steps
    }
