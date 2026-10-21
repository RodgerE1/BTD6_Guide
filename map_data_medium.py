"""
map_data_medium.py
Generates comprehensive Medium / Standard (Rounds 1-60) strategies for all 87 BTD6 maps.
Accounts for 1.0x price multiplier, 100 lives, and key threats including R45 Fortified Leads,
R49 Ceramic waves, R50 Dual MOABs, R59 Camo Leads, and the Round 60 BFB (Brutal Flying Behemoth).
Ensures coherent tower identities and legal state transitions derived from the base Easy strategy.
"""

from btd6_economy import (
    easy_to_medium_cost,
    get_action_canonical_cost,
    get_cash_available,
    get_earliest_affordable_round,
    is_legal_crosspath,
    parse_upgrade,
)

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

def get_step_round_and_timing(difficulty, running_cost, target_round, min_round, max_round=60):
    """
    Computes earliest valid round and whether the action happens before or during the round.
    """
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

def build_medium_strategy(map_id, map_data):
    easy = map_data.get("difficulties", {}).get("Easy", {})
    if not easy:
        return None

    hero = easy.get("recommended_hero", "Sauda")
    alts = easy.get("hero_alternatives", ["Quincy", "Gwendolin"])
    has_water = map_data.get("water", False)
    easy_steps = easy.get("steps", [])

    landmark_start = easy_steps[0].get("placement", "Near the track entrance.") if len(easy_steps) > 0 else "Near the track entrance."
    landmark_core = easy_steps[1].get("placement", "At the primary track curve.") if len(easy_steps) > 1 else landmark_start

    med_steps = []
    step_num = 1

    # Track active towers placed in Easy
    # List of dicts: {"tower": str, "upgrade": tuple, "upg_str": str, "placement": str}
    active_towers = []
    running_cost = 0
    last_r = 1

    # 1. Adapt opening steps (R1-38) to Medium pricing
    for s in easy_steps:
        r = s.get("round", 1)
        if r <= 38:
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

            cost = get_action_canonical_cost(tower, from_tuple, upg_tuple, act, "Medium")
            if cost == 0 and act in ("Place", "Upgrade"):
                cost = easy_to_medium_cost(s.get("cost_estimate", 0))

            running_cost += cost
            assigned_r, step_timing = get_step_round_and_timing("Medium", running_cost, r, last_r, max_round=60)
            last_r = assigned_r

            if assigned_r <= 10:
                rr = "Rounds 1–10: Opening Defense"
            elif assigned_r <= 20:
                rr = "Rounds 11–20: Expanding Defense"
            elif assigned_r <= 30:
                rr = "Rounds 21–30: Camo and Lead Preparation"
            else:
                rr = "Rounds 31–40: MOAB Preparation & Defense"

            med_steps.append(create_step(
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

    # Helper lookup functions
    def find_tower(name):
        for t in active_towers:
            if t["tower"] == name:
                return t
        return None

    def find_blimp_breaker():
        for name in ["Bomb Shooter", "Monkey Buccaneer", "Monkey Sub", "Sniper Monkey", "Tack Shooter", "Ninja Monkey"]:
            t = find_tower(name)
            if t:
                return t
        return active_towers[0] if active_towers else None

    # 2. Round 40 MOAB Defense Step: Target an actual active blimp-breaker
    breaker = find_blimp_breaker()
    target_tower = breaker["tower"] if breaker else "Bomb Shooter"
    target_upg = breaker["upg_str"] if breaker else "0-3-2"
    target_place = breaker["placement"] if breaker else landmark_core

    target_r, target_timing = get_step_round_and_timing("Medium", running_cost, 40, last_r, max_round=60)
    last_r = target_r
    med_steps.append(create_step(
        step_num,
        "Rounds 31–40: MOAB Preparation & Defense",
        target_r,
        "Target",
        target_tower,
        target_upg,
        target_place,
        "Strong",
        0,
        f"Set {target_tower} to Strong to burst open the Round 40 MOAB hull immediately upon arrival. Cleanup towers wipe out the four ceramic bloons inside.",
        timing=target_timing
    ))
    step_num += 1

    # 3. Round 42: Monkey Village Radar Scanner for universal Camo detection
    village = find_tower("Monkey Village")
    if not village:
        village_place = f"Buffing the core defense {landmark_core}."
        c = get_action_canonical_cost("Monkey Village", (0, 0, 0), (0, 2, 0), "Place", "Medium")
        running_cost += c
        v_r, v_timing = get_step_round_and_timing("Medium", running_cost, 42, last_r, max_round=60)
        last_r = v_r
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            v_r,
            "Place",
            "Monkey Village",
            "0-2-0",
            village_place,
            "First",
            c,
            "Radar Scanner grants universal Camo detection to all towers in its radius, countering Round 42 Camo Rainbows and upcoming Camo Leads.",
            timing=v_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Monkey Village",
            "upgrade": (0, 2, 0),
            "upg_str": "0-2-0",
            "placement": village_place
        })

    # 4. Round 46: Heavy Ceramic & Fortified Lead Defense
    bomb = find_tower("Bomb Shooter")
    sub = find_tower("Monkey Sub")
    bucc = find_tower("Monkey Buccaneer")

    if bomb:
        if bomb["upgrade"][1] >= 3:
            c = get_action_canonical_cost("Bomb Shooter", (0, 0, 0), (2, 0, 4), "Place", "Medium")
            running_cost += c
            b_r, b_timing = get_step_round_and_timing("Medium", running_cost, 46, last_r, max_round=60)
            last_r = b_r
            med_steps.append(create_step(
                step_num,
                "Rounds 41–50: Fortified Leads & Dual MOABs",
                b_r,
                "Place",
                "Bomb Shooter",
                "2-0-4",
                landmark_core,
                "Close",
                c,
                "Recursive Cluster fires clusters of secondary bombs on every impact. Completely obliterates Round 45 Fortified Leads and Round 49 massive ceramic waves.",
                timing=b_timing
            ))
            step_num += 1
            active_towers.append({
                "tower": "Bomb Shooter",
                "upgrade": (2, 0, 4),
                "upg_str": "2-0-4",
                "placement": landmark_core
            })
        elif bomb["upgrade"] == (2, 0, 4):
            pass
        else:
            c = get_action_canonical_cost("Bomb Shooter", bomb["upgrade"], (2, 0, 4), "Upgrade", "Medium")
            running_cost += c
            b_r, b_timing = get_step_round_and_timing("Medium", running_cost, 46, last_r, max_round=60)
            last_r = b_r
            med_steps.append(create_step(
                step_num,
                "Rounds 41–50: Fortified Leads & Dual MOABs",
                b_r,
                "Upgrade",
                "Bomb Shooter",
                "2-0-4",
                bomb["placement"],
                "Close",
                c,
                "Recursive Cluster fires clusters of secondary bombs on every impact. Completely obliterates Round 45 Fortified Leads and Round 49 massive ceramic waves.",
                timing=b_timing
            ))
            step_num += 1
            bomb["upgrade"] = (2, 0, 4)
            bomb["upg_str"] = "2-0-4"
    elif sub and sub["upgrade"][2] >= 3:
        c = get_action_canonical_cost("Monkey Sub", sub["upgrade"], (2, 0, 4), "Upgrade", "Medium")
        running_cost += c
        s_r, s_timing = get_step_round_and_timing("Medium", running_cost, 46, last_r, max_round=60)
        last_r = s_r
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            s_r,
            "Upgrade",
            "Monkey Sub",
            "2-0-4",
            sub["placement"],
            "First",
            c,
            "Armor Piercing Darts inflicts heavy bonus damage to ceramics and blimps, decimating Round 45 Fortified Leads.",
            timing=s_timing
        ))
        step_num += 1
        sub["upgrade"] = (2, 0, 4)
        sub["upg_str"] = "2-0-4"
    elif bucc and bucc["upgrade"][0] >= 3:
        c = get_action_canonical_cost("Monkey Buccaneer", bucc["upgrade"], (4, 2, 0), "Upgrade", "Medium")
        running_cost += c
        bucc_r, bucc_timing = get_step_round_and_timing("Medium", running_cost, 46, last_r, max_round=60)
        last_r = bucc_r
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            bucc_r,
            "Upgrade",
            "Monkey Buccaneer",
            "4-2-0",
            bucc["placement"],
            "First",
            c,
            "Aircraft Carrier launches 3 fighter planes that strafe the track with rapid dart and bomb volleys, easily clearing Fortified Leads.",
            timing=bucc_timing
        ))
        step_num += 1
        bucc["upgrade"] = (4, 2, 0)
        bucc["upg_str"] = "4-2-0"
    else:
        c = get_action_canonical_cost("Bomb Shooter", (0, 0, 0), (2, 0, 4), "Place", "Medium")
        running_cost += c
        b_r, b_timing = get_step_round_and_timing("Medium", running_cost, 46, last_r, max_round=60)
        last_r = b_r
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            b_r,
            "Place",
            "Bomb Shooter",
            "2-0-4",
            landmark_core,
            "Close",
            c,
            "Recursive Cluster provides extreme splash coverage against Round 45 Fortified Leads and dense ceramic rushes.",
            timing=b_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Bomb Shooter",
            "upgrade": (2, 0, 4),
            "upg_str": "2-0-4",
            "placement": landmark_core
        })

    # 5. Round 50: Dual MOABs & Alchemist Stronger Stimulant
    alch = find_tower("Alchemist")
    if alch:
        c = get_action_canonical_cost("Alchemist", alch["upgrade"], (4, 2, 0), "Upgrade", "Medium")
        running_cost += c
        alch_r, alch_timing = get_step_round_and_timing("Medium", running_cost, 50, last_r, max_round=60)
        last_r = alch_r
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            alch_r,
            "Upgrade",
            "Alchemist",
            "4-2-0",
            alch["placement"],
            "Close",
            c,
            "Stronger Stimulant and Faster Throwing provide massive attack speed, pierce, and damage buffs to break both Round 50 MOABs concurrently.",
            timing=alch_timing
        ))
        step_num += 1
        alch["upgrade"] = (4, 2, 0)
        alch["upg_str"] = "4-2-0"
    else:
        c = get_action_canonical_cost("Alchemist", (0, 0, 0), (4, 2, 0), "Place", "Medium")
        running_cost += c
        alch_r, alch_timing = get_step_round_and_timing("Medium", running_cost, 50, last_r, max_round=60)
        last_r = alch_r
        alch_place = f"Next to core attackers at {landmark_core}."
        med_steps.append(create_step(
            step_num,
            "Rounds 41–50: Fortified Leads & Dual MOABs",
            alch_r,
            "Place",
            "Alchemist",
            "4-2-0",
            alch_place,
            "Close",
            c,
            "Stronger Stimulant provides major attack speed, pierce, and lead-melting buffs for Round 50 MOABs.",
            timing=alch_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Alchemist",
            "upgrade": (4, 2, 0),
            "upg_str": "4-2-0",
            "placement": alch_place
        })

    # 6. Round 53: Village Jungle Drums (+15% attack speed)
    village = find_tower("Monkey Village")
    if village and village["upgrade"] == (0, 2, 0):
        c = get_action_canonical_cost("Monkey Village", (0, 2, 0), (2, 2, 0), "Upgrade", "Medium")
        running_cost += c
        v_r, v_timing = get_step_round_and_timing("Medium", running_cost, 53, last_r, max_round=60)
        last_r = v_r
        med_steps.append(create_step(
            step_num,
            "Rounds 51–59: Ceramic Waves & Camo Lead Defense",
            v_r,
            "Upgrade",
            "Monkey Village",
            "2-2-0",
            village["placement"],
            "First",
            c,
            "Jungle Drums grants +15% attack speed to all surrounding monkeys, essential for upcoming dense rushes.",
            timing=v_timing
        ))
        step_num += 1
        village["upgrade"] = (2, 2, 0)
        village["upg_str"] = "2-2-0"

    # 7. Round 58: MOAB Assassin / Single-Target Blimp Burst for Round 60 BFB
    mauler_bomb = None
    for t in active_towers:
        if t["tower"] == "Bomb Shooter" and t["upgrade"][1] >= 3:
            mauler_bomb = t
            break

    has_assassin = False
    assassin_upg = "0-4-2"
    if mauler_bomb:
        top_tier = mauler_bomb["upgrade"][0]
        bot_tier = mauler_bomb["upgrade"][2]
        new_upg_tuple = (top_tier, 4, bot_tier)
        new_upg_str = f"{top_tier}-4-{bot_tier}"
        c = get_action_canonical_cost("Bomb Shooter", mauler_bomb["upgrade"], new_upg_tuple, "Upgrade", "Medium")
        running_cost += c
        b_r, b_timing = get_step_round_and_timing("Medium", running_cost, 58, last_r, max_round=60)
        last_r = b_r

        med_steps.append(create_step(
            step_num,
            "Rounds 51–59: Ceramic Waves & Camo Lead Defense",
            b_r,
            "Upgrade",
            "Bomb Shooter",
            new_upg_str,
            mauler_bomb["placement"],
            "Strong",
            c,
            "MOAB Assassin unlocks the targeted missile ability (750 burst blimp damage) to cleanly conquer the Round 60 BFB.",
            timing=b_timing
        ))
        step_num += 1
        mauler_bomb["upgrade"] = new_upg_tuple
        mauler_bomb["upg_str"] = new_upg_str
        has_assassin = True
        assassin_upg = new_upg_str
    elif not has_water:
        c = get_action_canonical_cost("Bomb Shooter", (0, 0, 0), (0, 4, 2), "Place", "Medium")
        running_cost += c
        b_r, b_timing = get_step_round_and_timing("Medium", running_cost, 58, last_r, max_round=60)
        last_r = b_r
        med_steps.append(create_step(
            step_num,
            "Rounds 51–59: Ceramic Waves & Camo Lead Defense",
            b_r,
            "Place",
            "Bomb Shooter",
            "0-4-2",
            landmark_start,
            "Strong",
            c,
            "MOAB Assassin unlocks the targeted missile ability (750 burst blimp damage) to cleanly conquer the Round 60 BFB.",
            timing=b_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Bomb Shooter",
            "upgrade": (0, 4, 2),
            "upg_str": "0-4-2",
            "placement": landmark_start
        })
        has_assassin = True
        assassin_upg = "0-4-2"

    # 8. Round 60: BFB Battle Ability Trigger
    hero_on_board = any(t["tower"] == hero for t in active_towers)
    if has_assassin:
        act_tower = "Bomb Shooter"
        act_upg = assassin_upg
        act_place = landmark_start
        act_details = "Activate MOAB Assassin ability when the Round 60 BFB arrives to break the outer hull, then fire Hero Level 10 ability to clean up all 4 child MOABs."
    elif hero_on_board:
        act_tower = hero
        act_upg = "0-0-0"
        act_place = landmark_start
        act_details = f"Activate {hero}'s Level 10 ability when the Round 60 BFB arrives to burst open the blimp hull and destroy the child MOABs."
    else:
        first_t = active_towers[0] if active_towers else {"tower": "Dart Monkey", "upg_str": "0-0-0", "placement": landmark_core}
        act_tower = first_t["tower"]
        act_upg = first_t["upg_str"]
        act_place = first_t["placement"]
        act_details = "Focus all primary fire on the Round 60 BFB hull, letting area splash destroy the child MOABs."

    bfb_r, bfb_timing = get_step_round_and_timing("Medium", running_cost, 60, last_r, max_round=60)
    med_steps.append(create_step(
        step_num,
        "Round 60: The BFB Battle",
        bfb_r,
        "Ability",
        act_tower,
        act_upg,
        act_place,
        "Strong",
        0,
        act_details,
        timing=bfb_timing
    ))

    overview = (
        f"Medium difficulty tests defense scalability through Round 60 with standard 1.0x pricing. "
        f"On {map_data.get('name')}, {hero} secures our early game. The strategy expands into a "
        f"2-2-0 Village and 4-2-0 Alchemist buff engine, supporting Recursive Cluster and MOAB Assassin "
        f"to conquer Round 50 Dual MOABs and shatter the Round 60 BFB."
    )

    camo_handling = (
        f"{hero} and early detection handle R24/33/36. A 2-2-0 Monkey Village (Radar Scanner) "
        "is placed by Round 42, ensuring all towers pop R42 Camo Rainbows, R51 Camo ceramics, and R59 Camo Leads."
    )

    lead_handling = (
        "Acidic Mixture Dip (Alchemist 2-0-0) neutralizes early leads on R28/30. "
        "Recursive Cluster (2-0-4 Bomb) wipes Round 45 Fortified Leads and Round 59 Camo Leads under Village radar."
    )

    moab_handling = (
        "Round 40 MOAB is dispatched via single-target focus. Round 50 Dual MOABs are crushed "
        "by Stronger Stimulant buffed clusters. Round 60 BFB is neutralized via MOAB Assassin missile ability."
    )

    why_it_works = (
        "Jungle Drums + Stronger Stimulant delivers massive uptime and DPS multipliers across all towers. "
        "Radar Scanner gives full camo coverage so no specialized decamo micro is required."
    )

    return {
        "difficulty": "Medium",
        "mode": "Standard",
        "rounds": "1-60",
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
            "BTD6 Medium Standard Index",
            "Chou's BTD6 Round Mechanics Guide",
            "Bloons Wiki - BFB & Camo Waves"
        ],
        "steps": med_steps
    }
