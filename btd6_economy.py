"""
btd6_economy.py
Centralized BTD6 Game Economy, Capability Models, and Tower Price Data.
Provides versioned tower pricing, exact round income, legal crosspath verification,
and structured capability rules.
"""

import math
import re

# ==============================================================================
# 1. CANONICAL TOWERS & HEROES
# ==============================================================================
CANONICAL_TOWERS = {
    # Primary
    "Dart Monkey": {"type": "Primary", "water": False, "base_cost": 200},
    "Boomerang Monkey": {"type": "Primary", "water": False, "base_cost": 325},
    "Bomb Shooter": {"type": "Primary", "water": False, "base_cost": 525},
    "Tack Shooter": {"type": "Primary", "water": False, "base_cost": 280},
    "Ice Monkey": {"type": "Primary", "water": False, "base_cost": 500},
    "Glue Gunner": {"type": "Primary", "water": False, "base_cost": 275},

    # Military
    "Sniper Monkey": {"type": "Military", "water": False, "base_cost": 350},
    "Monkey Sub": {"type": "Military", "water": True, "base_cost": 325},
    "Monkey Buccaneer": {"type": "Military", "water": True, "base_cost": 500},
    "Monkey Ace": {"type": "Military", "water": False, "base_cost": 800},
    "Heli Pilot": {"type": "Military", "water": False, "base_cost": 1600},
    "Mortar Monkey": {"type": "Military", "water": False, "base_cost": 750},
    "Dartling Gunner": {"type": "Military", "water": False, "base_cost": 750},

    # Magic
    "Wizard Monkey": {"type": "Magic", "water": False, "base_cost": 375},
    "Super Monkey": {"type": "Magic", "water": False, "base_cost": 2500},
    "Ninja Monkey": {"type": "Magic", "water": False, "base_cost": 500},
    "Alchemist": {"type": "Magic", "water": False, "base_cost": 550},
    "Druid": {"type": "Magic", "water": False, "base_cost": 400},

    # Support
    "Banana Farm": {"type": "Support", "water": False, "base_cost": 1250},
    "Spike Factory": {"type": "Support", "water": False, "base_cost": 1000},
    "Monkey Village": {"type": "Support", "water": False, "base_cost": 1200},
    "Engineer Monkey": {"type": "Support", "water": False, "base_cost": 400},
    "Beast Handler": {"type": "Support", "water": False, "base_cost": 250},
}

CANONICAL_HEROES = {
    "Quincy": {"cost_easy": 455, "cost_medium": 540, "cost_hard": 585, "water": False},
    "Gwendolin": {"cost_easy": 615, "cost_medium": 725, "cost_hard": 780, "water": False},
    "Striker Jones": {"cost_easy": 640, "cost_medium": 750, "cost_hard": 810, "water": False},
    "Obyn Greenfoot": {"cost_easy": 550, "cost_medium": 650, "cost_hard": 700, "water": False},
    "Sauda": {"cost_easy": 510, "cost_medium": 600, "cost_hard": 650, "water": False},
    "Psi": {"cost_easy": 680, "cost_medium": 800, "cost_hard": 865, "water": False},
    "Etienne": {"cost_easy": 720, "cost_medium": 850, "cost_hard": 920, "water": False},
    "Admiral Brickell": {"cost_easy": 640, "cost_medium": 750, "cost_hard": 810, "water": True},
    "Benjamin": {"cost_easy": 1020, "cost_medium": 1200, "cost_hard": 1300, "water": False},
    "Adora": {"cost_easy": 850, "cost_medium": 1000, "cost_hard": 1080, "water": False},
    "Pat Fusty": {"cost_easy": 680, "cost_medium": 800, "cost_hard": 865, "water": True}, # Amphibious
    "Churchill": {"cost_easy": 1530, "cost_medium": 1800, "cost_hard": 1945, "water": False},
    "Captain Churchill": {"cost_easy": 1530, "cost_medium": 1800, "cost_hard": 1945, "water": False},
    "Ezili": {"cost_easy": 510, "cost_medium": 600, "cost_hard": 650, "water": False},
    "Geraldo": {"cost_easy": 550, "cost_medium": 650, "cost_hard": 700, "water": False},
    "Corvus": {"cost_easy": 700, "cost_medium": 825, "cost_hard": 890, "water": False},
    "Rosalia": {"cost_easy": 595, "cost_medium": 700, "cost_hard": 755, "water": False},
}

