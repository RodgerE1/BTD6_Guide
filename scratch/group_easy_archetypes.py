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

archetypes = {}
for mid, mdata in all_maps.items():
    strat = mdata.get("difficulties", {}).get("Easy")
    if not strat:
        continue
    ok, errs, _, _ = validate_strategy(strat, map_context=mdata, diff_name="Easy")
    if not ok:
        # Get signature of steps
        sig = tuple((s.get("round"), s.get("action"), s.get("tower"), s.get("upgrade")) for s in strat["steps"])
        if sig not in archetypes:
            archetypes[sig] = []
        archetypes[sig].append(mid)

print(f"Total failing archetypes: {len(archetypes)}")
for idx, (sig, maps) in enumerate(archetypes.items()):
    print(f"\n--- Archetype {idx+1} ({len(maps)} maps): {maps} ---")
    for s in sig:
        print("  ", s)
