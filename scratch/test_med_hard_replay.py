import os, sys, json
sys.path.insert(0, r"c:\Users\rodge\OneDrive\Desktop\BTD6_Guide")
from scratch.test_easy_replay import parse_upgrade, is_legal_crosspath

with open(r"c:\Users\rodge\OneDrive\Desktop\BTD6_Guide\guides.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for diff in ["Medium", "Hard"]:
    errors = []
    for mid, m in data["maps"].items():
        strat = m["difficulties"].get(diff)
        if not strat:
            errors.append(f"{mid} missing {diff}")
            continue
        active_towers = {}
        for s in strat["steps"]:
            act = s.get("action")
            tower = s.get("tower")
            upg = parse_upgrade(s.get("upgrade", ""))
            step_num = s.get("step_number")

            if upg and not is_legal_crosspath(upg):
                errors.append(f"{mid} {diff} Step {step_num}: illegal crosspath {upg}")

            if act == "Place":
                if tower not in active_towers:
                    active_towers[tower] = []
                active_towers[tower].append(upg or (0,0,0))
            elif act == "Upgrade":
                if tower not in active_towers or len(active_towers[tower]) == 0:
                    errors.append(f"{mid} {diff} Step {step_num}: upgrading '{tower}' which was never placed!")
                else:
                    compat = False
                    for idx, existing in enumerate(active_towers[tower]):
                        if upg and all(u >= e for u, e in zip(upg, existing)):
                            active_towers[tower][idx] = upg
                            compat = True
                            break
                    if not compat and upg:
                        errors.append(f"{mid} {diff} Step {step_num}: upgrading '{tower}' to {upg} drops levels from {active_towers[tower]}!")
            elif act in ("Target", "Ability"):
                if tower not in active_towers and "Hero" not in tower and tower not in ("Defense Fleet", "Radar Scanner & Defense"):
                    errors.append(f"{mid} {diff} Step {step_num}: {act} on '{tower}' which is not in active towers {list(active_towers.keys())}")

    print(f"Total {diff} replay errors found: {len(errors)}")
    for e in errors[:10]:
        print("  ", e)