ALL_VALID_TOWERS = set(CANONICAL_TOWERS.keys()) | set(CANONICAL_HEROES.keys())

# Difficulty price multipliers (rounded to nearest 5 in BTD6)
DIFF_MULTIPLIERS = {
    "Easy": 0.85,
    "Medium": 1.0,
    "Hard": 1.08,
    "Impoppable": 1.20
}

def round_cost_to_5(cost):
    return int(round(cost / 5.0) * 5)

def convert_cost(cost_medium, target_difficulty="Easy"):
    mult = DIFF_MULTIPLIERS.get(target_difficulty, 1.0)
    return round_cost_to_5(cost_medium * mult)

def easy_to_medium_cost(cost_easy):
    return round_cost_to_5(cost_easy * (1.0 / 0.85))

def easy_to_hard_cost(cost_easy):
    return round_cost_to_5(cost_easy * (1.08 / 0.85))

# ==============================================================================
# CANONICAL UPGRADE COSTS (Medium Difficulty Standard Base)
# Structure: [Path 1 (Tiers 1-5), Path 2 (Tiers 1-5), Path 3 (Tiers 1-5)]
# ==============================================================================
CANONICAL_UPGRADES = {
    "Dart Monkey": [
        [140, 220, 300, 1800, 15000],
        [100, 190, 400, 8000, 45000],
        [90, 140, 625, 2000, 23500]
    ],
    "Boomerang Monkey": [
        [200, 280, 1300, 3200, 32500],
        [175, 250, 1450, 4200, 35000],
        [100, 300, 1400, 3400, 50000]
    ],
    "Bomb Shooter": [
        [350, 650, 1200, 3600, 55000],
        [250, 400, 1100, 3100, 25000],
        [200, 300, 800, 2800, 35000]
    ],
    "Tack Shooter": [
        [150, 300, 600, 3500, 45000],
        [100, 225, 550, 2700, 20000],
        [100, 100, 450, 3200, 45000]
    ],
    "Ice Monkey": [
        [175, 350, 1500, 2500, 28000],
        [150, 350, 1750, 3000, 20000],
        [100, 200, 1750, 2600, 30000]
    ],
    "Glue Gunner": [
        [200, 300, 2500, 5000, 22000],
        [100, 1800, 2500, 5000, 28000],
        [200, 400, 2300, 3400, 28000]
    ],
    "Sniper Monkey": [
        [350, 1400, 3000, 8000, 32000],
        [250, 450, 3100, 7500, 14500],
        [400, 400, 3400, 4200, 40000]
    ],
    "Monkey Sub": [
        [130, 500, 700, 2500, 22000],
        [450, 500, 1450, 13000, 32000],
        [450, 1000, 1100, 2500, 25000]
    ],
    "Monkey Buccaneer": [
        [500, 650, 2950, 5400, 26000],
        [250, 500, 900, 4500, 26000],
        [180, 500, 900, 5500, 23000]
    ],
    "Monkey Ace": [
        [800, 650, 3000, 3200, 75000],
        [250, 350, 900, 3000, 30000],
        [500, 350, 2800, 24000, 85000]
    ],
    "Heli Pilot": [
        [800, 750, 1750, 10500, 45000],
        [300, 600, 4000, 12000, 30000],
        [600, 500, 3200, 12000, 35000]
    ],
    "Mortar Monkey": [
        [500, 500, 900, 8000, 27000],
        [300, 500, 900, 7500, 40000],
        [200, 500, 900, 11000, 40000]
    ],
    "Dartling Gunner": [
        [300, 900, 4250, 11000, 80000],
        [250, 950, 5250, 6000, 60000],
        [150, 1100, 3400, 12000, 58000]
    ],
    "Wizard Monkey": [
        [150, 450, 1300, 10000, 32000],
        [300, 900, 3000, 4200, 48000],
        [300, 300, 1500, 2800, 26000]
    ],
    "Super Monkey": [
        [2500, 3000, 20000, 100000, 500000],
        [1000, 1400, 7500, 22000, 90000],
        [3000, 1200, 5400, 55000, 200000]
    ],
    "Ninja Monkey": [
        [350, 350, 850, 2750, 35000],
        [250, 400, 900, 5200, 22000],
        [250, 400, 2250, 2750, 40000]
    ],
    "Alchemist": [
        [250, 350, 1250, 3000, 60000],
        [250, 450, 950, 4500, 45000],
        [650, 450, 1000, 2750, 35000]
    ],
    "Druid": [
        [250, 350, 1650, 4500, 65000],
        [250, 350, 1050, 5000, 35000],
        [100, 300, 700, 2500, 45000]
    ],
    "Banana Farm": [
        [500, 600, 3000, 19000, 100000],
        [300, 800, 4200, 7500, 100000],
        [250, 200, 2900, 18000, 68000]
    ],
    "Spike Factory": [
        [800, 600, 2300, 9500, 150000],
        [650, 800, 2400, 6000, 40000],
        [450, 150, 1400, 3500, 30000]
    ],
    "Monkey Village": [
        [500, 1500, 800, 3000, 25000],
        [250, 2000, 7500, 20000, 40000],
        [500, 500, 10000, 5000, 40000]
    ],
    "Engineer Monkey": [
        [500, 400, 575, 2500, 32000],
        [250, 300, 950, 3800, 42000],
        [450, 220, 450, 4200, 38000]
    ],
    "Beast Handler": [
        [180, 850, 2400, 10500, 65000],
        [215, 925, 2700, 11500, 70000],
        [160, 800, 2100, 9500, 60000]
    ],
}

