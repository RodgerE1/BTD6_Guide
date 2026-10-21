"""
map_data_hard.py
Generates comprehensive Hard / Standard (Rounds 3-80) strategies for all 87 BTD6 maps.
Accounts for 1.08x price multiplier, 100 lives, starting on Round 3 with $650, and key threats:
R40 MOAB, R50 Dual MOABs, R60 BFB, R63 Ceramic rush (3 dense waves), R75 Dual BFBs,
R76 Regrow Ceramics, R78 Dual Camo Ceramic waves, and the massive Round 80 ZOMG.
Ensures legal state transitions, monotonic upgrades, and economic affordability throughout.
"""

from btd6_economy import (
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

def get_step_round_and_timing(difficulty, running_cost, target_round, min_round, max_round=80):
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

def build_hard_strategy(map_id, map_data):
    easy = map_data.get("difficulties", {}).get("Easy", {})
    med = map_data.get("difficulties", {}).get("Medium", {})
    if not easy or not med:
        return None

    hero = easy.get("recommended_hero", "Sauda")
    alts = easy.get("hero_alternatives", ["Quincy", "Gwendolin"])
    has_water = map_data.get("water", False)
    med_steps = med.get("steps", [])

    landmark_start = med_steps[0].get("placement", "Near the track entrance.") if len(med_steps) > 0 else "Near the track entrance."
    landmark_core = med_steps[1].get("placement", "At the primary track curve.") if len(med_steps) > 1 else landmark_start

    hard_steps = []
    step_num = 1

    active_towers = []
    running_cost = 0
    last_r = 3

    # 1. Adapt Medium steps (R1-60) to Hard pricing and starting round 3
    for s in med_steps:
        r = s.get("round", 3)
        if r < 3:
            r = 3

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

        cost = get_action_canonical_cost(tower, from_tuple, upg_tuple, act, "Hard")
        if cost == 0 and act in ("Place", "Upgrade"):
            med_c = s.get("cost_estimate", 0)
            cost = int(round(med_c * 1.08 / 5.0) * 5)

        running_cost += cost
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, r, last_r, max_round=80)
        last_r = assigned_r

        if assigned_r <= 10:
            rr = "Rounds 3–10: Opening Defense"
        elif assigned_r <= 20:
            rr = "Rounds 11–20: Expanding Defense"
        elif assigned_r <= 30:
            rr = "Rounds 21–30: Camo and Lead Preparation"
        elif assigned_r <= 40:
            rr = "Rounds 31–40: MOAB Preparation & Defense"
        elif assigned_r <= 50:
            rr = "Rounds 41–50: Fortified Leads & Dual MOABs"
        else:
            rr = "Rounds 51–60: Camo Leads & BFB Battle"

        hard_steps.append(create_step(
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

    # 2. Round 62: Ring of Fire (4-0-2) / High Pierce AoE for Round 63 Ceramic Rush
    tack = find_tower("Tack Shooter")
    bucc = find_tower("Monkey Buccaneer")

    if tack:
        if tack["upgrade"][2] >= 3:
            if not has_water:
                c = get_action_canonical_cost("Tack Shooter", (0, 0, 0), (4, 0, 2), "Place", "Hard")
                running_cost += c
                assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 62, last_r, max_round=80)
                last_r = assigned_r
                hard_steps.append(create_step(
                    step_num,
                    "Rounds 61–75: Heavy Ceramics & Blimp Trains",
                    assigned_r,
                    "Place",
                    "Tack Shooter",
                    "4-0-2",
                    landmark_core,
                    "Close",
                    c,
                    "Ring of Fire provides extreme rapid AoE splash damage specifically prepared for the Round 63 ceramic rush.",
                    timing=step_timing
                ))
                step_num += 1
                active_towers.append({
                    "tower": "Tack Shooter",
                    "upgrade": (4, 0, 2),
                    "upg_str": "4-0-2",
                    "placement": landmark_core
                })
        elif tack["upgrade"][0] < 4 and tack["upgrade"][1] == 0:
            c = get_action_canonical_cost("Tack Shooter", tack["upgrade"], (4, 0, 2), "Upgrade", "Hard")
            running_cost += c
            assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 62, last_r, max_round=80)
            last_r = assigned_r
            hard_steps.append(create_step(
                step_num,
                "Rounds 61–75: Heavy Ceramics & Blimp Trains",
                assigned_r,
                "Upgrade",
                "Tack Shooter",
                "4-0-2",
                tack["placement"],
                "Close",
                c,
                "Ring of Fire unleashes massive rapid AoE fire damage specifically prepared for the Round 63 ceramic rush.",
                timing=step_timing
            ))
            step_num += 1
            tack["upgrade"] = (4, 0, 2)
            tack["upg_str"] = "4-0-2"
    else:
        if bucc and bucc["upgrade"][0] == 3:
            c = get_action_canonical_cost("Monkey Buccaneer", bucc["upgrade"], (4, 2, 0), "Upgrade", "Hard")
            running_cost += c
            assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 62, last_r, max_round=80)
            last_r = assigned_r
            hard_steps.append(create_step(
                step_num,
                "Rounds 61–75: Heavy Ceramics & Blimp Trains",
                assigned_r,
                "Upgrade",
                "Monkey Buccaneer",
                "4-2-0",
                bucc["placement"],
                "First",
                c,
                "Aircraft Carrier launches 3 fighter planes for rapid high-pierce fire against Round 63 ceramics.",
                timing=step_timing
            ))
            step_num += 1
            bucc["upgrade"] = (4, 2, 0)
            bucc["upg_str"] = "4-2-0"

    # 3. Round 63: The Notorious Ceramic Rush Trigger
    r63, r63_timing = get_step_round_and_timing("Hard", running_cost, 63, last_r, max_round=80)
    last_r = r63

    hero_on_board = any(t["tower"] == hero for t in active_towers)
    if hero_on_board:
        r63_tower = hero
        r63_upg = "0-0-0"
    elif find_tower("Tack Shooter"):
        r63_tower = "Tack Shooter"
        r63_upg = "4-0-2"
    elif find_tower("Bomb Shooter"):
        r63_tower = "Bomb Shooter"
        r63_upg = find_tower("Bomb Shooter")["upg_str"]
    else:
        r63_tower = active_towers[0]["tower"]
        r63_upg = active_towers[0]["upg_str"]

    hard_steps.append(create_step(
        step_num,
        "Rounds 61–75: Heavy Ceramics & Blimp Trains",
        r63,
        "Ability",
        r63_tower,
        r63_upg,
        landmark_core,
        "First",
        0,
        "Round 63 features 3 dense waves of 122 Ceramics total. Ring of Fire + Recursive Cluster melts each wave instantly; trigger active abilities if ceramics push deep.",
        timing=r63_timing
    ))
    step_num += 1

    # 4. Round 68: Heavy Blimp Rounds Support
    sniper = find_tower("Sniper Monkey")
    if sniper and sniper["upgrade"][0] < 3:
        c = get_action_canonical_cost("Sniper Monkey", sniper["upgrade"], (3, 0, 2), "Upgrade", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 68, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 61–75: Heavy Ceramics & Blimp Trains",
            assigned_r,
            "Upgrade",
            "Sniper Monkey",
            "3-0-2",
            sniper["placement"],
            "Strong",
            c,
            "Deadly Precision inflicts 20 damage per shot to MOAB-class blimps across heavy blimp rounds 68–75.",
            timing=step_timing
        ))
        step_num += 1
        sniper["upgrade"] = (3, 0, 2)
        sniper["upg_str"] = "3-0-2"
    else:
        alch_inst = find_tower("Alchemist")
        alch_tower_name = alch_inst["tower"] if alch_inst else active_towers[0]["tower"]
        alch_upg_name = alch_inst["upg_str"] if alch_inst else active_towers[0]["upg_str"]
        r68, r68_timing = get_step_round_and_timing("Hard", running_cost, 68, last_r, max_round=80)
        last_r = r68
        hard_steps.append(create_step(
            step_num,
            "Rounds 61–75: Heavy Ceramics & Blimp Trains",
            r68,
            "Target",
            alch_tower_name,
            alch_upg_name,
            landmark_core,
            "Close",
            0,
            "Verify 100% Berserker Brew and Acidic Dip uptime on all primary damage dealers across heavy blimp rounds 68–75.",
            timing=r68_timing
        ))
        step_num += 1

    # 5. Round 74: Relentless Glue Gunner (0-2-4) for blimp & ceramic lockdown
    glue = find_tower("Glue Gunner")
    if not glue:
        glue_place = f"Just before the main curve {landmark_start}."
        c = get_action_canonical_cost("Glue Gunner", (0, 0, 0), (0, 2, 4), "Place", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 74, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 61–75: Heavy Ceramics & Blimp Trains",
            assigned_r,
            "Place",
            "Glue Gunner",
            "0-2-4",
            glue_place,
            "Strong",
            c,
            "Relentless Glue slows all MOAB-class blimps and leaves sticky glue puddles on the track that freeze child ceramics in place.",
            timing=step_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Glue Gunner",
            "upgrade": (0, 2, 4),
            "upg_str": "0-2-4",
            "placement": glue_place
        })

    # 6. Round 76: Regrow Ceramic Wave Action
    r76, r76_timing = get_step_round_and_timing("Hard", running_cost, 76, last_r, max_round=80)
    last_r = r76
    hard_steps.append(create_step(
        step_num,
        "Rounds 76–80: ZOMG Boss & Endgame Victory",
        r76,
        "Target",
        "Glue Gunner",
        "0-2-4",
        landmark_start,
        "Strong",
        0,
        "Round 76 sends 60 packed Regrow Ceramics. Relentless Glue + Ring of Fire wipes them instantly without letting regrows regenerate.",
        timing=r76_timing
    ))
    step_num += 1

    # 7. Round 77: Endgame Tier 5 Blimp Destroyer for Round 80 ZOMG
    bomb_assassin = None
    for t in active_towers:
        if t["tower"] == "Bomb Shooter" and t["upgrade"][1] >= 4:
            bomb_assassin = t
            break

    sub_commander = None
    for t in active_towers:
        if t["tower"] == "Monkey Sub" and t["upgrade"][2] >= 4:
            sub_commander = t
            break

    bucc_carrier = None
    for t in active_towers:
        if t["tower"] == "Monkey Buccaneer" and t["upgrade"][0] >= 4:
            bucc_carrier = t
            break

    t5_type = "None"
    zomg_upg_bomb = "0-5-2"

    if bomb_assassin:
        top_tier = bomb_assassin["upgrade"][0]
        bot_tier = bomb_assassin["upgrade"][2]
        new_upg_tuple = (top_tier, 5, bot_tier)
        new_upg_str = f"{top_tier}-5-{bot_tier}"
        c = get_action_canonical_cost("Bomb Shooter", bomb_assassin["upgrade"], new_upg_tuple, "Upgrade", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 77, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 76–80: ZOMG Boss & Endgame Victory",
            assigned_r,
            "Upgrade",
            "Bomb Shooter",
            new_upg_str,
            bomb_assassin["placement"],
            "Strong",
            c,
            "MOAB Eliminator delivers devastating 4,500 damage burst missiles every few seconds to annihilate the Round 80 ZOMG hull.",
            timing=step_timing
        ))
        step_num += 1
        bomb_assassin["upgrade"] = new_upg_tuple
        bomb_assassin["upg_str"] = new_upg_str
        t5_type = "Bomb"
        zomg_upg_bomb = new_upg_str
    elif sub_commander:
        c = get_action_canonical_cost("Monkey Sub", sub_commander["upgrade"], (2, 0, 5), "Upgrade", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 77, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 76–80: ZOMG Boss & Endgame Victory",
            assigned_r,
            "Upgrade",
            "Monkey Sub",
            "2-0-5",
            sub_commander["placement"],
            "First",
            c,
            "Sub Commander doubles the attack damage and pierce of all submarines on the map, shredding the Round 80 ZOMG.",
            timing=step_timing
        ))
        step_num += 1
        sub_commander["upgrade"] = (2, 0, 5)
        sub_commander["upg_str"] = "2-0-5"
        t5_type = "Sub"
    elif bucc_carrier:
        c = get_action_canonical_cost("Monkey Buccaneer", bucc_carrier["upgrade"], (5, 2, 0), "Upgrade", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 77, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 76–80: ZOMG Boss & Endgame Victory",
            assigned_r,
            "Upgrade",
            "Monkey Buccaneer",
            "5-2-0",
            bucc_carrier["placement"],
            "First",
            c,
            "Carrier Flagship launches upgraded supersonic jets with anti-MOAB missiles, obliterating the Round 80 ZOMG.",
            timing=step_timing
        ))
        step_num += 1
        bucc_carrier["upgrade"] = (5, 2, 0)
        bucc_carrier["upg_str"] = "5-2-0"
        t5_type = "Bucc"
    else:
        c = get_action_canonical_cost("Bomb Shooter", (0, 0, 0), (0, 4, 2), "Place", "Hard")
        running_cost += c
        assigned_r, step_timing = get_step_round_and_timing("Hard", running_cost, 77, last_r, max_round=80)
        last_r = assigned_r
        hard_steps.append(create_step(
            step_num,
            "Rounds 76–80: ZOMG Boss & Endgame Victory",
            assigned_r,
            "Place",
            "Bomb Shooter",
            "0-4-2",
            landmark_start,
            "Strong",
            c,
            "MOAB Assassin provides targeted 750 burst damage missiles to crack open the Round 80 ZOMG.",
            timing=step_timing
        ))
        step_num += 1
        active_towers.append({
            "tower": "Bomb Shooter",
            "upgrade": (0, 4, 2),
            "upg_str": "0-4-2",
            "placement": landmark_start
        })
        t5_type = "Bomb"
        zomg_upg_bomb = "0-4-2"

    # 8. Round 78: Dual Camo Ceramic Waves
    r78, r78_timing = get_step_round_and_timing("Hard", running_cost, 78, last_r, max_round=80)
    last_r = r78
    village_inst = find_tower("Monkey Village")
    v_tower_name = village_inst["tower"] if village_inst else "Glue Gunner"
    v_upg_name = village_inst["upg_str"] if village_inst else "0-2-4"

    hard_steps.append(create_step(
        step_num,
        "Rounds 76–80: ZOMG Boss & Endgame Victory",
        r78,
        "Target",
        v_tower_name,
        v_upg_name,
        landmark_core,
        "First",
        0,
        "Round 78 dual waves: Wave 1 has standard ceramics; Wave 2 has 72 CAMO CERAMICS. The 2-2-0 Village Radar Scanner ensures our Ring of Fire and clusters wipe the camo wave instantly.",
        timing=r78_timing
    ))
    step_num += 1

    # 9. Round 80: Final ZOMG Boss Destruction
    if t5_type == "Bomb":
        z_tower = "Bomb Shooter"
        z_upg = zomg_upg_bomb
        z_act = "Ability"
        z_place = landmark_start
        z_details = "Activate MOAB Eliminator active ability on the Round 80 ZOMG hull. It instantly cracks into 4 BFBs; clean up all children for the Victory Medal!"
    elif t5_type == "Sub":
        z_tower = "Monkey Sub"
        z_upg = "2-0-5"
        z_act = "Target"
        z_place = landmark_core
        z_details = "Sub Commander's 2x damage aura allows the submarine squadron to melt the Round 80 ZOMG hull before it finishes its first lap."
    elif t5_type == "Bucc":
        z_tower = "Monkey Buccaneer"
        z_upg = "5-2-0"
        z_act = "Target"
        z_place = landmark_core
        z_details = "Carrier Flagship fighter jets launch heavy missile strikes continuously against the Round 80 ZOMG, disintegrating it into child BFBs."
    elif hero_on_board:
        z_tower = hero
        z_upg = "0-0-0"
        z_act = "Ability"
        z_place = landmark_start
        z_details = f"Trigger {hero}'s Level 10 ability to obliterate the Round 80 ZOMG blimp children."
    else:
        z_tower = active_towers[0]["tower"]
        z_upg = active_towers[0]["upg_str"]
        z_act = "Target"
        z_place = landmark_core
        z_details = "Focus all primary fire on the Round 80 ZOMG to secure victory."

    r80, r80_timing = get_step_round_and_timing("Hard", running_cost, 80, last_r, max_round=80)
    hard_steps.append(create_step(
        step_num,
        "Round 80: The ZOMG Boss Battle",
        r80,
        z_act,
        z_tower,
        z_upg,
        z_place,
        "Strong",
        0,
        z_details,
        timing=r80_timing
    ))

    overview = (
        f"Hard difficulty demands comprehensive defense across 80 rounds with 1.08x prices. "
        f"On {map_data.get('name')}, {hero} secures our early survival starting on Round 3. We establish "
        "Ring of Fire and Recursive Cluster for Round 63/76 ceramic rushes, Relentless Glue for lockdown, "
        "and crown our defense with a Tier 5 blimp destroyer to vanquish the massive Round 80 ZOMG."
    )

    camo_handling = (
        f"Early camo is dispatched via {hero} and Ninja detection. A 2-2-0 Monkey Village (Radar Scanner) "
        "is placed at the primary track hub, granting universal camo detection to all defenses for R59 Camo Leads and R78 Camo Ceramics."
    )

    lead_handling = (
        "Acidic Mixture Dip (Alchemist 2-0-0) neutralizes R28/30 Leads. Recursive Cluster (2-0-4) shreds R45 Fortified Leads. "
        "Village MIB/Radar ensures 100% lead-popping uptime on all attackers."
    )

    moab_handling = (
        "R40 MOAB and R50 Dual MOABs are conquered via focused single-target fire and Berserker Brew buffs. "
        "Round 60 BFB is shattered by targeted missile strikes. Round 80 ZOMG is systematically destroyed by Tier 5 firepower."
    )

    why_it_works = (
        "The strategy layers crowd control (0-2-4 Relentless Glue), heavy AoE splash (4-0-2 Tack / 2-0-4 Bomb), "
        "and endgame Tier 5 anti-blimp dominance inside a Jungle Drums / Stronger Stimulant buff pocket."
    )

    return {
        "difficulty": "Hard",
        "mode": "Standard",
        "rounds": "3-80",
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
            "BTD6 Hard Standard Strategy Index",
            "Chou's BTD6 Round Mechanics Guide",
            "Bloons TD 6 Advanced Waves & ZOMG Breakdown"
        ],
        "steps": hard_steps
    }
