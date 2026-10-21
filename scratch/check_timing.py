import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from btd6_economy import get_cash_available

with open('guides.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

for mid, m in db['maps'].items():
    strat = m['difficulties'].get('Easy')
    if not strat:
        continue
    cum = 0
    for s in strat['steps']:
        cum += s.get('cost_estimate', 0)
        r = s.get('round', 1)
        cash_b = get_cash_available('Easy', r, 'before_round')
        cash_d = get_cash_available('Easy', r, 'during_round')
        if cum > cash_b:
            snum = s.get('step_number')
            if cum <= cash_d:
                print(f"{mid} Easy Step {snum}: R{r} cum={cum} > cash_before={cash_b} <= cash_during={cash_d}")
            else:
                print(f"OVER DURING: {mid} Easy Step {snum}: R{r} cum={cum} > cash_during={cash_d}")