def is_valid_numeric_cost(val):
    """
    Validates whether val is a strictly valid finite numeric cost:
    - Must not be None
    - Must not be a boolean (bool is subclass of int in Python)
    - Must be an int or float
    - Must be finite (rejects NaN, +inf, -inf)
    - Must be non-negative (>= 0)
    """
    if val is None or isinstance(val, bool):
        return False
    if not isinstance(val, (int, float)):
        return False
    if not math.isfinite(val):
        return False
    if val < 0:
        return False
    return True

def get_canonical_upgrade_cost(tower, path_idx, tier, difficulty="Medium"):
    """Returns canonical cost of a specific tier upgrade for a tower at target difficulty."""
    if tower not in CANONICAL_UPGRADES:
        return 0
    paths = CANONICAL_UPGRADES[tower]
    if path_idx < 0 or path_idx >= len(paths):
        return 0
    tiers = paths[path_idx]
    if tier < 0 or tier >= len(tiers):
        return 0
    return convert_cost(tiers[tier], difficulty)

def get_transition_cost(tower, from_tuple, to_tuple, difficulty="Medium"):
    """Calculates canonical cost to transition from from_tuple to to_tuple."""
    if not from_tuple:
        from_tuple = (0, 0, 0)
    if not to_tuple:
        to_tuple = (0, 0, 0)
    total = 0
    for path_idx, (f, t) in enumerate(zip(from_tuple, to_tuple)):
        if t > f:
            for tier in range(f, t):
                total += get_canonical_upgrade_cost(tower, path_idx, tier, difficulty)
    return total

def get_action_canonical_cost(tower, from_tuple, to_tuple, action, difficulty="Medium"):
    """Calculates exact canonical purchase or upgrade cost for an action."""
    if action in ("Target", "Ability", "Sell"):
        return 0
    if action == "Place":
        if tower in CANONICAL_HEROES:
            cost_key = f"cost_{difficulty.lower()}"
            hero_info = CANONICAL_HEROES[tower]
            return hero_info.get(cost_key, convert_cost(hero_info.get("cost_medium", 600), difficulty))
        if tower in CANONICAL_TOWERS:
            base = convert_cost(CANONICAL_TOWERS[tower]["base_cost"], difficulty)
            upg_cost = get_transition_cost(tower, (0, 0, 0), to_tuple, difficulty)
            return base + upg_cost
        return 0
    elif action == "Upgrade":
        return get_transition_cost(tower, from_tuple, to_tuple, difficulty)
    return 0


