import json

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

with open("guides.json", "r", encoding="utf-8") as f:
    d = json.load(f)

all_maps = set(d["maps"].keys())
assigned_maps = set(MAP_HERO_INTELLIGENCE.keys())

print("Total in guides.json:", len(all_maps))
print("Total in MAP_HERO_INTELLIGENCE:", len(assigned_maps))
print("Missing:", all_maps - assigned_maps)
print("Extra:", assigned_maps - all_maps)

hero_counts = {}
for m, data in MAP_HERO_INTELLIGENCE.items():
    h = data["best_hero"]
    hero_counts[h] = hero_counts.get(h, 0) + 1

print("\nHero distribution across all 87 maps:")
for h, cnt in sorted(hero_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {h:20}: {cnt} maps")

print("\nTotal heroes with >= 1 map:", len(hero_counts), "/ 16")
