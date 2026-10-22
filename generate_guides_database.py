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
from map_data_impoppable import build_impoppable_strategy
from heroes_data import get_best_hero_for_map, get_strategy_hero_intel
from btd6_economy import get_cash_available
from btd6_replay import (
    validate_strategy,
    normalize_map_strategies,
    assign_explicit_tower_ids,
    prepare_and_validate_strategy,
    resolve_strategy_perks,
    TowerReplayEngine,
)

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
            mdata["difficulties"]["Medium"] = build_medium_strategy(mid, mdata)
            mdata["difficulties"]["Hard"] = build_hard_strategy(mid, mdata)
            mdata["difficulties"]["Impoppable"] = build_impoppable_strategy(mid, mdata)

            # Assign hero tactical reason and synergies tailored to each difficulty's build hero
            for diff in ["Easy", "Medium", "Hard", "Impoppable"]:
                diff_strat = mdata["difficulties"].get(diff)
                if not diff_strat:
                    continue
                s_hero = diff_strat.get("recommended_hero") or hero_intel["best_hero"]
                strat_hero_intel = get_strategy_hero_intel(s_hero, mid, mdata, difficulty=diff)
                diff_strat["best_hero_reason"] = strat_hero_intel["reason"]
                diff_strat["hero_synergies"] = strat_hero_intel["synergies"]
                if not diff_strat.get("hero_alternatives"):
                    diff_strat["hero_alternatives"] = strat_hero_intel["alternatives"]

        # Apply any saved user overrides for this map
        if mid in user_overrides:
            for diff, override_strat in user_overrides[mid].items():
                if diff in mdata.get("difficulties", {}):
                    mdata["difficulties"][diff] = override_strat
                    print(f"Preserved user override for {mid} [{diff}]")

        # Assign explicit tower IDs, stable step IDs, sync exact costs, and validate
        for diff in ["Easy", "Medium", "Hard", "Impoppable"]:
            strat = mdata.get("difficulties", {}).get(diff)
            if not strat:
                continue

            is_draft = strat.get("status") in ("Draft", "Needs Review", "Unverified Draft")
            is_valid, val_errs, _, prep_strat = prepare_and_validate_strategy(
                strat,
                map_context=mdata,
                diff_name=diff,
                map_id=mid,
                strict_threats=(not is_draft),
                sync_costs=True
            )
            if not is_valid:
                raise ValueError(f"Strategy {mid} [{diff}] failed pre-validation:\n" + "\n".join(val_errs[:5]))
            mdata["difficulties"][diff] = prep_strat

    # Sort maps alphabetically by map name
    sorted_maps = dict(sorted(all_maps.items(), key=lambda item: item[1]["name"].lower()))

    # Build top-level database structure
    database = {
        "version": "1.5.0",
        "last_updated": datetime.date.today().isoformat(),
        "total_maps": len(sorted_maps),
        "supported_difficulties": ["Easy", "Medium", "Hard", "Impoppable"],
        "future_expansion_difficulties": ["CHIMPS"],
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
        for diff in ["Easy", "Medium", "Hard", "Impoppable"]:
            st = m["difficulties"].get(diff, {}).get("status", "Needs Review")
            statuses[st] = statuses.get(st, 0) + 1

    total_strat = len(sorted_maps) * 4
    print(f"\nStrategy Verification Breakdown:")
    for st_name, count in statuses.items():
        if count > 0:
            print(f"  - {st_name:24} {count:3} / {total_strat}")

if __name__ == "__main__":
    compile_database()
