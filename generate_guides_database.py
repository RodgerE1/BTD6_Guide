"""
generate_guides_database.py
Compiles the comprehensive BTD6 strategy database for all 87 official maps
on Easy, Medium, and Hard difficulties into guides.json.
Validates all strategies before publishing, assigns stable step IDs,
and preserves user custom overrides across database regenerations.
"""

import json
import os
import datetime

from map_data_beginner import BEGINNER_MAPS
from map_data_intermediate import INTERMEDIATE_MAPS
from map_data_advanced import ADVANCED_MAPS
from map_data_expert import EXPERT_MAPS
from map_data_medium import build_medium_strategy
from map_data_hard import build_hard_strategy
from heroes_data import get_best_hero_for_map
from btd6_economy import get_cash_available
from btd6_replay import validate_strategy, normalize_map_strategies, assign_explicit_tower_ids, TowerReplayEngine

USER_OVERRIDES_PATH = os.path.join(os.path.dirname(__file__), "user_overrides.json")

def load_user_overrides():
    """Loads custom user-edited strategies so database regeneration never overwrites them."""
    if os.path.exists(USER_OVERRIDES_PATH):
        try:
            with open(USER_OVERRIDES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load user overrides ({e})")
    return {}

def compile_database(output_path=None):
    all_maps = {}

    def merge_maps(source, category_name):
        for mid, mdata in source.items():
            if mid in all_maps:
                raise ValueError(f"Duplicate map ID '{mid}' detected while loading {category_name} maps!")
            all_maps[mid] = mdata

    merge_maps(BEGINNER_MAPS, "Beginner")
    merge_maps(INTERMEDIATE_MAPS, "Intermediate")
    merge_maps(ADVANCED_MAPS, "Advanced")
    merge_maps(EXPERT_MAPS, "Expert")

    # Normalize early round progression and multi-tier pricing transitions
    normalize_map_strategies(all_maps)

    user_overrides = load_user_overrides()

    # Populate Medium and Hard difficulty strategies + Hero intelligence for all maps
    for mid, mdata in all_maps.items():
        hero_intel = get_best_hero_for_map(mid, mdata)
        mdata["best_hero"] = hero_intel["best_hero"]
        mdata["best_hero_reason"] = hero_intel["reason"]
        mdata["hero_alternatives"] = hero_intel["alternatives"]
        mdata["hero_synergies"] = hero_intel["synergies"]

        if "difficulties" in mdata:
            if mdata["difficulties"].get("Easy"):
                mdata["difficulties"]["Easy"]["best_hero_reason"] = hero_intel["reason"]
                mdata["difficulties"]["Easy"]["hero_synergies"] = hero_intel["synergies"]
            mdata["difficulties"]["Medium"] = build_medium_strategy(mid, mdata)
            if mdata["difficulties"].get("Medium"):
                mdata["difficulties"]["Medium"]["best_hero_reason"] = hero_intel["reason"]
                mdata["difficulties"]["Medium"]["hero_synergies"] = hero_intel["synergies"]
            mdata["difficulties"]["Hard"] = build_hard_strategy(mid, mdata)

        # Apply any saved user overrides for this map
        if mid in user_overrides:
            for diff, override_strat in user_overrides[mid].items():
                if diff in mdata.get("difficulties", {}):
                    mdata["difficulties"][diff] = override_strat
                    print(f"Preserved user override for {mid} [{diff}]")

        # Assign explicit tower IDs, stable step IDs, and sync exact costs for all steps
        for diff in ["Easy", "Medium", "Hard"]:
            strat = mdata.get("difficulties", {}).get(diff)
            if not strat:
                continue

            # 1. Assign persistent tower IDs
            assign_explicit_tower_ids(strat, mid, diff)

            # 2. Assign stable step IDs and sync cost_estimate with exact canonical pricing
            start_round = 3 if diff == "Hard" else 1
            max_round = 40 if diff == "Easy" else (60 if diff == "Medium" else 80)
            engine = TowerReplayEngine(difficulty=diff, start_round=start_round, max_round=max_round)
            for idx, s in enumerate(strat.get("steps", [])):
                if "step_id" not in s:
                    s["step_id"] = f"{mid}_{diff.lower()}_s{s.get('step_number', idx + 1)}"
                if "timing" not in s:
                    s["timing"] = "before_round"

                success, _ = engine.apply_step(s, idx)
                if success and engine.step_history:
                    exact_cost = engine.step_history[-1].get("cost", s.get("cost_estimate", 0))
                    s["cost_estimate"] = exact_cost

            # 3. Pre-validate before accepting into compilation
            is_draft = strat.get("status") in ("Draft", "Needs Review", "Unverified Draft")
            is_valid, val_errs, _, _ = validate_strategy(
                strat,
                map_context=mdata,
                diff_name=diff,
                strict_threats=(not is_draft)
            )
            if not is_valid:
                raise ValueError(f"Strategy {mid} [{diff}] failed pre-validation:\n" + "\n".join(val_errs[:5]))

    # Sort maps alphabetically by map name
    sorted_maps = dict(sorted(all_maps.items(), key=lambda item: item[1]["name"].lower()))

    # Build top-level database structure
    database = {
        "version": "1.4.0",
        "last_updated": datetime.date.today().isoformat(),
        "total_maps": len(sorted_maps),
        "supported_difficulties": ["Easy", "Medium", "Hard"],
        "future_expansion_difficulties": ["Impoppable", "CHIMPS"],
        "category_counts": {
            "Beginner": len(BEGINNER_MAPS),
            "Intermediate": len(INTERMEDIATE_MAPS),
            "Advanced": len(ADVANCED_MAPS),
            "Expert": len(EXPERT_MAPS)
        },
        "maps": sorted_maps
    }

    if output_path is None:
        output_path = os.path.join(os.path.dirname(__file__), "guides.json")
    temp_path = output_path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())

    os.replace(temp_path, output_path)

    print(f"Successfully generated {output_path}")
    print(f"Total Maps: {len(sorted_maps)}")
    print(f"  Beginner:     {len(BEGINNER_MAPS)}")
    print(f"  Intermediate: {len(INTERMEDIATE_MAPS)}")
    print(f"  Advanced:     {len(ADVANCED_MAPS)}")
    print(f"  Expert:       {len(EXPERT_MAPS)}")

    # Verification status breakdown
    statuses = {"Playtested": 0, "Structurally Validated": 0, "Verified": 0, "Needs Review": 0}
    for m in sorted_maps.values():
        for diff in ["Easy", "Medium", "Hard"]:
            st = m["difficulties"].get(diff, {}).get("status", "Needs Review")
            statuses[st] = statuses.get(st, 0) + 1

    total_strat = len(sorted_maps) * 3
    print(f"\nStrategy Verification Breakdown:")
    for st_name, count in statuses.items():
        if count > 0:
            print(f"  - {st_name:24} {count:3} / {total_strat}")

if __name__ == "__main__":
    compile_database()
