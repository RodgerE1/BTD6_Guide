"""
threat_radar_data.py
Tactical Bloons TD 6 Round & Wave Composition Database (Rounds 1–100).
Provides exact bloon counts, immunities, danger flags, RBE, and active defense readiness verification.
"""

# Danger round metadata and tactical notes
DANGER_ROUNDS = {
    24: {"flag": "👁️ FIRST CAMO", "type": "Camo", "severity": "Medium", "note": "1 Camo Green Bloon arrives. Requires Camo detection."},
    28: {"flag": "🛡️ FIRST LEAD", "type": "Lead", "severity": "Medium", "note": "6 Lead Bloons arrive. Sharp projectiles (darts, ninja shurikens, tacks) cannot damage Leads."},
    30: {"flag": "🛡️ LEAD CLUSTER", "type": "Lead", "severity": "Low", "note": "9 Lead Bloons in rapid succession."},
    33: {"flag": "👁️ CAMO PACK", "type": "Camo", "severity": "Low", "note": "13 Camo Reds and 1 Camo Yellow."},
    36: {"flag": "💨 PINK SWARM & REGROW", "type": "Speed/Regrow", "severity": "Medium", "note": "140 fast Pink Bloons + 4 Regrow Greens + 7 Camo Greens."},
    37: {"flag": "⚖️ WHITE/BLACK/LEAD MIX", "type": "Mixed", "severity": "Medium", "note": "25 Whites (immune to freeze), 25 Blacks (immune to explosions), 7 Leads, and 10 Camo Whites."},
    38: {"flag": "🦓 DENSE CERAMIC/ZEBRA", "type": "Mixed", "severity": "Medium", "note": "42 Whites, 17 Zebras, 14 Leads in a compressed stream."},
    40: {"flag": "💥 FIRST MOAB BLIMP", "type": "MOAB", "severity": "HIGH", "note": "The Round 40 MOAB (200 HP). Contains 4 Ceramic Bloons inside upon popping!"},
    42: {"flag": "👁️ CAMO RAINBOWS", "type": "Camo", "severity": "Medium", "note": "6 Camo Rainbow Bloons. High speed upon layer popping."},
    45: {"flag": "🛡️ FORTIFIED LEADS", "type": "Fortified Lead", "severity": "HIGH", "note": "4 Fortified Leads (require 4 explosive/acid hits each) + 24 Rainbows."},
    49: {"flag": "🌊 GREEN FLOOD & CERAMICS", "type": "Ceramic", "severity": "Medium", "note": "343 Greens + 20 Regrow Rainbows + 18 Ceramics."},
    50: {"flag": "💥 DUAL MOABS", "type": "MOAB", "severity": "HIGH", "note": "2 MOAB blimps back-to-back."},
    55: {"flag": "💥 MOAB & CERAMICS", "type": "MOAB/Ceramic", "severity": "Medium", "note": "1 MOAB + 30 dense Ceramics."},
    59: {"flag": "⚠️ CAMO LEADS!", "type": "Camo Lead", "severity": "CRITICAL", "note": "10 Camo Lead Bloons! Towers MUST have both Camo detection AND Lead popping power simultaneously!"},
    60: {"flag": "☠️ FIRST BFB BLIMP", "type": "BFB", "severity": "CRITICAL", "note": "The BFB (Brutal Flying Behemoth - 700 HP). Contains 4 MOABs inside (which contain 16 Ceramics)!"},
    62: {"flag": "🛡️ FORTIFIED LEAD WALL", "type": "Fortified Lead", "severity": "Medium", "note": "25 Fortified Leads + 6 Camo Rainbows + 2 MOABs."},
    63: {"flag": "🚨 THE NOTORIOUS CERAMIC RUSH", "type": "Ceramic Rush", "severity": "EXTREME", "note": "3 ultra-dense waves containing 122 Ceramic bloons! Most notorious run-killer in BTD6. Requires high pierce, crowd-control, or explosive/glue splash."},
    64: {"flag": "💥 6 MOABS & 3 BFBS", "type": "Blimps", "severity": "HIGH", "note": "Heavy blimp pressure testing sustained single-target DPS."},
    65: {"flag": "☠️ 3 BFBS & 20 LEADS", "type": "BFB/Lead", "severity": "HIGH", "note": "3 BFBs accompanied by 20 Leads and Regrow Rainbows."},
    70: {"flag": "💥 4 MOABS & 120 CAMO WHITES", "type": "Camo/MOAB", "severity": "Medium", "note": "High camo pierce test alongside 4 MOAB hulls."},
    75: {"flag": "☠️ 3 BFBS & 14 MOABS", "type": "Blimps", "severity": "HIGH", "note": "Dense blimp train leading into late-game."},
    76: {"flag": "🚨 THE REGROW CERAMIC WALL", "type": "Regrow Ceramic", "severity": "EXTREME", "note": "60 Regrow Ceramics in 2 instant dense clusters. If not popped instantly, they multiply and overwhelm defenses."},
    78: {"flag": "🚨 DUAL CERAMIC & CAMO CERAMIC", "type": "Camo Ceramic", "severity": "EXTREME", "note": "Wave 1: 68 Ceramics + 1 BFB. Wave 2: 72 CAMO CERAMICS! Devastating if camo detection lacks ceramic damage."},
    80: {"flag": "👑 THE ZOMG (ROUND 80 BOSS)", "type": "ZOMG", "severity": "MAXIMUM", "note": "Zeppelin of Mighty Gargantuaness (4,000 HP). Contains 4 BFBs, which split into 16 MOABs, which split into 64 Ceramics!"},
    85: {"flag": "👑 DUAL ZOMGS", "type": "ZOMG", "severity": "HIGH", "note": "2 ZOMG airships."},
    90: {"flag": "⚡ FIRST DDTS (DARK DIRIGIBLE TITANS)", "type": "DDT", "severity": "CRITICAL", "note": "3 DDT blimps! Blindingly fast, innate Camo, immune to sharp/darts (Lead property) and explosions (Black property)."},
    95: {"flag": "🚨 THE DEADLY DDT SWARM", "type": "DDT Swarm", "severity": "MAXIMUM", "note": "30 DDTs + 4 Fortified BFBs + 10 Regrow Leads. The ultimate speed and lead/camo test."},
    98: {"flag": "🌊 MASSIVE FORTIFIED BFB & ZOMG FLEET", "type": "Fortified Blimps", "severity": "MAXIMUM", "note": "8 Fortified BFBs, 30 Fortified MOABs, 8 ZOMGs. Dense blimp swarm."},
    99: {"flag": "⚡ FORTIFIED DDTS", "type": "Fortified DDT", "severity": "MAXIMUM", "note": "9 Fortified DDTs. Immense speed with doubled durability."},
    100: {"flag": "☠️ THE BAD (BIG AIRSHIP OF DOOM)", "type": "BAD", "severity": "MAXIMUM", "note": "The final boss (20,000 HP). Completely IMMUNE to all stuns, knockbacks, slows, and hooks! Spawns 2 ZOMGs and 3 DDTs upon destruction."}
}