# ==============================================================================
# 2. EXACT ROUND INCOME & CUMULATIVE CASH CURVE (ROUNDS 1–100)
# ==============================================================================
# Standard BTD6 Wave Red Bloon Equivalents (RBE) for Rounds 1–100
ROUND_RBE = {
    1: 20, 2: 35, 3: 35, 4: 71, 5: 59, 6: 57, 7: 75, 8: 104, 9: 90, 10: 204,
    11: 78, 12: 80, 13: 169, 14: 145, 15: 121, 16: 152, 17: 48, 18: 240, 19: 81, 20: 66,
    21: 230, 22: 176, 23: 154, 24: 5, 25: 111, 26: 207, 27: 220, 28: 138, 29: 260, 30: 207,
    31: 272, 32: 385, 33: 17, 34: 675, 35: 895, 36: 721, 37: 821, 38: 1158, 39: 1064, 40: 616,
    41: 660, 42: 282, 43: 1204, 44: 1150, 45: 1256, 46: 1152, 47: 558, 48: 1850, 49: 3847, 50: 1252,
    51: 1275, 52: 1695, 53: 1016, 54: 3640, 55: 3736, 56: 1880, 57: 1232, 58: 3280, 59: 3350, 60: 3164,
    61: 6530, 62: 1864, 63: 12688, 64: 13188, 65: 9952, 66: 6776, 67: 2984, 68: 5628, 69: 6120, 70: 3784,
    71: 6816, 72: 6328, 73: 11256, 74: 7532, 75: 18580, 76: 6240, 77: 20048, 78: 17724, 79: 15006, 80: 16656,
    81: 18984, 82: 18816, 83: 13248, 84: 31640, 85: 33312, 86: 22820, 87: 66624, 88: 51118, 89: 37632, 90: 2448,
    91: 29384, 92: 72784, 93: 36536, 94: 118920, 95: 42740, 96: 124576, 97: 49312, 98: 169760, 99: 14688, 100: 55760
}

def calculate_round_pop_cash(round_num):
    """Calculates cash earned purely from popping bloons during round_num."""
    rbe = ROUND_RBE.get(round_num, 100)
    if round_num <= 50:
        pop_mult = 1.0
    elif round_num <= 60:
        pop_mult = 0.5
    elif round_num <= 85:
        pop_mult = 0.2
    else:
        pop_mult = 0.1
    return int(rbe * pop_mult)

def calculate_round_income(round_num):
    """Calculates official total cash awarded by a completed round (pop cash + end bonus)."""
    pop_cash = calculate_round_pop_cash(round_num)
    end_bonus = 100 + round_num
    return pop_cash + end_bonus

# Precompute standard round incomes (R1 to R100)
ROUND_INCOME_TABLE = {r: calculate_round_income(r) for r in range(1, 101)}

# Starting cash by difficulty
STARTING_CASH = {
    "Easy": 650,
    "Medium": 650,
    "Hard": 650,       # Starts on Round 3 with $650
    "Impoppable": 650,
    "CHIMPS": 650
}

def get_starting_cash(difficulty="Medium", monkey_knowledge=False, more_starting_cash=None):
    """
    Returns starting cash for difficulty, factoring in the 'More Cash'
    Primary Monkey Knowledge perk (+$200 starting cash in non-CHIMPS modes).
    Accepts explicit more_starting_cash flag or general monkey_knowledge flag.
    """
    base = STARTING_CASH.get(difficulty, 650)
    has_more_cash = more_starting_cash if more_starting_cash is not None else monkey_knowledge
    if has_more_cash and difficulty != "CHIMPS":
        return base + 200
    return base

def get_cumulative_cash_ceiling(difficulty, round_num, monkey_knowledge=False, more_starting_cash=None):
    """
    Returns the maximum realistic cumulative cash earned by the END of round_num,
    including starting cash (with optional Monkey Knowledge).
    """
    start_round = 3 if difficulty == "Hard" else 1
    starting_cash = get_starting_cash(difficulty, monkey_knowledge=monkey_knowledge, more_starting_cash=more_starting_cash)
    if round_num < start_round:
        return starting_cash

    cash = starting_cash
    for r in range(start_round, round_num + 1):
        cash += ROUND_INCOME_TABLE.get(r, 0)
    return cash

def get_cash_available(difficulty, round_num, timing="before_round", monkey_knowledge=False, more_starting_cash=None):
    """
    Returns cash available at a given round based on action timing:
    - 'before_round' (default): cash available from starting cash plus rounds completed prior to round_num.
    - 'during_round': cash available prior to round_num plus pop cash earned during round_num (no end-of-round bonus).
    - 'after_round': cash available after round_num completes, including its end-of-round bonus.
    - 'monkey_knowledge': optional boolean factoring in 'More Cash' perk (+$200 starting cash).
    - 'more_starting_cash': optional explicit boolean for the +$200 starting cash perk.
    """
    start_round = 3 if difficulty == "Hard" else 1
    starting_cash = get_starting_cash(difficulty, monkey_knowledge=monkey_knowledge, more_starting_cash=more_starting_cash)
    if round_num < start_round:
        return starting_cash

    cash = starting_cash
    for r in range(start_round, round_num):
        cash += ROUND_INCOME_TABLE.get(r, 0)

    if timing == "during_round":
        cash += calculate_round_pop_cash(round_num)
    elif timing == "after_round":
        cash += ROUND_INCOME_TABLE.get(round_num, 0)

    return cash

