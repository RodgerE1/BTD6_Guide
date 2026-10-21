import os, sys
sys.path.insert(0, r"c:\Users\rodge\OneDrive\Desktop\BTD6_Guide")
from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS

all_maps = {}
all_maps.update(BEGINNER_MAPS)
all_maps.update(INTERMEDIATE_MAPS)
all_maps.update(ADVANCED_MAPS)
all_maps.update(EXPERT_MAPS)

def parse_upgrade(upg_str):
    if upg_str in ("Various", "None"):
        return None
    parts = upg_str.split("-")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        return tuple(int(p) for p in parts)
    return None

def is_legal_crosspath(t):
    if t is None:
        return True
    top, mid, bot = t
    if any(p < 0 or p > 5 for p in t):
        return False
    # at most two paths > 0
    non_zeros = sum(1 for p in t if p > 0)
    if non_zeros > 2:
        return False
    # at most one path > 2
    greater_than_2 = sum(1 for p in t if p > 2)
    if greater_than_2 > 1:
        return False
    return True

errors = []
for mid, m in all_maps.items():
    easy = m['difficulties']['Easy']
    active_towers = {} # tower_name -> list of current upgrades
    for s in easy['steps']:
        act = s.get('action')
        tower = s.get('tower')
        upg = parse_upgrade(s.get('upgrade', ''))
        step_num = s.get('step_number')
        
        if upg and not is_legal_crosspath(upg):
            errors.append(f"{mid} Easy Step {step_num}: illegal crosspath {upg}")

        if act == "Place":
            if tower not in active_towers:
                active_towers[tower] = []
            active_towers[tower].append(upg or (0,0,0))
        elif act == "Upgrade":
            if tower not in active_towers or len(active_towers[tower]) == 0:
                errors.append(f"{mid} Easy Step {step_num}: upgrading '{tower}' which was never placed!")
            else:
                # Find matching or compatible tower
                compat = False
                for idx, existing in enumerate(active_towers[tower]):
                    # can upgrade if upg >= existing on all paths
                    if upg and all(u >= e for u, e in zip(upg, existing)):
                        active_towers[tower][idx] = upg
                        compat = True
                        break
                if not compat and upg:
                    errors.append(f"{mid} Easy Step {step_num}: upgrading '{tower}' to {upg} drops levels from {active_towers[tower]}!")
        elif act in ("Target", "Ability"):
            if tower not in active_towers and "Hero" not in tower and tower != "Defense Fleet":
                errors.append(f"{mid} Easy Step {step_num}: {act} on '{tower}' which is not in active towers {list(active_towers.keys())}")

print(f"Total Easy errors found: {len(errors)}")
for e in errors[:10]:
    print("  ", e)
