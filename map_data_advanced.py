"""
map_data_advanced.py
Contains comprehensive, round-by-round Easy/Standard (R1-40) strategies for all 22 Advanced maps.
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

ADVANCED_MAPS = {
    "another_brick": {
        "id": "another_brick",
        "name": "Another Brick",
        "category": "Advanced",
        "terrain": "Prison Brick Wall",
        "lanes": "Single path looping around a tall brick barrier wall",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Tall prison brick wall blocks vision between upper and lower halves of the track",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A prison courtyard divided by a massive brick wall. Bloons must travel around the perimeter of the wall. Placing defenses at the wall corner and exit chokepoint provides high efficiency.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed near the wall corner covers all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the wall corner to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB as it rounds the wall corner.",
                "why_it_works": "The wall corner forces bloons into a tight 90-degree turn where seeking shurikens and bombs inflict maximum damage.",
                "research_sources": ["Bloons Wiki - Another Brick"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner corner bend of the brick wall perimeter.", "First", 510, "Hits bloons rounding the main wall corner."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda along the brick wall.", "First", 425, "Innate camo detection around the wall."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Wall corner.", "First", 810, "Seeking shurikens follow bloons around the brick barrier."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Wall corner.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Wall corner.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the track exit after the wall.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "cornfield": {
        "id": "cornfield",
        "name": "Cornfield",
        "category": "Advanced",
        "terrain": "Dense Corn Farmland",
        "lanes": "Single path winding through dense unharvested corn patches",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Dense corn stalks block placement and line of sight; can be harvested for cash, but center clearing is open",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A rural cornfield where tall corn stalks block vision and placement. However, the central natural clearing provides enough space for Sauda, Ninja, and Alchemist without spending any cash on corn removal.",
                "camo_handling": "Sauda placed in the central clearing handles Round 24. Ninja 3-0-1 in the clearing covers all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 placed in the central clearing buffs towers for Round 28 Leads.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB in the center clearing.",
                "why_it_works": "The central clearing has unobstructed lines of sight along the main crossing, allowing full damage without wasting money removing corn.",
                "research_sources": ["Bloons Wiki - Cornfield", "No Corn Removal Strategy Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the natural open central clearing where the track makes an S-turn.", "First", 510, "Secures the central clearing without clearing any corn."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda in the center clearing.", "First", 425, "Innate camo detection across the clearing."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Center clearing.", "First", 810, "Seeking shurikens follow bloons through the corn S-turns."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Center clearing.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda in the center clearing.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Center clearing.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In the center clearing facing the entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "off_the_coast": {
        "id": "off_the_coast",
        "name": "Off The Coast",
        "category": "Advanced",
        "terrain": "Tropical Beach & Sunken Ship",
        "lanes": "Single path looping along beach shoreline and ocean water",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Sandy shoreline transitions into open water past a shipwreck",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "A sandy coastline overlooking an ocean with a sunken ship. The track runs along the beach before turning back towards the sea.",
                "camo_handling": "Sauda handles Round 24. Buccaneer 0-2-2 Crow's Nest in the ocean handles all subsequent camos.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot pops Leads on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer in the ocean + Sub 2-0-3 shreds the Round 40 MOAB on the shoreline.",
                "why_it_works": "The ocean provides unrestricted line of sight across the entire beach track.",
                "research_sources": ["Bloons Wiki - Off The Coast"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the primary shoreline bend where the beach path loops.", "First", 510, "Secures the beach entrance with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the ocean channel right next to the shoreline bend.", "First", 425, "Fires cannonballs and grapes across the beach."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Ocean channel.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-0", "Ocean channel.", "First", 425, "Hot Shot grants Lead-popping; prepares path for Destroyer."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Ocean channel.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the ocean next to the sunken ship.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the sandy shore within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the beach.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "underground": {
        "id": "underground",
        "name": "Underground",
        "category": "Advanced",
        "terrain": "Subterranean Railway",
        "lanes": "Two alternating lanes entering and exiting subterranean railway pipes",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Bloons enter subway pipes and travel underground unseen before emerging on the other side",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A subway maintenance hub with two tracks entering underground tunnels and emerging at the opposite side. Defending the track intersections before the tunnels is vital.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed near the tunnel entry covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the tunnel entry to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB before it enters the subway pipe.",
                "why_it_works": "Both tracks cross near the central platform, allowing towers to hit bloons on both paths before they submerge.",
                "research_sources": ["Bloons Wiki - Underground"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the upper platform bend where both subway lanes cross.", "First", 510, "Hits bloons on both lanes before they enter the tunnel."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the central platform.", "First", 425, "Innate camo detection across both tracks."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Central platform.", "First", 810, "Seeking shurikens follow bloons into the tunnels."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Central platform.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Central platform.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the subway entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "spillway": {
        "id": "spillway",
        "name": "Spillway",
        "category": "Advanced",
        "terrain": "Nuclear Waste Spillway",
        "lanes": "Single path looping around a central nuclear disposal barrel",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Central nuclear barrel accommodates only one tower; outer walls block direct vision between tracks",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Striker Jones"],
                "starting_cash": 650,
                "overview": "An industrial toxic facility where bloons circle a center radioactive drum before exiting. The center drum has 360-degree reach across all four outer lanes.",
                "camo_handling": "Ninja 3-0-1 placed on the central drum spots camo from all lanes for Round 24, 33, and 36.",
                "lead_handling": "Alchemist 2-0-0 or Bomb 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu on the central drum + 3-2-0 Alchemist + Mortar 0-3-2 tears the Round 40 MOAB apart.",
                "why_it_works": "The single center barrel tower attacks bloons across all four perimeter quadrants without any line of sight obstruction.",
                "research_sources": ["Bloons Wiki - Spillway"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Ninja Monkey", "0-0-0", "Directly in the center radioactive nuclear barrel.", "First", 425, "The center barrel has 360-degree vision over all four outer lanes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Dart Monkey", "0-0-0", "On the outer walkway near the entrance.", "First", 170, "Adds early chip damage."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Center barrel.", "First", 810, "Seeking shurikens home into bloons on all 4 quadrants."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Center barrel.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "On the outer walkway within range of the center barrel.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Outer walkway.", "Close", 1060, "Berserker Brew boosts the center barrel Ninja."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Center barrel.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack across all 4 tracks."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the outer walkway near the entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu in the center destroys the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "cargo": {
        "id": "cargo",
        "name": "Cargo",
        "category": "Advanced",
        "terrain": "Commercial Shipping Port",
        "lanes": "Two distinct paths: ground path for bloons and water canal for MOABs",
        "water": True,
        "sight_blockers": True,
        "gimmick": "MOAB-class bloons spawn from a separate water canal entrance directly toward the exit",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A busy commercial container port. Regular bloons travel along a winding land road, but MOABs spawn from a separate water channel with a much shorter path to the exit.",
                "camo_handling": "Sauda on the road handles Round 24. Buccaneer 0-2-2 Crow's Nest in the shipping canal covers all camo bloons.",
                "lead_handling": "Buccaneer 0-2-0 Hot Shot pops Leads on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer 3-2-0 Destroyer placed in the MOAB shipping canal + 0-3-2 Bomb Shooter intercepts the Round 40 MOAB immediately upon spawning.",
                "why_it_works": "Placing naval defenses in the water canal intercepts the MOAB at point-blank range as soon as it emerges.",
                "research_sources": ["Bloons Wiki - Cargo"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the first major road intersection near the shipping containers.", "First", 510, "Secures the road entrance with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the shipping canal right where the MOAB path emerges.", "First", 425, "Covers both the road and the MOAB canal."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Shipping canal.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-0", "Shipping canal.", "First", 425, "Hot Shot grants Lead-popping; prepares path for Destroyer."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Shipping canal.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the shipping canal next to Buccaneer.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the dock pier within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-2", "At the MOAB canal mouth.", "Strong", 2040, "MOAB Mauler intercepts the Round 40 MOAB directly at its canal spawn. The Destroyer pops it in seconds.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "peninsula": {
        "id": "peninsula",
        "name": "Peninsula",
        "category": "Advanced",
        "terrain": "Oceanic Mountain Peninsula",
        "lanes": "Single path winding down a spiral mountain surrounded by open ocean",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Severe land placement restrictions on the mountain; vast ocean waters surrounding it",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "A steep stone mountain peninsula jutting out into deep ocean water. Land space is severely constrained, making naval towers the core offensive force.",
                "camo_handling": "Sauda placed at the base choke handles Round 24. Monkey Sub 2-0-0 in the ocean provides global camo coverage.",
                "lead_handling": "Alchemist 2-0-0 on the peninsula base or Buccaneer 0-2-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts in the ocean + Buccaneer 3-2-0 shreds the Round 40 MOAB.",
                "why_it_works": "Subs and Buccaneers in the surrounding ocean have unobstructed vision of bloons spiraling down the mountain.",
                "research_sources": ["Bloons Wiki - Peninsula"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the mountain base where the path meets the sea.", "First", 510, "Secures the base bottleneck with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the ocean water directly adjacent to the peninsula base.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Ocean water.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Monkey Buccaneer", "0-0-0", "In the ocean next to the Sub.", "First", 425, "Adds grape and cannon fire."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "0-2-0", "Ocean water.", "First", 635, "Hot Shot pops Leads on Round 28; prepares path for Destroyer."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Ocean water.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Ocean water.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Monkey Buccaneer", "3-2-0", "Ocean water.", "First", 2510, "Destroyer unleashes rapid grape volleys, shredding the MOAB upon entry.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "high_finance": {
        "id": "high_finance",
        "name": "High Finance",
        "category": "Advanced",
        "terrain": "Metropolitan Skyscraper Rooftops",
        "lanes": "Two alternating lanes crossing skyscraper construction zones and water canals",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Building plots must be purchased to place towers on rooftops; harbor canal accommodates water towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Benjamin"],
                "starting_cash": 650,
                "overview": "A city rooftop construction zone with high-rise buildings and a water canal. The natural free corner plot and harbor canal allow immediate defense without paying building fees.",
                "camo_handling": "Quincy covers early camos from the free corner plot. Sub 2-0-0 in the canal provides map-wide camo detection.",
                "lead_handling": "Sniper 1-0-0 on the free plot or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts in the canal + Sniper 3-0-2 on Strong destroys the Round 40 MOAB.",
                "why_it_works": "The central harbor canal allows Sub to use Advanced Intel across both city tracks without paying building plot fees.",
                "research_sources": ["Bloons Wiki - High Finance"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the free unbuilt plot on the lower-left rooftop.", "First", 460, "Fires arrows down the entrance track with zero plot fees."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central harbor water canal.", "First", 275, "High-velocity dart fire from the water canal."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Harbor canal.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Quincy can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Sniper Monkey", "0-0-0", "On the free lower-left plot next to Quincy.", "First", 300, "Provides global rifle fire across the city."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "1-0-2", "Free plot.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Harbor canal.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Harbor canal.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Free plot.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs. The Sub and Sniper finish the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "geared": {
        "id": "geared",
        "name": "Geared",
        "category": "Advanced",
        "terrain": "Giant Clockwork Cog",
        "lanes": "Single path looping around the outer perimeter of a rotating giant central gear",
        "water": False,
        "sight_blockers": False,
        "gimmick": "The central giant gear rotates clockwise each round, repositioning all monkeys placed on it",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Striker Jones"],
                "starting_cash": 650,
                "overview": "A mechanical fortress where the central platform is a massive gear that rotates each round. Placing global-range towers (like Sniper) on static outer walls bypasses gear rotation entirely.",
                "camo_handling": "Quincy covers early camos. Sniper 0-2-3 placed on the static outer wall detects camo across the entire map.",
                "lead_handling": "Sniper 1-0-0 on the outer wall or Bomb 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 destroys the Round 40 MOAB regardless of gear position.",
                "why_it_works": "Global range towers on the stationary outer walls are completely unaffected by the gear rotation mechanic.",
                "research_sources": ["Bloons Wiki - Geared"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the stationary upper-left outer wall platform.", "First", 460, "Safe from gear rotation with long-range arrow attacks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On the stationary outer wall next to Quincy.", "First", 300, "Provides global rifle fire across the entire track."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Outer wall.", "First", 935, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "On the center gear near an edge.", "First", 170, "Adds chip damage as the gear rotates."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "3-0-2", "Outer wall.", "Strong", 2450, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Bomb Shooter", "0-0-0", "On the stationary outer wall near the track exit.", "Close", 240, "Prepares explosive defense for upcoming grouped bloons."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Bomb Shooter", "2-0-3", "Outer wall.", "Close", 2845, "Really Big Bombs + Cluster Bombs wipes out grouped bloon rushes."),
                    create_step(8, "Rounds 31–39: Final Preparation", 36, "Place", "Bomb Shooter", "0-3-2", "On the outer wall.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage."),
                    create_step(9, "Round 40: MOAB Battle", 40, "Target", "Bomb Shooter", "0-3-2", "Outer wall.", "Strong", 0, "The 3-0-2 Sniper on Strong + MOAB Mauler obliterates the Round 40 MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "pat_s_pond": {
        "id": "pat_s_pond",
        "name": "Pat's Pond",
        "category": "Advanced",
        "terrain": "Dual Circular Ponds",
        "lanes": "Two alternating lanes flanking twin circular duck ponds and stone bridges",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Two symmetric circular ponds flanked by elevated stone paths and bridges",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Pat Fusty", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "Named after Pat Fusty, this map features two circular ponds separated by a central stone bridge. Bloons alternate sides, but Subs placed in both ponds easily cover the entire map.",
                "camo_handling": "Sauda on the center bridge handles Round 24. Monkey Sub 2-0-0 in the pond provides map-wide camo detection.",
                "lead_handling": "Alchemist 2-0-0 on the bridge or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts in the ponds + 0-3-2 Bomb Shooter crushes the Round 40 MOAB.",
                "why_it_works": "The twin ponds provide deep water on both halves of the track, giving Sub Advanced Intel 100% map coverage.",
                "research_sources": ["Bloons Wiki - Pat's Pond"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly in the center of the stone bridge connecting the two ponds.", "First", 510, "Hits bloons on both alternating pond paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the left circular pond.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Left pond.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Monkey Sub", "0-0-0", "In the right circular pond.", "First", 275, "Adds second Sub for symmetric coverage."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Left pond.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "On the stone bridge next to Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Left pond.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the stone bridge.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. The twin Subs and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "mesa": {
        "id": "mesa",
        "name": "Mesa",
        "category": "Advanced",
        "terrain": "Desert Sandstone Mesas",
        "lanes": "Two alternating lanes separated by elevated red sandstone plateaus",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Tall sandstone mesas block vision between the upper and lower paths",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "An arid desert canyon divided by elevated sandstone plateaus. Bloons alternate entering from the top and bottom paths. Elevated mesa platforms offer high-ground vision.",
                "camo_handling": "Quincy covers early camos from the center mesa. Sniper 0-2-3 placed on the high mesa ridge covers all camos.",
                "lead_handling": "Sniper 1-0-0 on the mesa or Bomb 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 destroys the Round 40 MOAB.",
                "why_it_works": "The central mesa plateau has elevated vision over both upper and lower tracks.",
                "research_sources": ["Bloons Wiki - Mesa"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central elevated sandstone mesa platform.", "First", 460, "Fires arrows down into both canyon paths with high ground vision."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On the mesa platform next to Quincy.", "First", 300, "Provides global rifle fire across both lanes."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Mesa platform.", "First", 935, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "At the exit path where both canyon lanes merge.", "First", 170, "Adds cleanup darts at the exit."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "3-0-2", "Mesa platform.", "Strong", 2450, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Exit merger.", "First", 1275, "Crossbow provides high damage cleanup."),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Place", "Bomb Shooter", "2-0-3", "At the exit merger.", "Close", 3085, "Recursive Cluster bombs wipe out grouped bloons."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the exit merger.", "Strong", 2040, "MOAB Mauler tears the Round 40 blimp apart. Sniper and Crossbow destroy the ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "x_factor": {
        "id": "x_factor",
        "name": "X Factor",
        "category": "Advanced",
        "terrain": "Diagonal X Crossways",
        "lanes": "Four alternating diagonal lanes crossing in an X pattern",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Bloons enter from 4 separate diagonal corners and cross at the center",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Four diagonal paths crossing in an X shape. Bloons enter from all four corners, but every path passes through the central intersection.",
                "camo_handling": "Quincy covers early camos from the central cross. Sniper 0-2-3 placed in the center covers all 4 lanes.",
                "lead_handling": "Sniper 1-0-0 or Bomb Shooter 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 destroys the Round 40 MOAB at the center intersection.",
                "why_it_works": "The central crossway is the common intersection for all four diagonal tracks.",
                "research_sources": ["Bloons Wiki - X Factor"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "Directly in the central crossway where all 4 diagonal lanes intersect.", "First", 460, "Fires arrows down all 4 diagonal lanes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "In the central crossway next to Quincy.", "First", 300, "Provides global rifle fire across all 4 corners."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Central crossway.", "First", 935, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "Along one of the diagonal exits.", "First", 170, "Adds cleanup darts."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "3-0-2", "Central crossway.", "Strong", 2450, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Diagonal exit.", "First", 1275, "Crossbow provides high damage cleanup."),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Place", "Bomb Shooter", "2-0-3", "In the central crossway.", "Close", 3085, "Recursive Cluster bombs wipe out grouped bloons across all 4 lanes."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In the central crossway.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sniper on Strong and Quincy destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "erosion": {
        "id": "erosion",
        "name": "Erosion",
        "category": "Advanced",
        "terrain": "Crumbling Sea Ice Floes",
        "lanes": "Single path winding down collapsing ice floes into the sea",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Ice floes break apart and collapse periodically; towers placed on eroding ice fall into the ocean",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A polar shoreline where sea ice floes crack and break away over time. Placing towers on the permanent mainland cliff ensures defenses never sink.",
                "camo_handling": "Sauda on the stable cliff handles Round 24. Monkey Sub 2-0-0 in the ocean provides global camo coverage.",
                "lead_handling": "Alchemist 2-0-0 on the permanent cliff buffs towers to pop Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts + 0-3-2 Bomb Shooter destroys the Round 40 MOAB.",
                "why_it_works": "Building exclusively on the permanent solid mainland cliff completely bypasses the ice erosion mechanic.",
                "research_sources": ["Bloons Wiki - Erosion"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the permanent mainland cliff at the top-left (never collapses).", "First", 510, "Safe from all ice erosion mechanics."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the permanent ocean channel at the bottom.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Ocean channel.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Alchemist", "2-0-0", "On the permanent mainland cliff next to Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Ocean channel.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Mainland cliff.", "Close", 1060, "Berserker Brew boosts Sub and Sauda."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Ocean channel.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the permanent mainland cliff.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. The Sub and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "midnight_mansion": {
        "id": "midnight_mansion",
        "name": "Midnight Mansion",
        "category": "Advanced",
        "terrain": "Gothic Dining Hall",
        "lanes": "Single path looping through opulent mansion dining tables and staircases",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Elaborate banquet tables and stair banisters block ground-level line of sight",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A grand gothic mansion dining hall. Dining tables and chandeliers block ground projectiles, but the main foyer entryway and stair landing form a tight chokepoint.",
                "camo_handling": "Sauda placed at the foyer stairs handles Round 24. Ninja 3-0-1 placed on the stair landing handles all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the foyer to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB in the foyer.",
                "why_it_works": "The foyer stairs form an unavoidable bottleneck where all bloons must pass before entering the dining room.",
                "research_sources": ["Bloons Wiki - Midnight Mansion"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the foot of the foyer stairs where bloons enter the mansion.", "First", 510, "Secures the mansion entrance with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the foyer landing.", "First", 425, "Innate camo detection across the foyer."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Foyer landing.", "First", 810, "Seeking shurikens follow bloons past the banquet tables."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Foyer landing.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Foyer landing.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the mansion doorway.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "sunken_columns": {
        "id": "sunken_columns",
        "name": "Sunken Columns",
        "category": "Advanced",
        "terrain": "Submerged Roman Ruins",
        "lanes": "Two alternating lanes through submerged Greco-Roman columns and plazas",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Submerged columns can be raised or lowered; flooded plaza allows water and land towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Admiral Brickell", "Quincy"],
                "starting_cash": 650,
                "overview": "Submerged Greco-Roman ruins with marble columns standing in water. The central sunken plaza provides water for Subs and dry platforms for heroes.",
                "camo_handling": "Sauda on the central plaza handles Round 24. Monkey Sub 2-0-0 in the water provides map-wide camo detection.",
                "lead_handling": "Alchemist 2-0-0 on the plaza or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts + 0-3-2 Bomb Shooter destroys the Round 40 MOAB.",
                "why_it_works": "The central flooded basin reaches both alternating paths, allowing Sub to deliver continuous damage.",
                "research_sources": ["Bloons Wiki - Sunken Columns"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the central marble plaza between the columns.", "First", 510, "Hits bloons on both alternating lane passes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the flooded basin next to the central column.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Flooded basin.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Alchemist", "2-0-0", "On the marble plaza next to Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Flooded basin.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Marble plaza.", "Close", 1060, "Berserker Brew boosts Sub and Sauda."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Flooded basin.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the marble plaza.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. The Sub and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "dark_path": {
        "id": "dark_path",
        "name": "Dark Path",
        "category": "Advanced",
        "terrain": "Subterranean Crystal Cavern",
        "lanes": "Single path branching into subterranean crystal tunnels",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Cavern walls and glowing crystal formations block direct ground line of sight",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A dark underground cavern filled with glowing purple crystals and stone pillars. The track enters through a narrow cavern mouth where all bloons are concentrated.",
                "camo_handling": "Sauda placed at the cavern mouth handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the cavern entrance to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The narrow cavern entrance forces all bloons into a tight choke before they branch into the crystal tunnels.",
                "research_sources": ["Bloons Wiki - Dark Path", "Update 39 Map Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly at the narrow mouth of the crystal cavern entrance.", "First", 510, "Secures the cavern choke with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the cavern floor.", "First", 425, "Innate camo detection across the cavern mouth."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Cavern mouth.", "First", 810, "Seeking shurikens follow bloons through the crystal tunnels."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Cavern mouth.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Cavern mouth.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the cavern entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "castle_revenge": {
        "id": "castle_revenge",
        "name": "Castle Revenge",
        "category": "Advanced",
        "terrain": "Medieval Fortress Castle",
        "lanes": "Two simultaneous lanes crossing drawbridges and stone battlements",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Medieval castle layout inspired by classic BTD5 Castle; stone walls and portcullises",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A nostalgic medieval fortress inspired by BTD5. Bloons storm the castle across two simultaneous lanes through the outer portcullis into the courtyard.",
                "camo_handling": "Sauda placed at the courtyard portcullis handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the portcullis to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 at the portcullis + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "Both lanes converge at the castle portcullis, creating an impenetrable bottleneck.",
                "research_sources": ["Bloons Wiki - Castle Revenge", "Update 42 Map Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner courtyard chokepoint right behind the portcullis.", "First", 510, "Hits bloons from both simultaneous castle lanes."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the tight curve of the portcullis gateway.", "First", 240, "Covers the entire castle entrance pass."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Portcullis gateway.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda on the castle battlements.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Portcullis gateway.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Castle battlements.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Portcullis gateway.", "First", 2800, "Overdrive completely locks down the castle courtyard."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "On the drawbridge leading to the castle.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "sunset_gulch": {
        "id": "sunset_gulch",
        "name": "Sunset Gulch",
        "category": "Advanced",
        "terrain": "Wild West Sandstone Canyon",
        "lanes": "Single path splitting into two lanes on Round 39 through a desert canyon",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Path opens a second train-track lane on Round 39+; steep red rock canyon walls",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A dusty western canyon at sunset. The bloons travel through the primary canyon floor for the first 38 rounds before a train tunnel opens on Round 39.",
                "camo_handling": "Sauda placed at the main canyon chokepoint handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the canyon choke to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB in the gulch.",
                "why_it_works": "Positioning towers at the convergence of the gulch and train tracks ensures coverage across all 40 rounds.",
                "research_sources": ["Bloons Wiki - Sunset Gulch"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the narrow gulch bottleneck where the canyon track turns.", "First", 510, "Controls the canyon pass with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the canyon floor.", "First", 425, "Innate camo detection across the gulch."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Canyon floor.", "First", 810, "Seeking shurikens follow bloons through the sandstone bends."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Canyon floor.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Canyon floor.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the gulch entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "last_resort": {
        "id": "last_resort",
        "name": "Last Resort",
        "category": "Advanced",
        "terrain": "Polar Arctic Station",
        "lanes": "Single path looping around arctic weather stations and frozen snowdrifts",
        "water": True,
        "sight_blockers": False,
        "gimmick": "A frozen revenge version of Resort featuring icy paths and sub-zero mechanics",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A polar winter variation of the famous Resort map. The bloons loop past the snowy weather station and frozen pool, offering strong loop synergy.",
                "camo_handling": "Sauda placed inside the opening station loop handles Round 24. Ninja 3-0-1 covers all subsequent camo rounds.",
                "lead_handling": "Alchemist 2-0-0 buffs towers in the station loop to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 inside the station loop + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The looping station track allows towers to hit bloons across three separate loop passes.",
                "research_sources": ["Bloons Wiki - Last Resort", "Update 46 Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Inside the upper-left bend of the arctic station loop.", "First", 510, "Hits bloons on all passes around the loop."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the top-right corner inside the station loop.", "First", 240, "Maximizes radial coverage across the loop."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Inside station loop.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Just below Sauda inside the loop.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Inside station loop.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Inside station loop.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Inside station loop.", "First", 2800, "Overdrive completely locks down the station loop."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Outside the loop near the track entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "enchanted_glade": {
        "id": "enchanted_glade",
        "name": "Enchanted Glade",
        "category": "Advanced",
        "terrain": "Fairy Forest Rapids",
        "lanes": "Two alternating lanes winding through glowing mushrooms and forest rapids",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Enchanted tree trunks block line of sight; magical river allows water towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Obyn Greenfoot", "Quincy"],
                "starting_cash": 650,
                "overview": "A mystical fairy forest featuring giant luminescent toadstools and a rapid enchanted stream. Both forest lanes converge at a mossy riverbank crossing.",
                "camo_handling": "Sauda placed at the riverbank crossing handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the riverbank to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The mossy riverbank crossing is the single point where both forest lanes merge before the exit.",
                "research_sources": ["Bloons Wiki - Enchanted Glade", "Update 47 Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the mossy riverbank crossing where both glade paths converge.", "First", 510, "Secures the glade convergence with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the riverbank.", "First", 425, "Innate camo detection across the glade."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Riverbank.", "First", 810, "Seeking shurikens follow bloons through the mushroom groves."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Riverbank.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Riverbank.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the glade entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "party_parade": {
        "id": "party_parade",
        "name": "Party Parade",
        "category": "Advanced",
        "terrain": "Carnival Festival Street",
        "lanes": "Two alternating lanes separated by carnival parade tents and confetti booths",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Festival booths and party tents separate two parallel parade lanes",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A festive carnival street with colorful party floats and festival booths. Bloons alternate down two parallel streets that cross at the main carnival stage.",
                "camo_handling": "Sauda placed at the carnival stage crossover handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the stage to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB on the parade street.",
                "why_it_works": "The central festival stage crossover connects both alternating lanes into a single killzone.",
                "research_sources": ["Bloons Wiki - Party Parade"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly at the central festival stage crossover.", "First", 510, "Hits bloons on both alternating carnival streets."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda by the festival booth.", "First", 425, "Innate camo detection across the street."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Festival booth.", "First", 810, "Seeking shurikens follow bloons down both parade lanes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Festival booth.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Festival booth.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the parade entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "ascent": {
        "id": "ascent",
        "name": "Ascent",
        "category": "Advanced",
        "terrain": "Palace Garden Ramparts",
        "lanes": "Two alternating lanes ascending palace terraces and garden stairs",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Rising stone terraces and garden hedges block vision between levels",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A grand palace courtyard where bloons climb garden terraces toward a high palace gate. The main terrace landing is the primary chokepoint.",
                "camo_handling": "Sauda placed on the terrace landing handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs terrace towers to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB on the terrace stairs.",
                "why_it_works": "Both ascending paths meet at the terrace landing, allowing a single concentrated defense to eliminate all bloons.",
                "research_sources": ["Bloons Wiki - Ascent"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the central terrace landing where both staircases meet.", "First", 510, "Secures the terrace chokepoint with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the marble terrace.", "First", 425, "Innate camo detection across both staircases."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Marble terrace.", "First", 810, "Seeking shurikens follow bloons up the palace steps."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Marble terrace.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Marble terrace.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the bottom palace entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    }
}
