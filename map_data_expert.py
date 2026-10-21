"""
map_data_expert.py
Contains comprehensive, round-by-round Easy/Standard (R1-40) strategies for all 13 Expert maps.
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

EXPERT_MAPS = {
    "dark_castle": {
        "id": "dark_castle",
        "name": "Dark Castle",
        "category": "Expert",
        "terrain": "Gothic Castle Drawbridge & Moat",
        "lanes": "Four lanes converging onto a single castle drawbridge",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Widely regarded as the easiest Expert map; four tracks converge directly onto a single wooden drawbridge",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A gothic castle surrounded by a water moat. While officially an Expert map, all four bloon paths converge into a single narrow drawbridge, making it one of the most reliable maps for concentrated defense.",
                "camo_handling": "Sauda placed directly at the drawbridge entrance handles Round 24 camo green. Monkey Sub 2-0-0 in the moat provides map-wide camo detection.",
                "lead_handling": "Alchemist 2-0-0 placed next to Sauda on the castle wall buffs the drawbridge defenders to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 at the drawbridge + Sub 2-0-3 Triple Guns + 0-3-2 Bomb Shooter crushes the Round 40 MOAB as soon as it touches the bridge.",
                "why_it_works": "The drawbridge funnels 100% of bloons into a single narrow lane surrounded by land and water placement spots.",
                "research_sources": ["Bloons Wiki - Dark Castle", "BTD6 Community Dark Castle Guides"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly in front of the castle drawbridge gate where all 4 paths converge.", "First", 510, "Hits all bloons from all four tracks at the drawbridge bottleneck."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the castle moat water right beside the drawbridge.", "First", 275, "Provides rapid dart fire from the moat."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Castle moat.", "First", 980, "Advanced Intel allows Sub to shoot anywhere towers have vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Tack Shooter", "0-0-0", "On the castle bank next to Sauda at the drawbridge.", "First", 240, "Covers the entire width of the drawbridge bottleneck."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Drawbridge bank.", "First", 1555, "Tack Sprayer fires 16 tacks into the concentrated bloon stream."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "On the castle wall next to Sauda and Tack.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Drawbridge bank.", "First", 2800, "Overdrive completely locks down the drawbridge gate."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the drawbridge entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive obliterate the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "flooded_valley": {
        "id": "flooded_valley",
        "name": "Flooded Valley",
        "category": "Expert",
        "terrain": "Massive Dam Reservoir",
        "lanes": "Single path traveling along the lower rocky valley before the dam",
        "water": True,
        "sight_blockers": True,
        "gimmick": "The valley is flooded by a massive dam; land towers can only be placed on the upper dam rim",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Admiral Brickell",
                "hero_alternatives": ["Quincy", "Sauda"],
                "starting_cash": 650,
                "overview": "A towering hydro-electric dam holding back a deep lake. Land monkeys can only stand on the upper dam walkway, but the vast water allows Monkey Subs to dominate.",
                "camo_handling": "Monkey Sub 2-0-0 with Advanced Intel or Quincy on the dam ledge covers all camos effortlessly.",
                "lead_handling": "Monkey Sub 0-3-0 (Ballistic Missile) or Sniper 1-0-0 on the dam ledge pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts + Ballistic Missile 0-3-2 shreds the Round 40 MOAB in the water.",
                "why_it_works": "The entire reservoir provides deep water for Sub Commander and AP Darts with unobstructed global vision.",
                "research_sources": ["Bloons Wiki - Flooded Valley", "Expert Naval Strategy Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Monkey Sub", "0-0-0", "In the reservoir water close to the dam wall.", "First", 275, "High-velocity dart fire from the reservoir."),
                    create_step(2, "Rounds 1–10: Opening Defense", 4, "Place", "Dart Monkey", "0-0-0", "On the top ledge of the dam overlooking the track.", "First", 170, "Provides vision for the Sub's Advanced Intel."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 10, "Upgrade", "Monkey Sub", "2-0-2", "Reservoir water.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Dart Monkey can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Place", "Sniper Monkey", "0-0-0", "On the top dam ledge next to Dart Monkey.", "First", 300, "Provides global rifle fire from the high ground."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Reservoir water.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Sniper Monkey", "1-0-2", "Top dam ledge.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Reservoir water.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Top dam ledge.", "Strong", 2450, "Deadly Precision delivers massive MOAB damage. The AP Darts Sub finishes the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "infernal": {
        "id": "infernal",
        "name": "Infernal",
        "category": "Expert",
        "terrain": "Volcanic Magma Chasms",
        "lanes": "Two alternating lanes across floating obsidian rocks in a lake of fire",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Tiny floating obsidian islands allow only 1 tower each; vast lava lake",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A hellish volcanic chasm where towers can only be placed on small floating obsidian rocks. Quincy placed on the center rock reaches both paths easily.",
                "camo_handling": "Quincy handles early camos from the center rock. Sniper 0-2-3 placed on a side rock covers all camos.",
                "lead_handling": "Sniper 1-0-0 on a side rock or Wizard 0-1-0 Fireball pops Leads on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Wizard 0-3-2 Dragon's Breath destroys the Round 40 MOAB.",
                "why_it_works": "Global range towers (Sniper) and long-range heroes (Quincy) completely bypass the placement restrictions.",
                "research_sources": ["Bloons Wiki - Infernal"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central circular obsidian rock in the middle of the lava.", "First", 460, "Has range covering both the left and right lava paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On the small obsidian rock at the top-left.", "First", 300, "Provides global rifle fire across the magma."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Top-left rock.", "First", 935, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Wizard Monkey", "0-0-0", "On the bottom-right obsidian rock.", "First", 320, "Adds magical energy bolts."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Wizard Monkey", "0-2-2", "Bottom-right rock.", "First", 850, "Fireball and Wall of Fire melt Leads on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Sniper Monkey", "3-0-2", "Top-left rock.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Wizard Monkey", "0-3-2", "Bottom-right rock.", "First", 2720, "Dragon's Breath spews continuous flames across the lava track."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the bottom obsidian rock.", "Strong", 1530, "MOAB Mauler delivers heavy blimp damage. Deadly Precision Sniper and Dragon's Breath destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "muddy_puddles": {
        "id": "muddy_puddles",
        "name": "Muddy Puddles",
        "category": "Expert",
        "terrain": "Rainy Mud Trenches",
        "lanes": "Four parallel lanes cycling through muddy puddles",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Bloons travel down four separate vertical paths; deep mud puddles accommodate water towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Four vertical muddy paths with water puddles in between. Bloons cycle through the four paths sequentially. Global towers like Sniper and Sub with Advanced Intel are mandatory.",
                "camo_handling": "Quincy placed on the center island handles early camos. Monkey Sub 2-0-0 in the puddles provides map-wide camo support.",
                "lead_handling": "Sniper 1-0-0 on the center island pops Leads on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Sub 2-0-4 AP Darts crushes the Round 40 MOAB on whichever path it spawns.",
                "why_it_works": "Global range attacks from Sniper and Advanced Intel Sub reach all four parallel tracks simultaneously.",
                "research_sources": ["Bloons Wiki - Muddy Puddles", "BTD6 Expert Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the center dry island between path 2 and path 3.", "First", 460, "Fires arrows across the two middle tracks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central muddy puddle between path 2 and 3.", "First", 275, "Provides dart fire from the water puddle."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Central puddle.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Quincy can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Sniper Monkey", "0-0-0", "On the center island next to Quincy.", "First", 300, "Provides global rifle fire across all 4 tracks."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "1-0-2", "Center island.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Central puddle.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Central puddle.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Center island.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs. The Sub and Sniper finish the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "bloody_puddles": {
        "id": "bloody_puddles",
        "name": "Bloody Puddles",
        "category": "Expert",
        "terrain": "Crimson Blood Swamps",
        "lanes": "Five alternating and simultaneous lanes crossing red water puddles",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Widely considered the hardest map in BTD6; five separate vertical lanes with alternating bloon flows",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "The infamous five-lane bloody swamp. Bloons cycle across all five lanes. On Easy difficulty, a central global setup with Quincy, Sniper, and Sub handles all lanes with precision.",
                "camo_handling": "Quincy handles early camos. Monkey Sub 2-0-0 with Advanced Intel in the red puddle covers all 5 tracks.",
                "lead_handling": "Sniper 1-0-0 pops Leads on Round 28 with infinite global range.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Sub 2-0-4 AP Darts crushes the Round 40 MOAB on any lane.",
                "why_it_works": "Global range towers are the only viable way to defend 5 separate lanes without splitting cash thin.",
                "research_sources": ["Bloons Wiki - Bloody Puddles", "BTD6 Bloody Puddles Compendium"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central dry sandbar between lane 3 and lane 4.", "First", 460, "Covers the central lanes with long-range arrows."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central red puddle between lane 2 and lane 3.", "First", 275, "Provides dart fire from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Central red puddle.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Quincy can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Sniper Monkey", "0-0-0", "On the central sandbar next to Quincy.", "First", 300, "Provides global rifle fire across all 5 tracks."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "1-0-2", "Central sandbar.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28 across any lane."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Central red puddle.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Central red puddle.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Central sandbar.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs. The Sub and Sniper finish the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "ouch": {
        "id": "ouch",
        "name": "#Ouch",
        "category": "Expert",
        "terrain": "Flooded Crossroads Pond",
        "lanes": "Four perpendicular lanes forming a pound (#) sign around a central water square",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Four separate crossing paths forming a grid around a central square water reservoir",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Four straight tracks intersecting like a tic-tac-toe / pound sign around a square pond. The central pond touches all four track intersections.",
                "camo_handling": "Quincy covers early camos from the upper-left quadrant. Monkey Sub 2-0-0 in the central pond covers all four paths.",
                "lead_handling": "Sniper 1-0-0 or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts in the center pond + Sniper 3-0-2 on Strong destroys the Round 40 MOAB.",
                "why_it_works": "The central square pond touches all four paths, allowing naval towers to cover the entire grid.",
                "research_sources": ["Bloons Wiki - #Ouch"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "In the top-left intersection quadrant between vertical lane 1 and horizontal lane 1.", "First", 460, "Fires arrows across both top tracks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central square water pond.", "First", 275, "Provides dart fire from the central water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Central pond.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Quincy can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Sniper Monkey", "0-0-0", "In the top-left quadrant next to Quincy.", "First", 300, "Provides global rifle fire across all 4 intersections."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "1-0-2", "Top-left quadrant.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Central pond.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Central pond.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Top-left quadrant.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs. The Sub and Sniper finish the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "quad": {
        "id": "quad",
        "name": "Quad",
        "category": "Expert",
        "terrain": "Four-Corner Intersection",
        "lanes": "Four independent lanes entering from each corner of the map",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Four independent tracks entering from top-left, top-right, bottom-left, and bottom-right",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "Four separate paths enter from the four corners and cross the map. Towers with global range and central area coverage are essential.",
                "camo_handling": "Quincy placed in the center handles early camos. Sniper 0-2-3 placed in the center covers all four corners.",
                "lead_handling": "Sniper 1-0-0 on Strong pops Leads on Round 28 across any path.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 in the center destroys the Round 40 MOAB.",
                "why_it_works": "Sniper and Quincy in the center can hit bloons on all four corner tracks without moving.",
                "research_sources": ["Bloons Wiki - Quad"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "In the exact center of the map between all 4 track crossings.", "First", 455, "Fires arrows into all 4 corner paths."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "In the center of the map next to Quincy.", "First", 300, "Provides global rifle fire across all 4 corners."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Center map.", "First", 980, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "At one of the corner crossings.", "First", 170, "Adds cleanup darts."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 24, "Upgrade", "Sniper Monkey", "3-0-2", "Center map.", "Strong", 3740, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot.", timing="before_round"),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Corner crossing.", "First", 970, "Crossbow provides high damage cleanup.", timing="during_round"),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Place", "Bomb Shooter", "2-0-3", "In the center map.", "Close", 2400, "Recursive Cluster bombs wipe out grouped bloons across all 4 lanes.", timing="during_round"),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "In the center map.", "Strong", 2355, "MOAB Mauler delivers heavy blimp damage. Sniper on Strong and Quincy destroy the MOAB.", timing="before_round")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "ravine": {
        "id": "ravine",
        "name": "Ravine",
        "category": "Expert",
        "terrain": "Deep Mountain Chasm",
        "lanes": "Four alternating lanes across narrow mountain paths and a wooden bridge",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Steep canyon walls block lower sight; bloons converge across a single rickety wooden bridge",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A treacherous mountain gorge with steep cliffs and four entry paths that converge onto a central wooden bridge. Defending the bridge chokepoint is key.",
                "camo_handling": "Quincy on the wooden bridge handles early camos. Sniper 0-2-3 placed on the high cliff ledge covers all paths.",
                "lead_handling": "Sniper 1-0-0 on the cliff ledge pops Leads on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 destroys the Round 40 MOAB on the wooden bridge.",
                "why_it_works": "The wooden bridge is the single physical convergence for all ravine paths.",
                "research_sources": ["Bloons Wiki - Ravine"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central wooden bridge where the ravine paths converge.", "First", 455, "Fires arrows across the bridge chokepoint."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On the elevated cliff ledge overlooking the ravine.", "First", 300, "Provides global rifle fire with high-ground vision."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Cliff ledge.", "First", 980, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "At the exit of the wooden bridge.", "First", 170, "Adds cleanup darts."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 24, "Upgrade", "Sniper Monkey", "3-0-2", "Cliff ledge.", "Strong", 3740, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot.", timing="before_round"),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Bridge exit.", "First", 970, "Crossbow provides high damage cleanup.", timing="during_round"),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Place", "Bomb Shooter", "2-0-3", "At the bridge exit.", "Close", 2400, "Recursive Cluster bombs wipe out grouped bloons.", timing="during_round"),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the bridge entrance.", "Strong", 2355, "MOAB Mauler delivers heavy blimp damage. Sniper on Strong and Quincy destroy the MOAB.", timing="before_round")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "sanctuary": {
        "id": "sanctuary",
        "name": "Sanctuary",
        "category": "Expert",
        "terrain": "Floating Marble Slabs",
        "lanes": "Two alternating lanes across floating marble platforms over water",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Floating marble slabs shift positions every round; central temple pool allows water towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "An ancient temple sanctuary where marble platforms float over deep water and shift positions each round. The central water pool remains stable and offers great Sub placement.",
                "camo_handling": "Quincy handles early camos from the stationary ground. Monkey Sub 2-0-0 in the central pool covers all camos.",
                "lead_handling": "Sniper 1-0-0 or Sub 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub 2-0-4 Armor Piercing Darts + Sniper 3-0-2 on Strong destroys the Round 40 MOAB.",
                "why_it_works": "The central temple pool is unaffected by shifting platforms, providing stable naval firepower.",
                "research_sources": ["Bloons Wiki - Sanctuary"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the stationary marble bank at the top-left.", "First", 460, "Safe from shifting platforms with long-range arrows."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Sub", "0-0-0", "In the central permanent temple pool.", "First", 275, "Provides dart fire from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Temple pool.", "First", 980, "Advanced Intel allows Sub to shoot anywhere Quincy can see."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Sniper Monkey", "0-0-0", "On the stationary marble bank next to Quincy.", "First", 300, "Provides global rifle fire across the sanctuary."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "1-0-2", "Marble bank.", "Strong", 935, "Full Metal Jacket pops Leads on Round 28."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Upgrade", "Monkey Sub", "2-0-3", "Temple pool.", "First", 1105, "Triple Guns fires high-frequency darts."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Temple pool.", "First", 2125, "Armor Piercing Darts inflicts heavy damage to ceramics and blimps."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Sniper Monkey", "3-0-2", "Marble bank.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOABs. The Sub and Sniper finish the blimp.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "workshop": {
        "id": "workshop",
        "name": "Workshop",
        "category": "Expert",
        "terrain": "Industrial Conveyor Factory",
        "lanes": "Single path along high-speed industrial conveyor belts with reverse levers",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Conveyor belts accelerate bloons; interactive track extensions and reverse levers can be purchased",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "An automated monkey workshop where bloons travel along fast motorized conveyor belts. Defending the central conveyor junction before bloons accelerate is essential.",
                "camo_handling": "Sauda placed at the conveyor junction handles Round 24. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the conveyor junction to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB at the conveyor junction.",
                "why_it_works": "The central conveyor junction is before the speed-up belts, giving towers standard bloon speed to hit.",
                "research_sources": ["Bloons Wiki - Workshop"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the primary conveyor belt junction near the workshop entrance.", "First", 510, "Hits bloons before they enter the high-speed conveyor section."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda on the factory floor.", "First", 425, "Innate camo detection across the conveyor."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Factory floor.", "First", 810, "Seeking shurikens follow bloons down the belts."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Factory floor.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Factory floor.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the conveyor entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "dark_dungeons": {
        "id": "dark_dungeons",
        "name": "Dark Dungeons",
        "category": "Expert",
        "terrain": "Subterranean Dungeon Citadel",
        "lanes": "Two main lanes with secret statue passages and spike/fire traps",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Massive subterranean fortress with interactive spike and fire traps and statue secret paths",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A vast dungeon fortress with stone arches and dungeon cells. Both main dungeon paths pass beneath the central stone archway before splitting toward the lower cells.",
                "camo_handling": "Quincy on the central stone arch handles early camos. Ninja 3-0-1 covers all subsequent camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the stone arch to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB under the stone arch.",
                "why_it_works": "The central stone archway is the primary chokepoint where both dungeon lanes converge.",
                "research_sources": ["Bloons Wiki - Dark Dungeons"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the central stone archway overlooking both dungeon entry corridors.", "First", 460, "Fires arrows down both dungeon hallways."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "On the stone walkway beneath the arch.", "First", 425, "Innate camo detection across both corridors."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Stone walkway.", "First", 810, "Seeking shurikens follow bloons through the dungeon arches."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Stone walkway.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja on the walkway.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Stone walkway.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the dungeon hallway entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Quincy destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "glacial_trail": {
        "id": "glacial_trail",
        "name": "Glacial Trail",
        "category": "Expert",
        "terrain": "Frigid Arctic Cavern",
        "lanes": "Single path through freezing ice caverns with periodic tower freezing",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Severe cold mechanics freeze monkeys solid periodically, cycling which towers can attack",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A freezing glacial trail where biting arctic cold causes monkeys to periodically freeze solid and thaw in alternating cycles. Staggering placements ensures at least one tower is always active.",
                "camo_handling": "Quincy handles early camos. Sniper 0-2-3 placed on a separate ice shelf covers all camos when thawed.",
                "lead_handling": "Sniper 1-0-0 on the ice shelf or Bomb 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Sniper 3-0-2 Deadly Precision on Strong + Bomb Shooter 0-3-2 destroys the Round 40 MOAB.",
                "why_it_works": "Staggering tower placements between different ice shelves ensures continuous defense even when one tower freezes.",
                "research_sources": ["Bloons Wiki - Glacial Trail", "Update 40 Release Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "On the upper ice shelf overlooking the trail entrance.", "First", 455, "Fires arrows down the glacial path."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Sniper Monkey", "0-0-0", "On a separate lower ice shelf away from Quincy.", "First", 300, "Provides global rifle fire when thawed."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Sniper Monkey", "1-0-2", "Lower ice shelf.", "First", 980, "Full Metal Jacket and Faster Firing clears bloons quickly."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Dart Monkey", "0-0-0", "At the trail exit shelf.", "First", 170, "Adds third staggered tower for freeze cycle redundancy."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 24, "Upgrade", "Sniper Monkey", "3-0-2", "Lower ice shelf.", "Strong", 3740, "Deadly Precision pops Leads on Round 28 and inflicts 20 damage per shot.", timing="before_round"),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Dart Monkey", "0-2-3", "Exit shelf.", "First", 970, "Crossbow provides high damage cleanup.", timing="during_round"),
                    create_step(7, "Rounds 31–39: Final Preparation", 34, "Place", "Bomb Shooter", "2-0-3", "Near the trail bend.", "Close", 2400, "Recursive Cluster bombs wipe out grouped bloons.", timing="during_round"),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Near the trail entrance.", "Strong", 2355, "MOAB Mauler delivers heavy blimp damage. Sniper on Strong and Quincy destroy the MOAB.", timing="before_round")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "blons": {
        "id": "blons",
        "name": "Blons",
        "category": "Expert",
        "terrain": "Minimalist Lawn Corner",
        "lanes": "Single microscopic track corner (4.2 RBS)",
        "water": True,
        "sight_blockers": False,
        "gimmick": "The shortest official track in Bloons TD 6; bloons only travel around a tiny 90-degree corner",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "The infamous minimalist challenge map with the shortest track in the entire game (a single tiny right-angle corner). Every millisecond counts; towers must be placed directly at the apex of the corner.",
                "camo_handling": "Sauda placed directly at the corner apex attacks immediately from Round 1 and handles Round 24 camo green with zero travel time.",
                "lead_handling": "Alchemist 2-0-0 placed right next to Sauda buffs her swords for Round 28 Leads.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive at the corner apex + Spike Factory 0-2-3 at the corner exit shreds the Round 40 MOAB before it leaves the screen.",
                "why_it_works": "Placing Tack Overdrive and Sauda directly touching the corner apex delivers maximum burst DPS within the short track length.",
                "research_sources": ["Bloons Wiki - Blons", "r/btd6 Blons Community Guides"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly at the apex of the tiny track corner.", "First", 510, "Swords hit bloons the instant they appear on screen."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Immediately adjacent to Sauda at the inner corner apex.", "First", 240, "Radial tacks cover the entire track corner."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Corner apex.", "First", 620, "Faster shooting and extra pierce stops fast bloon leaks."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Touching Sauda and Tack Shooter.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Corner apex.", "First", 935, "Tack Sprayer fires 16 tacks continuously across the corner."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Next to Sauda.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Corner apex.", "First", 2800, "Overdrive delivers extreme point-blank DPS."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Spike Factory", "0-2-3", "At the very exit point of the tiny corner.", "Normal", 2210, "Long Life Spikes piles heavy spikes at the exit. Overdrive cracks the MOAB and spikes catch all ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    }
}
