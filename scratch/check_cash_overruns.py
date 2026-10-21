import json, sys
sys.path.insert(0, ".")
from btd6_economy import get_cumulative_cash_ceiling

with open("guides.json", "r", encoding="utf-8") as f:
    data = json.load(f)

over_steps = []
for mid, m in data["maps"].items():
    for diff in ["Easy", "Medium", "Hard"]:
        strat = m["difficulties"].get(diff)
        if not strat:
            continue
        cum = 0
        for s in strat["steps"]:
            cum += s.get("cost_estimate", 0)
            r = s.get("round", 1)
            ceil = get_cumulative_cash_ceiling(diff, r)
            if cum > ceil:
                over_steps.append((mid, diff, s.get("step_number"), r, cum, ceil, cum - ceil))

print(f"Total steps over ceiling: {len(over_steps)}")
over_steps.sort(key=lambda x: x[6], reverse=True)
for x in over_steps[:20]:
    print(f"{x[0]} {x[1]} Step {x[2]} (R{x[3]}): cum=${x[4]} > ceil=${x[5]} (diff=+${x[6]})")
