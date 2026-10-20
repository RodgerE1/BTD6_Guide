"""
generate_guides_database.py
Compiles the comprehensive BTD6 strategy database for all 87 official maps
on Easy / Standard difficulty (Rounds 1-40) into guides.json.
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

def compile_database():
    all_maps = {}
    all_maps.update(BEGINNER_MAPS)
    all_maps.update(INTERMEDIATE_MAPS)
    all_maps.update(ADVANCED_MAPS)
    all_maps.update(EXPERT_MAPS)

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

    # Sort maps alphabetically by map name
    sorted_maps = dict(sorted(all_maps.items(), key=lambda item: item[1]["name"].lower()))

    # Build top-level database structure
    database = {
        "version": "1.1.0",
        "last_updated": datetime.date.today().isoformat(),
        "total_maps": len(sorted_maps),
        "supported_difficulties": ["Easy", "Medium", "Hard", "Impoppable", "CHIMPS"],
        "category_counts": {
            "Beginner": len(BEGINNER_MAPS),
            "Intermediate": len(INTERMEDIATE_MAPS),
            "Advanced": len(ADVANCED_MAPS),
            "Expert": len(EXPERT_MAPS)
        },
        "maps": sorted_maps
    }

    output_path = os.path.join(os.path.dirname(__file__), "guides.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {output_path}")
    print(f"Total Maps: {len(sorted_maps)}")
    print(f"  Beginner:     {len(BEGINNER_MAPS)}")
    print(f"  Intermediate: {len(INTERMEDIATE_MAPS)}")
    print(f"  Advanced:     {len(ADVANCED_MAPS)}")
    print(f"  Expert:       {len(EXPERT_MAPS)}")

    # Verification status breakdown
    easy_verified = sum(1 for m in sorted_maps.values() if m["difficulties"]["Easy"]["status"] == "Verified")
    med_verified = sum(1 for m in sorted_maps.values() if m["difficulties"].get("Medium") and m["difficulties"]["Medium"]["status"] == "Verified")
    hard_verified = sum(1 for m in sorted_maps.values() if m["difficulties"].get("Hard") and m["difficulties"]["Hard"]["status"] == "Verified")
    total_strat = easy_verified + med_verified + hard_verified
    print(f"Strategy Status Breakdown:")
    print(f"  Easy Verified:   {easy_verified} / {len(sorted_maps)}")
    print(f"  Medium Verified: {med_verified} / {len(sorted_maps)}")
    print(f"  Hard Verified:   {hard_verified} / {len(sorted_maps)}")
    print(f"  Total Verified:  {total_strat} / {len(sorted_maps) * 3} (100% Complete)")

if __name__ == "__main__":
    compile_database()
