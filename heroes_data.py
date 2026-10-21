"""
heroes_data.py
Comprehensive database and tactical intelligence for all 16 official Bloons TD 6 Heroes.
Provides detailed hero stats, placement types, abilities, best map affinities, and synergy ratings.
"""

HEROES_DATABASE = {
    "Sauda": {
        "name": "Sauda",
        "title": "The Swordmaster",
        "icon": "⚔️",
        "color": "#f38ba8",
        "category": "Hero",
        "cost_easy": 510,
        "cost_medium": 600,
        "cost_hard": 650,
        "placement_type": "Land",
        "innate_camo": True,
        "innate_lead": False,
        "lead_level": 7,
        "level_milestones": {
            "Lv1": "Dual swords attack close targets at blinding speed. Detects Camo bloons naturally.",
            "Lv3": "Leaping Sword ability: Jumps into the air and crashes down on the strongest bloon, dealing heavy damage and popping Leads.",
            "Lv7": "Swords gain Lead popping power permanently.",
            "Lv10": "Sword Charge ability: Dashes across the entire track from end to start, obliterating all bloons in her path."
        },
        "best_map_types": "Single-lane tracks, sharp curves, intersections, central loops, and chokepoints.",
        "synergies": ["Alchemist (Acidic Mixture Dip / Berserker Brew)", "Glue Gunner (extra damage against slowed targets)", "Ice Monkey"],
        "weakness": "Extremely short attack range; struggles on split multi-lane tracks with no central intersection.",
        "summary": "The premier early-game hero. Low starting cost allows purchasing on Round 1 in Easy/Medium, effortlessly soloing early rounds while providing innate Camo detection."
    },
    "Quincy": {
        "name": "Quincy",
        "title": "Son of Quincy",
        "icon": "🏹",
        "color": "#89b4fa",
        "category": "Hero",
        "cost_easy": 455,
        "cost_medium": 540,
        "cost_hard": 585,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 5,
        "innate_lead": False,
        "lead_level": 7,
        "level_milestones": {
            "Lv1": "Rapid bow shots with arrow bounces.",
            "Lv3": "Rapid Shot: Triples attack speed for a short duration.",
            "Lv5": "Gains permanent Camo detection.",
            "Lv7": "Exploding Arrows: Arrows explode on contact, popping Lead bloons.",
            "Lv10": "Storm of Arrows: Rains down hundreds of arrows across the entire screen, wiping dense ceramic and rainbow waves."
        },
        "best_map_types": "Straight paths, long lanes, maps with distant dual lanes, and open terrain.",
        "synergies": ["Alchemist (Berserker Brew)", "Monkey Village (Jungle Drums)", "Sniper Monkey"],
        "weakness": "Moderate pierce against hyper-dense clusters without abilities.",
        "summary": "The reliable all-rounder. Affordable starting price, early Camo (Lv5) and Lead (Lv7) answers, and a screen-clearing ability on Round 10 for emergency ceramic rushes."
    },
    "Gwendolin": {
        "name": "Gwendolin",
        "title": "The Pyromaniac",
        "icon": "🔥",
        "color": "#fab387",
        "category": "Hero",
        "cost_easy": 615,
        "cost_medium": 725,
        "cost_hard": 780,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Flamethrower attacks with high pierce. Melts Lead bloons from Round 1.",
            "Lv3": "Cocktail of Fire: Hurls a flaming flask that leaves a burning pool on the track, melting clustered rushes.",
            "Lv4": "Heat It Up: Generates periodic fire rings that grant +1 pierce and fire damage to all nearby monkeys.",
            "Lv10": "Firestorm: Ignites all bloons on the entire screen and buffs all monkeys on screen with Heat It Up."
        },
        "best_map_types": "Chokepoints, clustered tracks, lead-heavy rounds, and Primary tower clusters.",
        "synergies": ["Tack Shooter (Tack Zone / Ring of Fire)", "Ninja Monkey", "Dart Monkey"],
        "weakness": "Cannot pop Purple bloons without assistance; lacks innate Camo detection.",
        "summary": "Area-of-effect specialist that pops Leads naturally from Level 1 and grants team-wide pierce/damage buffs to surrounding monkeys."
    },
    "Striker Jones": {
        "name": "Striker Jones",
        "title": "The Artillery Commander",
        "icon": "💣",
        "color": "#a6e3a1",
        "category": "Hero",
        "cost_easy": 640,
        "cost_medium": 750,
        "cost_hard": 810,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Fires explosive bazooka shells that pop Lead bloons.",
            "Lv3": "Concussive Shell: Targets the strongest bloon on screen, dealing heavy damage and stunning it.",
            "Lv5": "Grants +10% attack speed and +1 pierce to all Bomb Shooters and Mortar Monkeys.",
            "Lv6": "Black Bloon Immunity: Allows all nearby explosive towers to pop Black and Zebra bloons.",
            "Lv10": "Artillery Command: Instantly resets all Bomb and Mortar active abilities and doubles their attack speed."
        },
        "best_map_types": "Maps with high obstacle count (pairs with Mortars) and maps with concentrated loop chokepoints (pairs with Bomb Shooters).",
        "synergies": ["Bomb Shooter (MOAB Mauler / Recursive Cluster)", "Mortar Monkey", "Monkey Village"],
        "weakness": "Slow early attack rate; completely dependent on explosive synergy for maximum value.",
        "summary": "The premier explosive strategist. Removes the Black bloon vulnerability from all bombs and mortars, doubling their firepower and resetting abilities."
    },
    "Obyn Greenfoot": {
        "name": "Obyn Greenfoot",
        "title": "Guardian of the Forest",
        "icon": "🌿",
        "color": "#a6e3a1",
        "category": "Hero",
        "cost_easy": 550,
        "cost_medium": 650,
        "cost_hard": 700,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Fires seeking spirit wolf energy bolts that pop Lead bloons and seek targets behind walls.",
            "Lv2": "Nature's Ward: Plants a totem that slows all nearby bloons by 30-40%.",
            "Lv3": "Brambles: Spawns sharp thorny brambles on the track that pop up to 500 bloons, including Camo and Lead.",
            "Lv10": "Wall of Trees: Summons a massive hollow tree trunk that swallows up to 2,000 bloons/ceramics/blimps and bursts into cash when full."
        },
        "best_map_types": "Complex maps with line-of-sight blockers, Magic monkey clusters, and tight curves.",
        "synergies": ["Druid (Druid of Wrath / Poplust / Avatar of Wrath)", "Ninja Monkey", "Wizard Monkey"],
        "weakness": "Totem and Bramble placements have randomized track placement elements.",
        "summary": "Master of nature and the ultimate buffer for Magic Monkeys. Wall of Trees completely devours Round 63 and Round 76 ceramic rushes while generating bonus cash."
    },
    "Captain Churchill": {
        "name": "Captain Churchill",
        "title": "The Armored Tank",
        "icon": "🛡️",
        "color": "#f9e2af",
        "category": "Hero",
        "cost_easy": 1700,
        "cost_medium": 2000,
        "cost_hard": 2160,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 6,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Fires heavy cannon shells (Lead popping) and rapid machine-gun bullets simultaneously.",
            "Lv3": "Armor Piercing Shells: Cannon shells deal massive extra damage to Ceramic and MOAB-class bloons.",
            "Lv6": "Gains innate Camo detection for both cannon and machine gun.",
            "Lv10": "MOAB Barrage: Fires a barrage of 16 guided missiles at up to 16 blimps simultaneously on screen."
        },
        "best_map_types": "Long straightaways, high-density tracks, and late-game rounds (Hard / Impoppable).",
        "synergies": ["Monkey Village (Primary Mentoring / Camo)", "Alchemist (Stronger Stimulant)", "Glue Storm"],
        "weakness": "High purchase cost ($2,000) prevents early placement; levels up slower than other heroes.",
        "summary": "A rolling fortress of immense pure damage. When placed pointing down a long straight lane, Churchill shreds through Ceramic clusters and ZOMGs with zero team assistance."
    },
    "Benjamin": {
        "name": "Benjamin",
        "title": "The Code Hacker",
        "icon": "💻",
        "color": "#94e2d5",
        "category": "Hero",
        "cost_easy": 1020,
        "cost_medium": 1200,
        "cost_hard": 1295,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": False,
        "lead_level": 0,
        "level_milestones": {
            "Lv1": "Generates $100 bonus cash at the end of every round.",
            "Lv3": "Biohack: Increases attack damage of 4 nearby monkeys by +1 for 9 seconds.",
            "Lv4": "Skims: Steals cash from newly spawned bloons, boosting round income significantly.",
            "Lv7": "Bloon Trojan: Sends a virus to a bloon or blimp, completely preventing it from spawning children upon destruction!",
            "Lv10": "Syphon Funding: Downgrades newly spawned bloon waves by 1 tier and doubles cash earned."
        },
        "best_map_types": "Standard Easy/Medium/Hard maps, Boss events, Half Cash, and Deflation.",
        "synergies": ["Banana Farm (Banks)", "Spike Factory", "Global Range Snipers"],
        "weakness": "Zero direct attack; ineffective on CHIMPS mode where income is disabled.",
        "summary": "The ultimate economic snowball hero. Generates thousands in passive income, while Bloon Trojan deletes MOAB and BFB ceramics before they can even spawn."
    },
    "Ezili": {
        "name": "Ezili",
        "title": "The Voodoo Mystic",
        "icon": "🔮",
        "color": "#cba6f7",
        "category": "Hero",
        "cost_easy": 510,
        "cost_medium": 600,
        "cost_hard": 650,
        "placement_type": "Land",
        "innate_camo": True,
        "innate_lead": False,
        "lead_level": 4,
        "level_milestones": {
            "Lv1": "Voodoo staff fires curse orbs that strip Regrow from bloons and pop Camo from Lv1.",
            "Lv3": "Heartstopper: Prevents any bloon on the screen from regrowing for 6 seconds.",
            "Lv7": "Sacrificial Totem: Drains 10 lives to give all monkeys +1 pierce, +range, +attack speed, and Camo detection.",
            "Lv10": "MOAB Hex: Places a lethal decaying curse on the strongest blimp (including BADs). When it pops, it leaves ZERO child bloons and jumps to the next blimp!"
        },
        "best_map_types": "Alternate Bloons Rounds (ABR), late-game Round 80-100 blimp battles, and Camo-heavy tracks.",
        "synergies": ["Prince of Darkness", "Elite Defender", "Sub Commander"],
        "weakness": "Very low early-game attack speed and single-target pierce.",
        "summary": "Voodoo specialist designed to dismantle late-game blimps. MOAB Hex completely deletes the ZOMG and BAD hulls without letting ceramic children leak."
    },
    "Pat Fusty": {
        "name": "Pat Fusty",
        "title": "The Giant Monkey",
        "icon": "🦍",
        "color": "#fab387",
        "category": "Hero",
        "cost_easy": 680,
        "cost_medium": 800,
        "cost_hard": 865,
        "placement_type": "Land or Water",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": False,
        "lead_level": 2,
        "level_milestones": {
            "Lv1": "Heavy ground slam that knocks bloons backward. Can be placed on water or land.",
            "Lv2": "Slams gain Lead popping power and stun bloons.",
            "Lv3": "Rallying Roar: Gives +1 damage to all monkeys within his roar radius.",
            "Lv10": "Big Squeeze: Grabs a MOAB or BFB in his giant hands and crushes it to pieces over a few seconds."
        },
        "best_map_types": "Tight chokepoints, aquatic channels, bridges, and short loop maps.",
        "synergies": ["Tack Zone (2-0-5 Tack)", "Sun Avatar (3-0-2 Super)", "Grandmaster Ninja"],
        "weakness": "Very short melee attack range; requires careful placement right on the track curve.",
        "summary": "Amphibious giant capable of standing on water or land. His Rallying Roar (+1 damage) turns multi-projectile towers like Tack Zone and Sun Avatar into monstrous boss-shredders."
    },
    "Admiral Brickell": {
        "name": "Admiral Brickell",
        "title": "The Naval Commander",
        "icon": "⚓",
        "color": "#89b4fa",
        "category": "Hero",
        "cost_easy": 640,
        "cost_medium": 750,
        "cost_hard": 810,
        "placement_type": "Water",
        "innate_camo": True,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Fires revolver shots and drops sea mines that linger in the water until bloons arrive. Detects Camo and pops Leads via mines.",
            "Lv3": "Naval Tactics: Gives all water towers (Subs, Buccaneers, and water-placed monkeys) double attack speed and Lead/Camo popping.",
            "Lv7": "Sea mines gain increased blast radius and stun MOAB-class bloons.",
            "Lv10": "Mega Mine: Deploys a gigantic devastating naval mine that tracks toward the largest blimp on screen, dealing massive explosive damage."
        },
        "best_map_types": "Water-dominant maps (Flooded Valley, Peninsula, Spillway, Off the Coast, Spice Islands, Sunken Columns).",
        "synergies": ["Monkey Sub (Sub Commander 2-0-5 / Pre-Emptive 2-5-0)", "Monkey Buccaneer (Carrier Flagship / Pirate Lord)"],
        "weakness": "Must be placed in water; completely unusable on land-only maps.",
        "summary": "The supreme water commander. Her Naval Tactics ability turns standard Sub and Buccaneer fleets into unstoppable blimp-annihilators."
    },
    "Etienne": {
        "name": "Etienne",
        "title": "The Drone Operator",
        "icon": "🛸",
        "color": "#94e2d5",
        "category": "Hero",
        "cost_easy": 720,
        "cost_medium": 850,
        "cost_hard": 920,
        "placement_type": "Land",
        "innate_camo": True,
        "innate_lead": False,
        "lead_level": 0,
        "level_milestones": {
            "Lv1": "Pilots remote drones that fly along the track to attack bloons.",
            "Lv3": "Drone Swarm: Deploys additional combat drones for high burst damage.",
            "Lv8": "UAV GLOBAL CAMO: Permanently grants Camo detection to EVERY SINGLE MONKEY on the entire map!",
            "Lv10": "UCAV: Summons a high-tech combat aircraft that circles the map, carpet-bombing bloons with missiles."
        },
        "best_map_types": "Multi-lane tracks, separated tracks, obstacle-heavy maps, and any map with difficult camo positioning.",
        "synergies": ["Any high-damage tower lacking camo (Tack Zone, Bomb Shooters, Berserker Alchemists)", "Perma-Spike"],
        "weakness": "Low early single-target damage until Level 10 UCAV is unlocked.",
        "summary": "The king of utility. Level 8 grants map-wide permanent Camo detection to all monkeys, saving thousands of dollars otherwise spent on Camo Villages or crosspaths."
    },
    "Psi": {
        "name": "Psi",
        "title": "The Psionic Prodigy",
        "icon": "🧠",
        "color": "#cba6f7",
        "category": "Hero",
        "cost_easy": 680,
        "cost_medium": 800,
        "cost_hard": 865,
        "placement_type": "Land",
        "innate_camo": True,
        "innate_lead": True,
        "lead_level": 6,
        "level_milestones": {
            "Lv1": "Infinite range psionic vibrations that ignore line of sight, walls, and obstacles completely.",
            "Lv3": "Psychic Blast: Emits a shockwave that stuns all bloons in a wide radius.",
            "Lv6": "Psionic strike can target and destroy Lead bloons.",
            "Lv10": "Psionic Scream: Screams with psionic energy, blowing away and disintegrating large portions of bloons and Ceramics on screen.",
            "Lv14": "Can target and destroy MOAB and BFB blimps directly with psionic destruction."
        },
        "best_map_types": "Expert maps, multi-lane tracks with walls, separated lanes (Sanctuary, Geared, Muddy Puddles, Ravine, Quad, Workshop).",
        "synergies": ["Sniper Monkey", "Spike Factory", "Global Range towers"],
        "weakness": "Destruction takes time to channel; bloons can leak if targeted too late along the exit.",
        "summary": "Infinite range psionic master. Ignores 100% of walls and sight blockers, striking bloons anywhere on the map with zero distance drop-off."
    },
    "Geraldo": {
        "name": "Geraldo",
        "title": "The Mystic Shopkeeper",
        "icon": "🎒",
        "color": "#f9e2af",
        "category": "Hero",
        "cost_easy": 595,
        "cost_medium": 700,
        "cost_hard": 755,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": False,
        "lead_level": 0,
        "level_milestones": {
            "Lv1": "Carries a portable magic shop. Stocks Shooty Turrets, Nails, Stack of Camo Potion, and Sharpening Stone.",
            "Lv4": "Shop stocks Pickles (+1 damage) and Rare Quincy Action Figure (investment item).",
            "Lv8": "Shop stocks Gerry's Fire (grants a fiery pepper attack to any tower) and Fertilizer.",
            "Lv10": "Shop stocks Rejuvenation Potion (restores abilities and lives) and Paragon Power Totem."
        },
        "best_map_types": "High-difficulty maps, CHIMPS, Expert challenges, and Boss events.",
        "synergies": ["Sharpening Stone + high projectile pierce towers (Tack, Ninja, Sub)", "Gerry's Fire"],
        "weakness": "Requires active shop management and purchasing items; high micromanagement.",
        "summary": "The Swiss army knife hero. His shop provides exact tactical tools for every threat: Camo potions, Lead-popping fire, sharp turrets, and Paragon power totems."
    },
    "Corvus": {
        "name": "Corvus",
        "title": "The Spirit Mage",
        "icon": "👻",
        "color": "#b4befe",
        "category": "Hero",
        "cost_easy": 615,
        "cost_medium": 725,
        "cost_hard": 780,
        "placement_type": "Land",
        "innate_camo": True,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Commands a Spirit that attacks bloons within range. Harvests mana from popped bloons to cast spells.",
            "Lv3": "Nourish ability: Sacrifices mana to rapidly level up Corvus.",
            "Lv5": "Spells: Trample (crushes dense clusters), Spear (pierces straight lines), Ancestral Might (turns spirit into a titan).",
            "Lv10": "Dark Ritual: Channels soul power to instantly refill mana and unleash apocalyptic ghost strikes."
        },
        "best_map_types": "Expert maps, 1-tower or low-cost CHIMPS runs, and complex micro strategies.",
        "synergies": ["Spike Factory", "Alchemist", "Village"],
        "weakness": "Highest micromanagement demand in the game; requires continuous spellbook navigation.",
        "summary": "The highest skill ceiling hero. When played with proper spell management, Corvus can solo the vast majority of rounds in the game with minimal tower support."
    },
    "Rosalia": {
        "name": "Rosalia",
        "title": "The Jetpack Tinkerer",
        "icon": "🚀",
        "color": "#f38ba8",
        "category": "Hero",
        "cost_easy": 680,
        "cost_medium": 800,
        "cost_hard": 865,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": True,
        "lead_level": 1,
        "level_milestones": {
            "Lv1": "Fires lasers and grenades from dual weapons while hovering on her jetpack. Can fly to any open position on the map.",
            "Lv3": "Scatter Grenade: Launches a cluster of high-explosive pellets that decimate grouped bloons.",
            "Lv5": "Grants 5-10% discount on all Monkey Ace and Heli Pilot purchases and upgrades.",
            "Lv10": "Anti-Bloon Missile: Fires a guided tracking mega-missile that seeks and explodes the strongest blimp on screen."
        },
        "best_map_types": "Maps with changing tracks, multi-stage lanes, and aerial Military tower strategies.",
        "synergies": ["Monkey Ace (Spectre / Sky Shredder)", "Heli Pilot (Apache Prime)", "Alchemist"],
        "weakness": "Requires active repositioning to maintain optimal angle on shifting tracks.",
        "summary": "Mobile aerial firepower. Her jetpack allows instant repositioning across the battlefield, while her discounts accelerate mid-game Ace and Heli power spikes."
    },
    "Adora": {
        "name": "Adora",
        "title": "The High Priestess of the Sun",
        "icon": "☀️",
        "color": "#f9e2af",
        "category": "Hero",
        "cost_easy": 850,
        "cost_medium": 1000,
        "cost_hard": 1080,
        "placement_type": "Land",
        "innate_camo": False,
        "camo_level": 0,
        "innate_lead": False,
        "lead_level": 0,
        "level_milestones": {
            "Lv1": "Fires seeking divine bolts of radiant sunlight.",
            "Lv3": "Long Arm of Light: Tremendously increases attack range and damage, allowing bolts to pierce Lead bloons.",
            "Lv7": "Blood Sacrifice: Sacrifices a selected friendly tower to instantly gain massive XP and buff her attack speed.",
            "Lv10": "Ball of Light: Conjures an orb of blazing solar energy that shreds all nearby bloons and blimps.",
            "Lv20": "Sun Temple Transformation: Buffs True Sun God and Sun Temples with double attack speed."
        },
        "best_map_types": "Late-game freeplay runs, single-lane tracks with high temple synergy, and Magic monkey setups.",
        "synergies": ["Super Monkey (Sun Avatar / Sun Temple / True Sun God)", "Alchemist", "Monkey Village"],
        "weakness": "High base cost, slow natural leveling unless utilizing Blood Sacrifice, lacks early Lead/Camo.",
        "summary": "The goddess of endgame DPS. Her Blood Sacrifice bypasses normal XP leveling, and at Level 20 she massively enhances all Sun Temples on the screen."
    }
}

