import os, re

def patch_intermediate():
    path = os.path.join(os.path.dirname(__file__), "..", "map_data_intermediate.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. cracked: Step 3 timing="during_round"
    content = content.replace(
        'create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Upper pond.", "First", 1765, "Twin Guns and Airburst Darts fire bursts of seeking darts across the track.")',
        'create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Upper pond.", "First", 1765, "Twin Guns and Airburst Darts fire bursts of seeking darts across the track.", timing="during_round")'
    )

    # 2. spring_spring: Step 3 timing="during_round"
    content = content.replace(
        'create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Right spring pond.", "First", 1765, "Twin Guns and Airburst Darts give rapid multi-dart popping on both spring paths.")',
        'create_step(3, "Rounds 11–20: Expanding Defense", 11, "Upgrade", "Monkey Sub", "2-0-2", "Right spring pond.", "First", 1765, "Twin Guns and Airburst Darts give rapid multi-dart popping on both spring paths.", timing="during_round")'
    )

    # 3. firing_range:
    # step 5 round 22 -> 24
    # step 6 timing during_round
    # step 7 timing during_round
    # step 8 timing during_round
    old_fr = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Sniper Monkey", "3-0-2", "On the elevated wooden sniper tower.", "Strong", 3740, "Deadly Precision pops Leads and destroys Ceramics with massive per-shot damage."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Tack Shooter", "2-0-3", "In the center trench gap.", "First", 935, "More Tacks and Faster Shooting shreds dense packs in the trench."),
                    create_step(7, "Rounds 31–39: Midgame Defense", 34, "Upgrade", "Tack Shooter", "2-0-4", "In the center trench gap.", "First", 2720, "The Overdrive unleashes extreme close-range dart saturation."),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Near the trench exit.", "Strong", 2355, "MOAB Mauler with Missile Launcher directly targets the blimp; Sniper and Overdrive pop ceramics.")'''

    new_fr = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 24, "Upgrade", "Sniper Monkey", "3-0-2", "On the elevated wooden sniper tower.", "Strong", 3740, "Deadly Precision pops Leads and destroys Ceramics with massive per-shot damage."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Upgrade", "Tack Shooter", "2-0-3", "In the center trench gap.", "First", 935, "More Tacks and Faster Shooting shreds dense packs in the trench.", timing="during_round"),
                    create_step(7, "Rounds 31–39: Midgame Defense", 34, "Upgrade", "Tack Shooter", "2-0-4", "In the center trench gap.", "First", 2720, "The Overdrive unleashes extreme close-range dart saturation.", timing="during_round"),
                    create_step(8, "Round 40: MOAB Battle", 37, "Place", "Bomb Shooter", "0-3-2", "Near the trench exit.", "Strong", 2355, "MOAB Mauler with Missile Launcher directly targets the blimp; Sniper and Overdrive pop ceramics.", timing="during_round")'''
    content = content.replace(old_fr, new_fr)

    # 4. downstream, bazaar, water_park, luminous_cove: Naval steps 5-8 replacement
    # downstream
    old_ds = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Center river bend.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the river.", "First", 2360, "Triple Guns with Advanced Intel provides constant long-range dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the bank within range of Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Near the exit river bridge.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    new_ds = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Center river bend.", "First", 3485, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-0", "In the river.", "First", 810, "Advanced Intel provides global camo and dart coverage."),
                    create_step(7, "Rounds 31–39: Midgame Defense", 32, "Upgrade", "Monkey Sub", "2-0-3", "In the river.", "First", 2165, "Triple Guns dramatically scales up fast-firing dart output."),
                    create_step(8, "Rounds 31–39: Midgame Defense", 36, "Place", "Alchemist", "3-0-0", "On the bank within range of Buccaneer.", "Close", 2040, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(9, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Near the exit river bridge.", "Strong", 1930, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    content = content.replace(old_ds, new_ds)

    # bazaar
    old_bz = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Oasis canal.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the canal.", "First", 2360, "Triple Guns with Advanced Intel provides constant long-range dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the canal bank.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Near the oasis exit.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    new_bz = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Oasis canal.", "First", 3485, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-0", "In the canal.", "First", 810, "Advanced Intel provides global camo and dart coverage."),
                    create_step(7, "Rounds 31–39: Midgame Defense", 32, "Upgrade", "Monkey Sub", "2-0-3", "In the canal.", "First", 2165, "Triple Guns dramatically scales up fast-firing dart output."),
                    create_step(8, "Rounds 31–39: Midgame Defense", 36, "Place", "Alchemist", "3-0-0", "On the canal bank.", "Close", 2040, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(9, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Near the oasis exit.", "Strong", 1930, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    content = content.replace(old_bz, new_bz)

    # water_park
    old_wp = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Main pool.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the wave pool.", "First", 2360, "Triple Guns with Advanced Intel provides constant long-range dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "Between the pools.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "At the slide exit.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    new_wp = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "Main pool.", "First", 3485, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-0", "In the wave pool.", "First", 810, "Advanced Intel provides global camo and dart coverage."),
                    create_step(7, "Rounds 31–39: Midgame Defense", 32, "Upgrade", "Monkey Sub", "2-0-3", "In the wave pool.", "First", 2165, "Triple Guns dramatically scales up fast-firing dart output."),
                    create_step(8, "Rounds 31–39: Midgame Defense", 36, "Place", "Alchemist", "3-0-0", "Between the pools.", "Close", 2040, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(9, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "At the slide exit.", "Strong", 1930, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    content = content.replace(old_wp, new_wp)

    # luminous_cove
    old_lc = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "In the cove bay.", "First", 2510, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-3", "In the glowing waters.", "First", 2360, "Triple Guns with Advanced Intel provides constant long-range dart fire."),
                    create_step(7, "Rounds 31–39: Final Preparation", 33, "Place", "Alchemist", "3-0-0", "On the rocky outcrop near Buccaneer.", "Close", 1885, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(8, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Along the track exit.", "Strong", 1530, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    new_lc = '''                    create_step(5, "Rounds 21–30: Camo and Lead Preparation", 22, "Upgrade", "Monkey Buccaneer", "3-2-0", "In the cove bay.", "First", 3485, "Destroyer unleashes rapid grape barrages."),
                    create_step(6, "Rounds 21–30: Camo and Lead Preparation", 27, "Place", "Monkey Sub", "2-0-0", "In the glowing waters.", "First", 810, "Advanced Intel provides global camo and dart coverage."),
                    create_step(7, "Rounds 31–39: Midgame Defense", 32, "Upgrade", "Monkey Sub", "2-0-3", "In the glowing waters.", "First", 2165, "Triple Guns dramatically scales up fast-firing dart output."),
                    create_step(8, "Rounds 31–39: Midgame Defense", 36, "Place", "Alchemist", "3-0-0", "On the rocky outcrop near Buccaneer.", "Close", 2040, "Berserker Brew boosts the Destroyer's fire rate and damage."),
                    create_step(9, "Round 40: MOAB Battle", 38, "Place", "Bomb Shooter", "0-3-0", "Along the track exit.", "Strong", 1930, "MOAB Mauler targets the blimp. The Destroyer and Sub effortlessly pop the MOAB and ceramic insides.")'''
    content = content.replace(old_lc, new_lc)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched map_data_intermediate.py successfully.")

patch_intermediate()
