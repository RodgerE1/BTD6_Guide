import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from btd6_replay import validate_strategy

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

easy_fails = []
for mid, mdata in all_maps.items():
    strat = mdata.get("difficulties", {}).get("Easy")
    if not strat:
        easy_fails.append((mid, ["Missing Easy"]))
        continue
    ok, errs, warns, _ = validate_strategy(strat, map_context=mdata, diff_name="Easy")
    if not ok:
        easy_fails.append((mid, errs))

print(f"Total Easy fails: {len(easy_fails)}")
for mid, errs in easy_fails:
    print(f"--- {mid} ---")
    for e in errs:
        print("  ", e)
