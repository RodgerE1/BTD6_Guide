import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from map_data_medium import build_medium_strategy
from map_data_hard import build_hard_strategy
from btd6_replay import validate_strategy, normalize_map_strategies

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

normalize_map_strategies(all_maps)

for mid, mdata in all_maps.items():
    mdata["difficulties"]["Medium"] = build_medium_strategy(mid, mdata)
    mdata["difficulties"]["Hard"] = build_hard_strategy(mid, mdata)

fails = []
total = 0
for mid, mdata in all_maps.items():
    for diff in ["Easy", "Medium", "Hard"]:
        strat = mdata.get("difficulties", {}).get(diff)
        if not strat:
            fails.append((mid, diff, ["Missing strategy"]))
            continue
        total += 1
        ok, errs, warns, _ = validate_strategy(strat, map_context=mdata, diff_name=diff)
        if not ok:
            fails.append((mid, diff, errs))

print(f"Total strategies validated: {total}")
print(f"Total failures: {len(fails)}")
if fails:
    for mid, diff, errs in fails[:10]:
        print(f"--- {mid} [{diff}] ---")
        for e in errs:
            print("  ", e)
else:
    print("[SUCCESS] ALL 261 STRATEGIES PASS 100% VALIDATION!")
