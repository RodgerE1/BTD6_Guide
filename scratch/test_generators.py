import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from map_data_medium import build_medium_strategy
from map_data_hard import build_hard_strategy
from btd6_replay import validate_strategy
from btd6_economy import get_action_canonical_cost, parse_upgrade

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

print(f"Total maps loaded: {len(all_maps)}")

med_fails = []
hard_fails = []

for mid, mdata in all_maps.items():
    med_strat = build_medium_strategy(mid, mdata)
    ok_m, errs_m, _, _ = validate_strategy(med_strat, map_context=mdata, diff_name="Medium")
    if not ok_m:
        med_fails.append((mid, errs_m))

    mdata["difficulties"]["Medium"] = med_strat
    hard_strat = build_hard_strategy(mid, mdata)
    ok_h, errs_h, _, _ = validate_strategy(hard_strat, map_context=mdata, diff_name="Hard")
    if not ok_h:
        hard_fails.append((mid, errs_h))

print(f"Medium failures: {len(med_fails)}")
if med_fails:
    print("Sample Med fail:", med_fails[0])

print(f"Hard failures: {len(hard_fails)}")
if hard_fails:
    print("Sample Hard fail:", hard_fails[0])
