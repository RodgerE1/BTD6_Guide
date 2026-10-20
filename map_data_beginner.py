"""
map_data_beginner.py
Contains comprehensive, round-by-round Easy/Standard (R1-40) strategies for all 26 Beginner maps.
"""

def create_step(step_number, round_range, round_num, action, tower, upgrade, placement, targeting, cost, details):
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
        "details": details
    }

BEGINNER_MAPS = {
    "monkey_meadow": {
        "id": "monkey_meadow",
        "name": "Monkey Meadow",
        "category": "Beginner",
        "terrain": "Grassland Meadow",
        "lanes": "Single winding lane with center loop",
        "water": False,
        "sight_blockers": False,
        "gimmick": "None (Open field with high visibility)",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "The iconic starter map features a long, winding dirt track through an open grassy meadow with a prominent center loop. Towers placed in the inner bends maximize attack uptime as bloons circle around them.",
                "camo_handling": "Sauda hits camo naturally from Round 1. Ninja Monkey (0-0-0) placed on Round 18 adds redundant camo detection well before Round 24 (single green camo) and Round 33 (camo reds/yellows).",
                "lead_handling": "Alchemist (2-0-0 Acidic Mixture Dip) placed on Round 26 grants lead-popping to Sauda and Ninja, easily neutralizing Round 28 and 30 Lead Bloons.",
                "moab_handling": "Bomb Shooter upgraded to 0-3-2 (MOAB Mauler) placed at the center bend on Round 36 tears through the Round 40 MOAB hull, while Sauda and 4-0-1 Ninja shred the ceramic children.",
                "why_it_works": "The central loop allows high-damage melee and short-range towers to hit bloons twice. Sauda + 4-0-1 Ninja + 3-2-0 Alchemist provides top-tier pierce, tracking shurikens, and lead buff.",
                "research_sources": ["Bloons Wiki - Monkey Meadow", "BTD6 Beginner Index", "In-Game Easy Playtesting"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Inside the upper bend of the central circular loop where her swords reach both lanes.", "First", 510, "Sauda soloes the early rounds with zero leaks due to dual-lane coverage and high base pierce."),
                    create_step(2, "Rounds 1–10: Opening Defense", 8, "Place", "Dart Monkey", "0-0-0", "Slightly below Sauda along the straightaway heading into the loop.", "First", 170, "Adds extra chip damage and cleans up stray fast blue bloons."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Dart Monkey", "0-2-2", "Same location.", "First", 480, "Quick Shots and Enhanced Eyes increase attack speed and projectile range."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 18, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda inside the center loop.", "First", 425, "Provides innate camo detection and fast shuriken delivery across the intersection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Center loop next to Sauda.", "First", 1370, "Double Shot and Seeking Shuriken effortlessly wipe out Round 24 camo green and dense wave packs."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Immediately above the Ninja and Sauda within range of both.", "Strong", 1050, "Acidic Mixture Dip enables both Sauda and the Ninja to pop Round 28 and 30 Lead Bloons instantly."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Ninja Monkey", "4-0-1", "Center loop.", "First", 2340, "Bloonjitsu fires 5 shurikens simultaneously, utterly dominating mid-game ceramic and rainbow rushes."),
                    create_step(8, "Rounds 31–39: Final Preparation", 35, "Upgrade", "Alchemist", "3-2-0", "Next to Ninja.", "Close", 1275, "Berserker Brew gives +1 damage and increased attack speed to the Bloonjitsu Ninja."),
                    create_step(9, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the primary entrance turn just before the loop.", "Strong", 2040, "MOAB Mauler deals massive bonus blimp damage. When the MOAB arrives on Round 40, activate Sauda's Leaping Sword ability to instantly crack the hull and mop up the ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "tree_stump": {
        "id": "tree_stump",
        "name": "Tree Stump",
        "category": "Beginner",
        "terrain": "Forest Clearing",
        "lanes": "Single path spiraling around a large tree stump",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Center tree stump offers elevated high-ground bonus range and unobstructed line of sight",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "The track circles around a massive elevated tree stump. Towers placed on top of the stump gain enhanced range and shoot over the surrounding trees.",
                "camo_handling": "Sauda placed at the base intersection detects camo from Round 1. A 0-2-3 Dart Monkey on top of the stump detects all camos on Round 24 and 33.",
                "lead_handling": "Obyn's nature attack or a 1-0-0 Sniper placed on the stump pops Leads effortlessly on Round 28.",
                "moab_handling": "Tack Shooter upgraded to 2-0-4 Overdrive at the inner bend combined with Sauda's Leaping Sword obliterates the Round 40 MOAB in seconds.",
                "why_it_works": "The circular track wraps completely around the central stump. A high-damage Overdrive Tack inside the loop hits bloons during 80% of their journey.",
                "research_sources": ["Bloons Wiki - Tree Stump", "BTD6 Strategy Compendium"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the lower track loop directly beneath the tree stump.", "First", 510, "Guarantees full defense against early bloons while earning gold for high-ground towers."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Directly in the tight inner bend of the lower track wrap.", "First", 240, "Positions the Tack Shooter where every nail strikes passing bloons."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Lower track wrap.", "First", 620, "Faster shooting and extra pierce easily clear dense swarms."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 16, "Place", "Dart Monkey", "0-0-0", "On top of the elevated tree stump platform.", "First", 170, "Takes advantage of elevated line of sight over all obstacles."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 21, "Upgrade", "Dart Monkey", "0-2-3", "Top of tree stump.", "First", 1275, "Crossbow gives long range and camo detection across both sides of the tree stump."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 25, "Place", "Sniper Monkey", "1-0-0", "Top of tree stump next to Dart Monkey.", "Strong", 650, "Full Metal Jacket pops Leads on Round 28 with infinite range."),
                    create_step(7, "Rounds 31–39: Final Preparation", 31, "Upgrade", "Tack Shooter", "2-0-4", "Lower track wrap.", "First", 2800, "The Overdrive upgrade sprays 32 tacks at super-high speed, melting ceramics and grouped bloons."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Upgrade", "Sniper Monkey", "3-0-2", "Top of tree stump.", "Strong", 2450, "Deadly Precision inflicts 20 damage per shot to MOAB-class bloons. The MOAB breaks instantly over the Tack Overdrive.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "town_center": {
        "id": "town_center",
        "name": "Town Center",
        "category": "Beginner",
        "terrain": "Village Town",
        "lanes": "Single path looping through village streets with a central pond",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Central pond accommodates water towers; town buildings block low line-of-sight",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "Winding cobblestone streets wrap around a central water pond and village houses. The pond offers ideal positioning for Buccaneer and Sub, while the main crossroads is an ideal killzone.",
                "camo_handling": "Sauda handles Round 24. Buccaneer upgraded to 0-2-2 (Crow's Nest) spots all camos effortlessly.",
                "lead_handling": "Buccaneer's Hot Shot (0-2-0) or Sauda's level 3 ability destroys Lead Bloons on Round 28.",
                "moab_handling": "Monkey Buccaneer upgraded to 3-2-0 Destroyer unleashes a barrage of flaming darts and grapes that tears the Round 40 MOAB apart.",
                "why_it_works": "The central pond gives the Buccaneer 360-degree coverage over 3 separate track segments, creating maximum firing uptime.",
                "research_sources": ["Bloons Wiki - Town Center", "Community Easy Walkthroughs"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the main crossroad turn just southwest of the central pond.", "First", 510, "Anchors the early defense, catching bloons as they turn the corner."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the center of the village pond.", "First", 425, "Provides long-range dual-cannon fire across multiple track lanes."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Village pond.", "First", 210, "Grape Shot fires 4 sharp grapes with every attack."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Village pond.", "First", 680, "Hot Shot pops Leads with fire; Crow's Nest grants full Camo vision."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Village pond.", "First", 2510, "Destroyer attacks 5x faster, shredding dense bloon waves and Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Alchemist", "2-0-0", "On the grass bank next to the pond, within range of Buccaneer.", "Strong", 1050, "Acidic Mixture Dip boosts grape damage and range."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Bomb Shooter", "2-0-3", "At the hairpin bend south of the pond.", "Close", 2150, "Cluster Bombs eradicate grouped rainbow and ceramic bloons."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "North of the crossroads.", "Strong", 1530, "MOAB Mauler targets the blimp directly. The Destroyer and Sauda instantly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "resort": {
        "id": "resort",
        "name": "Resort",
        "category": "Beginner",
        "terrain": "Tropical Holiday Resort",
        "lanes": "Single path featuring a notorious loop around the entrance building and pool",
        "water": True,
        "sight_blockers": False,
        "gimmick": "The opening loop has bloons circle 3 consecutive times around a single small square",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "Resort is famous as one of the best farming and easiest maps in BTD6. The bloon path immediately enters a tight square loop around the poolside cafe where bloons travel around the same spot 3 times.",
                "camo_handling": "Sauda placed inside the loop has innate camo detection. A 0-2-3 Dart Monkey covers any strays.",
                "lead_handling": "Sauda's level 3 Leaping Sword and an Alchemist 2-0-0 placed inside the loop pop Leads instantly on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 (Overdrive) in the top-right corner of the pool loop inflicts continuous damage across all 3 passes, shredding the MOAB before it leaves the resort entrance.",
                "why_it_works": "Towers placed in the loop get 3 separate chances to hit every single bloon. A single Overdrive Tack does triple its normal DPS.",
                "research_sources": ["Bloons Wiki - Resort", "r/btd6 Resort Meta Guide"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly in the top-left bend of the entrance pool loop.", "First", 510, "Hits bloons on their entrance pass, circular pass, and exit pass."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the top-right corner inside the pool loop.", "First", 240, "The single best Tack Shooter placement in the entire game."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Inside pool loop.", "First", 620, "Faster shooting and extra pierce clears through all initial waves."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Just below Sauda inside the loop.", "Strong", 1050, "Buffs Sauda and Tack with Lead-popping and +1 damage."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Upgrade", "Tack Shooter", "2-0-3", "Inside pool loop.", "First", 935, "Tack Sprayer fires 16 tacks per volley into the 3-lane intersection."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Inside pool loop.", "Close", 1060, "Berserker Brew makes the Tack Sprayer rip through Round 28 Leads and 30 swarms."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Inside pool loop.", "First", 2800, "The Overdrive upgrade turns the entrance loop into an inescapable shredder."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-0", "Outside the pool loop near the entrance path.", "Strong", 1530, "Weakens the Round 40 MOAB hull. The Overdrive Tack destroys the blimp and ceramic contents instantly.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "logs": {
        "id": "logs",
        "name": "Logs",
        "category": "Beginner",
        "terrain": "Woodland Marsh",
        "lanes": "Single extremely long path weaving between fallen logs and small ponds",
        "water": True,
        "sight_blockers": False,
        "gimmick": "The longest bloon track in Bloons TD 6 (over 2 minutes of travel time for a red bloon)",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot", "Benjamin"],
                "starting_cash": 650,
                "overview": "Logs is the longest map in the game. Bloons weave back and forth between fallen tree trunks, giving players massive amounts of time to pop bloons and build defenses.",
                "camo_handling": "Sauda hits camo naturally from Round 1. A 0-2-3 Dart Monkey or 3-0-1 Ninja provides additional coverage.",
                "lead_handling": "Alchemist 2-0-0 or 1-0-0 Sniper pops leads effortlessly on Round 28.",
                "moab_handling": "The massive track length means any basic Tier 3/4 setup like 2-0-4 Tack or 4-0-1 Ninja destroys the MOAB with over 75% of the track remaining.",
                "why_it_works": "Because the track is so exceptionally long, bloons spend maximum time in tower ranges. Almost any cohesive setup easily wins.",
                "research_sources": ["Bloons Wiki - Logs", "BTD6 Longest Maps Compendium"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the central U-turn intersection where multiple log paths cross.", "First", 510, "Easily defends all early rounds while cash accumulates."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the center bend directly adjacent to Sauda.", "First", 240, "Covers three parallel segments of the log path."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-3", "Center bend.", "First", 1555, "Tack Sprayer with Faster Shooting wipes out fast pinks and grouped greens."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 18, "Place", "Ninja Monkey", "0-0-0", "Next to Sauda in the center clearing.", "First", 425, "Innate camo detection ensures Round 24 green camo is neutralized."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Upgrade", "Ninja Monkey", "3-0-1", "Center clearing.", "First", 1370, "Double Shot shurikens home into bloons across multiple logs."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Adjacent to Sauda and Tack Shooter.", "Strong", 1050, "Gives lead-popping to Tack and Sauda for Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Center bend.", "First", 2800, "Overdrive completely controls the center intersection."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Ninja Monkey", "4-0-1", "Center clearing.", "First", 2340, "Bloonjitsu + Overdrive + Sauda annihilates the Round 40 MOAB almost instantly upon entry.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "cubism": {
        "id": "cubism",
        "name": "Cubism",
        "category": "Beginner",
        "terrain": "Geometric Art",
        "lanes": "Single multi-loop path through modern art triangles and squares",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Features multiple large geometric water ponds allowing heavy marine defense",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A very long, looping geometric art map with sharp angular bends and three large water triangles. The long path and abundant water make it one of the easiest maps in the game.",
                "camo_handling": "Sauda handles Round 24. Monkey Sub (2-0-0) placed in the upper triangular pool provides map-wide camo decamo with Submerge & Support (3-0-0).",
                "lead_handling": "Alchemist 2-0-0 or Bomb Shooter 0-3-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Sub upgraded to 2-0-4 (Sub Commander path) or Buccaneer 3-2-0 melts the Round 40 MOAB easily.",
                "why_it_works": "The track wraps around triangular water reservoirs, allowing Subs with Advanced Darts to attack bloons everywhere.",
                "research_sources": ["Bloons Wiki - Cubism", "BTD6 Beginner Guides"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the primary loop intersection in the upper-left.", "First", 510, "Chops through early reds and blues."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Monkey Sub", "0-0-0", "In the upper triangular water pool.", "First", 275, "Provides fast dart attacks from the water."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Monkey Sub", "2-0-2", "Upper water pool.", "First", 980, "Advanced Intel allows the Sub to shoot anywhere any tower has vision."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Tack Shooter", "0-0-0", "In the tight triangular corner near Sauda.", "First", 240, "Covers three sharp turns."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Sub", "2-0-3", "Upper water pool.", "First", 1105, "Triple Guns fires high-frequency darts with map-wide intel."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Next to Sauda.", "Strong", 1050, "Enables lead popping on Round 28."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Monkey Sub", "2-0-4", "Upper water pool.", "First", 2125, "Armor Piercing Darts deals massive bonus damage against Ceramics and MOABs."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Along the central lane bend.", "Strong", 1530, "Cracks the MOAB outer layer. The 2-0-4 Sub cleans up all ceramic ceramics from across the map.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "in_the_loop": {
        "id": "in_the_loop",
        "name": "In The Loop",
        "category": "Beginner",
        "terrain": "Cobblestone Garden",
        "lanes": "Single path featuring two wide circular loops and a central water pond",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Two distinct loops allow towers inside either loop to attack bloons for extended periods",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "The track winds through two large cobblestone loops with a small pond in the upper section. The lower loop creates a natural killzone for circular area-of-effect towers.",
                "camo_handling": "Sauda handles early camos. A 0-2-3 Dart Monkey or Ninja 3-0-1 guarantees complete camo safety.",
                "lead_handling": "Alchemist 2-0-0 buffing Sauda and Tack Shooter destroys Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive placed inside the bottom loop strips the MOAB layer immediately as it circles the loop.",
                "why_it_works": "Bloons must circle the complete perimeter of the loop. A high-attack-speed Tack Shooter gets continuous hits.",
                "research_sources": ["Bloons Wiki - In The Loop"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Inside the lower circular loop at the entrance crossover.", "First", 510, "Hits bloons both as they enter and as they circle the loop."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Directly in the center of the lower loop.", "First", 240, "Covers the entire inner circle of the track."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Lower loop center.", "First", 620, "Faster shooting and extra pierce clears grouped bloons."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda inside the lower loop.", "Strong", 1050, "Gives lead-popping to Sauda and Tack before Round 28."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Lower loop center.", "First", 935, "Tack Sprayer sprays 16 tacks continuously across the circle."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Next to Sauda.", "Close", 1060, "Berserker Brew boosts Tack damage and attack speed."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Lower loop center.", "First", 2800, "Overdrive completely obliterates all mid-game bloon waves."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-2", "At the entrance path leading into the upper loop.", "Strong", 2040, "Weakens the Round 40 MOAB before it reaches the lower loop. Sauda and Overdrive finish it off.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "four_circles": {
        "id": "four_circles",
        "name": "Four Circles",
        "category": "Beginner",
        "terrain": "Stone Circles",
        "lanes": "Single path weaving through four stone circular rings",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Four distinct circular track sections that bloons traverse in sequence",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "The track weaves sequentially through four stone circular rings. The center junction where the rings meet provides great coverage over multiple sections.",
                "camo_handling": "Sauda in the central junction spots camo from Round 1. Ninja 3-0-1 adds redundant camo coverage.",
                "lead_handling": "Alchemist 2-0-0 placed between Sauda and Tack handles Leads on Round 28 and 30.",
                "moab_handling": "Overdrive Tack (2-0-4) inside the first circle plus Bloonjitsu Ninja shreds the Round 40 MOAB.",
                "why_it_works": "The concentric loops force bloons to travel extensive curved paths, allowing Tack and Ninja towers to hit them repeatedly.",
                "research_sources": ["Bloons Wiki - Four Circles"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the central junction between circle 1 and circle 2.", "First", 510, "Cuts through bloons moving between the first two rings."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Inside the first circular ring.", "First", 240, "Deals radial damage throughout the first circle."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Circle 1.", "First", 620, "Faster shooting handles pink and white bloon rushes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda at the central junction.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Central junction.", "First", 1370, "Double Shot clears dense packs effortlessly."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Grants lead-popping for Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Circle 1.", "First", 3735, "Overdrive provides overwhelming DPS in the first ring."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Ninja Monkey", "4-0-1", "Central junction.", "First", 2340, "Bloonjitsu + Overdrive + Sauda pops the MOAB before it finishes circle 2.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "hedge": {
        "id": "hedge",
        "name": "Hedge",
        "category": "Beginner",
        "terrain": "Hedge Maze",
        "lanes": "Single path through tall green hedge labyrinth",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Tall hedges block line of sight completely, forcing towers to shoot only within their corridor",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Quincy",
                "hero_alternatives": ["Sauda", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A winding hedge maze with tall walls that block projectile vision. Placing towers at corner intersections or using towers that ignore obstacles (like Mortar or Wizard) is key.",
                "camo_handling": "Quincy gains camo detection at level 5. A 0-2-3 Dart Monkey positioned down the central alley covers all camos on Round 24 and 33.",
                "lead_handling": "Alchemist 2-0-0 or Bomb Shooter 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Bomb Shooter 0-3-2 MOAB Mauler placed at the primary corner bend bursts the Round 40 MOAB, while Crossbow Dart cleans up ceramics.",
                "why_it_works": "Placing towers right at the corner cutouts allows them to see down two corridors simultaneously, bypassing the hedge vision restrictions.",
                "research_sources": ["Bloons Wiki - Hedge"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Quincy", "0-0-0", "At the first major corner turn inside the hedge maze.", "First", 460, "Has straight line of sight down the entrance alley."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Dart Monkey", "0-0-0", "At the second corner bend looking down the main long hedge path.", "First", 170, "Adds piercing dart attacks along the corridor."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Dart Monkey", "0-2-2", "Main corridor bend.", "First", 480, "Faster attack speed and long range."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Tack Shooter", "0-0-0", "In the tight hairpin turn in the middle of the maze.", "First", 240, "Close-range multi-shot fits inside the hedge enclosure."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Dart Monkey", "0-2-3", "Main corridor bend.", "First", 1275, "Crossbow penetrates through dense waves with full camo detection."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Bomb Shooter", "2-0-0", "Next to Tack Shooter at the hairpin.", "Close", 935, "Heavy bombs pop Round 28 Leads easily within the narrow corridor."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Dart Monkey", "0-2-4", "Main corridor bend.", "First", 1700, "Sharp Shooter lands heavy critical hits down the entire length of the hedge."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Bomb Shooter", "2-3-0", "Hairpin turn.", "Strong", 1870, "MOAB Mauler delivers devastating damage to the Round 40 blimp. Quincy's Storm of Arrows cleans up any escaping ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "end_of_the_road": {
        "id": "end_of_the_road",
        "name": "End of the Road",
        "category": "Beginner",
        "terrain": "Desert Roadblock",
        "lanes": "Single path traveling down a dusty road into a dead-end barricade",
        "water": False,
        "sight_blockers": False,
        "gimmick": "The bloons travel straight down the road, loop around barricades, and turn back",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Striker Jones"],
                "starting_cash": 650,
                "overview": "A dusty road leading to a dead-end construction roadblock. Bloons travel along the road, turn around at the barricade, and travel back along an adjacent path.",
                "camo_handling": "Sauda placed at the turnaround loop detects camo naturally from Round 1. Ninja 3-0-1 backs her up.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the turnaround to pop Leads on Round 28.",
                "moab_handling": "Bomb Shooter 0-3-2 MOAB Mauler and Tack 2-0-4 Overdrive at the barricade destroy the MOAB upon arrival.",
                "why_it_works": "Bloons must turn 180 degrees at the end of the road. Towers placed at the dead-end hit bloons coming and going.",
                "research_sources": ["Bloons Wiki - End of the Road"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner turnaround bend right at the barricade.", "First", 510, "Hits bloons approaching and leaving the dead end."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Inside the U-turn curve at the roadblock.", "First", 240, "Covers the entire 180-degree turn."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "U-turn curve.", "First", 620, "Faster attacks stop grouped bloons."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Ninja Monkey", "0-0-0", "Next to Sauda at the barricade.", "First", 425, "Provides camo detection and seeking shurikens."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Barricade.", "First", 1370, "Double Shot sweeps early camo waves."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "Between Sauda and Tack Shooter.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "U-turn curve.", "First", 3735, "Overdrive melts ceramics and fast rushes."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the straightaway leading into the barricade.", "Strong", 2040, "MOAB Mauler softens the MOAB blimp. The Overdrive Tack finishes it at the roadblock.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "alpine_run": {
        "id": "alpine_run",
        "name": "Alpine Run",
        "category": "Beginner",
        "terrain": "Snowy Mountain Ski Trail",
        "lanes": "Single serpentine path winding down a snow-covered mountain",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Series of gentle S-curves down a mountain slope with pine trees",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A winding mountain ski slope with gentle snowy S-bends. Towers positioned inside the hairpins get extended firing time across two adjacent track lanes.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 provides complete camo coverage for Round 33 and 36.",
                "lead_handling": "Alchemist 2-0-0 buffs Ninja and Sauda to pop Leads on Round 28.",
                "moab_handling": "Bloonjitsu Ninja (4-0-1) + Berserker Brew Alchemist + Bomb 0-3-0 shatters the Round 40 MOAB on the first slope.",
                "why_it_works": "The serpentine curves force bloons to weave back and forth, allowing seeking shurikens and bombs to hit them continuously.",
                "research_sources": ["Bloons Wiki - Alpine Run"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "In the first sharp downhill hair-pin turn near the top.", "First", 510, "Guarantees clean early round pops with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda in the upper curve.", "First", 425, "Innate camo detection and fast shuriken delivery."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Upper curve.", "First", 810, "Seeking shurikens follow bloons through the S-turns."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Upper curve.", "First", 985, "Double Shot fires two shurikens per attack."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Grants lead-popping for Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Upper curve.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per volley."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the second hairpin turn down the slope.", "Strong", 2040, "MOAB Mauler bursts the blimp hull. The Bloonjitsu Ninja shreds all ceramic children.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "frozen_over": {
        "id": "frozen_over",
        "name": "Frozen Over",
        "category": "Beginner",
        "terrain": "Icy Cavern",
        "lanes": "Single path looping around a frozen prehistoric Cave Monkey",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Contains an easter egg prehistoric Cave Monkey encased in ice that can be chipped free",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A winding icy track circling around a frozen cave monkey in a block of ice. The loop around the central ice block creates an ideal killzone.",
                "camo_handling": "Sauda placed inside the loop spots camo on Round 24. Ninja 3-0-1 handles all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 placed next to Sauda melts Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive at the bottom loop plus Sauda's Leaping Sword ability wipes out the Round 40 MOAB.",
                "why_it_works": "The loop around the ice block provides high concentration of track, allowing short-range high-DPS towers to maximize damage.",
                "research_sources": ["Bloons Wiki - Frozen Over"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Inside the lower track bend circling the frozen cave monkey.", "First", 510, "Covers multiple passes around the ice."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the tightest inner corner of the ice block loop.", "First", 240, "Maximizes radial coverage across the curve."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Ice block loop.", "First", 620, "Faster shooting and extra pierce clears grouped bloons."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda and Tack Shooter.", "Strong", 1050, "Gives lead-popping for Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Ice block loop.", "First", 935, "Tack Sprayer showers the loop with 16 tacks."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Next to Sauda.", "Close", 1060, "Berserker Brew boosts Tack damage and attack speed."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Ice block loop.", "First", 2800, "Overdrive completely locks down the inner circle."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the entrance loop.", "Strong", 2040, "MOAB Mauler breaks the blimp layer immediately. Sauda and Overdrive clean up the ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "park_path": {
        "id": "park_path",
        "name": "Park Path",
        "category": "Beginner",
        "terrain": "Public Park",
        "lanes": "Single path looping around flower beds and a central ornamental pond",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Central water pond allows naval towers with 360-degree coverage",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A pleasant public park featuring winding gravel paths around flower beds and an ornamental pond. The track loops around the pond twice, giving water towers exceptional value.",
                "camo_handling": "Sauda handles Round 24 camo green. Buccaneer upgraded to 0-2-2 Crow's Nest handles all subsequent camos.",
                "lead_handling": "Buccaneer's Hot Shot (0-2-0) pops Lead Bloons on Round 28 with flaming grape volleys.",
                "moab_handling": "Buccaneer upgraded to 3-2-0 Destroyer fires super-fast flaming grape bursts that demolish the Round 40 MOAB.",
                "why_it_works": "The central pond is surrounded on nearly all sides by the track, giving naval towers 100% active firing time.",
                "research_sources": ["Bloons Wiki - Park Path"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the first major loop intersection west of the pond.", "First", 510, "Easily holds early waves with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the center of the ornamental park pond.", "First", 425, "Covers both the entrance and exit park paths."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Park pond.", "First", 210, "Grape Shot adds 4 sharp grapes per shot."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Park pond.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest grants Camo vision."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Park pond.", "First", 2510, "Destroyer attacks at rapid-fire speed, clearing swarms and Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Alchemist", "2-0-0", "On the grass shoreline next to the pond.", "Strong", 1050, "Acidic Mixture Dip buffs the Buccaneer's grape volleys."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Bomb Shooter", "2-0-3", "Along the southern path curve.", "Close", 2150, "Recursive cluster clears any grouped bloons."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Next to Sauda.", "Strong", 1530, "Delivers heavy blimp damage. The 3-2-0 Destroyer and Sauda shred the MOAB and ceramic children.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "lotus_island": {
        "id": "lotus_island",
        "name": "Lotus Island",
        "category": "Beginner",
        "terrain": "Tropical Coral Lagoon",
        "lanes": "Single path weaving through sandy islets and lotus flower pools",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Interactive lotus flowers can be clicked to stun bloons in their vicinity",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A tropical paradise featuring sandy islets surrounded by calm ocean waters and blooming lotus flowers. Abundant water allows full naval setups.",
                "camo_handling": "Sauda spots camo from Round 1. Monkey Sub 2-0-0 provides Advanced Intel camo coverage from water.",
                "lead_handling": "Alchemist 2-0-0 or Buccaneer 0-2-0 pops Leads on Round 28.",
                "moab_handling": "Monkey Buccaneer 3-2-0 Destroyer combined with Monkey Sub 2-0-3 shreds the Round 40 MOAB in the lagoon.",
                "why_it_works": "Naval towers in the center lagoon have clear lines of sight across all the sandy bridges.",
                "research_sources": ["Bloons Wiki - Lotus Island"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the central sandbank where the path loops between two lotus flowers.", "First", 510, "Chops all early bloons as they cross the sand bridge."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the ocean lagoon directly above the central sandbank.", "First", 425, "Fires cannonballs and darts across the island."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Ocean lagoon.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Ocean lagoon.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Ocean lagoon.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the lagoon next to Buccaneer.", "First", 2360, "Triple Guns with Advanced Intel provides constant long-range dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the sandbank within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the lower sandbank.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "candy_falls": {
        "id": "candy_falls",
        "name": "Candy Falls",
        "category": "Beginner",
        "terrain": "Confectionery Candyland",
        "lanes": "Single path winding down chocolate waterfalls and candy bridges",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Chocolate river allows water towers; easter egg sequence unlocks secret pet",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A vibrant candy landscape with winding paths crossing a flowing chocolate river. The bridges and chocolate water offer ideal placement for hybrid land and water defenses.",
                "camo_handling": "Sauda covers early camos. A 3-0-1 Ninja Monkey or 0-2-2 Buccaneer guarantees complete camo control.",
                "lead_handling": "Alchemist 2-0-0 placed next to Sauda melts Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB over the chocolate river.",
                "why_it_works": "The multiple river crossings force bloons past central land spots multiple times.",
                "research_sources": ["Bloons Wiki - Candy Falls"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the first candy cane bridge crossing near the chocolate river.", "First", 510, "Defends all early waves effortlessly."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Next to Sauda on the gingerbread bank.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Gingerbread bank.", "First", 810, "Seeking shurikens follow bloons over the bridges."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Gingerbread bank.", "First", 985, "Double Shot handles dense swarms."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Adjacent to Sauda and Ninja.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Gingerbread bank.", "First", 2340, "Bloonjitsu unleashes 5 shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the lower candy bend.", "Strong", 2040, "MOAB Mauler cracks the MOAB hull. Sauda and Bloonjitsu delete the ceramics.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "winter_park": {
        "id": "winter_park",
        "name": "Winter Park",
        "category": "Beginner",
        "terrain": "Snowy Urban Park",
        "lanes": "Single path splitting around a central fountain and gazebo",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Track splits into two paths around a frozen fountain and reunites at the gazebo",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A snow-covered park where the track splits into two symmetric branches circling around a frozen fountain, then reconverges near a wooden gazebo.",
                "camo_handling": "Sauda placed at the path convergence detects camo from Round 1. Ninja 3-0-1 provides complete camo security.",
                "lead_handling": "Alchemist 2-0-0 placed at the convergence buffs Sauda and Tack to pop Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive at the fountain convergence rips the Round 40 MOAB apart as it passes the gazebo.",
                "why_it_works": "Placing defenses at the convergence point ensures 100% of bloons pass through your killzone regardless of which path they took around the fountain.",
                "research_sources": ["Bloons Wiki - Winter Park"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the path merger point right in front of the park gazebo.", "First", 510, "Covers bloons from both split lanes simultaneously."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the inner curve of the path merger.", "First", 240, "Radial fire strikes bloons from both sides."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Path merger.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda and Tack Shooter.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Path merger.", "First", 935, "Tack Sprayer fires 16 tacks into the converged track."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Next to Sauda.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Path merger.", "First", 2800, "Overdrive completely locks down the merger point."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Along the entrance straightaway before the split.", "Strong", 2040, "MOAB Mauler deals heavy blimp damage. Sauda and Overdrive destroy the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "carved": {
        "id": "carved",
        "name": "Carved",
        "category": "Beginner",
        "terrain": "Giant Halloween Pumpkin",
        "lanes": "Single path weaving through the carved face of a giant pumpkin",
        "water": False,
        "sight_blockers": False,
        "gimmick": "The path weaves in and out of the pumpkin's eyes, nose, and smiling mouth",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A festive Halloween map where the track winds through the carved features of a giant pumpkin. The center nose and mouth loops create exceptional overlap.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 handles all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers inside the pumpkin face to pop Leads on Round 28.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive placed inside the nose cavity destroys the Round 40 MOAB as it loops through the mouth.",
                "why_it_works": "The central nose hollow touches track on three sides, giving radial towers immense efficiency.",
                "research_sources": ["Bloons Wiki - Carved"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Inside the triangular carved nose cavity of the pumpkin.", "First", 510, "Hits bloons passing through both eyes and into the mouth."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Directly adjacent to Sauda inside the nose hollow.", "First", 240, "Covers three separate track segments."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Nose hollow.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Just below the nose inside the pumpkin mouth curve.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Nose hollow.", "First", 935, "Tack Sprayer fires 16 tacks per volley."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Pumpkin mouth.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Nose hollow.", "First", 2800, "Overdrive completely shreds all bloons entering the pumpkin face."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the left eye entrance.", "Strong", 2040, "MOAB Mauler strips the MOAB layer. Sauda and Overdrive obliterate the ceramic children.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "skates": {
        "id": "skates",
        "name": "Skates",
        "category": "Beginner",
        "terrain": "Frozen Ice Rink",
        "lanes": "Single path looping around wooden benches and an open ice rink",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Wide turns and straightaways around ice with a central water pond",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Gwendolin"],
                "starting_cash": 650,
                "overview": "A snowy outdoor ice rink with wooden benches and lamp posts. The track wraps around the perimeter of the rink, creating wide sweeping bends.",
                "camo_handling": "Sauda handles Round 24. Ninja 3-0-1 placed near the center covers all camo bloons.",
                "lead_handling": "Alchemist 2-0-0 buffs Sauda and Ninja to easily pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB on the main ice straightaway.",
                "why_it_works": "The long straightaways allow seeking shurikens and bombs to hit bloons for prolonged periods.",
                "research_sources": ["Bloons Wiki - Skates"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner corner bend where bloons enter the main rink.", "First", 510, "Catches bloons entering the ice rink."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Next to Sauda on the wooden deck.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Wooden deck.", "First", 810, "Seeking shurikens follow bloons across the ice."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Wooden deck.", "First", 985, "Double Shot clears fast pinks and dense waves."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Wooden deck.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the long outer bend of the rink.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "the_cabin": {
        "id": "the_cabin",
        "name": "The Cabin",
        "category": "Beginner",
        "terrain": "Snowy Woodland Cabin",
        "lanes": "Single path winding past a cozy cabin porch and frozen pond",
        "water": True,
        "sight_blockers": True,
        "gimmick": "The cabin building blocks line of sight behind it; frozen pond allows water towers",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A scenic snowy forest cabin with a warm fireplace and a small pond. The track curves sharply around the front porch, making the porch area the primary chokepoint.",
                "camo_handling": "Sauda placed on the porch bend spots camo from Round 1. Ninja 3-0-1 provides complete camo safety.",
                "lead_handling": "Alchemist 2-0-0 buffs porch towers to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 at the porch bend + 0-3-2 Bomb Shooter melts the Round 40 MOAB before it leaves the front yard.",
                "why_it_works": "The front porch bend creates a tight hairpin turn where short-range towers can deliver maximum DPS.",
                "research_sources": ["Bloons Wiki - The Cabin"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Directly in the sharp bend in front of the cabin porch.", "First", 510, "Slices through bloons as they turn the cabin corner."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Inside the sharp porch curve right next to Sauda.", "First", 240, "Fits cleanly inside the hairpin turn."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Porch curve.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "On the grass bank next to the cabin steps.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Porch curve.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Cabin steps.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Porch curve.", "First", 2800, "Overdrive completely locks down the front yard."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the entrance path leading to the cabin.", "Strong", 2040, "MOAB Mauler cracks the MOAB hull. Sauda and Overdrive obliterate the ceramic contents.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "scrapyard": {
        "id": "scrapyard",
        "name": "Scrapyard",
        "category": "Beginner",
        "terrain": "Industrial Junkyard",
        "lanes": "Single path through scrap metal piles with an interactive trash compactor",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Interactive trash compactor crushes bloons on the track when activated",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Striker Jones"],
                "starting_cash": 650,
                "overview": "An industrial junkyard filled with scrap cars and metal girders. Bloons loop past a working scrap crusher that can be activated for burst damage.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 placed near the compactor handles all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers near the compactor to pop Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB before the exit.",
                "why_it_works": "The central track loops provide great synergy between Ninja and Alchemist.",
                "research_sources": ["Bloons Wiki - Scrapyard"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the main loop bend just before the trash compactor.", "First", 510, "Controls the scrap entrance with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda near the scrap pile.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Near scrap pile.", "First", 810, "Seeking shurikens follow bloons through the scrap metal."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Near scrap pile.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Near scrap pile.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the track entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "one_two_tree": {
        "id": "one_two_tree",
        "name": "One Two Tree",
        "category": "Beginner",
        "terrain": "Enchanted Forest Tree",
        "lanes": "Single path winding down terraces of a giant magical tree",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Designated land tiles grant massive category-specific buffs (Primary, Military, Magic, Support)",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A magical giant tree with marked colored tiles that buff specific tower categories (e.g. +range, +pierce, discount). Placing matching tower types on these tiles makes defense extremely powerful.",
                "camo_handling": "Sauda placed on the Primary buff tile spots camo from Round 1. Ninja on the Magic buff tile adds rapid camo destruction.",
                "lead_handling": "Alchemist 2-0-0 on the Magic tile buffs surrounding towers for Round 28 Leads.",
                "moab_handling": "Tack Shooter 2-0-4 Overdrive on the Primary buff tile gains extra range and pierce, eviscerating the Round 40 MOAB.",
                "why_it_works": "Taking advantage of the category buff tiles increases tower attack speed and range by 15-25% for free.",
                "research_sources": ["Bloons Wiki - One Two Tree"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "On the Primary-buffed tile near the center path crossover.", "First", 510, "Gains bonus range and pierce to dominate early rounds."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "On the adjacent Primary tile in the tight bend.", "First", 240, "Gains enhanced pierce from the tile buff."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Primary tile.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Ninja Monkey", "0-0-0", "On the nearby Magic-buffed tile.", "First", 425, "Innate camo detection with magic buffs."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Ninja Monkey", "3-0-1", "Magic tile.", "First", 1370, "Double Shot handles dense swarms."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Alchemist", "2-0-0", "On the Magic tile next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Primary tile.", "First", 2800, "Overdrive with Primary buffs shreds all mid-game bloons."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Upgrade", "Ninja Monkey", "4-0-1", "Magic tile.", "First", 2340, "Bloonjitsu + Overdrive + Sauda annihilates the Round 40 MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "middle_of_the_road": {
        "id": "middle_of_the_road",
        "name": "Middle of the Road",
        "category": "Beginner",
        "terrain": "Suburban Highway",
        "lanes": "Single path curving around a road construction barrier and farm barn",
        "water": False,
        "sight_blockers": False,
        "gimmick": "Wide road layout with multiple crossover views and open building clearings",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A quiet rural road crossing through green fields past a barn. The track curves gently in a wide loop, offering plenty of open space for towers.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 covers all subsequent camo rounds.",
                "lead_handling": "Alchemist 2-0-0 placed next to Sauda melts Leads on Round 28.",
                "moab_handling": "Ninja 4-0-1 Bloonjitsu + 3-2-0 Alchemist + 0-3-2 Bomb Shooter crushes the Round 40 MOAB easily.",
                "why_it_works": "The gentle road curves give seeking shurikens and bombs plenty of room to pop bloons.",
                "research_sources": ["Bloons Wiki - Middle of the Road"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner curve of the main road bend near the barn.", "First", 510, "Secures the road entrance with zero leaks."),
                    create_step(2, "Rounds 1–10: Opening Defense", 7, "Place", "Ninja Monkey", "0-0-0", "Adjacent to Sauda along the roadside.", "First", 425, "Innate camo detection and fast shurikens."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Ninja Monkey", "2-0-1", "Roadside.", "First", 810, "Seeking shurikens follow bloons down the highway."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Upgrade", "Ninja Monkey", "3-0-1", "Roadside.", "First", 985, "Double Shot clears fast pinks and grouped bloons."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 23, "Place", "Alchemist", "2-0-0", "Next to Ninja and Sauda.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 28, "Upgrade", "Alchemist", "3-0-0", "Next to Ninja.", "Close", 1060, "Berserker Brew boosts Ninja shurikens."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Upgrade", "Ninja Monkey", "4-0-1", "Roadside.", "First", 2340, "Bloonjitsu unleashes 5 seeking shurikens per attack."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the road entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Bloonjitsu and Sauda destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "tinkerton": {
        "id": "tinkerton",
        "name": "Tinkerton",
        "category": "Beginner",
        "terrain": "Steampunk Workshop",
        "lanes": "Single path weaving through clockwork gears and copper pipes",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Steampunk machinery and elevated walkways created for hero Rosalia",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Rosalia", "Quincy"],
                "starting_cash": 650,
                "overview": "A clockwork inventor's workshop with copper machinery and elevated platforms. The track loops around central gear assemblies before exiting through brass arches.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 placed near the central gear ensures all camos are eliminated.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the central gear to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 at the gear chokepoint + 0-3-2 Bomb Shooter demolishes the Round 40 MOAB.",
                "why_it_works": "The central gear assembly creates a natural choke point where short-range towers hit bloons repeatedly.",
                "research_sources": ["Bloons Wiki - Tinkerton", "Update 43 Map Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the inner loop around the central clockwork gear.", "First", 510, "Hits bloons looping around the gear mechanism."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Directly adjacent to the central gear teeth.", "First", 240, "Radial fire reaches multiple track segments."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Central gear.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda by the copper pipes.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Central gear.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Copper pipes.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Central gear.", "First", 2800, "Overdrive completely controls the workshop floor."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Near the copper pipe entrance.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "spa_pits": {
        "id": "spa_pits",
        "name": "Spa Pits",
        "category": "Beginner",
        "terrain": "Geothermal Hot Springs",
        "lanes": "Single path winding through steaming geothermal mineral baths",
        "water": True,
        "sight_blockers": False,
        "gimmick": "Steaming mineral pools accommodate water towers; relaxing bath ambiance",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Admiral Brickell"],
                "starting_cash": 650,
                "overview": "A geothermal bath resort with steaming mineral pools. The path curves between the hot spring pools, allowing strong synergy between land and water monkeys.",
                "camo_handling": "Sauda spots camo from Round 1. Monkey Sub 2-0-0 in the central hot spring provides map-wide camo detection.",
                "lead_handling": "Alchemist 2-0-0 or Bomb 0-3-0 handles Lead Bloons on Round 28.",
                "moab_handling": "Monkey Buccaneer 3-2-0 Destroyer in the mineral pool + 0-3-2 Bomb shreds the Round 40 MOAB.",
                "why_it_works": "The steaming pools give water towers full vision across the surrounding walkways.",
                "research_sources": ["Bloons Wiki - Spa Pits", "Update 48 Patch Notes"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the stone walkway bend between the two main hot spring pools.", "First", 510, "Controls the walkway with dual-lane reach."),
                    create_step(2, "Rounds 1–10: Opening Defense", 5, "Place", "Monkey Buccaneer", "0-0-0", "In the central mineral bath pool.", "First", 425, "Fires cannonballs and darts across the walkways."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Buccaneer", "0-1-0", "Mineral bath pool.", "First", 210, "Grape Shot fires 4 grapes."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 15, "Upgrade", "Monkey Buccaneer", "0-2-2", "Mineral bath pool.", "First", 680, "Hot Shot grants Lead-popping; Crow's Nest provides full Camo detection."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Mineral bath pool.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 26, "Place", "Monkey Sub", "2-0-3", "In the adjacent pool.", "First", 2360, "Triple Guns with Advanced Intel provides constant dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the stone bank within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "On the walkway.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "three_mines_round": {
        "id": "three_mines_round",
        "name": "Three Mines 'Round",
        "category": "Beginner",
        "terrain": "Mining Quarry",
        "lanes": "Single path with three concentric circular minecart loops",
        "water": True,
        "sight_blockers": True,
        "gimmick": "Three concentric circular loops where bloons traverse inward toward a mine shaft",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A gold and coal quarry featuring three concentric circular track loops. Towers placed between the loops hit bloons on up to three separate passes.",
                "camo_handling": "Sauda handles Round 24 camo green. Ninja 3-0-1 placed between the rings covers all subsequent camos.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the central track switch to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 inside the first minecart loop + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "Towers placed between the concentric circles get three distinct opportunities to damage every bloon.",
                "research_sources": ["Bloons Wiki - Three Mines 'Round"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "At the junction where track loop 1 meets track loop 2.", "First", 510, "Hits bloons crossing between the first two mine loops."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "Inside the first circular mine loop.", "First", 240, "Covers the entire inner circle of track 1."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Loop 1.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda at the mine junction.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Loop 1.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Mine junction.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Loop 1.", "First", 2800, "Overdrive completely locks down the quarry track."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the entrance minecart track.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    },

    "skull_tweak": {
        "id": "skull_tweak",
        "name": "Skull Tweak",
        "category": "Beginner",
        "terrain": "Desert Canyon",
        "lanes": "Single path curving around a skull-shaped rock formation",
        "water": False,
        "sight_blockers": True,
        "gimmick": "Skull rock formation creates a natural choke point and sight line restriction",
        "difficulties": {
            "Easy": {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "hero_alternatives": ["Quincy", "Obyn Greenfoot"],
                "starting_cash": 650,
                "overview": "A desert canyon featuring a giant carved stone skull. Bloons travel along the canyon floor and loop directly through the mouth of the skull.",
                "camo_handling": "Sauda placed at the skull entrance spots camo from Round 1. Ninja 3-0-1 provides complete camo security.",
                "lead_handling": "Alchemist 2-0-0 buffs towers at the skull entrance to pop Leads on Round 28.",
                "moab_handling": "Overdrive Tack 2-0-4 inside the skull cavity + 0-3-2 Bomb Shooter easily destroys the Round 40 MOAB.",
                "why_it_works": "The skull's jaw forms a narrow canyon pass where all bloons are concentrated.",
                "research_sources": ["Bloons Wiki - Skull Tweak"],
                "steps": [
                    create_step(1, "Rounds 1–10: Opening Defense", 1, "Place", "Sauda", "0-0-0", "Right inside the mouth of the stone skull formation.", "First", 510, "Catches all bloons entering the skull canyon."),
                    create_step(2, "Rounds 1–10: Opening Defense", 6, "Place", "Tack Shooter", "0-0-0", "In the tight curve directly below Sauda in the skull jaw.", "First", 240, "Covers the entire inner bend of the canyon."),
                    create_step(3, "Rounds 11–20: Expanding Defense", 12, "Upgrade", "Tack Shooter", "2-0-2", "Skull jaw.", "First", 620, "Faster shooting and extra pierce."),
                    create_step(4, "Rounds 11–20: Expanding Defense", 17, "Place", "Alchemist", "2-0-0", "Next to Sauda by the skull rock.", "Strong", 1050, "Acidic Mixture Dip handles Round 28 Leads."),
                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Tack Shooter", "2-0-3", "Skull jaw.", "First", 935, "Tack Sprayer fires 16 tacks continuously."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Alchemist", "3-0-0", "Skull rock.", "Close", 1060, "Berserker Brew boosts Tack damage and fire rate."),
                    create_step(7, "Rounds 31–39: Final Preparation", 32, "Upgrade", "Tack Shooter", "2-0-4", "Skull jaw.", "First", 2800, "Overdrive completely locks down the canyon choke."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "At the canyon entrance before the skull.", "Strong", 2040, "MOAB Mauler delivers heavy blimp damage. Sauda and Overdrive destroy the MOAB.")
                ]
            },
            "Medium": None, "Hard": None, "Impoppable": None, "CHIMPS": None
        }
    }
}
