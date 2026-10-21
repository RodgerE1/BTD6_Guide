import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from btd6_replay import validate_strategy

def apply_fixes_to_map(mdata):
    strat = mdata.get("difficulties", {}).get("Easy")
    if not strat:
        return
    steps = strat["steps"]
    mid = mdata.get("id")

    # Archetype 1, 4, 5: Naval maps
    if mid in ['lotus_island', 'spa_pits', 'downstream', 'water_park', 'luminous_cove', 'protect_the_yacht', 'off_the_coast', 'bazaar', 'cargo']:
        # Replace steps 6, 7, 8
        s1_5 = steps[:5]
        s_hero = strat.get("recommended_hero", "Sauda")
        # Ensure step 5 has canonical cost
        s1_5[4]["cost_estimate"] = 3485
        
        # New step 6: Place Sub 2-0-0
        new_s6 = {
            "step_number": 6,
            "round_range": "Rounds 21–30: Camo and Lead Preparation",
            "round": 27,
            "action": "Place",
            "tower": "Monkey Sub",
            "upgrade": "2-0-0",
            "placement": steps[5].get("placement", "Lagoon next to Buccaneer."),
            "targeting": "First",
            "cost_estimate": 810,
            "details": "Advanced Intel provides global camo and dart coverage.",
            "timing": "before_round"
        }
        # New step 7: Upgrade Sub 2-0-3
        new_s7 = {
            "step_number": 7,
            "round_range": "Rounds 31–39: Midgame Defense",
            "round": 32,
            "action": "Upgrade",
            "tower": "Monkey Sub",
            "upgrade": "2-0-3",
            "placement": steps[5].get("placement", "Lagoon next to Buccaneer."),
            "targeting": "First",
            "cost_estimate": 2165,
            "details": "Triple Guns dramatically scales up fast-firing dart output.",
            "timing": "before_round"
        }
        # New step 8: Place Alchemist 3-0-0
        new_s8 = {
            "step_number": 8,
            "round_range": "Rounds 31–39: Midgame Defense",
            "round": 36,
            "action": "Place",
            "tower": "Alchemist",
            "upgrade": "3-0-0",
            "placement": steps[6].get("placement", "On the shore within range of Buccaneer."),
            "targeting": "Close",
            "cost_estimate": 2040,
            "details": "Berserker Brew directly enhances Destroyer attack speed and damage.",
            "timing": "before_round"
        }
        # New step 9: Place Bomb Shooter 0-3-0 or 0-3-2
        bomb_upg = steps[7].get("upgrade", "0-3-0") if len(steps) > 7 else "0-3-0"
        bomb_cost = 1930 if bomb_upg == "0-3-0" else 2415
        new_s9 = {
            "step_number": 9,
            "round_range": "Round 40: MOAB Battle",
            "round": 38,
            "action": "Place",
            "tower": "Bomb Shooter",
            "upgrade": bomb_upg,
            "placement": steps[7].get("placement", "Along the track bend."),
            "targeting": "Strong",
            "cost_estimate": bomb_cost,
            "details": "MOAB Mauler targets the blimp; Destroyer and Sub clean up ceramics effortlessly.",
            "timing": "before_round"
        }
        strat["steps"] = s1_5 + [new_s6, new_s7, new_s8, new_s9]

    # Archetype 2, 6, 7, 9, 11, 12: Sub step 3 timing during_round
    elif mid in ['cracked', 'spring_spring', 'erosion', 'sunken_columns', 'peninsula', 'high_finance', 'muddy_puddles', 'bloody_puddles', 'ouch', 'sanctuary', 'pat_s_pond', 'dark_castle', 'flooded_valley']:
        steps[2]["timing"] = "during_round"

    # Archetype 3: firing_range
    elif mid == 'firing_range':
        steps[4]["round"] = 24
        steps[5]["timing"] = "during_round"
        steps[6]["timing"] = "during_round"
        steps[7]["timing"] = "during_round"

    # Archetype 8: geared
    elif mid == 'geared':
        steps[4]["round"] = 24

    # Archetype 10: mesa, x_factor, quad, ravine, glacial_trail
    elif mid in ['mesa', 'x_factor', 'quad', 'ravine', 'glacial_trail']:
        steps[4]["round"] = 24
        steps[5]["timing"] = "during_round"
        steps[6]["timing"] = "during_round"

    # Archetype 13: infernal
    elif mid == 'infernal':
        steps[5]["round"] = 30
        steps[6]["round"] = 35
        steps[6]["timing"] = "during_round"

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

for mid, mdata in all_maps.items():
    apply_fixes_to_map(mdata)

still_failing = []
for mid, mdata in all_maps.items():
    strat = mdata.get("difficulties", {}).get("Easy")
    ok, errs, warns, _ = validate_strategy(strat, map_context=mdata, diff_name="Easy")
    if not ok:
        still_failing.append((mid, errs))

print(f"Total maps checked: {len(all_maps)}")
print(f"Total still failing: {len(still_failing)}")
if still_failing:
    for mid, errs in still_failing:
        print(f"--- {mid} ---")
        for e in errs:
            print("  ", e)
else:
    print("[SUCCESS] ALL 87 EASY STRATEGIES PASS VALIDATION!")
