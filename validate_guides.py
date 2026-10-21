"""
validate_guides.py
Comprehensive, rigorous validation and replay engine for BTD6 strategy database.
Enforces structural integrity, legal state transitions, crosspath legality,
economic feasibility, and active tactical capability coverage using the shared btd6_replay engine.
"""

import json
import os
import sys

from btd6_economy import (
    ALL_VALID_TOWERS,
    CANONICAL_HEROES,
    DIFF_MULTIPLIERS,
    get_cumulative_cash_ceiling,
    get_tower_capabilities,
    is_legal_crosspath,
    parse_upgrade,
)
from btd6_replay import TowerReplayEngine, validate_strategy

EXPECTED_MAP_COUNTS = {
    "Beginner": 26,
    "Intermediate": 26,
    "Advanced": 22,
    "Expert": 13
}
EXPECTED_TOTAL_MAPS = 87

def validate_database(data=None, db_path=None):
    """
    Validates the BTD6 strategy guide database.
    Can accept a pre-loaded dict or load from db_path.
    Returns: (success: bool, errors: list, warnings: list, stats: dict)
    """
    if data is None:
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "guides.json")
        if not os.path.exists(db_path):
            return False, [f"Database file not found: {db_path}"], [], {}
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            return False, [f"Failed to parse database JSON: {e}"], [], {}

    errors = []
    warnings = []
    stats = {
        "total_maps": 0,
        "category_counts": {},
        "status_counts": {"Playtested": 0, "Structurally Validated": 0, "Verified": 0, "Needs Review": 0},
        "difficulty_counts": {"Easy": 0, "Medium": 0, "Hard": 0}
    }

    # 1. Root structure checks
    if not isinstance(data, dict):
        return False, [f"Database root must be a JSON dictionary object, found {type(data).__name__}."], [], stats

    required_root_keys = ["version", "total_maps", "supported_difficulties", "category_counts", "maps"]
    for k in required_root_keys:
        if k not in data:
            errors.append(f"Root object missing required key '{k}'")

    maps = data.get("maps")
    if not isinstance(maps, dict):
        errors.append(f"Root key 'maps' must be a dictionary, found {type(maps).__name__}")
        return False, errors, warnings, stats

    stats["total_maps"] = len(maps)
    if len(maps) != EXPECTED_TOTAL_MAPS:
        errors.append(f"Expected {EXPECTED_TOTAL_MAPS} maps in database, found {len(maps)}")

    # 2. Category distribution
    cat_counts = {"Beginner": 0, "Intermediate": 0, "Advanced": 0, "Expert": 0}

    # 3. Validate each map & each strategy
    for map_id, map_data in maps.items():
        if not isinstance(map_data, dict):
            errors.append(f"Map '{map_id}' must be a dictionary object.")
            continue

        required_map_keys = ["id", "name", "category", "terrain", "lanes", "water", "sight_blockers", "gimmick", "difficulties", "best_hero"]
        for k in required_map_keys:
            if k not in map_data:
                errors.append(f"Map '{map_id}' missing required key '{k}'")

        category = map_data.get("category")
        if category in cat_counts:
            cat_counts[category] += 1
        else:
            errors.append(f"Map '{map_id}' has invalid category '{category}'")

        difficulties = map_data.get("difficulties", {})
        if not isinstance(difficulties, dict):
            errors.append(f"Map '{map_id}' difficulties must be a dictionary.")
            continue

        for diff_name in ["Easy", "Medium", "Hard"]:
            if diff_name not in difficulties or difficulties[diff_name] is None:
                errors.append(f"Map '{map_id}' is missing {diff_name} strategy")
                continue

            strat = difficulties[diff_name]
            stats["difficulty_counts"][diff_name] = stats["difficulty_counts"].get(diff_name, 0) + 1

            status = strat.get("status", "Needs Review") if isinstance(strat, dict) else "Needs Review"
            stats["status_counts"][status] = stats["status_counts"].get(status, 0) + 1

            # Validate using shared strategy validator
            ok, strat_errors, strat_warnings, _ = validate_strategy(
                strat, map_context=map_data, diff_name=diff_name, strict_threats=True
            )
            if not ok:
                for err in strat_errors:
                    errors.append(f"Map '{map_id}' {diff_name}: {err}")
            for warn in strat_warnings:
                warnings.append(f"Map '{map_id}' {diff_name}: {warn}")

    stats["category_counts"] = cat_counts
    for cat, exp in EXPECTED_MAP_COUNTS.items():
        if cat_counts.get(cat, 0) != exp:
            errors.append(f"Category '{cat}' expected {exp} maps, found {cat_counts.get(cat, 0)}")

    success = len(errors) == 0
    return success, errors, warnings, stats

def run_cli_validation():
    print("=" * 65)
    print("BTD6 Strategy Guide Database — Rigorous Invariant Validation")
    print("=" * 65)

    success, errors, warnings, stats = validate_database()

    print(f"Total Maps Checked:      {stats.get('total_maps', 0)} / {EXPECTED_TOTAL_MAPS}")
    for cat in ["Beginner", "Intermediate", "Advanced", "Expert"]:
        print(f"  - {cat:13} {stats['category_counts'].get(cat, 0):2} / {EXPECTED_MAP_COUNTS[cat]}")

    print(f"\nVerification Breakdown:")
    for st_name, count in stats.get("status_counts", {}).items():
        if count > 0:
            print(f"  - {st_name:24} {count:3} / {EXPECTED_TOTAL_MAPS * 3}")

    print(f"\nValidation Diagnostics:")
    print(f"  - Invariant Violations (Errors): {len(errors)}")
    print(f"  - Optimization Warnings:         {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for w in warnings[:10]:
            print(f"  [WARN] {w}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more warnings")

    if errors:
        print("\nInvariant Violation Failures:")
        for e in errors[:20]:
            print(f"  [FAIL] {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")
        print("\n[RESULT] Database Validation FAILED.")
        return False
    else:
        print("\n[RESULT] Database Validation PASSED (100% Structural, Replay & Economic Invariants Satisfied)")
        return True

if __name__ == "__main__":
    ok = run_cli_validation()
    sys.exit(0 if ok else 1)
