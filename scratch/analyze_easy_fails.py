import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from btd6_replay import validate_strategy, TowerReplayEngine
from btd6_economy import get_cash_available, get_action_canonical_cost

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

for mid, mdata in all_maps.items():
    strat = mdata.get("difficulties", {}).get("Easy")
    if not strat:
        continue
    ok, errs, _, _ = validate_strategy(strat, map_context=mdata, diff_name="Easy")
    if not ok:
        print(f"\n==================== {mid} ====================")
        for e in errs:
            print("ERROR:", e)
        # Show all steps and running costs
        eng = TowerReplayEngine("Easy")
        for i, s in enumerate(strat["steps"]):
            # compute canonical cost
            act = s.get("action")
            tower = s.get("tower")
            upg_str = s.get("upgrade")
            r = s.get("round")
            timing = s.get("timing", "before_round")
            ok_step, err_step = eng.apply_step(s, i+1)
            spent = eng.cumulative_cost_spent
            cb = get_cash_available("Easy", r, "before_round")
            cd = get_cash_available("Easy", r, "during_round")
            print(f"  Step {i+1}: R{r} ({timing}) | {act} {tower} {upg_str} | spent={spent} (before={cb}, during={cd}) | step_ok={ok_step}")
