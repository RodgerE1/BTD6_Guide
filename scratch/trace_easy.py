import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from map_data_beginner import BEGINNER_MAPS
from btd6_replay import TowerReplayEngine
from btd6_economy import get_cash_available

strat = BEGINNER_MAPS['lotus_island']['difficulties']['Easy']
eng = TowerReplayEngine('Easy')
for i, s in enumerate(strat['steps']):
    ok, err = eng.apply_step(s, i+1)
    r = s.get('round')
    c_before = get_cash_available('Easy', r, 'before_round')
    c_during = get_cash_available('Easy', r, 'during_round')
    print(f"Step {i+1} (R{r}): {s.get('action')} {s.get('tower')} {s.get('upgrade')} | cost={s.get('cost')} | cum_spent={eng.cumulative_cost_spent} | cash_avail(R{r})={c_before}/{c_during} | err={err}")
