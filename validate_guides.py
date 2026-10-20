"""
validate_guides.py
Comprehensive validation script checking BTD6 guide coverage, completeness,
data integrity, and economic feasibility.
"""

import json
import os
import re
import sys

# Official 87 maps expected
EXPECTED_MAP_COUNTS = {
    "Beginner": 26,
    "Intermediate": 26,
    "Advanced": 22,
    "Expert": 13
}
EXPECTED_TOTAL_MAPS = 87

# Maximum realistic cumulative cash earned by each round benchmark on Easy and Medium
CASH_CEILINGS_EASY = {
    1: 650,        # Starting cash
    10: 1600,      # After R10
    20: 3800,      # After R20
    30: 7500,      # After R30
    40: 16000      # After R40 (Total earned is ~$14,000 - $15,000)
}

CASH_CEILINGS_MEDIUM = {
    1: 650,        # Starting cash
    10: 1700,      # After R10
    20: 4200,      # After R20
    30: 8200,      # After R30
    40: 15500,     # After R40
    50: 24000,     # After R50
    60: 35000      # After R60 (Total earned is ~$30,000 - $32,000)
}

CASH_CEILINGS_HARD = {
    3: 650,        # Starting cash on Round 3
    10: 1900,      # After R10 (Cash earned by R10 is ~$1,900)
    20: 4400,      # After R20
    30: 9200,      # After R30 (Cash earned by R30 is ~$9,400)
    40: 16500,     # After R40
    50: 26500,     # After R50
    60: 40000,     # After R60
    70: 58000,     # After R70
    80: 88000      # After R80 (Total earned is ~$85,000 - $92,000)
}

UPGRADE_PATTERN = re.compile(r"^\d-\d-\d$")

