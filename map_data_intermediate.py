"""
map_data_intermediate.py
Contains comprehensive, round-by-round Easy/Standard (R1-40) strategies for all 26 Intermediate maps.
"""

def create_step(step_number, round_range, round_num, action, tower, upgrade, placement, targeting, cost, details, timing="before_round"):
    return {
        "step_number": step_number,
        "round_range": round_range,
        "round": round_num,
        "action": action,
        "tower": tower,
        "upgrade": upgrade,
        "placement": placement,
        "targeting": targeting,
        "cost_estimate": cost,
        "details": details,
        "timing": timing
    }

INTERMEDIATE_MAPS = {
    "balance": {
        "id": "balance",
        "name": "Balance",
        "category": "Intermediate",
        "terrain": "Stone Temple Spiral",
        "lanes": "Single path spiraling inwards to a central pit then out",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Concentric spiral where bloons circle a tiny central circular platform multiple times",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A symmetrical stone spiral leading directly into a small center pit. The central round pedestal is the single most dominant placement spot in BTD6, as bloons circle it four consecutive times.",
                "camo_handling": "Sauda placed dead-center in the spiral hits all camos naturally from Round 1. Ninja 3-0-1 placed adjacent provides backup.",
                "lead_handling": "Alchemist 2-0-0 or Sauda's level 3 ability destroys Lead Bloons on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive placed on the center circle next to Sauda sprays hundreds of tacks into the MOAB as it spirals, obliterating it before it reaches the center pit.",
                "why_it_works": "Towers placed in the center hit bloons continuously for almost 90% of the round duration.",
                "research_sources": ["Bloons Wiki - Balance", "BTD6 Intermediate Meta Guides"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly in the center circular platform of the spiral.", "First", 510, "Hits bloons on all 4 spiral revolutions."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "On the center circular platform right next to Sauda.", "First", 240, "Covers the entire inner spiral."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Center platform.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "On the outer edge of the center platform.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Center platform.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Center platform.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Center platform.", "First", 2800, "Overdrive completely vaporizes everything entering the spiral."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the path leading into the outer spiral.", "Strong", 2040, "MOAB Mauler weakens the blimp before it enters the center. Overdrive finishes it instantly.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "spice_islands": {
        "id": "spice_islands",
        "name": "Spice Islands",
        "category": "Intermediate",
        "terrain": "Tropical Archipelago",
        "lanes": "Single path weaving between small sandy oceanic islands",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Almost entirely open water with only small circular sandbars for land towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Admiral Brickell",
                "hero_alternatives": ["Sauda", "Quincy"],
                "starting_cash": 650,
                "overview": "A chain of small tropical sandbars surrounded by deep ocean water. The map is built for naval superiority, allowing Buccaneer and Sub spam to dominate.",
                "camo_handling": "Monkey Sub 2-0-0 with Advanced Intel or Buccaneer 0-2-2 Crow's Nest handles all camos with ease.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer + Sub 2-0-3 Triple Guns shreds the Round 40 MOAB in open ocean.",
                "why_it_works": "The entire map is water. Sub and Buccaneer have completely unrestricted line of sight across all islands.",
                "research_sources": ["Bloons Wiki - Spice Islands"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Monkey Sub", "0-0-0", "In the ocean channel between island 1 and island 2.", "First", 275, "High-velocity dart fire across the first crossing."),
                    create_step(2, "Rounds 1–10: Opening Defense", 4, "Place", "Dart Monkey", "0-0-0", "On the first small sandy island.", "First", 170, "Provides vision for Sub's Advanced Intel."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 10, "Upgrade", "Monkey Sub", "2-0-0", "Ocean channel.", "First", 595, "Advanced Intel allows Sub to shoot anywhere Dart Monkey can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 14, "Place", "Monkey Buccaneer", "0-0-0", "In the water next to island 2.", "First", 425, "Adds heavy cannon and grape fire."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 21, "Upgrade", "Monkey Buccaneer", "0-2-2", "Next to island 2.", "First", 890, "Hot Shot pops Leads on Round 28; Crow's Nest detects Camos."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Ocean channel.", "First", 1105, "Triple Guns rapidly fires darts across the map."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Buccaneer", "3-2-0", "Next to island 2.", "First", 2510, "Destroyer unleashes devastating grape volleys."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Monkey Sub", "2-0-4", "Ocean channel.", "First", 2125, "Armor Piercing Darts inflicts heavy blimp damage. The MOAB pops almost immediately upon entering.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "chutes": {
        "id": "chutes",
        "name": "Chutes",
        "category": "Intermediate",
        "terrain": "Tropical Beach Slides",
        "lanes": "Two alternating lanes down steep wooden water chutes",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Bloons alternate between the left and right chutes, requiring balanced defense across both tracks",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Two steep wooden chutes on a sandy beach. Bloons alternate sides every round. Placing towers in the central divide allows them to cover both tracks.",
                "camo_handling": "Quincy placed in the center hits camo from level 5. A 0-2-3 Dart Monkey in the center covers both lanes for Round 24 and 33.",
                "lead_handling": "Alchemist 2-0-0 or Bomb Shooter 0-3-0 in the central divide pops Leads on Round 28.",
                "moab_handling": "Bomb Shooter 0-3-2 MOAB Mauler in the center divide + 2-0-3 Spike Factory at the bottom exit guarantees the MOAB is destroyed.",
                "why_it_works": "Towers placed in the middle ridge reach both the left and right chute tracks equally.",
                "research_sources": ["Bloons Wiki - Chutes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "In the center sandy divide between the left and right chutes.", "First", 460, "Has range covering both alternating chutes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Dart Monkey", "0-0-0", "Directly below Quincy in the center divide.", "First", 170, "Adds piercing darts across both lanes."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Dart Monkey", "0-2-2", "Center divide.", "First", 480, "Faster attack speed and long range."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Tack Shooter", "0-0-0", "At the bottom intersection where both chutes meet the beach.", "First", 240, "Catches bloons exiting either chute."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 21, "Upgrade", "Dart Monkey", "0-2-3", "Center divide.", "First", 1275, "Crossbow hits camo bloons on Round 24 and 33 across both chutes."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 25, "Place", "Bomb Shooter", "2-0-3", "In the center divide.", "Close", 3085, "Recursive Cluster bombs pop Round 28 Leads and grouped bloons."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Bottom intersection.", "First", 3735, "Overdrive completely locks down the bottom exit."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In the center divide.", "Strong", 2040, "MOAB Mauler deals massive damage to the Round 40 blimp. Overdrive and Quincy finish it off.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "rake": {
        "id": "rake",
        "name": "Rake",
        "category": "Intermediate",
        "terrain": "Japanese Zen Garden",
        "lanes": "Two crossing paths over wooden bridges and raked sand",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Two distinct paths that cross directly over each other at a wooden bridge",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A beautiful Japanese zen garden with two intersecting paths that cross each other over a wooden bridge. The crossover intersection is the premier killzone.",
                "camo_handling": "Sauda placed at the bridge crossover spots camo from Round 1. Ninja 3-0-1 placed adjacent provides total camo control.",
                "lead_handling": "Alchemist 2-0-0 placed next to Sauda buffs the crossover towers to pop Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive at the crossover + 0-3-2 Bomb Shooter destroys the Round 40 MOAB as it crosses the bridge.",
                "why_it_works": "Both lanes cross at the exact same physical bridge, allowing a single concentrated defense to handle 100% of bloons.",
                "research_sources": ["Bloons Wiki - Rake"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly at the central wooden bridge crossover where both lanes intersect.", "First", 510, "Hits bloons on both lanes with full sword reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the corner directly adjacent to the bridge crossover.", "First", 240, "Radial fire hits both crossing paths."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Bridge crossover.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "On the stone garden bank next to Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Bridge crossover.", "First", 935, "Tack Sprayer fires 16 tacks into both lanes."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Stone garden bank.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Bridge crossover.", "First", 2800, "Overdrive completely locks down the bridge."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the upper path before the bridge.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "streambed": {
        "id": "streambed",
        "name": "Streambed",
        "category": "Intermediate",
        "terrain": "Dry Riverbed",
        "lanes": "Single path looping along mud banks and a small water puddle",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Small central puddle allows 1-2 water towers; multiple hairpin bends",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A winding muddy riverbed with sharp bends and a small central water pool. The main hairpin turn around the water hole is the prime defensive hub.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 placed near the water hole ensures complete camo safety.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the riverbed bend to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The riverbed loop wraps tightly around the central bend, giving towers high attack uptime.",
                "research_sources": ["Bloons Wiki - Streambed"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the tightest inner bend of the riverbed loop near the puddle.", "First", 510, "Secures the early riverbed with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the riverbank.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Riverbank.", "First", 810, "Seeking shurikens follow bloons through the mud curves."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Riverbank.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Riverbank.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the riverbed entrance bend.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "cracked": {
        "id": "cracked",
        "name": "Cracked",
        "category": "Intermediate",
        "terrain": "Shattered Canyon",
        "lanes": "Single path winding through deep canyon fissures with water pools",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Deep cracks and water channels allow both land and water tower placement",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A cracked arid landscape with deep chasms and water pools. The track winds through multiple circular curves around the cracks.",
                "camo_handling": "Sauda handles Round 24. Monkey Sub 2-0-0 in the water chasm provides map-wide camo support.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the central chasm to pop Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 (Armor Piercing Darts) + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The water chasms run directly beneath the track curves, giving Subs excellent firing angles.",
                "research_sources": ["Bloons Wiki - Cracked"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the primary loop intersection at the center of the cracks.", "First", 510, "Controls the central chasm pass."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central water chasm pool.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Central water pool.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Alchemist", "2-0-0", "Next to Sauda on the stone rim.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Central water pool.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Stone rim.", "Close", 1060, "Berserker Brew boosts Sub and Sauda."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Central water pool.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the stone path leading into the crack.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. The Sub and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "downstream": {
        "id": "downstream",
        "name": "Downstream",
        "category": "Intermediate",
        "terrain": "River Delta Island",
        "lanes": "Single path splitting across two river branches around a central island",
        "water": True,
        "sight_blockers": False,
        "gimmick": "The river splits into two streams; bloons follow the left and right banks",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A scenic river delta with a central forested island. The water flow divides the track into two branches that both flank the central island.",
                "camo_handling": "Sauda placed on the central island covers early camos. Sub 2-0-0 in the river provides global camo coverage.",
                "lead_handling": "Alchemist 2-0-0 on the island or Buccaneer 0-2-0 pops Leads on Round 28.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the main river + Sub 2-0-3 shreds the Round 40 MOAB.",
                "why_it_works": "The central island reaches both water channels, allowing land and water towers to cover both paths simultaneously.",
                "research_sources": ["Bloons Wiki - Downstream"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the tip of the central island facing the river fork.", "First", 510, "Hits bloons before they split down the river branches."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the river channel next to the island.", "First", 425, "Covers both river paths."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "River channel.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "River channel.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "River channel.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the river fork.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the island within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the island.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "firing_range": {
        "id": "firing_range",
        "name": "Firing Range",
        "category": "Intermediate",
        "terrain": "Military Target Range",
        "lanes": "Single path through target sandbags and firing benches",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Target benches and clay walls block vision; elevated wooden benches offer sniper platforms",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Striker Jones"],
                "starting_cash": 650,
                "overview": "A military shooting range with sandbag barriers and wooden benches. Elevated benches allow Snipers to ignore ground obstacles.",
                "camo_handling": "Quincy covers early camos from the bench. Sniper 0-2-3 placed on the elevated bench detects camo across the entire range.",
                "lead_handling": "Sniper 1-0-0 on the bench or Bomb Shooter 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Sniper 3-0-2 (Deadly Precision) on Strong + Bomb Shooter 0-3-2 cracks the Round 40 MOAB instantly.",
                "why_it_works": "Snipers on the elevated firing bench have unlimited global range and ignore all the ground barriers.",
                "research_sources": ["Bloons Wiki - Firing Range"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the elevated wooden firing bench.", "First", 455, "Fires arrows over the clay barriers with high ground vision."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On the firing bench next to Quincy.", "First", 300, "Provides global rifle fire across the range."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Firing bench.", "First", 980, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Tack Shooter", "0-0-0", "At the ground gap where bloons enter the main firing alley.", "First", 240, "Close-range multi-shot inside the alley."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 24, "Upgrade", "Sniper Monkey", "3-0-2", "Firing bench.", "Strong", 3740, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot.", timing="before_round"),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Tack Shooter", "2-0-3", "Alley gap.", "First", 940, "Tack Sprayer shreds grouped bloon waves.", timing="before_round"),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Upgrade", "Tack Shooter", "2-0-4", "Alley gap.", "First", 2720, "Overdrive completely controls the ground alley.", timing="during_round"),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the firing alley entrance.", "Strong", 2355, "MOAB Mauler delivers heavy blimp damage. Deadly Precision Sniper and Overdrive pop the MOAB.", timing="during_round")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "karts_n_darts": {
        "id": "karts_n_darts",
        "name": "Karts N' Darts",
        "category": "Intermediate",
        "terrain": "Go-Kart Racing Track",
        "lanes": "Single path looping around racing tracks and grandstands",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Moving go-karts drive across the track periodically, popping bloons on collision",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A colorful go-kart racetrack where bloons follow the paved course. The periodic kart collisions provide free damage against bloon swarms.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed near the start/finish line ensures complete camo safety.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the start line to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 at the hairpin bend + 0-3-2 Bomb Shooter destroys the Round 40 MOAB on the straightaway.",
                "why_it_works": "The hairpin racing turns force bloons into tight clusters where Tack and Ninja excel.",
                "research_sources": ["Bloons Wiki - Karts N' Darts"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner curve of the start/finish line hairpin.", "First", 510, "Secures the race entrance with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the tight hairpin turn directly adjacent to Sauda.", "First", 240, "Covers the entire 180-degree racing bend."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Hairpin turn.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda and Tack Shooter.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Hairpin turn.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Next to Sauda.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Hairpin turn.", "First", 2800, "Overdrive completely locks down the hairpin."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the straightaway leading into the turn.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "moon_landing": {
        "id": "moon_landing",
        "name": "Moon Landing",
        "category": "Intermediate",
        "terrain": "Lunar Crater Surface",
        "lanes": "Single path looping through three deep lunar impact craters",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Steep crater walls completely block ground-level vision; Mortar Monkey excels",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Striker Jones", "Sauda"],
                "starting_cash": 650,
                "overview": "The moon's surface marked by deep craters that block line of sight. Towers outside craters cannot shoot inside, but Mortar Monkeys and high-placed towers bypass all walls.",
                "camo_handling": "Mortar Monkey 0-2-3 (Signal Flare) strips Camo from all bloons, neutralizing Round 24, 33, 36, and 37 camos.",
                "lead_handling": "Mortar Monkey naturally pops Leads with explosive shells from Round 1.",
                "moab_handling": "Mortar Monkey 2-3-0 (Heavy Shells) targeting the central crater + Quincy's abilities destroy the Round 40 MOAB.",
                "why_it_works": "Mortar shells fire over all crater rims, inflicting massive splash damage throughout the crater intersections.",
                "research_sources": ["Bloons Wiki - Moon Landing"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the elevated crater rim between crater 1 and crater 2.", "First", 460, "Has high ground vision down into the track entrance."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Mortar Monkey", "0-0-0", "In the flat lunar base area away from the craters.", "First", 700, "Target the blast reticle in the center of the first crater."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Mortar Monkey", "0-2-2", "Lunar base.", "First", 980, "Bigger Blast and Faster Reload maximizes splash coverage."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "Inside the second crater on the path.", "First", 170, "Adds cleanup darts inside the crater."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Mortar Monkey", "0-2-3", "Lunar base.", "First", 765, "Signal Flare decamos all bloons and pops Leads easily on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Inside second crater.", "First", 1275, "Crossbow provides high damage cleanup inside the crater."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Place", "Bomb Shooter", "2-0-3", "Inside the central crater.", "Close", 3085, "Recursive Cluster bombs wipe out dense mid-game waves."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Inside the first crater.", "Strong", 2040, "MOAB Mauler tears the Round 40 blimp apart. Mortar and Crossbow destroy the ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "haunted": {
        "id": "haunted",
        "name": "Haunted",
        "category": "Intermediate",
        "terrain": "Haunted Graveyard",
        "lanes": "Two alternating lanes through tombstone paths and eerie crypts",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Two distinct paths through the graveyard where bloons alternate sides each round",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A misty graveyard with tombstones and two winding paths that alternate waves. Towers placed in the central divide reach both lanes easily.",
                "camo_handling": "Sauda covers early camos. Ninja 3-0-1 placed in the central divide ensures both alternating paths are protected.",
                "lead_handling": "Alchemist 2-0-0 placed between the paths buffs towers to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB on whichever path it takes.",
                "why_it_works": "The central cemetery strip is narrow enough for Bloonjitsu shurikens to cover both left and right tracks.",
                "research_sources": ["Bloons Wiki - Haunted"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the central grass strip between the left and right graveyard paths.", "First", 510, "Has range touching both alternating paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda in the center strip.", "First", 425, "Innate camo detection and fast shurikens across both paths."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Center strip.", "First", 810, "Seeking shurikens follow bloons on both lanes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Center strip.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Center strip.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In the center strip.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "encrypted": {
        "id": "encrypted",
        "name": "Encrypted",
        "category": "Intermediate",
        "terrain": "Ancient Catacombs",
        "lanes": "Single path looping through four elemental crypt chambers",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Four crypt pedestals restricted to specific tower categories (Primary, Military, Magic, Support)",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "An ancient subterranean tomb with four stone sarcophagus platforms marked with tower category symbols. Towers placed on matching pedestals gain elevated placement.",
                "camo_handling": "Sauda covers Round 24. Ninja 3-0-1 placed on the Magic pedestal handles all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 on the Magic pedestal buffs surrounding towers for Round 28 Leads.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive on the Primary pedestal + 0-3-2 Bomb Shooter destroys the Round 40 MOAB.",
                "why_it_works": "The central track loops directly past all four elemental pedestals, creating great synergy.",
                "research_sources": ["Bloons Wiki - Encrypted"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the central stone crossover near the entrance.", "First", 510, "Defends the early rounds cleanly."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "On the Primary pedestal in the inner curve.", "First", 240, "Covers the central crypt intersection."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Primary pedestal.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Ninja Monkey", "0-0-0", "On the Magic pedestal.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Magic pedestal.", "First", 1370, "Double Shot handles dense swarms."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "On the Magic pedestal next to Ninja.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Primary pedestal.", "First", 2800, "Overdrive completely locks down the catacombs."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the path leading into the tomb.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "bazaar": {
        "id": "bazaar",
        "name": "Bazaar",
        "category": "Intermediate",
        "terrain": "Desert Marketplace",
        "lanes": "Two parallel lanes flanking an oasis canal and market stalls",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Two outer paths with tent canopies that block vision; central water canal",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A desert bazaar with two outer lanes running past market stalls. The central water canal allows water towers with clear line of sight over both lanes.",
                "camo_handling": "Quincy covers early camos from the center bridge. Buccaneer 0-2-2 Crow's Nest in the canal provides complete camo vision.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot or Bomb 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the canal + 0-3-2 Bomb Shooter shreds the Round 40 MOAB on both lanes.",
                "why_it_works": "The central canal sits directly between the two outer paths, giving naval towers equal range across both.",
                "research_sources": ["Bloons Wiki - Bazaar"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central stone bridge crossing the oasis canal.", "First", 460, "Fires arrows down both the left and right market lanes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the central oasis canal.", "First", 425, "Covers both market paths with grape fire."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Oasis canal.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Oasis canal.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Oasis canal.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the canal next to Buccaneer.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the bridge within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the bridge.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "adoras_temple": {
        "id": "adoras_temple",
        "name": "Adora's Temple",
        "category": "Intermediate",
        "terrain": "Sun God Pyramid",
        "lanes": "Single path ascending temple terraces around water basins",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Tiered pyramid steps block lower vision; central water pools allow Sub/Buccaneer",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Adora",
                "hero_alternatives": ["Sauda", "Quincy"],
                "starting_cash": 650,
                "overview": "A grand stepped pyramid temple honoring the Sun God. The track climbs the tiers of the pyramid, offering elevated platforms and water basins.",
                "camo_handling": "Ninja 3-0-1 placed on the pyramid steps or Sub 2-0-0 in the temple basin handles all camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers on the pyramid steps to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB on the temple steps.",
                "why_it_works": "The tiered stairs force bloons to loop around the central altar, giving towers multiple firing passes.",
                "research_sources": ["Bloons Wiki - Adora's Temple"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Ninja Monkey", "0-0-0", "On the central pyramid landing terrace.", "First", 425, "Innate camo detection and fast shurikens down the steps."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Dart Monkey", "0-0-0", "At the base entrance to the pyramid.", "First", 170, "Adds early chip damage."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Pyramid terrace.", "First", 810, "Seeking shurikens follow bloons up the steps."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Pyramid terrace.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja on the terrace.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Pyramid terrace.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the base of the pyramid.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu destroys the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "spring_spring": {
        "id": "spring_spring",
        "name": "Spring Spring",
        "category": "Intermediate",
        "terrain": "Springtime Riverbank",
        "lanes": "Two alternating lanes crossing over wooden bridges and ponds",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Two paths alternate bloon waves through spring streams and flower meadows",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A pastoral spring setting with two streams and wooden footbridges. Bloons alternate paths each round, but both streams run close together near the center.",
                "camo_handling": "Sauda handles Round 24. Monkey Sub 2-0-0 in the central stream provides map-wide camo support.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the bridge crossing to pop Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 (Armor Piercing Darts) + 0-3-2 Bomb Shooter crushes the Round 40 MOAB on both paths.",
                "why_it_works": "The central stream allows Sub with Advanced Intel to attack bloons on both alternating paths without moving.",
                "research_sources": ["Bloons Wiki - Spring Spring"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the central grass bank between the two wooden footbridges.", "First", 510, "Hits bloons on both alternating stream paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central spring stream.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Spring stream.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Alchemist", "2-0-0", "Next to Sauda on the grass bank.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Spring stream.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Grass bank.", "Close", 1060, "Berserker Brew boosts Sub and Sauda."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Spring stream.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the bridge entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. The Sub and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "bloonarius_prime": {
        "id": "bloonarius_prime",
        "name": "Bloonarius Prime",
        "category": "Intermediate",
        "terrain": "Toxic Slime River",
        "lanes": "Two alternating paths with prime-number rounds diverting into the slime sludge",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Bloons divert into a secondary slime path on prime-numbered rounds (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A swamp corrupted by the toxic essence of Bloonarius. On prime-numbered rounds, bloons divert into a toxic sludge channel. Placing defenses where both tracks converge is essential.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed at the convergence point covers both standard and prime tracks.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the convergence to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB (Round 40 is not prime, so it follows the standard path).",
                "why_it_works": "Positioning defenses at the convergence point ensures bloons are attacked regardless of whether the round is prime.",
                "research_sources": ["Bloons Wiki - Bloonarius Prime"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the track convergence point where the slime lane rejoins the main road.", "First", 510, "Hits bloons on both standard and prime paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda at the convergence.", "First", 425, "Innate camo detection across both tracks."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Convergence.", "First", 810, "Seeking shurikens follow bloons on both lanes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Convergence.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Convergence.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the main entrance road.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "covered_garden": {
        "id": "covered_garden",
        "name": "Covered Garden",
        "category": "Intermediate",
        "terrain": "Botanical Greenhouse",
        "lanes": "Single path looping through four glass-domed quadrants",
        "water": True,
        "sight_blockers": True,
        "gimmick": "A rotating glass roof covers 3 of 4 quadrants each round; towers under glass cannot be clicked, bought, or upgraded",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A botanical greenhouse divided into four quadrants by a rotating glass canopy. Each round, three quadrants are locked beneath glass, requiring strategic pre-planning for tower placement and upgrades.",
                "camo_handling": "Sauda placed on Round 1 in quadrant 1 covers early camos. Ninja 3-0-1 placed in an adjacent quadrant provides complete camo redundancy.",
                "lead_handling": "Alchemist 2-0-0 or Bomb Shooter 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive + 0-3-2 Bomb Shooter destroys the Round 40 MOAB.",
                "why_it_works": "Towers continue to attack even when covered by glass. As long as towers are placed and upgraded when their quadrant is open, full DPS is maintained.",
                "research_sources": ["Bloons Wiki - Covered Garden"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In quadrant 1 (uncovered on Round 1) at the inner track bend.", "First", 510, "Secures early rounds from inside quadrant 1."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Tack Shooter", "0-0-0", "In the inner curve of quadrant 1 next to Sauda.", "First", 240, "Placed before quadrant 1 is covered by glass."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 10, "Upgrade", "Tack Shooter", "2-0-2", "Quadrant 1.", "First", 620, "Upgrade during a round when quadrant 1 is open."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Place", "Ninja Monkey", "0-0-0", "In quadrant 2 when it becomes uncovered.", "First", 425, "Innate camo detection across the greenhouse."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Quadrant 2.", "First", 1370, "Double Shot handles dense swarms."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Next to Sauda and Tack in quadrant 1 when open.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Quadrant 1.", "First", 2800, "Overdrive completely locks down the inner bend."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In whatever quadrant is open on Round 37.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "quarry": {
        "id": "quarry",
        "name": "Quarry",
        "category": "Intermediate",
        "terrain": "Stone Quarry Pit",
        "lanes": "Two alternating lanes descending into a stone excavation pit",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Stepped stone elevations block ground vision; central crane and deep pit",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A deep stone excavation quarry with tiered cliff walls and two alternating entry paths that descend into the pit floor.",
                "camo_handling": "Sauda placed on the pit floor handles Round 24. Ninja 3-0-1 placed nearby handles all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs pit floor towers to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB on the pit floor.",
                "why_it_works": "Both alternating paths lead into the bottom of the quarry, making the pit floor the ideal killzone.",
                "research_sources": ["Bloons Wiki - Quarry"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the quarry pit floor where both descent ramps converge.", "First", 510, "Catches bloons from both descending paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the pit floor.", "First", 425, "Innate camo detection across the pit."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Pit floor.", "First", 810, "Seeking shurikens follow bloons through the stone ramps."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Pit floor.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Pit floor.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the pit entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "quiet_street": {
        "id": "quiet_street",
        "name": "Quiet Street",
        "category": "Intermediate",
        "terrain": "Suburban Cul-de-sac",
        "lanes": "Two alternating lanes crossing a residential driveway and sidewalks",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Two alternating lanes cross each other at the center intersection; houses block corner vision",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A quiet suburban street with houses, driveways, and sidewalks. Bloons alternate entering from the top and bottom roads, crossing at the central asphalt junction.",
                "camo_handling": "Sauda placed at the asphalt junction handles Round 24 camo green. Ninja 3-0-1 covers all subsequent camo rounds.",
                "lead_handling": "Alchemist 2-0-0 placed at the intersection buffs towers for Round 28 Leads.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The central crossroads connects both alternating paths, allowing a single defense to handle all bloons.",
                "research_sources": ["Bloons Wiki - Quiet Street"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly at the central crossroads junction of the driveway.", "First", 510, "Hits bloons from both alternating street paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the sidewalk curb.", "First", 425, "Innate camo detection across the intersection."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Sidewalk curb.", "First", 810, "Seeking shurikens follow bloons down both streets."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Sidewalk curb.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Sidewalk curb.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the main road entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "polyphemus": {
        "id": "polyphemus",
        "name": "Polyphemus",
        "category": "Intermediate",
        "terrain": "Volcanic Caldera Eye",
        "lanes": "Single path spiraling around a cyclopean eye pit with dynamic water levels",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Central water pit drains and fills periodically, altering tower placement capabilities",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A mythical volcanic eye caldera where bloons spiral around a giant pupil. The central water basin drains and refills throughout the game.",
                "camo_handling": "Sauda placed on the solid outer rim handles Round 24. Ninja 3-0-1 provides complete camo safety.",
                "lead_handling": "Alchemist 2-0-0 placed on the outer rim buffs towers to pop Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive + 0-3-2 Bomb Shooter destroys the Round 40 MOAB as it spirals.",
                "why_it_works": "Placing core defenses on the permanent solid stone rim avoids all water-drain mechanics while maintaining full coverage.",
                "research_sources": ["Bloons Wiki - Polyphemus"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the stable stone rim at the inner spiral bend.", "First", 510, "Secures the spiral entrance on permanent dry land."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the tight curve of the stone rim next to Sauda.", "First", 240, "Covers the inner spiral bend."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Stone rim.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda and Tack Shooter.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Stone rim.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Stone rim.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Stone rim.", "First", 2800, "Overdrive completely locks down the caldera spiral."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the spiral entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "water_park": {
        "id": "water_park",
        "name": "Water Park",
        "category": "Intermediate",
        "terrain": "Amusement Water Park",
        "lanes": "Single path looping through waterslides and a lazy river canal",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Waterslides create elevated barriers; lazy river offers premium water tower placement",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "A vibrant waterpark featuring colorful tube slides and a looping lazy river. The lazy river loop encloses the central path, creating ideal water tower spots.",
                "camo_handling": "Sauda handles Round 24. Buccaneer 0-2-2 Crow's Nest in the lazy river provides full camo coverage.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot pops Leads on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the lazy river + 0-3-2 Bomb Shooter easily shreds the Round 40 MOAB.",
                "why_it_works": "Naval towers in the lazy river have 360-degree firing coverage across multiple slide exits.",
                "research_sources": ["Bloons Wiki - Water Park", "Update 38 Release Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the splashdown landing where the main waterslide meets the deck.", "First", 510, "Secures the slide exit with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the central lazy river canal.", "First", 425, "Covers both slide paths with grape fire."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Lazy river.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Lazy river.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Lazy river.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the lazy river next to Buccaneer.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the deck within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the deck.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "sulfur_springs": {
        "id": "sulfur_springs",
        "name": "Sulfur Springs",
        "category": "Intermediate",
        "terrain": "Volcanic Geyser Fields",
        "lanes": "Single path curving around bubbling yellow sulfur vents and geysers",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Bubbling sulfur pools allow water towers; volcanic ridges offer elevated platforms",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A geothermal area with boiling sulfur geysers and yellow mineral pools. The track winds between steaming vents in a serpentine path.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed near the main geyser bend covers all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the geyser bend to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter destroys the Round 40 MOAB.",
                "why_it_works": "The winding sulfur paths force bloons to loop tightly around the central mineral ridge.",
                "research_sources": ["Bloons Wiki - Sulfur Springs", "Update 41 Map Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the tight inner bend between the two main sulfur vents.", "First", 510, "Secures the geothermal entrance with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the mineral ridge.", "First", 425, "Innate camo detection across the geysers."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Mineral ridge.", "First", 810, "Seeking shurikens follow bloons through the sulfur curves."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Mineral ridge.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Mineral ridge.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the sulfur entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "luminous_cove": {
        "id": "luminous_cove",
        "name": "Luminous Cove",
        "category": "Intermediate",
        "terrain": "Bioluminescent Sea Grotto",
        "lanes": "Single path curving around glowing coral tide pools",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Deep aquatic tide pools designed to showcase the Mermonkey tower",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "A glowing underground sea cave filled with bioluminescent coral and crystal water pools. The track winds around deep tide pools, offering ample water space.",
                "camo_handling": "Sauda handles Round 24. Buccaneer 0-2-2 Crow's Nest in the tide pool provides full camo coverage.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot pops Leads on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the tide pool + 0-3-2 Bomb Shooter shreds the Round 40 MOAB.",
                "why_it_works": "The central bioluminescent cove gives naval towers 360-degree firing range over the reef path.",
                "research_sources": ["Bloons Wiki - Luminous Cove", "Update 44 Map Overview"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the coral reef path at the primary cove loop.", "First", 510, "Secures the cove entrance with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the glowing central tide pool.", "First", 425, "Fires cannonballs and grapes across the reef."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Central tide pool.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Central tide pool.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Central tide pool.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the adjacent tide pool.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the reef within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the reef path.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "ancient_portal": {
        "id": "ancient_portal",
        "name": "Ancient Portal",
        "category": "Intermediate",
        "terrain": "Mystic Ruin Portals",
        "lanes": "Single path splitting through dimensional teleportation portals",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Bloons enter teleportation portals and emerge across the map in different lanes",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Ancient mystical ruins where arcane stone portals teleport bloons from one lane to another. Defending the final portal exit convergence is crucial.",
                "camo_handling": "Sauda placed at the portal exit handles Round 24. Ninja 3-0-1 provides complete camo safety across all portals.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the portal exit to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "Regardless of portal teleportation routes, all bloons must pass through the final exit courtyard.",
                "research_sources": ["Bloons Wiki - Ancient Portal", "Update 45 Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the final portal exit junction where teleported bloons converge.", "First", 510, "Secures the exit courtyard."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda at the portal exit.", "First", 425, "Innate camo detection across the courtyard."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Portal exit.", "First", 810, "Seeking shurikens follow bloons through the portals."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Portal exit.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Portal exit.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the primary portal entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "protect_the_yacht": {
        "id": "protect_the_yacht",
        "name": "Protect the Yacht",
        "category": "Intermediate",
        "terrain": "Luxury Marina Bay",
        "lanes": "Two alternating lanes circling a moored luxury superyacht",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Bloons sail around a docked luxury yacht in crystal turquoise marina waters",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "A sunny tropical marina where bloons navigate water channels around a docked superyacht. The open water and dock piers allow versatile tower placement.",
                "camo_handling": "Sauda on the dock pier handles Round 24. Buccaneer 0-2-2 Crow's Nest in the marina handles all subsequent camos.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot pops Leads on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the marina + Sub 2-0-3 shreds the Round 40 MOAB before it reaches the yacht stern.",
                "why_it_works": "The marina water provides 100% open lines of sight for naval towers.",
                "research_sources": ["Bloons Wiki - Protect the Yacht"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the main dock pier where the marina walkway meets the track.", "First", 510, "Secures the dock entrance with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the marina bay right beside the yacht.", "First", 425, "Fires cannonballs and grapes across the marina."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Marina bay.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Marina bay.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Marina bay.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the marina next to Buccaneer.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the dock pier within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the dock pier.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "lost_crevasse": {
        "id": "lost_crevasse",
        "name": "Lost Crevasse",
        "category": "Intermediate",
        "terrain": "Arctic Glacial Crevasse",
        "lanes": "Two alternating lanes descending into a deep frozen glacier rift",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Deep glacial ice shelves with freezing pools and steep ice bridges",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A freezing glacial gorge with two alternating paths winding through ice bridges and icy melt pools. The central ice bridge chokepoint is the optimal defense zone.",
                "camo_handling": "Sauda placed on the ice bridge handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs ice bridge towers to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB in the gorge.",
                "why_it_works": "Both alternating lanes pass over the central ice bridge, creating a single chokepoint for all bloons.",
                "research_sources": ["Bloons Wiki - Lost Crevasse"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the center of the main ice bridge crossing the crevasse.", "First", 510, "Hits bloons from both alternating glacial lanes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the ice shelf.", "First", 425, "Innate camo detection across the crevasse."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Ice shelf.", "First", 810, "Seeking shurikens follow bloons through the frozen gorge."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Ice shelf.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Ice shelf.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the crevasse entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    }
}