# Standard wave bloon composition breakdown (Rounds 1–100)
# Structure: {round_num: {"bloons": [{"type": "Red", "count": 20, "camo": False, "regrow": False, "fortified": False}], "rbe": int, "cash": int}}
ROUND_COMPOSITION = {
    1: {"bloons": [{"type": "Red", "count": 20}], "rbe": 20, "cash": 121},
    2: {"bloons": [{"type": "Red", "count": 35}], "rbe": 35, "cash": 137},
    3: {"bloons": [{"type": "Red", "count": 25}, {"type": "Blue", "count": 5}], "rbe": 35, "cash": 138},
    4: {"bloons": [{"type": "Red", "count": 35}, {"type": "Blue", "count": 18}], "rbe": 71, "cash": 175},
    5: {"bloons": [{"type": "Red", "count": 5}, {"type": "Blue", "count": 27}], "rbe": 59, "cash": 164},
    6: {"bloons": [{"type": "Red", "count": 15}, {"type": "Blue", "count": 15}, {"type": "Green", "count": 4}], "rbe": 57, "cash": 163},
    7: {"bloons": [{"type": "Red", "count": 20}, {"type": "Blue", "count": 20}, {"type": "Green", "count": 5}], "rbe": 75, "cash": 182},
    8: {"bloons": [{"type": "Red", "count": 10}, {"type": "Blue", "count": 26}, {"type": "Green", "count": 14}], "rbe": 104, "cash": 213},
    9: {"bloons": [{"type": "Green", "count": 30}], "rbe": 90, "cash": 201},
    10: {"bloons": [{"type": "Blue", "count": 102}], "rbe": 204, "cash": 319},
    11: {"bloons": [{"type": "Red", "count": 10}, {"type": "Blue", "count": 10}, {"type": "Green", "count": 12}, {"type": "Yellow", "count": 3}], "rbe": 78, "cash": 197},
    12: {"bloons": [{"type": "Blue", "count": 15}, {"type": "Green", "count": 10}, {"type": "Yellow", "count": 5}], "rbe": 80, "cash": 201},
    13: {"bloons": [{"type": "Blue", "count": 50}, {"type": "Green", "count": 23}], "rbe": 169, "cash": 293},
    14: {"bloons": [{"type": "Red", "count": 49}, {"type": "Blue", "count": 15}, {"type": "Green", "count": 10}, {"type": "Yellow", "count": 9}], "rbe": 145, "cash": 273},
    15: {"bloons": [{"type": "Red", "count": 20}, {"type": "Blue", "count": 15}, {"type": "Green", "count": 12}, {"type": "Yellow", "count": 5}, {"type": "Pink", "count": 3}], "rbe": 121, "cash": 253},
    16: {"bloons": [{"type": "Green", "count": 40}, {"type": "Yellow", "count": 8}], "rbe": 152, "cash": 286},
    17: {"bloons": [{"type": "Yellow", "count": 12}], "rbe": 48, "cash": 187},
    18: {"bloons": [{"type": "Green", "count": 80}], "rbe": 240, "cash": 384},
    19: {"bloons": [{"type": "Green", "count": 10}, {"type": "Yellow", "count": 4}, {"type": "Pink", "count": 7}], "rbe": 81, "cash": 231},
    20: {"bloons": [{"type": "Black", "count": 6}], "rbe": 66, "cash": 224},
    21: {"bloons": [{"type": "Yellow", "count": 40}, {"type": "Pink", "count": 14}], "rbe": 230, "cash": 396},
    22: {"bloons": [{"type": "White", "count": 16}], "rbe": 176, "cash": 350},
    23: {"bloons": [{"type": "Black", "count": 7}, {"type": "White", "count": 7}], "rbe": 154, "cash": 333},
    24: {"bloons": [{"type": "Blue", "count": 1}, {"type": "Green", "count": 1, "camo": True}], "rbe": 5, "cash": 186},
    25: {"bloons": [{"type": "Yellow", "count": 25}, {"type": "Purple", "count": 1}], "rbe": 111, "cash": 296},
    26: {"bloons": [{"type": "Pink", "count": 23}, {"type": "Zebra", "count": 4}], "rbe": 207, "cash": 395},
    27: {"bloons": [{"type": "Red", "count": 100}, {"type": "Blue", "count": 60}], "rbe": 220, "cash": 412},
    28: {"bloons": [{"type": "Lead", "count": 6}], "rbe": 138, "cash": 336},
    29: {"bloons": [{"type": "Yellow", "count": 50}, {"type": "Regrow Yellow", "count": 15}], "rbe": 260, "cash": 465},
    30: {"bloons": [{"type": "Lead", "count": 9}], "rbe": 207, "cash": 417},
    31: {"bloons": [{"type": "Black", "count": 8}, {"type": "Zebra", "count": 8}], "rbe": 272, "cash": 487},
    32: {"bloons": [{"type": "Black", "count": 15}, {"type": "White", "count": 20}], "rbe": 385, "cash": 607},
    33: {"bloons": [{"type": "Red", "count": 13, "camo": True}, {"type": "Yellow", "count": 1, "camo": True}], "rbe": 17, "cash": 251},
    34: {"bloons": [{"type": "Yellow", "count": 140}, {"type": "Zebra", "count": 5}], "rbe": 675, "cash": 921},
    35: {"bloons": [{"type": "Pink", "count": 35}, {"type": "Rainbow", "count": 18}], "rbe": 895, "cash": 1157},
    36: {"bloons": [{"type": "Pink", "count": 140}, {"type": "Green", "count": 7, "camo": True}], "rbe": 721, "cash": 985},
    37: {"bloons": [{"type": "Black", "count": 25}, {"type": "White", "count": 25}, {"type": "Lead", "count": 7}, {"type": "White", "count": 10, "camo": True}], "rbe": 821, "cash": 1093},
    38: {"bloons": [{"type": "White", "count": 42}, {"type": "Zebra", "count": 17}, {"type": "Lead", "count": 14}], "rbe": 1158, "cash": 1458},
    39: {"bloons": [{"type": "Black", "count": 10}, {"type": "White", "count": 10}, {"type": "Rainbow", "count": 18}], "rbe": 1064, "cash": 1369},
    40: {"bloons": [{"type": "MOAB", "count": 1}], "rbe": 616, "cash": 928},
    41: {"bloons": [{"type": "Black", "count": 60}], "rbe": 660, "cash": 984},
    42: {"bloons": [{"type": "Rainbow", "count": 6, "camo": True}], "rbe": 282, "cash": 618},
    43: {"bloons": [{"type": "Rainbow", "count": 10}, {"type": "Ceramic", "count": 7}], "rbe": 1204, "cash": 1572},
    44: {"bloons": [{"type": "Zebra", "count": 50}], "rbe": 1150, "cash": 1526},
    45: {"bloons": [{"type": "Fortified Lead", "count": 4, "fortified": True}, {"type": "Rainbow", "count": 24}], "rbe": 1256, "cash": 1642},
    46: {"bloons": [{"type": "Ceramic", "count": 6}, {"type": "Fortified Ceramic", "count": 3, "fortified": True}], "rbe": 1152, "cash": 1546},
    47: {"bloons": [{"type": "Pink", "count": 70}, {"type": "Camo Ceramic", "count": 2, "camo": True}], "rbe": 558, "cash": 974},
    48: {"bloons": [{"type": "Purple", "count": 40}, {"type": "Rainbow", "count": 30}], "rbe": 1850, "cash": 2296},
    49: {"bloons": [{"type": "Green", "count": 343}, {"type": "Rainbow", "count": 20}, {"type": "Ceramic", "count": 18}], "rbe": 3847, "cash": 4357},
    50: {"bloons": [{"type": "MOAB", "count": 2}, {"type": "Red", "count": 20}], "rbe": 1252, "cash": 1622},
    51: {"bloons": [{"type": "Ceramic", "count": 10}, {"type": "Rainbow", "count": 5}], "rbe": 1275, "cash": 1655},
    52: {"bloons": [{"type": "Rainbow", "count": 25}, {"type": "Ceramic", "count": 5}], "rbe": 1695, "cash": 2085},
    53: {"bloons": [{"type": "Pink", "count": 80}, {"type": "MOAB", "count": 1}], "rbe": 1016, "cash": 1424},
    54: {"bloons": [{"type": "Ceramic", "count": 35}], "rbe": 3640, "cash": 4120},
    55: {"bloons": [{"type": "Ceramic", "count": 30}, {"type": "MOAB", "count": 1}], "rbe": 3736, "cash": 4236},
    56: {"bloons": [{"type": "Rainbow", "count": 40}], "rbe": 1880, "cash": 2340},
    57: {"bloons": [{"type": "MOAB", "count": 2}], "rbe": 1232, "cash": 1632},
    58: {"bloons": [{"type": "Ceramic", "count": 15}, {"type": "Fortified Ceramic", "count": 10, "fortified": True}], "rbe": 3280, "cash": 3810},
    59: {"bloons": [{"type": "Camo Lead", "count": 10, "camo": True}, {"type": "Ceramic", "count": 30}], "rbe": 3350, "cash": 3890},
    60: {"bloons": [{"type": "BFB", "count": 1}], "rbe": 3164, "cash": 3784},
    61: {"bloons": [{"type": "Zebra", "count": 150}, {"type": "MOAB", "count": 5}], "rbe": 6530, "cash": 7240},
    62: {"bloons": [{"type": "Fortified Lead", "count": 25, "fortified": True}, {"type": "MOAB", "count": 2}], "rbe": 1864, "cash": 2380},
    63: {"bloons": [{"type": "Ceramic", "count": 122}], "rbe": 12688, "cash": 13398},
    64: {"bloons": [{"type": "MOAB", "count": 6}, {"type": "BFB", "count": 3}], "rbe": 13188, "cash": 13988},
    65: {"bloons": [{"type": "Lead", "count": 20}, {"type": "BFB", "count": 3}], "rbe": 9952, "cash": 10722},
    66: {"bloons": [{"type": "MOAB", "count": 11}], "rbe": 6776, "cash": 7616},
    67: {"bloons": [{"type": "Ceramic", "count": 14}, {"type": "Fortified Ceramic", "count": 9, "fortified": True}], "rbe": 2984, "cash": 3614},
    68: {"bloons": [{"type": "MOAB", "count": 4}, {"type": "BFB", "count": 1}], "rbe": 5628, "cash": 6408},
    69: {"bloons": [{"type": "Lead", "count": 40}, {"type": "Ceramic", "count": 50}], "rbe": 6120, "cash": 7040},
    70: {"bloons": [{"type": "Camo White", "count": 120, "camo": True}, {"type": "MOAB", "count": 4}], "rbe": 3784, "cash": 4724},
    71: {"bloons": [{"type": "Ceramic", "count": 30}, {"type": "MOAB", "count": 6}], "rbe": 6816, "cash": 7746},
    72: {"bloons": [{"type": "BFB", "count": 2}], "rbe": 6328, "cash": 7208},
    73: {"bloons": [{"type": "MOAB", "count": 8}, {"type": "BFB", "count": 2}], "rbe": 11256, "cash": 12266},
    74: {"bloons": [{"type": "Ceramic", "count": 42}, {"type": "BFB", "count": 1}], "rbe": 7532, "cash": 8502},
    75: {"bloons": [{"type": "Lead", "count": 20}, {"type": "MOAB", "count": 14}, {"type": "BFB", "count": 3}], "rbe": 18580, "cash": 19780},
    76: {"bloons": [{"type": "Regrow Ceramic", "count": 60, "regrow": True}], "rbe": 6240, "cash": 7320},
    77: {"bloons": [{"type": "MOAB", "count": 12}, {"type": "BFB", "count": 4}], "rbe": 20048, "cash": 21328},
    78: {"bloons": [{"type": "Ceramic", "count": 68}, {"type": "Camo Ceramic", "count": 72, "camo": True}, {"type": "BFB", "count": 1}], "rbe": 17724, "cash": 19044},
    79: {"bloons": [{"type": "Regrow Rainbow", "count": 50, "regrow": True}, {"type": "BFB", "count": 4}], "rbe": 15006, "cash": 16426},
    80: {"bloons": [{"type": "ZOMG", "count": 1}], "rbe": 16656, "cash": 18126},
    81: {"bloons": [{"type": "BFB", "count": 6}], "rbe": 18984, "cash": 20564},
    82: {"bloons": [{"type": "MOAB", "count": 10}, {"type": "BFB", "count": 4}], "rbe": 18816, "cash": 20436},
    83: {"bloons": [{"type": "Ceramic", "count": 80}, {"type": "MOAB", "count": 8}], "rbe": 13248, "cash": 14888},
    84: {"bloons": [{"type": "BFB", "count": 10}], "rbe": 31640, "cash": 33420},
    85: {"bloons": [{"type": "ZOMG", "count": 2}], "rbe": 33312, "cash": 35212},
    86: {"bloons": [{"type": "Fortified BFB", "count": 5, "fortified": True}], "rbe": 22820, "cash": 24840},
    87: {"bloons": [{"type": "ZOMG", "count": 4}], "rbe": 66624, "cash": 68984},
    88: {"bloons": [{"type": "Lead", "count": 50}, {"type": "ZOMG", "count": 3}], "rbe": 51118, "cash": 53448},
    89: {"bloons": [{"type": "MOAB", "count": 20}, {"type": "BFB", "count": 8}], "rbe": 37632, "cash": 40152},
    90: {"bloons": [{"type": "DDT", "count": 3, "camo": True, "lead": True}], "rbe": 2448, "cash": 4728},
    91: {"bloons": [{"type": "Ceramic", "count": 100}, {"type": "BFB", "count": 6}], "rbe": 29384, "cash": 32024},
    92: {"bloons": [{"type": "ZOMG", "count": 4}, {"type": "MOAB", "count": 10}], "rbe": 72784, "cash": 75784},
    93: {"bloons": [{"type": "DDT", "count": 6, "camo": True, "lead": True}, {"type": "BFB", "count": 10}], "rbe": 36536, "cash": 39656},
    94: {"bloons": [{"type": "BFB", "count": 6}, {"type": "ZOMG", "count": 6}], "rbe": 118920, "cash": 122820},
    95: {"bloons": [{"type": "DDT", "count": 30, "camo": True, "lead": True}, {"type": "Fortified BFB", "count": 4, "fortified": True}], "rbe": 42740, "cash": 46240},
    96: {"bloons": [{"type": "MOAB", "count": 40}, {"type": "ZOMG", "count": 6}], "rbe": 124576, "cash": 128976},
    97: {"bloons": [{"type": "Fortified ZOMG", "count": 2, "fortified": True}], "rbe": 49312, "cash": 53212},
    98: {"bloons": [{"type": "Fortified BFB", "count": 8, "fortified": True}, {"type": "ZOMG", "count": 8}], "rbe": 169760, "cash": 174880},
    99: {"bloons": [{"type": "Fortified DDT", "count": 9, "fortified": True, "camo": True, "lead": True}], "rbe": 14688, "cash": 18408},
    100: {"bloons": [{"type": "BAD", "count": 1}], "rbe": 55760, "cash": 61280}
}