def get_earliest_affordable_round(difficulty, cumulative_cost, max_round=100, timing="before_round", monkey_knowledge=False):
    """
    Returns the earliest round by which cumulative_cost can realistically be afforded.
    If the cost cannot be afforded by max_round, returns None (explicit failure).
    """
    if not is_valid_numeric_cost(cumulative_cost):
        return None

    start_round = 3 if difficulty == "Hard" else 1
    starting_cash = get_starting_cash(difficulty, monkey_knowledge=monkey_knowledge)
    if cumulative_cost <= starting_cash:
        return start_round

    for r in range(start_round, max_round + 1):
        cash = get_cash_available(difficulty, r, timing=timing, monkey_knowledge=monkey_knowledge)
        if cash >= cumulative_cost:
            return r
    return None


# ==============================================================================
# 3. UPGRADE PARSING & CROSSPATH VALIDATION
# ==============================================================================
UPGRADE_REGEX = re.compile(r"^(\d)-(\d)-(\d)$")

def parse_upgrade(upg_str):
    """Parses an upgrade string like '3-0-2' into an integer tuple (3, 0, 2)."""
    if not upg_str or upg_str in ("Various", "None"):
        return None
    m = UPGRADE_REGEX.match(upg_str.strip())
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None

def is_legal_crosspath(upg):
    """
    Checks if an upgrade tuple or string is legal in BTD6:
    - Path tiers in 0..5
    - At most two paths upgraded (> 0)
    - At most one path upgraded beyond Tier 2 (> 2)
    """
    if upg is None:
        return True
    if isinstance(upg, str):
        if upg in ("Various", "None"):
            return True
        upg = parse_upgrade(upg)
        if upg is None:
            return False

    top, mid, bot = upg
    if any(p < 0 or p > 5 for p in (top, mid, bot)):
        return False

    non_zeros = sum(1 for p in (top, mid, bot) if p > 0)
    if non_zeros > 2:
        return False

    greater_than_2 = sum(1 for p in (top, mid, bot) if p > 2)
    if greater_than_2 > 1:
        return False

    return True


