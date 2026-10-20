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

def get_best_hero_for_map(map_id, map_data):
    """
    Evaluates map characteristics (lanes, water, obstacles, category, gimmick)
    and returns the optimal #1 hero, detailed tactical justification, alternative heroes, and synergy notes.
    """
    category = map_data.get("category", "Beginner")
    lanes = map_data.get("lanes", "Single").lower()
    has_water = map_data.get("water", False)
    sight_blocked = map_data.get("sight_blockers", False)
    gimmick = map_data.get("gimmick", "").lower()
    m_name = map_data.get("name", "")

    # 1. Specialized Map Overrides
    if "flooded valley" in m_name.lower():
        return {
            "best_hero": "Admiral Brickell",
            "reason": "Flooded Valley is almost entirely submerged in water. Brickell placed at the center floodgate provides unmatched mine placement and double attack speed to all naval subs and buccaneers.",
            "alternatives": ["Etienne", "Psi"],
            "synergies": "Monkey Sub (Sub Commander 2-0-5) + Buccaneer (Pirate Lord 0-5-2)"
        }
    if "spillway" in m_name.lower():
        return {
            "best_hero": "Admiral Brickell",
            "reason": "The central drain barrel is the only placement spot that reaches all incoming bloon pipes. Brickell fits perfectly in the center barrel and drops mega mines that destroy all 5 paths simultaneously.",
            "alternatives": ["Pat Fusty", "Psi"],
            "synergies": "Central Barrel Water Buff + Ring of Fire around perimeter"
        }
    if "sanctuary" in m_name.lower() or "geared" in m_name.lower() or "ravine" in m_name.lower() or "quad" in m_name.lower():
        return {
            "best_hero": "Psi",
            "reason": "This expert map features separated lanes, moving terrain, or heavy sight blockers. Psi attacks anywhere on the entire map regardless of obstacles with infinite range and no projectile travel time.",
            "alternatives": ["Geraldo", "Quincy"],
            "synergies": "Sniper Monkey (Elite Defender 0-2-5) + Spike Factory at exits"
        }
    if "infernal" in m_name.lower():
        return {
            "best_hero": "Quincy",
            "reason": "The tiny isolated rock islands in the lava have strict placement room. Quincy fits onto the early lower rock and uses his long range and bouncing arrows to cover both lanes effortlessly.",
            "alternatives": ["Psi", "Etienne"],
            "synergies": "Sniper Monkey + Boomerang Monkey on upper rocks"
        }
    if "dark castle" in m_name.lower():
        return {
            "best_hero": "Sauda",
            "reason": "While an Expert map, all four bloon tracks converge directly into a single wooden castle drawbridge. Sauda placed at the drawbridge entrance strikes 100% of bloons from all four lanes.",
            "alternatives": ["Quincy", "Obyn Greenfoot"],
            "synergies": "Alchemist 3-2-0 on castle wall + Sub 2-0-3 Triple Guns in moat"
        }
    if "muddy puddles" in m_name.lower() or "bloody puddles" in m_name.lower():
        return {
            "best_hero": "Quincy",
            "reason": "Multiple parallel muddy tracks make single-spot defenders ineffective. Quincy's low starting cost ($540) and long bouncing range can cover multiple tracks across rounds.",
            "alternatives": ["Geraldo", "Psi"],
            "synergies": "Sub 2-0-0 Advanced Intel + Dart Monkeys on muddy banks"
        }

    # 2. Heuristic Evaluation for General Maps
    # If the map is multi-lane and has heavy sight blockers -> Psi or Etienne
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

    # If the map has significant water and lanes converge near water -> Admiral Brickell or Sauda
    if has_water and ("peninsula" in m_name.lower() or "off the coast" in m_name.lower() or "spice islands" in m_name.lower() or "sunken" in m_name.lower()):
        return {
            "best_hero": "Admiral Brickell",
            "reason": f"Extensive water layout on {m_name} allows building a premier Sub and Buccaneer fleet. Brickell's Naval Tactics doubles their attack speed and grants Lead/Camo popping to all naval towers.",
            "alternatives": ["Sauda", "Etienne", "Quincy"],
            "synergies": "Sub Commander (2-0-5) + Buccaneer (Pirate Lord 0-5-2)"
        }

    # Single lane or intersecting chokepoint maps -> Sauda is Queen
    return {
        "best_hero": "Sauda",
        "reason": f"{m_name} features tight curves or lane intersections where short-range melee towers excel. Sauda costs only $510, soloes early rounds, has innate Camo, and crushes early Lead/MOABs with abilities.",
        "alternatives": ["Quincy", "Gwendolin", "Obyn Greenfoot"],
        "synergies": "Alchemist (3-2-0 Berserker Brew) + Ninja Monkey (4-0-1 Bloonjitsu)"
    }