def get_round_data(round_num):
    """Returns the full data package for a given round number (1-100)."""
    comp = ROUND_COMPOSITION.get(round_num, {"bloons": [{"type": "Bloons", "count": 20}], "rbe": 100, "cash": 200})
    danger = DANGER_ROUNDS.get(round_num, None)
    return {
        "round": round_num,
        "danger": danger,
        "is_danger": danger is not None,
        "bloons": comp.get("bloons", []),
        "rbe": comp.get("rbe", 0),
        "cash": comp.get("cash", 0)
    }

def check_strategy_defense_readiness(round_num, strategy_steps):
    """
    Evaluates whether the provided strategy steps up to round_num have adequate
    Camo, Lead, Blimp, and Ceramic popping coverage.
    """
    active_steps = [s for s in strategy_steps if s.get("round", 1) <= round_num]

    has_camo = False
    has_lead = False
    has_moab_dmg = False
    has_ceramic_cc = False

    camo_providers = []
    lead_providers = []
    moab_providers = []
    ceramic_providers = []

    for s in active_steps:
        tower = s.get("tower", "").lower()
        upg = s.get("upgrade", "0-0-0")
        t_str = f"{s.get('tower')} [{upg}]"

        # Check Camo capability
        if "sauda" in tower or "etienne" in tower or "psi" in tower or "ezili" in tower:
            has_camo = True
            camo_providers.append(t_str)
        elif "ninja" in tower:
            has_camo = True
            camo_providers.append(t_str)
        elif "sub" in tower and ("2-" in upg or "3-" in upg or "4-" in upg or "5-" in upg):
            has_camo = True
            camo_providers.append(t_str)
        elif "village" in tower and ("-2-" in upg or "-3-" in upg or "-4-" in upg or "-5-" in upg):
            has_camo = True
            camo_providers.append(t_str)
        elif "sniper" in tower and ("-2" in upg):
            has_camo = True
            camo_providers.append(t_str)
        elif "wizard" in tower and ("-2" in upg or "0-2-" in upg):
            has_camo = True
            camo_providers.append(t_str)
        elif "dart" in tower and ("-2" in upg or "-3" in upg or "-4" in upg):
            has_camo = True
            camo_providers.append(t_str)

        # Check Lead capability
        if "alchemist" in tower and ("2-" in upg or "3-" in upg or "4-" in upg or "5-" in upg):
            has_lead = True
            lead_providers.append(t_str)
        elif "bomb" in tower:
            has_lead = True
            lead_providers.append(t_str)
        elif "sauda" in tower and round_num >= 7:
            has_lead = True
            lead_providers.append(t_str)
        elif "gwendolin" in tower or "striker" in tower or "churchill" in tower or "obyn" in tower:
            has_lead = True
            lead_providers.append(t_str)
        elif "wizard" in tower and ("-1-" in upg or "-2-" in upg or "1-" in upg):
            has_lead = True
            lead_providers.append(t_str)
        elif "glue" in tower and ("2-" in upg or "3-" in upg or "4-" in upg):
            has_lead = True
            lead_providers.append(t_str)
        elif "mortar" in tower:
            has_lead = True
            lead_providers.append(t_str)

        # Check MOAB / Blimp damage
        if "mauler" in s.get("details", "").lower() or ("bomb" in tower and "-3-" in upg or "-4-" in upg):
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "sub" in tower and ("-3" in upg or "-4" in upg or "-5" in upg):
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "buccaneer" in tower and ("3-" in upg or "4-" in upg or "-4-" in upg):
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "ninja" in tower and ("4-" in upg or "5-" in upg):
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "super" in tower:
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "tack" in tower and ("-4" in upg or "-5" in upg):
            has_moab_dmg = True
            moab_providers.append(t_str)
        elif "heli" in tower or "ace" in tower:
            has_moab_dmg = True
            moab_providers.append(t_str)

        # Check Ceramic Crowd Control
        if "bloonjitsu" in s.get("details", "").lower() or ("ninja" in tower and "4-" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)
        elif "tack" in tower and ("4-" in upg or "-4" in upg or "-5" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)
        elif "bomb" in tower and ("-4" in upg or "-5" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)
        elif "glue" in tower and ("3-" in upg or "4-" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)
        elif "boomerang" in tower and ("4-" in upg or "-4" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)
        elif "wizard" in tower and ("-4" in upg or "-5" in upg):
            has_ceramic_cc = True
            ceramic_providers.append(t_str)

    return {
        "round": round_num,
        "camo_ready": has_camo,
        "camo_towers": list(dict.fromkeys(camo_providers)),
        "lead_ready": has_lead,
        "lead_towers": list(dict.fromkeys(lead_providers)),
        "moab_ready": has_moab_dmg,
        "moab_towers": list(dict.fromkeys(moab_providers)),
        "ceramic_ready": has_ceramic_cc,
        "ceramic_towers": list(dict.fromkeys(ceramic_providers))
    }