# ==============================================================================
# 4. STRUCTURED TACTICAL CAPABILITY RULES
# ==============================================================================
def get_hero_level_at_round(hero_name, placed_round, current_round):
    """
    Calculates estimated hero level based strictly on when the hero was placed
    and how many rounds the hero has been active on the board.
    """
    if placed_round is None or current_round < placed_round:
        return 0
    rounds_active = current_round - placed_round
    # Standard hero leveling gives ~1 level every 3 rounds
    return max(1, min(20, 1 + rounds_active // 3))

def get_tower_capabilities(tower_name, upg_tuple, hero_level=None):
    """
    Evaluates exact tactical popping capabilities for a tower instance.
    Returns: dict(camo, lead, moab_damage, bfb_damage, zomg_damage, ceramic_cc, grants_camo, grants_lead)
    """
    top, mid, bot = upg_tuple if upg_tuple else (0, 0, 0)
    t_name = tower_name.strip()

    camo = False
    lead = False
    moab = False
    bfb = False
    zomg = False
    ceramic = False
    grants_camo = False
    grants_lead = False

    # 1. Heroes
    if t_name == "Sauda":
        camo = True # Innate Camo from Lv1
        if hero_level is not None and hero_level >= 7:
            lead = True
        if hero_level is not None and hero_level >= 3:
            moab = True # Leaping Sword
        if hero_level is not None and hero_level >= 10:
            ceramic = True
            bfb = True
        if hero_level is not None and hero_level >= 15:
            zomg = True
    elif t_name == "Quincy":
        if hero_level is not None and hero_level >= 5:
            camo = True
        if hero_level is not None and hero_level >= 7:
            lead = True
        if hero_level is not None and hero_level >= 3:
            moab = True
        if hero_level is not None and hero_level >= 10:
            ceramic = True
            bfb = True
        if hero_level is not None and hero_level >= 15:
            zomg = True
    elif t_name == "Gwendolin":
        lead = True # Innate Lead from Lv1
        moab = True
        if hero_level is not None and hero_level >= 10:
            ceramic = True
            bfb = True
        if hero_level is not None and hero_level >= 16:
            zomg = True
    elif t_name == "Obyn Greenfoot":
        lead = True # Innate magic pops leads
        moab = True
        ceramic = True
        if hero_level is not None and hero_level >= 10:
            bfb = True
    elif t_name == "Striker Jones":
        lead = True
        moab = True
        ceramic = True
        if hero_level is not None and hero_level >= 10:
            bfb = True
    elif t_name == "Etienne":
        camo = True
        if hero_level is not None and hero_level >= 8:
            grants_camo = True # UAV Global Camo buff
        if hero_level is not None and hero_level >= 10:
            moab = True
            bfb = True
            ceramic = True
    elif t_name == "Admiral Brickell":
        camo = True
        lead = True # Sea mines pop leads
        moab = True
        ceramic = True
        if hero_level is not None and hero_level >= 10:
            bfb = True
            zomg = True
    elif t_name == "Psi":
        camo = True
        lead = True
        moab = True
        ceramic = True
        if hero_level is not None and hero_level >= 14:
            bfb = True
        if hero_level is not None and hero_level >= 20:
            zomg = True
    elif t_name in ("Captain Churchill", "Churchill"):
        lead = True # Innate explosive shells
        if hero_level is not None and hero_level >= 3:
            moab = True
            ceramic = True
        if hero_level is not None and hero_level >= 6:
            camo = True
        if hero_level is not None and hero_level >= 10:
            bfb = True
            zomg = True
    elif t_name == "Benjamin":
        if hero_level is not None and hero_level >= 7:
            moab = True # Bloon Trojan removes blimp child spawns
        if hero_level is not None and hero_level >= 10:
            bfb = True # Syphon Funding blimp downgrade
    elif t_name == "Ezili":
        camo = True # Innate Camo detection
        if hero_level is not None and hero_level >= 4:
            lead = True
        if hero_level is not None and hero_level >= 10:
            moab = True
            bfb = True
            zomg = True # MOAB Hex obliterates blimps
    elif t_name == "Pat Fusty":
        if hero_level is not None and hero_level >= 2:
            lead = True
            ceramic = True
        if hero_level is not None and hero_level >= 3:
            moab = True
        if hero_level is not None and hero_level >= 10:
            bfb = True # Big Squeeze
    elif t_name == "Adora":
        if hero_level is not None and hero_level >= 3:
            lead = True # Long Arm of Light
        if hero_level is not None and hero_level >= 10:
            moab = True
            ceramic = True
            bfb = True
        if hero_level is not None and hero_level >= 20:
            zomg = True
    elif t_name == "Geraldo":
        camo = True # Camo potion
        lead = True # Nails, turrets, sharpening
        if hero_level is not None and hero_level >= 8:
            moab = True
            ceramic = True # Gerry's Fire
        if hero_level is not None and hero_level >= 10:
            bfb = True
            zomg = True
    elif t_name == "Corvus":
        camo = True
        lead = True
        if hero_level is not None and hero_level >= 5:
            ceramic = True
            moab = True
        if hero_level is not None and hero_level >= 10:
            bfb = True
            zomg = True
    elif t_name == "Rosalia":
        lead = True
        if hero_level is not None and hero_level >= 3:
            ceramic = True # Scatter Grenade
        if hero_level is not None and hero_level >= 10:
            moab = True
            bfb = True # Anti-Bloon Missile

    # 2. Primary Towers
    elif t_name == "Dart Monkey":
        if bot >= 2: # Enhanced Eyesight / Crossbow
            camo = True
        if bot >= 4: # Sharpshooter / Crossbow Master
            moab = True
            bfb = (bot >= 5)
            lead = (bot >= 5)
            zomg = (bot >= 5)
        if top >= 4: # Juggernaut
            lead = True
            ceramic = True
            if top >= 5: # Ultra-Juggernaut
                moab = True
                bfb = True

    elif t_name == "Boomerang Monkey":
        if mid >= 2: # Red Hot 'Rangs
            lead = True
        if bot >= 4: # MOAB Press
            moab = True
            bfb = True
            zomg = (bot >= 5)
        if top >= 4: # Glaive Ricochet / More Glaives
            ceramic = True

    elif t_name == "Bomb Shooter":
        lead = True # Innate Lead popping
        if mid >= 3: # MOAB Mauler (0-3-0+) / MOAB Assassin (0-4-0)
            moab = True
            bfb = (mid >= 4)
            zomg = (mid >= 5) # MOAB Eliminator
        if bot >= 4: # Recursive Cluster (2-0-4)
            ceramic = True
            moab = True
            bfb = (bot >= 5)
        if top >= 4: # Bloon Impact
            ceramic = True
            if top >= 5: # Bloon Crush
                bfb = True
                zomg = True

    elif t_name == "Tack Shooter":
        if top >= 4: # Ring of Fire (4-0-0)
            lead = True
            ceramic = True
            moab = True
            bfb = (top >= 5)
            zomg = (top >= 5)
        if bot >= 4: # Overdrive (2-0-4)
            moab = True
            bfb = True
            zomg = (bot >= 5) # The Tack Zone
        if mid >= 4: # Blade Maelstrom
            ceramic = True

    elif t_name == "Ice Monkey":
        if mid >= 2 or bot >= 2:
            lead = (mid >= 3 or top >= 4)
        if top >= 4: # Embrittlement (detects/removes camo!)
            camo = True
            lead = True
            moab = True
            bfb = True
        if bot >= 4: # Icicles / Icicle Impale
            ceramic = True
            moab = True
            bfb = True
            zomg = (bot >= 5)

    elif t_name == "Glue Gunner":
        if top >= 2: # Corrosive Glue
            lead = True
        if top >= 3: # Bloon Dissolver
            ceramic = True
        if bot >= 3: # MOAB Glue (0-2-3 / 0-2-4 Relentless Glue)
            moab = True
            bfb = (bot >= 4)
            ceramic = (bot >= 4)
            zomg = (bot >= 5)

    # 3. Military Towers
    elif t_name == "Sniper Monkey":
        if mid >= 2: # Night Vision Goggles
            camo = True
        if top >= 1: # Full Metal Jacket
            lead = True
        if top >= 3: # Deadly Precision / Maim MOAB
            moab = True
            lead = True
            bfb = (top >= 4)
            zomg = (top >= 5)
        if bot >= 3: # Semi-Automatic / Bouncing Bullet
            ceramic = True
            moab = True
            bfb = (bot >= 4)

    elif t_name == "Monkey Sub":
        if top >= 2: # Advanced Intel (with sight)
            camo = True
        if top >= 3: # Submerge & Support (decamo!)
            camo = True
            grants_camo = True
        if bot >= 3: # Triple Guns / AP Darts / Sub Commander
            moab = True
            ceramic = True
            bfb = (bot >= 4)
            zomg = (bot >= 5)
        if mid >= 3: # Ballistic Missile (pops leads!)
            lead = True
            moab = True
            bfb = (mid >= 4)
            zomg = (mid >= 4) # First Strike kills ZOMGs instantly

    elif t_name == "Monkey Buccaneer":
        if mid >= 2: # Hot Shot (pops leads)
            lead = True
        if bot >= 2: # Crow's Nest
            camo = True
        if top >= 3: # Destroyer (3-2-0) / Aircraft Carrier
            moab = True
            ceramic = True
            bfb = (top >= 4)
            zomg = (top >= 5)
        if mid >= 4: # Monkey Pirates (harpoon)
            moab = True
            bfb = True
            zomg = (mid >= 5) # Pirate Lord

    elif t_name == "Monkey Ace":
        if mid >= 2: # Spy Plane
            camo = True
        if top >= 3: # Fighter Plane (missiles)
            lead = True
            moab = True
            bfb = (top >= 4)
            zomg = (top >= 5)
        if bot >= 3: # Bomber Ace / Operation Dart Storm
            ceramic = True
            moab = True
            bfb = (bot >= 4)

    elif t_name == "Heli Pilot":
        if bot >= 2: # IFR
            camo = True
        if top >= 3: # Apache Dartship
            moab = True
            bfb = True
            lead = (top >= 4)
            zomg = (top >= 5)
        if mid >= 3: # Downdraft
            ceramic = True

    elif t_name == "Mortar Monkey":
        lead = True # Innate explosive Lead popping
        if mid >= 3: # Heavy Shells
            moab = True
            bfb = (mid >= 4)
        if bot >= 3: # Signal Flare (decamo!)
            camo = True
            grants_camo = True
        if top >= 3: # Shell Shock / The Big One
            ceramic = True
            moab = (top >= 4)
            bfb = (top >= 5)

    elif t_name == "Dartling Gunner":
        if mid >= 2: # Focused Firing / Advanced Targeting
            camo = (mid >= 2)
        if top >= 3: # Laser Cannon
            lead = True
        if mid >= 3: # Hydra Rocket Pods
            lead = True
            moab = True
            bfb = (mid >= 4)
            zomg = (mid >= 5)

    # 4. Magic Towers
    elif t_name == "Wizard Monkey":
        if bot >= 2: # Monkey Sense
            camo = True
        if mid >= 1: # Fireball / Wall of Fire
            lead = True
        if top >= 3: # Arcane Mastery / Archmage
            moab = True
            bfb = (top >= 4)
            zomg = (top >= 5)
            lead = (top >= 4)
        if bot >= 4: # Necromancer / Prince of Darkness
            ceramic = True
            moab = True
            bfb = True
            camo = True
            lead = True
            zomg = (bot >= 5)

    elif t_name == "Super Monkey":
        if mid >= 2: # Epic Range / Ultravision
            camo = True
        if top >= 2: # Plasma Blasts
            lead = True
        if top >= 3 or mid >= 3 or bot >= 3: # Sun Avatar / Robo Monkey / Dark Knight
            moab = True
            ceramic = True
            bfb = True
            zomg = (top >= 4 or mid >= 4 or bot >= 4)
        if bot >= 3: # Dark Knight (Plasma blades pop Lead)
            lead = True

    elif t_name == "Ninja Monkey":
        camo = True # Innate Camo detection
        if bot >= 3: # Flash Bomb
            lead = True
        if top >= 3: # Double Shot / Bloonjitsu (4-0-1)
            ceramic = True
            moab = True
            bfb = (top >= 4)
            zomg = (top >= 5)
        if mid >= 4: # Bloon Sabotage
            moab = True
            bfb = True
            zomg = True

    elif t_name == "Alchemist":
        if top >= 2: # Acidic Mixture Dip
            lead = True
            grants_lead = True
        if top >= 3: # Berserker Brew / Stronger Stimulant
            moab = True # Massive damage and pierce buff to nearby towers
            bfb = True
            ceramic = True
            lead = True
            grants_lead = True

    elif t_name == "Druid":
        if top >= 1: # Hard Thorns
            lead = True
        if top >= 4: # Ball Lightning
            ceramic = True
        if bot >= 3: # Druid of Wrath / Poplust
            moab = True
            bfb = (bot >= 4)

    # 5. Support Towers
    elif t_name == "Monkey Village":
        if mid >= 2: # Radar Scanner (grants Camo to all towers in radius!)
            camo = True
            grants_camo = True
        if mid >= 3: # MIB (Monkey Intelligence Bureau - pops all types!)
            lead = True
            grants_lead = True

    elif t_name == "Spike Factory":
        if top >= 2: # White Hot Spikes
            lead = True
        if bot >= 3: # Spike Storm / Deadly Spikes
            moab = True
            bfb = (bot >= 4)
            zomg = (bot >= 5)
            ceramic = True

    elif t_name == "Engineer Monkey":
        if mid >= 2: # Cleansing Foam (decamo & delead)
            camo = True
            lead = True
            grants_camo = True
        if top >= 4: # Sentry Expert
            lead = True
            moab = True
        if top >= 5: # Sentry Champion
            ceramic = True
            bfb = True
            zomg = True
        if mid >= 4: # Overclock
            moab = True
            bfb = True
        if bot >= 4: # Bloon Trap
            ceramic = True
        if bot >= 5: # XXL Trap
            bfb = True
            zomg = True

    elif t_name == "Beast Handler":
        if mid >= 3: # Horned Owl
            camo = True
        if bot >= 3: # Adasaurus
            lead = True
        if top >= 2: # Great White
            moab = True
        if top >= 4: # Orca
            bfb = True
            ceramic = True
        if top >= 5: # Megalodon
            zomg = True
        if mid >= 4: # Golden Eagle
            ceramic = True
            moab = True
        if bot >= 4: # Velociraptor
            ceramic = True
            moab = True
            bfb = True
        if bot >= 5: # Giganotosaurus
            zomg = True
            lead = True

    return {
        "camo": camo,
        "lead": lead,
        "moab_damage": moab,
        "bfb_damage": bfb,
        "zomg_damage": zomg,
        "ceramic_cc": ceramic,
        "grants_camo": grants_camo,
        "grants_lead": grants_lead
    }