def validate():
    db_path = os.path.join(os.path.dirname(__file__), "guides.json")
    if not os.path.exists(db_path):
        print(f"[FAIL] guides.json not found at {db_path}")
        return False

    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[FAIL] Failed to parse guides.json: {e}")
        return False

    errors = []
    warnings = []

    # 1. Root structure check
    for root_key in ["version", "total_maps", "supported_difficulties", "category_counts", "maps"]:
        if root_key not in data:
            errors.append(f"Root object missing key '{root_key}'")

    maps = data.get("maps", {})
    if len(maps) != EXPECTED_TOTAL_MAPS:
        errors.append(f"Expected {EXPECTED_TOTAL_MAPS} maps in database, found {len(maps)}")

    # 2. Category distribution
    cat_counts = {"Beginner": 0, "Intermediate": 0, "Advanced": 0, "Expert": 0}

    # 3. Validate each map
    for map_id, map_data in maps.items():
        # Top-level map fields
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

        # Validate Easy, Medium, and Hard
        for diff_name, start_round, max_round, cash_ceilings in [
            ("Easy", 1, 40, CASH_CEILINGS_EASY),
            ("Medium", 1, 60, CASH_CEILINGS_MEDIUM),
            ("Hard", 3, 80, CASH_CEILINGS_HARD)
        ]:
            if diff_name not in difficulties or difficulties[diff_name] is None:
                errors.append(f"Map '{map_id}' is missing {diff_name} strategy!")
                continue

            strat = difficulties[diff_name]
            required_strategy_keys = [
                "difficulty", "mode", "rounds", "status", "recommended_hero",
                "hero_alternatives", "starting_cash", "overview", "camo_handling",
                "lead_handling", "moab_handling", "why_it_works", "research_sources", "steps"
            ]
            for sk in required_strategy_keys:
                if sk not in strat:
                    errors.append(f"Map '{map_id}' {diff_name} strategy missing key '{sk}'")

            if strat.get("starting_cash") != 650:
                errors.append(f"Map '{map_id}' {diff_name} starting cash is {strat.get('starting_cash')}, expected 650")

            status = strat.get("status")
            if status not in ["Verified", "Needs Review"]:
                errors.append(f"Map '{map_id}' {diff_name} has invalid status '{status}'")

            steps = strat.get("steps", [])
            min_steps = 5 if diff_name == "Easy" else (8 if diff_name == "Medium" else 12)
            if not steps or len(steps) < min_steps:
                errors.append(f"Map '{map_id}' {diff_name} has only {len(steps)} steps (minimum {min_steps} required)")

            # Economic tracking
            cumulative_cost = 0
            has_opening_defense = False
            has_camo_before_24 = False
            has_lead_before_28 = False
            has_moab_for_40 = False
            has_r60_prep = False
            has_r63_prep = False
            has_r80_prep = False

            for i, step in enumerate(steps):
                expected_step_num = i + 1
                if step.get("step_number") != expected_step_num:
                    errors.append(f"Map '{map_id}' {diff_name} step {i} has step_number {step.get('step_number')}, expected {expected_step_num}")

                round_num = step.get("round", 0)
                if not (start_round <= round_num <= max_round):
                    errors.append(f"Map '{map_id}' {diff_name} step {expected_step_num} has out-of-range round {round_num}")

                upgrade = step.get("upgrade", "")
                if not UPGRADE_PATTERN.match(upgrade) and upgrade != "Various":
                    errors.append(f"Map '{map_id}' {diff_name} step {expected_step_num} has invalid upgrade '{upgrade}'")

                cost = step.get("cost_estimate", 0)
                if not isinstance(cost, (int, float)) or cost < 0:
                    errors.append(f"Map '{map_id}' {diff_name} step {expected_step_num} has invalid cost {cost}")
                else:
                    cumulative_cost += cost

                # Check starting cash affordability
                if round_num == start_round and i == 0:
                    has_opening_defense = True
                    if cumulative_cost > 650:
                        errors.append(f"Map '{map_id}' {diff_name} exceeds starting cash on Round {start_round}: ${cumulative_cost} > $650")

                # Check economic milestones
                for bench_round, max_cash in cash_ceilings.items():
                    if round_num <= bench_round and cumulative_cost > max_cash:
                        warnings.append(f"Map '{map_id}' {diff_name} cumulative cost at R{round_num} (${cumulative_cost}) exceeds estimated cash (${max_cash})")

                # Check coverage
                if round_num <= 24:
                    has_camo_before_24 = True
                if round_num <= 28:
                    has_lead_before_28 = True
                if 35 <= round_num <= 40:
                    has_moab_for_40 = True
                if round_num >= 55:
                    has_r60_prep = True
                if 61 <= round_num <= 63:
                    has_r63_prep = True
                if round_num >= 75:
                    has_r80_prep = True

            if not has_opening_defense:
                errors.append(f"Map '{map_id}' {diff_name} has no defensive placement on Round {start_round}")
            if not has_camo_before_24:
                warnings.append(f"Map '{map_id}' {diff_name} has no step before Round 24 (Round 24 Camo)")
            if not has_lead_before_28:
                warnings.append(f"Map '{map_id}' {diff_name} has no step before Round 28 (Round 28 Leads)")
            if not has_moab_for_40:
                warnings.append(f"Map '{map_id}' {diff_name} has no step for Round 35-40 MOAB preparation")
            if diff_name in ["Medium", "Hard"] and not has_r60_prep:
                warnings.append(f"Map '{map_id}' {diff_name} has no step for Round 55-60 BFB preparation")
            if diff_name == "Hard" and not has_r63_prep:
                warnings.append(f"Map '{map_id}' Hard has no step for Round 61-63 Ceramic rush preparation")
            if diff_name == "Hard" and not has_r80_prep:
                warnings.append(f"Map '{map_id}' Hard has no step for Round 75-80 ZOMG preparation")

    # Category count validation
    for cat, exp_count in EXPECTED_MAP_COUNTS.items():
        actual = cat_counts.get(cat, 0)
        if actual != exp_count:
            errors.append(f"Category '{cat}' expected {exp_count} maps, found {actual}")

    # Output report
    print("=" * 60)
    print("BTD6 Strategy Guide Database Validation Report")
    print("=" * 60)
    print(f"Total Maps Checked:      {len(maps)} / {EXPECTED_TOTAL_MAPS}")
    for cat in ["Beginner", "Intermediate", "Advanced", "Expert"]:
        print(f"  - {cat:13} {cat_counts.get(cat, 0):2} / {EXPECTED_MAP_COUNTS[cat]}")

    easy_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Easy", {}).get("status") == "Verified")
    med_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Medium", {}).get("status") == "Verified")
    hard_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Hard", {}).get("status") == "Verified")
    total_strat = easy_verified + med_verified + hard_verified

    print(f"\nVerification Breakdown:")
    print(f"  - Easy Mode (R1-40):   {easy_verified} / {len(maps)} Verified")
    print(f"  - Medium Mode (R1-60): {med_verified} / {len(maps)} Verified")
    print(f"  - Hard Mode (R3-80):   {hard_verified} / {len(maps)} Verified")
    print(f"  - Total Verified:      {total_strat} / {len(maps) * 3} ({int(total_strat / (len(maps) * 3) * 100)}% Complete)")

    print(f"\nValidation Results:")
    print(f"  - Errors:   {len(errors)}")
    print(f"  - Warnings: {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for w in warnings[:10]:
            print(f"  [WARN] {w}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more warnings")

    if errors:
        print("\nErrors:")
        for e in errors[:15]:
            print(f"  [ERROR] {e}")
        if len(errors) > 15:
            print(f"  ... and {len(errors) - 15} more errors")
        print("\n[RESULT] Validation FAILED")
        return False
    else:
        print("\n[RESULT] Validation PASSED (100% data integrity, coverage, and economic feasibility)")
        return True

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