MAP_HERO_INTELLIGENCE = {
    # Beginner Maps (24)
    "monkey_meadow": {
        "best_hero": "Sauda",
        "reason": "Classic single-loop layout where placing Sauda inside the upper bend gives dual-lane coverage, shredding early rounds with zero leaks.",
        "alternatives": ["Quincy", "Gwendolin", "Obyn Greenfoot"],
        "synergies": "Alchemist (3-2-0 Berserker Brew) + Ninja Monkey (4-0-1 Bloonjitsu)"
    },
    "tree_stump": {
        "best_hero": "Captain Churchill",
        "reason": "Mounting Churchill atop the high central tree stump provides 360-degree elevated vision and continuous armor-piercing artillery along the spiraling path.",
        "alternatives": ["Sauda", "Gwendolin", "Obyn Greenfoot"],
        "synergies": "Monkey Village (2-2-0 Primary Mentoring) + Alchemist (4-2-0 Stronger Stimulant)"
    },
    "town_center": {
        "best_hero": "Sauda",
        "reason": "The central crossroads intersection near the pond gives Sauda multiple sweeps on every bloon as it enters and leaves the center square.",
        "alternatives": ["Quincy", "Etienne", "Benjamin"],
        "synergies": "Tack Shooter (2-0-4 Overdrive) + Alchemist (3-2-0)"
    },
    "middle_of_the_road": {
        "best_hero": "Sauda",
        "reason": "Central roundabout layout ensures bloons pass Sauda's swords twice, allowing her high pierce and abilities to dismantle dense waves.",
        "alternatives": ["Quincy", "Gwendolin", "Adora"],
        "synergies": "Boomerang Monkey (4-0-2 MOAB Press) + Ice Monkey (0-2-4)"
    },
    "one_two_tree": {
        "best_hero": "Geraldo",
        "reason": "Map buff tiles amplify Geraldo's Shootey Turrets, Sharpening Stone, and Fertilizer, creating immense value across all categories.",
        "alternatives": ["Sauda", "Benjamin", "Etienne"],
        "synergies": "Dart Monkey (Apex Plasma Master build) + Ninja Monkey on magic tiles"
    },
    "scrapyard": {
        "best_hero": "Geraldo",
        "reason": "The interactive junk compactor combines with Geraldo's shop utilities (Nails, Turrets, Gerry's Fire) to solve tricky rounds cheaply.",
        "alternatives": ["Sauda", "Quincy", "Pat Fusty"],
        "synergies": "Tack Shooter (0-4-2 Maelstrom) + Bomb Shooter (2-0-4)"
    },
    "the_cabin": {
        "best_hero": "Gwendolin",
        "reason": "The narrow snowy straightaway in front of the cabin concentrates bloons directly into Gwen's Cocktail of Fire and Heat It Up aura.",
        "alternatives": ["Sauda", "Obyn Greenfoot", "Quincy"],
        "synergies": "Ring of Fire (4-0-2 Tack) + Monkey Sub (2-0-4 in pond)"
    },
    "resort": {
        "best_hero": "Sauda",
        "reason": "The famous quadruple-pass loop allows Sauda placed in the center loop to slice bloons four separate times per lap with extreme efficiency.",
        "alternatives": ["Geraldo", "Benjamin", "Captain Churchill"],
        "synergies": "Tack Zone (2-0-5) + Super Brittle (5-2-0 Ice) + Alchemist"
    },
    "skates": {
        "best_hero": "Sauda",
        "reason": "Tight ice rink bends give Sauda continuous contact, while her Leaping Sword easily handles clustered mid-game Leads and Ceramics.",
        "alternatives": ["Quincy", "Etienne", "Gwendolin"],
        "synergies": "Ice Monkey (2-0-4 Cryo Cannon) + Wizard Monkey (0-2-4)"
    },
    "lotus_island": {
        "best_hero": "Sauda",
        "reason": "The central track loops around the island perimeter, giving Sauda continuous contact while interactive lotus flowers stun escaping bloons.",
        "alternatives": ["Admiral Brickell", "Pat Fusty", "Quincy"],
        "synergies": "Buccaneer (0-3-2 Cannon Ship) + Alchemist (3-2-0)"
    },
    "candy_falls": {
        "best_hero": "Sauda",
        "reason": "Gentle winding curves with a single stone bridge crossing allow Sauda to solo the opening 20+ rounds with virtually zero support.",
        "alternatives": ["Quincy", "Pat Fusty", "Etienne"],
        "synergies": "Ninja Monkey (4-0-1 Bloonjitsu) + Alchemist (4-2-0)"
    },
    "winter_park": {
        "best_hero": "Sauda",
        "reason": "Twin fountain loops force bloons to circle around Sauda multiple times, maximizing her high melee DPS and Sword Charge coverage.",
        "alternatives": ["Quincy", "Captain Churchill", "Benjamin"],
        "synergies": "Tack Shooter (2-0-4 Overdrive) + Village (2-2-0)"
    },
    "carved": {
        "best_hero": "Sauda",
        "reason": "Placing Sauda inside the carved pumpkin mouth grants coverage over both incoming and looped paths simultaneously.",
        "alternatives": ["Obyn Greenfoot", "Gwendolin", "Ezili"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Tack Zone (2-0-5)"
    },
    "park_path": {
        "best_hero": "Sauda",
        "reason": "The central figure-eight intersection allows Sauda to attack bloons on both loops while keeping abilities ready for MOABs.",
        "alternatives": ["Quincy", "Obyn Greenfoot", "Gwendolin"],
        "synergies": "Bomb Shooter (2-0-4 Recursive Cluster) + Primary Training (3-2-0 Village)"
    },
    "hedge": {
        "best_hero": "Obyn Greenfoot",
        "reason": "Dense hedge walls block line-of-sight for straight-line towers. Obyn's seeking spirit wolves bypass hedges, and Wall of Trees catches sudden leaks.",
        "alternatives": ["Sauda", "Etienne", "Quincy"],
        "synergies": "Druid of the Forest (0-4-0) + Poplust (0-1-4 Druids) + Alchemist"
    },
    "end_of_the_road": {
        "best_hero": "Gwendolin",
        "reason": "A long, single dead-end road approach gives Gwendolin's Cocktail of Fire and Firestorm full lane coverage to burn Leads and Ceramic rushes.",
        "alternatives": ["Sauda", "Quincy", "Captain Churchill"],
        "synergies": "Boomerang Monkey (4-0-2 Glaive Ricochet) + Bomb Shooter (2-0-4)"
    },
    "logs": {
        "best_hero": "Captain Churchill",
        "reason": "The longest track in Bloons history provides endless straightaways where Churchill's high-velocity armor-piercing shells pierce hundreds of bloons.",
        "alternatives": ["Sauda", "Gwendolin", "Benjamin"],
        "synergies": "Village (2-3-0 MIB) + Alchemist (4-2-0) + Super Monkey (3-0-2)"
    },
    "cubism": {
        "best_hero": "Etienne",
        "reason": "The multi-faceted winding layout requires wide coverage; Etienne's Level 8 global Camo saves immense cash, and UCAV wipes dense mid-game waves.",
        "alternatives": ["Sauda", "Admiral Brickell", "Quincy"],
        "synergies": "Tack Zone (2-0-5) in the square loop + Buccaneer (0-4-2 in water)"
    },
    "four_circles": {
        "best_hero": "Etienne",
        "reason": "Four isolated circular paths divide tower coverage; Etienne's aerial drones and global UAV cover every circle without needing repositioning.",
        "alternatives": ["Sauda", "Psi", "Quincy"],
        "synergies": "Monkey Sub (2-0-4) in center pond + Sniper Monkey (0-2-4)"
    },
    "alpine_run": {
        "best_hero": "Geraldo",
        "reason": "Winding downhill mountain track where Geraldo's Shootey Turrets, Gerry's Fire, and Creepy Idol provide cheap and versatile crowd control.",
        "alternatives": ["Sauda", "Quincy", "Obyn Greenfoot"],
        "synergies": "Dart Monkey (Apex Plasma Master) + Spike Factory (0-2-5 at exit)"
    },
    "frozen_over": {
        "best_hero": "Sauda",
        "reason": "The spiral track wrapping around the frozen caveman provides dense curve contact where Sauda easily wipes early waves.",
        "alternatives": ["Quincy", "Gwendolin", "Pat Fusty"],
        "synergies": "Tack Shooter (2-0-4 Overdrive) + Ice Monkey (2-0-4)"
    },
    "in_the_loop": {
        "best_hero": "Captain Churchill",
        "reason": "Concentric loops and intersecting straightaways allow Churchill's explosive tank shells to bounce and pierce through multiple track passes.",
        "alternatives": ["Sauda", "Etienne", "Gwendolin"],
        "synergies": "Primary Mentoring (4-2-0 Village) + Ring of Fire (4-0-2 Tack)"
    },
    "spa_pits": {
        "best_hero": "Geraldo",
        "reason": "Bubbling volcanic springs with tight curves allow Geraldo's shop utilities (Shooty Turrets, Nails, Fire Sauce) to dominate key turns.",
        "alternatives": ["Sauda", "Gwendolin", "Admiral Brickell"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Tack Zone (2-0-5)"
    },
    "tinkerton": {
        "best_hero": "Rosalia",
        "reason": "Rosalia's signature inventor workshop; her jetpack flight easily hops between the upper and lower conveyor tracks while her grenades pop Leads.",
        "alternatives": ["Sauda", "Etienne", "Benjamin"],
        "synergies": "Heli Pilot (3-0-2) + Monkey Ace (2-0-4 Spectre) + Engineer (4-2-0)"
    },

    # Intermediate Maps (24)
    "bloonarius_prime": {
        "best_hero": "Etienne",
        "reason": "Bloon paths switch between prime and non-prime rounds; Etienne's global UAV and flying drones provide seamless coverage across shifting paths.",
        "alternatives": ["Sauda", "Quincy", "Psi"],
        "synergies": "Sniper Monkey (0-2-4) + Heli Pilot (4-0-2 Apache)"
    },
    "balance": {
        "best_hero": "Sauda",
        "reason": "The center circular dais is the premier Sauda spot in the game: 100% of all bloons pass directly under her dual blades on every lap.",
        "alternatives": ["Adora", "Gwendolin", "Pat Fusty"],
        "synergies": "Tack Zone (2-0-5) + Ring of Fire (4-0-2) + Berserker Brew (3-2-0)"
    },
    "bazaar": {
        "best_hero": "Psi",
        "reason": "Three separated marketplace lanes with obstacle awnings block conventional towers; Psi attacks bloons over all canopies with infinite range.",
        "alternatives": ["Etienne", "Quincy", "Geraldo"],
        "synergies": "Sniper Monkey (0-2-5 Elite Defender) + Wizard (0-2-4)"
    },
    "cracked": {
        "best_hero": "Sauda",
        "reason": "Intersecting dry riverbed crossings allow Sauda to lock down early bloons while water sections allow cheap Sub backup.",
        "alternatives": ["Quincy", "Admiral Brickell", "Obyn Greenfoot"],
        "synergies": "Monkey Sub (2-0-4 Sub Commander) + Buccaneer (0-3-2)"
    },
    "streambed": {
        "best_hero": "Sauda",
        "reason": "Tight corners along the winding riverbank give Sauda maximum contact time and easy early-game solo capability.",
        "alternatives": ["Admiral Brickell", "Quincy", "Gwendolin"],
        "synergies": "Buccaneer (0-5-2 Pirate Lord) + Tack Shooter (2-0-4)"
    },
    "chutes": {
        "best_hero": "Quincy",
        "reason": "Fast dual sand chutes require affordable opening defense; Quincy's bouncing arrows and Storm of Arrows cover both chutes reliably.",
        "alternatives": ["Sauda", "Etienne", "Gwendolin"],
        "synergies": "Sub Monkey (2-0-3) in water pool + Ninja (4-0-1 Bloonjitsu)"
    },
    "rake": {
        "best_hero": "Etienne",
        "reason": "Diverging paths across the garden intersect only at the exit; Etienne's Level 8 global Camo and UCAV provide full dual-lane control.",
        "alternatives": ["Sauda", "Quincy", "Psi"],
        "synergies": "Ninja Monkey (4-0-2) + Alchemist (4-2-0) at central intersection"
    },
    "spice_islands": {
        "best_hero": "Admiral Brickell",
        "reason": "Vast ocean archipelago allows building a colossal Sub and Buccaneer fleet; Brickell's Naval Tactics doubles all naval attack speed.",
        "alternatives": ["Sauda", "Pat Fusty", "Etienne"],
        "synergies": "Sub Commander (2-0-5) + Buccaneer (0-5-2 Pirate Lord)"
    },
    "moon_landing": {
        "best_hero": "Striker Jones",
        "reason": "Crater trenches completely block normal vision. Striker Jones boosts Mortar Monkeys with faster firing and massive artillery stuns into craters.",
        "alternatives": ["Psi", "Etienne", "Quincy"],
        "synergies": "Mortar Monkey (2-4-0 Artillery Battery) + Bomb Shooter (2-0-4 Recursive)"
    },
    "haunted": {
        "best_hero": "Etienne",
        "reason": "Two parallel lanes split the track; Etienne's global Camo eliminates the need for expensive split Villages on both sides.",
        "alternatives": ["Sauda", "Quincy", "Obyn Greenfoot"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Tack Zone (2-0-5)"
    },
    "downstream": {
        "best_hero": "Etienne",
        "reason": "Multi-branch river tracks split bloons across islands; Etienne's drones freely fly between diverging streams without pathing restrictions.",
        "alternatives": ["Admiral Brickell", "Sauda", "Quincy"],
        "synergies": "Monkey Sub (2-0-4) + Alchemist (4-2-0) + Ninja (4-0-1)"
    },
    "firing_range": {
        "best_hero": "Quincy",
        "reason": "Elevated central bench overlooking the firing range gives Quincy full range coverage over both crossing lanes.",
        "alternatives": ["Captain Churchill", "Sauda", "Etienne"],
        "synergies": "Sniper Monkey (0-2-4) on towers + Crossbow Master (0-2-5)"
    },
    "karts_n_darts": {
        "best_hero": "Rosalia",
        "reason": "Multiple race tracks with rapid kart bloons require Rosalia's flight repositioning and anti-lead grenades to cover the winding circuit.",
        "alternatives": ["Sauda", "Etienne", "Quincy"],
        "synergies": "Tack Zone (2-0-5) in pit lane + Boomerang (0-2-4 MOAB Press)"
    },
    "spring_spring": {
        "best_hero": "Etienne",
        "reason": "Split paths around twin ponds split bloons; Etienne's aerial drones seamlessly support both tracks while ponds allow Sub support.",
        "alternatives": ["Admiral Brickell", "Sauda", "Quincy"],
        "synergies": "Sub Monkey (2-0-4 Armor Piercing Darts) + Buccaneer (3-2-0)"
    },
    "encrypted": {
        "best_hero": "Striker Jones",
        "reason": "Graveyard tombs with line-of-sight walls make Mortars and Bomb Shooters the strongest defense, massively buffed by Striker Jones.",
        "alternatives": ["Psi", "Sauda", "Etienne"],
        "synergies": "Mortar Monkey (0-2-4 Shattering Shells) + Bomb Shooter (2-0-4)"
    },
    "covered_garden": {
        "best_hero": "Geraldo",
        "reason": "The 4 glass greenhouse quadrants rotate every round, covering towers. Geraldo's pre-placed turrets, nails, and totems remain active under glass.",
        "alternatives": ["Etienne", "Psi", "Corvus"],
        "synergies": "Sniper Monkey (0-2-4) in center open plot + Dart Monkey turrets"
    },
    "polyphemus": {
        "best_hero": "Admiral Brickell",
        "reason": "The central cyclops eye provides water access that periodically floods and drains; Brickell deploys deadly mega mines that hit both paths.",
        "alternatives": ["Pat Fusty", "Psi", "Sauda"],
        "synergies": "Buccaneer (0-4-2 Pirate) in the eye + Spike Factory at exit"
    },
    "water_park": {
        "best_hero": "Pat Fusty",
        "reason": "Placed directly in the central splash pool, Pat Fusty's amphibious fists slam and knock back bloons exiting the water slides while his Roar buffs towers.",
        "alternatives": ["Admiral Brickell", "Sauda", "Etienne"],
        "synergies": "Tack Zone (2-0-5) + Buccaneer (0-3-2) in water pool"
    },
    "sulfur_springs": {
        "best_hero": "Gwendolin",
        "reason": "Geothermal vents and tight straightaways concentrate bloons into Gwendolin's Heat It Up aura and fire traps for rapid lead and ceramic burning.",
        "alternatives": ["Sauda", "Geraldo", "Quincy"],
        "synergies": "Ring of Fire (4-0-2 Tack) + Alchemist (3-2-0 Berserker)"
    },
    "lost_crevasse": {
        "best_hero": "Obyn Greenfoot",
        "reason": "Narrow icy crevasse choke concentrates all bloons; Obyn's Brambles and Wall of Trees trap every single wave with 100% efficiency.",
        "alternatives": ["Psi", "Sauda", "Corvus"],
        "synergies": "Druid of the Forest (0-4-0) + Poplust (0-1-4 Druids)"
    },
    "ancient_portal": {
        "best_hero": "Pat Fusty",
        "reason": "Bloons teleworking through portal gates emerge clumped together, making Pat's Big Squeeze and Roar devastating for area-of-effect destruction.",
        "alternatives": ["Sauda", "Psi", "Geraldo"],
        "synergies": "Recursive Cluster (2-0-4 Bomb) + Tack Zone (2-0-5)"
    },
    "quarry": {
        "best_hero": "Psi",
        "reason": "Stepped quarry stone walls block projectile line of sight. Psi's psionic attacks ignore quarry depth and target bloons across all levels.",
        "alternatives": ["Etienne", "Geraldo", "Quincy"],
        "synergies": "Sniper Monkey (0-2-4) on elevated ramparts + Spike Factory"
    },
    "quiet_street": {
        "best_hero": "Psi",
        "reason": "Urban townhouses block horizontal sightlines. Psi attacks through structures with zero hindrance, targeting both streets simultaneously.",
        "alternatives": ["Etienne", "Sauda", "Quincy"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Tack Shooter"
    },
    "luminous_cove": {
        "best_hero": "Adora",
        "reason": "Glowing subterranean cove where Adora's radiant homing bolts illuminate and bend around the cavern walls to shred bloon packs.",
        "alternatives": ["Sauda", "Admiral Brickell", "Psi"],
        "synergies": "Sun Avatar (3-0-2 Super) + Alchemist (4-2-0) + Buccaneer"
    },

    # Advanced Maps (24)
    "another_brick": {
        "best_hero": "Captain Churchill",
        "reason": "The long straight road behind the brick wall allows Churchill's armor-piercing shells to pierce dozens of bloons per shot without obstruction.",
        "alternatives": ["Sauda", "Etienne", "Psi"],
        "synergies": "Primary Mentoring (4-2-0 Village) + Recursive Cluster (2-0-4)"
    },
    "off_the_coast": {
        "best_hero": "Admiral Brickell",
        "reason": "Wide open ocean allows deploying a massive naval armada; Brickell's Naval Tactics doubles the attack speed of Sub Commander and Pirate Lord.",
        "alternatives": ["Sauda", "Etienne", "Quincy"],
        "synergies": "Sub Commander (2-0-5) + Buccaneer (0-5-2 Pirate Lord)"
    },
    "cornfield": {
        "best_hero": "Adora",
        "reason": "Dense corn stalks block line-of-sight. Adora's elevated divine bolts seek and bend over the stalks without spending thousands clearing corn.",
        "alternatives": ["Psi", "Etienne", "Sauda"],
        "synergies": "Ultra-Juggernaut (5-2-0 Dart) + Super Monkey (3-0-2 Sun Avatar)"
    },
    "underground": {
        "best_hero": "Ezili",
        "reason": "Dual intersecting underground pipes create tight straightaways where Ezili's curse and Heartstopper neutralize regrows and blimps.",
        "alternatives": ["Psi", "Quincy", "Etienne"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Spike Factory (0-2-5)"
    },
    "pat_s_pond": {
        "best_hero": "Pat Fusty",
        "reason": "Pat's namesake home; placed in the central pond, his huge slaps stun and push back both paths while roaring to buff naval subs and land towers.",
        "alternatives": ["Admiral Brickell", "Etienne", "Psi"],
        "synergies": "Monkey Sub (2-0-4 Armor Piercing Darts) + Tack Zone (2-0-5)"
    },
    "peninsula": {
        "best_hero": "Admiral Brickell",
        "reason": "The elevated rock peninsula is surrounded by deep ocean; Brickell commands a lethal fleet of subs and buccaneers with sea mines.",
        "alternatives": ["Sauda", "Etienne", "Quincy"],
        "synergies": "Sub Commander (2-0-5) + Carrier Flagship (5-2-0 Buccaneer)"
    },
    "high_finance": {
        "best_hero": "Benjamin",
        "reason": "Expensive plot construction costs make Benjamin's bank interest and cash skimming essential for early economic expansion.",
        "alternatives": ["Psi", "Geraldo", "Etienne"],
        "synergies": "Monkey Bank (2-3-0) + Sun Avatar (3-0-2 on central skyscraper)"
    },
    "spillway": {
        "best_hero": "Admiral Brickell",
        "reason": "The central drain barrel is the only placement spot that reaches all incoming bloon pipes; Brickell fits inside and drops mega mines that destroy all 5 paths.",
        "alternatives": ["Pat Fusty", "Psi", "Striker Jones"],
        "synergies": "Mortar Monkey (2-4-0) + Ring of Fire around perimeter"
    },
    "cargo": {
        "best_hero": "Benjamin",
        "reason": "Harbor layout with a separate MOAB exit benefits immensely from Benjamin's Bloon Trojan, which prevents MOABs from releasing ceramic children.",
        "alternatives": ["Psi", "Etienne", "Sauda"],
        "synergies": "Buccaneer (0-5-2 Pirate Lord) in dock + Sniper Monkey (0-2-4)"
    },
    "geared": {
        "best_hero": "Psi",
        "reason": "The central rotating gear moves towers away from the bloon track each round; Psi attacks bloons anywhere with infinite range, completely immune to rotation.",
        "alternatives": ["Geraldo", "Sniper Monkey / Etienne", "Quincy"],
        "synergies": "Sniper Monkey (0-2-5 Elite Defender) + Heli Pilot (4-0-2 Apache)"
    },
    "sunken_columns": {
        "best_hero": "Admiral Brickell",
        "reason": "Submerged trenches provide prime water placement for ballistics and mega mines, dominating the converging bloon paths.",
        "alternatives": ["Psi", "Sauda", "Etienne"],
        "synergies": "Sub Commander (2-0-5) + Buccaneer (0-4-2 Cannon Ship)"
    },
    "x_factor": {
        "best_hero": "Psi",
        "reason": "Diagonal criss-crossing tracks with blind spots make targeting difficult; Psi's infinite range covers the entire crossroad with zero blind angles.",
        "alternatives": ["Etienne", "Quincy", "Geraldo"],
        "synergies": "Sniper Monkey (0-2-4) + Wizard (0-2-4 Prince of Darkness)"
    },
    "mesa": {
        "best_hero": "Quincy",
        "reason": "Two desert tracks separated by a stone canyon; Quincy's low starting cost and long bouncing arrows cover both canyon paths easily.",
        "alternatives": ["Psi", "Etienne", "Sauda"],
        "synergies": "Sniper Monkey (0-2-5 Elite Defender) + Alchemist (4-2-0)"
    },
    "erosion": {
        "best_hero": "Corvus",
        "reason": "Collapsing ice floes shift the board throughout the game; Corvus's Soul Harvest sustains devastating spells and spirit micro from any position.",
        "alternatives": ["Psi", "Admiral Brickell", "Sauda"],
        "synergies": "Buccaneer (0-4-2 Pirate Lord) + Ice Monkey (0-2-4 Cryo Cannon)"
    },
    "midnight_mansion": {
        "best_hero": "Ezili",
        "reason": "Haunted mansion corridors block line-of-sight for normal monkeys; Ezili curses bloons through solid walls and her MOAB Hex vaporizes BFBs.",
        "alternatives": ["Psi", "Geraldo", "Sauda"],
        "synergies": "Wizard Monkey (0-2-4 Prince of Darkness) + Tack Zone in foyer"
    },
    "dark_path": {
        "best_hero": "Obyn Greenfoot",
        "reason": "Dark cavern track where Obyn buffs magic monkeys and Druid clusters, while placing Wall of Trees at the cavern exit to swallow rushes.",
        "alternatives": ["Psi", "Sauda", "Corvus"],
        "synergies": "Druid of the Forest (0-4-0) + Poplust (0-1-4) + Alchemist"
    },
    "enchanted_glade": {
        "best_hero": "Corvus",
        "reason": "Mystic forest where Soul Harvest fuels board-wide hexes and spirit strikes to obliterate multi-lane bloon waves.",
        "alternatives": ["Psi", "Obyn Greenfoot", "Geraldo"],
        "synergies": "Wizard Monkey (0-2-4) + Ninja Monkey (4-0-2) + Alchemist"
    },
    "castle_revenge": {
        "best_hero": "Gwendolin",
        "reason": "Siege ramparts give Gwendolin's fire blasts coverage over both castle gates, while Heat It Up grants Lead-popping to all rampart monkeys.",
        "alternatives": ["Sauda", "Striker Jones", "Etienne"],
        "synergies": "Ring of Fire (4-0-2 Tack) + Bomb Shooter (2-0-4 Recursive Cluster)"
    },
    "party_parade": {
        "best_hero": "Geraldo",
        "reason": "Carnival turns where Geraldo's nail traps, Gerry's fire, and bunny swarm control crowded parade lanes with high efficiency.",
        "alternatives": ["Psi", "Sauda", "Etienne"],
        "synergies": "Tack Zone (2-0-5) + Boomerang (0-2-4 MOAB Press)"
    },
    "last_resort": {
        "best_hero": "Adora",
        "reason": "Pyramid-style oasis layout where Adora's divine homing bolts bend around the palms to strike approaching bloons at extreme range.",
        "alternatives": ["Sauda", "Benjamin", "Quincy"],
        "synergies": "Sun Temple (4-0-2 Super) + Alchemist (4-2-0 Stronger Stimulant)"
    },
    "ascent": {
        "best_hero": "Psi",
        "reason": "Ascent features multiple separated elevation tiers and sight obstacles; Psi targets bloons across all tiers simultaneously with infinite range.",
        "alternatives": ["Etienne", "Quincy", "Geraldo"],
        "synergies": "Sniper Monkey (0-2-4) + Wizard Monkey (0-2-4 Prince of Darkness)"
    },
    "sunset_gulch": {
        "best_hero": "Psi",
        "reason": "Deep canyon gorge with cliff sight blockers; Psi targets bloons across the canyon depths effortlessly without line-of-sight penalties.",
        "alternatives": ["Etienne", "Quincy", "Geraldo"],
        "synergies": "Sniper Monkey (0-2-5 Elite Defender) + Spike Factory at exit"
    },
    "protect_the_yacht": {
        "best_hero": "Admiral Brickell",
        "reason": "Naval channel track where Brickell's fleet defends the central yacht with devastating mega mines and doubled attack speed.",
        "alternatives": ["Pat Fusty", "Etienne", "Sauda"],
        "synergies": "Sub Commander (2-0-5) + Buccaneer (0-5-2 Pirate Lord)"
    },
    "three_mines_round": {
        "best_hero": "Striker Jones",
        "reason": "Circular mine tracks where clustered Bomb Shooters and Mortars under Striker decimate tight groups and stun incoming blimps.",
        "alternatives": ["Psi", "Sauda", "Etienne"],
        "synergies": "Bomb Shooter (2-0-4 Recursive) + Mortar (2-4-0 Artillery Battery)"
    },

    # Expert Maps (15)
    "sanctuary": {
        "best_hero": "Psi",
        "reason": "Moving elevation tiles displace ground towers; Psi attacks bloons anywhere regardless of moving platforms with infinite range.",
        "alternatives": ["Geraldo", "Quincy", "Etienne"],
        "synergies": "Sniper Monkey (0-2-5 Elite Defender) + Spike Factory at exit"
    },
    "ravine": {
        "best_hero": "Psi",
        "reason": "Narrow mountain chasm with extreme sight blockers; Psi's mind blast penetrates all rock faces to destroy bloons on both sides.",
        "alternatives": ["Corvus", "Geraldo", "Rosalia"],
        "synergies": "Sniper Monkey (0-2-4) + Dart Monkey (0-2-5 Crossbow Master)"
    },
    "flooded_valley": {
        "best_hero": "Admiral Brickell",
        "reason": "Almost entirely submerged in water; Brickell placed at the floodgate provides unmatched mine placement and doubles attack speed for naval subs and boats.",
        "alternatives": ["Etienne", "Psi", "Pat Fusty"],
        "synergies": "Monkey Sub (Sub Commander 2-0-5) + Buccaneer (Pirate Lord 0-5-2)"
    },
    "infernal": {
        "best_hero": "Quincy",
        "reason": "Tiny isolated rock islands in lava have strict placement space. Quincy fits on the early lower rock and uses bouncing arrows to cover both lanes.",
        "alternatives": ["Psi", "Etienne", "Geraldo"],
        "synergies": "Sniper Monkey (0-2-4) + Boomerang Monkey on upper rocks"
    },
    "bloody_puddles": {
        "best_hero": "Quincy",
        "reason": "Ultra-spread parallel tracks make single defenders ineffective; Quincy's cheap cost ($540) and bouncing arrows are vital for early survival.",
        "alternatives": ["Geraldo", "Psi", "Corvus"],
        "synergies": "Sub 2-0-0 Advanced Intel + Dart Monkeys on muddy banks"
    },
    "muddy_puddles": {
        "best_hero": "Quincy",
        "reason": "Multiple parallel muddy streams require cheap early coverage; Quincy's bouncing arrows and rapid shot handle early alternating tracks.",
        "alternatives": ["Geraldo", "Psi", "Sauda"],
        "synergies": "Sub 2-0-3 Triple Guns + Dart Monkey (0-2-3)"
    },
    "ouch": {
        "best_hero": "Psi",
        "reason": "#Ouch has four disconnected quadrant tracks and heavy water/sight obstacles; Psi targets bloons across all lanes simultaneously with infinite range.",
        "alternatives": ["Geraldo", "Admiral Brickell", "Quincy"],
        "synergies": "Ninja Monkey (4-0-1) + Alchemist (4-2-0) in center cross"
    },
    "quad": {
        "best_hero": "Psi",
        "reason": "Four separate tracks coming from all four directions with zero central overlap; Psi hits bloons on all four paths without repositioning.",
        "alternatives": ["Geraldo", "Etienne", "Quincy"],
        "synergies": "Sniper Monkey (0-2-5) + Spike Factory at bottom exits"
    },
    "dark_castle": {
        "best_hero": "Sauda",
        "reason": "All four bloon tracks converge directly onto a single wooden drawbridge. Sauda placed at the drawbridge entrance strikes 100% of bloons from all lanes.",
        "alternatives": ["Quincy", "Obyn Greenfoot", "Psi"],
        "synergies": "Sub (2-0-4) in moat + Alchemist (4-2-0) on castle wall"
    },
    "workshop": {
        "best_hero": "Benjamin",
        "reason": "Short conveyor track with expensive track extensions where Benjamin's Bloon Trojan neutralizes MOAB ceramic children and funds extensions.",
        "alternatives": ["Geraldo", "Psi", "Sauda"],
        "synergies": "Spike Factory (0-2-5 Perma-Spike) + Village (2-3-0 MIB)"
    },
    "blons": {
        "best_hero": "Sauda",
        "reason": "Extremely short straight corner track; Sauda's instant melee burst damage and cheap cost are mandatory for stopping instant leaks.",
        "alternatives": ["Quincy", "Tack Shooter", "Psi"],
        "synergies": "Tack Zone (2-0-5) + Ice Monkey (2-0-4) + Alchemist"
    },
    "dark_dungeons": {
        "best_hero": "Corvus",
        "reason": "Deep underground dungeon traps; Corvus's Spirit micro clears bloons in narrow corridors while soul harvest fuels devastating board-wide spells.",
        "alternatives": ["Psi", "Geraldo", "Quincy"],
        "synergies": "Spike Factory at dungeon exits + Sniper Monkey (0-2-4)"
    },
    "glacial_trail": {
        "best_hero": "Corvus",
        "reason": "Map freezing mechanics periodically freeze ordinary monkeys; Corvus's Spirit and spells operate immune to frost, maintaining 100% uptime.",
        "alternatives": ["Psi", "Sauda", "Geraldo"],
        "synergies": "Ice Monkey (0-2-4) + Wizard (0-2-4) + Alchemist"
    },
    "adoras_temple": {
        "best_hero": "Adora",
        "reason": "Adora's canonical sacred home; her Blood Sacrifice instantly levels her up and massively enhances all Sun Temples on the pyramid.",
        "alternatives": ["Sauda", "Psi", "Quincy"],
        "synergies": "Sun Temple (4-0-2 Super Monkey) + Alchemist (4-2-0)"
    },
    "skull_tweak": {
        "best_hero": "Ezili",
        "reason": "Tight skull canyon where Ezili's necrotic hexes destroy incoming blimps and Heartstopper prevents regrow bloon explosions.",
        "alternatives": ["Sauda", "Psi", "Geraldo"],
        "synergies": "Bomb Shooter (2-0-4) + Wizard Monkey (0-2-4)"
    }
}

def get_best_hero_for_map(map_id, map_data):
    """
    Evaluates map characteristics and returns the optimal #1 hero, detailed tactical justification,
    alternative heroes, and synergy notes. Prioritizes the curated 87-map database, falling back to
    heuristic evaluation if an unknown map is passed.
    """
    if map_id in MAP_HERO_INTELLIGENCE:
        return dict(MAP_HERO_INTELLIGENCE[map_id])

    # Fallback heuristic evaluation for custom or unknown maps
    category = map_data.get("category", "Beginner")
    lanes = map_data.get("lanes", "Single").lower()
    has_water = map_data.get("water", False)
    sight_blocked = map_data.get("sight_blockers", False)
    m_name = map_data.get("name", map_id)

    if ("multi" in lanes or "separated" in lanes or "two" in lanes or "three" in lanes or "four" in lanes):
        if sight_blocked or category == "Expert":
            return {
                "best_hero": "Psi",
                "reason": f"{m_name} has multiple separated paths and sight obstacles. Psi targets bloons across all lanes simultaneously, ignoring every obstacle with infinite psionic range.",
                "alternatives": ["Etienne", "Quincy", "Geraldo"],
                "synergies": "Sniper Monkey (0-2-4) + Wizard Monkey (0-2-4 Prince of Darkness)"
            }
        else:
            return {
                "best_hero": "Etienne",
                "reason": f"With multiple active bloon lanes on {m_name}, Etienne's Level 8 global Camo detection covers every monkey across all paths without needing expensive Camo Villages.",
                "alternatives": ["Sauda", "Quincy", "Obyn Greenfoot"],
                "synergies": "Tack Zone (2-0-5) + Recursive Cluster (2-0-4 Bomb)"
            }

    if has_water and ("peninsula" in m_name.lower() or "off the coast" in m_name.lower() or "spice islands" in m_name.lower() or "sunken" in m_name.lower()):
        return {
            "best_hero": "Admiral Brickell",
            "reason": f"Extensive water layout on {m_name} allows building a premier Sub and Buccaneer fleet. Brickell's Naval Tactics doubles their attack speed and grants Lead/Camo popping to all naval towers.",
            "alternatives": ["Sauda", "Etienne", "Quincy"],
            "synergies": "Sub Commander (2-0-5) + Buccaneer (Pirate Lord 0-5-2)"
        }

    return {
        "best_hero": "Sauda",
        "reason": f"{m_name} features tight curves or lane intersections where short-range melee towers excel. Sauda costs only $510, soloes early rounds, has innate Camo, and crushes early Lead/MOABs with abilities.",
        "alternatives": ["Quincy", "Gwendolin", "Obyn Greenfoot"],
        "synergies": "Alchemist (3-2-0 Berserker Brew) + Ninja Monkey (4-0-1 Bloonjitsu)"
    }


def get_strategy_hero_intel(hero_name, map_id, map_data, difficulty="Easy"):
    """
    Returns tactical intelligence (reason, alternatives, synergies)
    tailored specifically to the given hero on the specified map and difficulty.
    Ensures tactical reasons and synergies align directly with the strategy's build.
    """
    map_hero_intel = get_best_hero_for_map(map_id, map_data)
    m_name = map_data.get("name", map_id)

    # If the strategy hero matches the map's signature hero, use the curated intelligence
    if hero_name and hero_name == map_hero_intel.get("best_hero"):
        return {
            "hero": hero_name,
            "reason": map_hero_intel.get("reason", ""),
            "alternatives": map_hero_intel.get("alternatives", []),
            "synergies": map_hero_intel.get("synergies", "")
        }

    h_data = HEROES_DATABASE.get(hero_name, {})
    cost_key = f"cost_{difficulty.lower()}" if difficulty else "cost_easy"
    cost_val = h_data.get(cost_key, h_data.get("cost_easy", 510))

    # Map-specific tailored reasons for strategy heroes
    if hero_name == "Sauda":
        if map_id == "cargo":
            reason = (
                f"Sauda's affordable starting cost (${cost_val} on {difficulty}) allows placing her immediately on Round 1 "
                f"at the road intersection to solo land waves with innate Camo detection, letting defenses invest into "
                f"naval and explosive towers to intercept the separate MOAB canal."
            )
            synergies = "Monkey Buccaneer (3-2-0 Destroyer) + Alchemist (3-2-0 Berserker Brew) + Bomb Shooter (0-3-2)"
            alternatives = ["Quincy", "Admiral Brickell"]
        elif map_id == "the_cabin":
            reason = (
                f"Sauda placed on the sharp front porch hairpin curve slices bloons with maximum contact time and provides "
                f"innate Camo detection from Round 1, effortlessly protecting the cabin entrance."
            )
            synergies = "Tack Shooter (2-0-4 Overdrive) + Alchemist (3-2-0) + Bomb Shooter (0-3-2)"
            alternatives = ["Quincy", "Gwendolin", "Obyn Greenfoot"]
        elif map_id == "tree_stump":
            reason = (
                f"Sauda locks down the spiraling stump base with high melee pierce and innate Camo, allowing easy saving "
                f"for heavy mid-game artillery and primary tower upgrades."
            )
            synergies = "Monkey Village (2-2-0) + Tack Shooter (2-0-4) + Alchemist (3-2-0)"
            alternatives = ["Captain Churchill", "Quincy", "Gwendolin"]
        elif map_id == "peninsula":
            reason = (
                f"Sauda locks down the tight land choke at the base of the mountain, handling early rounds and early camos "
                f"while naval Subs and Buccaneers dominate the surrounding ocean."
            )
            synergies = "Monkey Sub (2-0-4 AP Darts) + Buccaneer (3-2-0 Destroyer) + Alchemist"
            alternatives = ["Admiral Brickell", "Quincy"]
        elif map_id == "workshop":
            reason = (
                f"Sauda's compact footprint fits cleanly at the track junction ahead of the conveyor track, securing early rounds "
                f"with dual-blade slashing while saving funds for track mechanisms and mid-game defense."
            )
            synergies = "Spike Factory (0-2-4) + Alchemist (3-2-0) + Boomerang Monkey"
            alternatives = ["Benjamin", "Quincy", "Geraldo"]
        elif map_id == "one_two_tree":
            reason = (
                f"Sauda placed on the central intersection covers multiple converging tracks, dealing high melee damage "
                f"while magic and military towers take advantage of specialized buff tiles."
            )
            synergies = "Ninja Monkey (4-0-1 Bloonjitsu) + Alchemist (3-2-0 Berserker Brew)"
            alternatives = ["Geraldo", "Quincy", "Etienne"]
        elif map_id == "scrapyard":
            reason = (
                f"Sauda controls the junkyard hairpin turn near the trash compactor, slicing through dense early clusters "
                f"and handling Camo bloons without early support."
            )
            synergies = "Tack Shooter (2-0-4 Overdrive) + Bomb Shooter (2-0-4 Recursive Cluster)"
            alternatives = ["Geraldo", "Quincy", "Pat Fusty"]
        elif map_id == "off_the_coast":
            reason = (
                f"Sauda defends the shore chokepoint against early bloons, providing innate Camo popping and early stability "
                f"so naval investments can scale in open water."
            )
            synergies = "Monkey Buccaneer (3-2-0 Destroyer) + Monkey Sub (2-0-3 Triple Guns)"
            alternatives = ["Admiral Brickell", "Quincy"]
        elif map_id == "haunted":
            reason = (
                f"Sauda placed at the lane intersection provides dual-track melee coverage, securing early rounds with "
                f"innate Camo detection while defenses build for mid-game blimps."
            )
            synergies = "Ninja Monkey (4-0-1 Bloonjitsu) + Alchemist (3-2-0 Berserker Brew)"
            alternatives = ["Etienne", "Quincy"]
        elif map_id == "midnight_mansion":
            reason = (
                f"Sauda fits cleanly in the interior mansion chokepoints, maximizing close-range blade damage while "
                f"bypassing tight line-of-sight constraints."
            )
            synergies = "Tack Shooter (2-0-4 Overdrive) + Alchemist (3-2-0 Berserker Brew)"
            alternatives = ["Ezili", "Quincy"]
        elif map_id == "tinkerton":
            reason = (
                f"Sauda's fast melee attack locks down conveyor track intersections, effortlessly popping early waves "
                f"and camos while saving for heavy mechanical defense."
            )
            synergies = "Tack Shooter (2-0-4 Overdrive) + Village (2-2-0) + Alchemist"
            alternatives = ["Rosalia", "Quincy"]
        else:
            reason = (
                f"Sauda's affordable starting cost (${cost_val} on {difficulty}) allows immediate placement on Round 1 "
                f"at key curves on {m_name}, soloing early rounds with innate Camo detection and high pierce abilities."
            )
            synergies = "Alchemist (3-2-0 Berserker Brew) + Tack Shooter (2-0-4 Overdrive) / Ninja Monkey (4-0-1 Bloonjitsu)"
            alternatives = [map_hero_intel.get("best_hero", "Quincy"), "Quincy", "Gwendolin"]
    elif hero_name == "Quincy":
        if map_id == "high_finance":
            reason = (
                f"Quincy's low starting cost (${cost_val} on {difficulty}) and long bouncing arrow range cover multiple separated "
                f"city building lanes without paying expensive early plot construction fees."
            )
            synergies = "Sniper Monkey (0-2-4) + Dart Monkey + Monkey Village (2-2-0)"
            alternatives = ["Benjamin", "Psi", "Etienne"]
        elif map_id == "geared":
            reason = (
                f"Quincy's affordable cost (${cost_val} on {difficulty}) and long range bouncing arrows provide reliable early coverage "
                f"while saving cash for long-range Snipers and Heli Pilots immune to gear rotation."
            )
            synergies = "Sniper Monkey (0-2-4) + Heli Pilot (3-0-2) + Alchemist"
            alternatives = ["Psi", "Geraldo", "Etienne"]
        elif map_id == "x_factor":
            reason = (
                f"Quincy's bouncing arrows and Storm of Arrows cover the separated diagonal tracks cleanly through the early game, "
                f"detecting Camo at Lv5 and popping Leads at Lv7."
            )
            synergies = "Sniper Monkey (0-2-4) + Wizard (0-2-4 Prince of Darkness)"
            alternatives = ["Psi", "Etienne", "Geraldo"]
        elif map_id == "moon_landing":
            reason = (
                f"Quincy provides cheap, reliable starting defense over crater walls, saving funds for Mortar and Tack towers "
                f"that bypass sight obstruction."
            )
            synergies = "Mortar Monkey (2-4-0) + Tack Shooter (2-0-4 Overdrive)"
            alternatives = ["Striker Jones", "Psi", "Etienne"]
        elif map_id == "quad":
            reason = (
                f"Quincy's affordable starting cost and long bouncing range allow early defense across four distant lanes, "
                f"giving time to establish multi-target coverage."
            )
            synergies = "Sniper Monkey (0-2-4) + Monkey Sub (2-0-3 Triple Guns)"
            alternatives = ["Psi", "Etienne"]
        elif map_id == "ravine":
            reason = (
                f"Quincy's high-speed arrows provide critical early defense along the narrow canyon path before difficult "
                f"multi-lane waves emerge."
            )
            synergies = "Sniper Monkey (0-2-4) + Alchemist (3-2-0)"
            alternatives = ["Psi", "Etienne"]
        elif map_id == "sanctuary":
            reason = (
                f"Quincy's low starting cost helps navigate moving sanctuary platforms, covering shifting lanes with bouncing arrows."
            )
            synergies = "Sniper Monkey (0-2-4) + Heli Pilot (3-0-2)"
            alternatives = ["Psi", "Etienne"]
        elif map_id == "bazaar":
            reason = (
                f"Quincy's long range covers multiple separated bazaar lanes, handling early camos and ceramic rushes with Storm of Arrows."
            )
            synergies = "Sniper Monkey (0-2-4) + Wizard (0-2-4 Prince of Darkness)"
            alternatives = ["Psi", "Etienne", "Geraldo"]
        elif map_id == "ouch":
            reason = (
                f"Quincy's cheap cost (${cost_val} on {difficulty}) allows an immediate foothold on #Ouch, providing vital early pierce "
                f"across the center intersection."
            )
            synergies = "Ninja Monkey (4-0-1) + Monkey Sub (2-0-3) + Alchemist"
            alternatives = ["Psi", "Geraldo"]
        else:
            reason = (
                f"Quincy's low starting cost (${cost_val} on {difficulty}) and long bouncing arrow range provide dependable multi-lane "
                f"coverage across {m_name}, handling early Camo (Lv5) and Lead (Lv7) with zero leaks."
            )
            synergies = "Alchemist (Berserker Brew) + Monkey Village (Jungle Drums) + Sniper Monkey (0-2-4)"
            alternatives = [map_hero_intel.get("best_hero", "Sauda"), "Sauda", "Etienne"]
    elif hero_name == "Admiral Brickell":
        reason = (
            f"Extensive water layout on {m_name} maximizes Brickell's Naval Tactics, doubling attack speed and granting "
            f"Lead/Camo popping to surrounding water towers."
        )
        synergies = "Monkey Buccaneer (3-2-0 Destroyer) + Monkey Sub (2-0-4 Armor Piercing Darts)"
        alternatives = ["Sauda", "Quincy", "Pat Fusty"]
    elif hero_name == "Adora":
        reason = (
            f"Adora provides high-damage seeking magic bolts with unobstructed elevation across {m_name}, scaling into "
            f"a powerful late-game damage carry."
        )
        synergies = "Super Monkey (3-0-2 Sun Avatar) + Alchemist (3-2-0 Berserker Brew)"
        alternatives = ["Sauda", "Quincy", "Obyn Greenfoot"]
    else:
        reason = h_data.get("summary", f"{hero_name} provides strong tactical capabilities across {m_name}.")
        syn_list = h_data.get("synergies", [])
        synergies = ", ".join(syn_list) if isinstance(syn_list, list) else str(syn_list)
        alternatives = [map_hero_intel.get("best_hero", "Sauda"), "Sauda", "Quincy"]

    # Filter alternatives so the hero itself is not in its own alternatives
    alternatives = [a for a in alternatives if a != hero_name]
    if not alternatives:
        alternatives = ["Quincy", "Sauda"]

    return {
        "hero": hero_name,
        "reason": reason,
        "alternatives": alternatives,
        "synergies": synergies
    }

