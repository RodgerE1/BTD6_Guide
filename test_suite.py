"""
test_suite.py
Comprehensive Regression Test Suite for the BTD6 Strategy Guide Application.
Exercises real application classes (DataManager, SettingsManager, export_printable_html)
and validates all 8 findings from the code review:
1. Shared validate_strategy() across editor, loader, validator, and replay engine.
2. Authoritative canonical pricing, rejecting NaN, booleans, and cost-zero tampering.
3. Timing-aware purchase validation (before_round vs during_round) and $1B unaffordability.
4. Robust malformed data diagnostics (null step, string round "8", null tower).
5. Radar and Replay agreement (orphan upgrades rejected, persistent tower tracking).
6. Tactical capability checks (blimp tiers, R63 ceramic CC, composite ability checks).
7. Accurate 70% sale refund tracking from recorded investments.
8. Real DataManager & SettingsManager persistence tests with injected write failures.
9. Actual HTML export sanitization with XSS payload verification.
10. 100% invariant satisfaction across all 87 maps in production guides.json.
"""

import unittest
from unittest.mock import patch
import os
import json
import tempfile
import html
import math

from btd6_economy import (
    is_legal_crosspath,
    parse_upgrade,
    get_cumulative_cash_ceiling,
    get_earliest_affordable_round,
    get_tower_capabilities,
    get_action_canonical_cost,
    is_valid_numeric_cost,
    CANONICAL_UPGRADES,
    DIFF_MULTIPLIERS,
    get_cash_available,
    calculate_round_pop_cash,
    calculate_round_income,
    get_starting_cash
)
from btd6_replay import (
    validate_strategy,
    validate_strategy_schema,
    TowerReplayEngine,
    TowerInstance,
    CANONICAL_HEROES,
    assign_explicit_tower_ids
)
from heroes_data import MAP_HERO_INTELLIGENCE, HEROES_DATABASE
from threat_radar_data import (
    check_strategy_defense_readiness,
    get_round_data
)
from validate_guides import validate_database
from btd6_guide import DataManager, SettingsManager, BTD6GuideApp


class TestCrosspathLegality(unittest.TestCase):
    def test_valid_crosspaths(self):
        valid = [
            "0-0-0", "5-2-0", "5-0-2", "0-5-2", "2-5-0", "0-2-5", "2-0-5",
            "4-2-0", "3-0-2", "0-3-2", "2-0-4", "1-0-0", "0-1-0", "0-0-1",
            "2-2-0", "0-2-2", "2-0-2", "Various", "None"
        ]
        for cp in valid:
            self.assertTrue(is_legal_crosspath(cp), f"Expected '{cp}' to be legal")

    def test_invalid_crosspaths(self):
        invalid = [
            "9-9-9",  # Absurd tier
            "5-3-0",  # Two paths > tier 2
            "3-3-3",  # Three paths upgraded
            "0-6-0",  # Tier > 5
            "3-0-3",  # Two paths > tier 2
            "1-1-1",  # Three paths upgraded
            "0-0-6",  # Tier > 5
            "-1-0-0", # Negative tier
            "invalid",
            ""
        ]
        for cp in invalid:
            self.assertFalse(is_legal_crosspath(cp), f"Expected '{cp}' to be illegal")


class TestEconomicModelAndAuthoritativePricing(unittest.TestCase):
    def test_starting_cash(self):
        self.assertEqual(get_cumulative_cash_ceiling("Easy", 0), 650)
        self.assertEqual(get_cumulative_cash_ceiling("Medium", 0), 650)
        self.assertEqual(get_cumulative_cash_ceiling("Hard", 2), 650)
        self.assertEqual(get_cumulative_cash_ceiling("Easy", 1), 771)

    def test_monotonically_increasing_cash(self):
        for diff in ("Easy", "Medium", "Hard"):
            start_r = 3 if diff == "Hard" else 1
            last_cash = 0
            for r in range(start_r, 81):
                cash = get_cumulative_cash_ceiling(diff, r)
                self.assertGreater(cash, last_cash, f"Cash ceiling regressed at R{r} on {diff}")
                last_cash = cash

    def test_earliest_affordable_round_finite_and_unaffordable(self):
        self.assertEqual(get_earliest_affordable_round("Easy", 500), 1)
        self.assertEqual(get_earliest_affordable_round("Hard", 500), 3)

        r_10k = get_earliest_affordable_round("Medium", 10000)
        self.assertGreaterEqual(r_10k, 30)
        self.assertLessEqual(r_10k, 40)

        # Finding 3: Requesting affordability for $1 billion must return None, not round 62 or 100
        r_unaffordable = get_earliest_affordable_round("Medium", 1_000_000_000, max_round=60)
        self.assertIsNone(r_unaffordable, "One billion dollars should not be affordable and must return None")

    def test_numeric_validation_rejects_nan_and_booleans(self):
        # Finding 2: Reject NaN and booleans
        self.assertFalse(is_valid_numeric_cost(float('nan')), "NaN cost must be rejected")
        self.assertFalse(is_valid_numeric_cost(float('inf')), "Infinite cost must be rejected")
        self.assertFalse(is_valid_numeric_cost(True), "Boolean True must not be treated as a valid number")
        self.assertFalse(is_valid_numeric_cost(False), "Boolean False must not be treated as a valid number")
        self.assertFalse(is_valid_numeric_cost(-50), "Negative numbers must be rejected")
        self.assertTrue(is_valid_numeric_cost(425), "Valid positive integer must be accepted")
        self.assertTrue(is_valid_numeric_cost(0), "Zero must be accepted")

    def test_canonical_upgrade_costs(self):
        # Buccaneer 0-2-0 -> 3-2-0 on Easy
        # Top path tier 1 ($425) + tier 2 ($550) + tier 3 ($2510) = $3485
        cost = get_action_canonical_cost("Monkey Buccaneer", (0, 2, 0), (3, 2, 0), "Upgrade", "Easy")
        self.assertEqual(cost, 3485, "Multi-tier upgrade 0-2-0 -> 3-2-0 must include all purchased intermediate tiers")


class TestThreatRadarIntegrityAndAgreement(unittest.TestCase):
    def test_invented_tower_not_moab_ready(self):
        caps = get_tower_capabilities("Invented Plasma Catapult", (0, 4, 0))
        self.assertFalse(caps["moab_damage"], "Invented tower with 0-4-0 must NOT report MOAB-ready")
        self.assertFalse(caps["camo"], "Invented tower must NOT report Camo-ready")

    def test_orphan_upgrade_rejected_by_radar(self):
        # Finding 5: A strategy containing ONLY an upgrade to Bomb Shooter 0-3-0
        # without placement must NOT report Lead-ready or MOAB-ready!
        steps = [
            {"step_number": 1, "round": 10, "action": "Upgrade", "tower": "Bomb Shooter", "upgrade": "0-3-0"}
        ]
        readiness = check_strategy_defense_readiness(28, steps)
        self.assertFalse(readiness["lead_ready"], "Orphan upgrade without placement must NOT report Lead-ready")
        readiness_40 = check_strategy_defense_readiness(40, steps)
        self.assertFalse(readiness_40["moab_ready"], "Orphan upgrade without placement must NOT report MOAB-ready")

    def test_hero_arrival_round_affects_level(self):
        # Finding 6: Hero arrival round determines capability
        # Sauda placed R1 is level >= 7 by R40 (has Lead & Camo)
        steps_early = [{"step_number": 1, "round": 1, "action": "Place", "tower": "Sauda", "upgrade": "0-0-0"}]
        readiness_early = check_strategy_defense_readiness(28, steps_early)
        self.assertTrue(readiness_early["lead_ready"], "Sauda placed R1 reaches level 3+ before R28 to pop Lead")

        # Sauda placed on R35 is only level 1-2 on R37 and cannot pop Lead
        steps_late = [{"step_number": 1, "round": 35, "action": "Place", "tower": "Sauda", "upgrade": "0-0-0"}]
        readiness_late = check_strategy_defense_readiness(37, steps_late)
        self.assertFalse(readiness_late["lead_ready"], "Sauda placed late on R35 cannot pop Lead on R37")


class TestValidationEngineRejection(unittest.TestCase):
    def setUp(self):
        self.valid_map = {
            "id": "test_map",
            "name": "Test Map",
            "category": "Beginner",
            "terrain": "Grass",
            "lanes": "Single",
            "water": False,
            "sight_blockers": False,
            "gimmick": "None",
            "difficulties": {
                "Easy": {
                    "difficulty": "Easy",
                    "mode": "Standard",
                    "rounds": "1-40",
                    "status": "Structurally Validated",
                    "recommended_hero": "Sauda",
                    "hero_alternatives": ["Quincy"],
                    "starting_cash": 650,
                    "overview": "Overview text.",
                    "camo_handling": "Camo text.",
                    "lead_handling": "Lead text.",
                    "moab_handling": "MOAB text.",
                    "why_it_works": "Why text.",
                    "research_sources": ["Wiki"],
                    "steps": [
                        {"step_number": 1, "step_id": "s1", "round_range": "R1-10", "round": 1, "action": "Place", "tower": "Sauda", "upgrade": "0-0-0", "placement": "A", "targeting": "First", "cost_estimate": 510, "details": "d", "timing": "before_round"},
                        {"step_number": 2, "step_id": "s2", "round_range": "R1-10", "round": 6, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "placement": "B", "targeting": "First", "cost_estimate": 170, "details": "d", "timing": "before_round"},
                        {"step_number": 3, "step_id": "s3", "round_range": "R11-20", "round": 12, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-2-2", "placement": "B", "targeting": "First", "cost_estimate": 350, "details": "d", "timing": "before_round"},
                        {"step_number": 4, "step_id": "s4", "round_range": "R21-30", "round": 22, "action": "Place", "tower": "Bomb Shooter", "upgrade": "2-0-3", "placement": "C", "targeting": "Close", "cost_estimate": 2500, "details": "d", "timing": "before_round"},
                        {"step_number": 5, "step_id": "s5", "round_range": "R31-40", "round": 35, "action": "Place", "tower": "Bomb Shooter", "upgrade": "0-3-2", "placement": "D", "targeting": "Strong", "cost_estimate": 2040, "details": "d", "timing": "before_round"}
                    ]
                },
                "Medium": None,
                "Hard": None
            }
        }

    def test_catches_illegal_crosspath_999(self):
        mutated = json.loads(json.dumps(self.valid_map))
        mutated["difficulties"]["Easy"]["steps"][1]["tower"] = "Banana Farm"
        mutated["difficulties"]["Easy"]["steps"][1]["upgrade"] = "9-9-9"

        ok, errs, _, _ = validate_strategy(mutated["difficulties"]["Easy"], map_context=mutated, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("illegal crosspath '9-9-9'" in err for err in errs))

    def test_catches_one_million_dollar_purchase(self):
        mutated = json.loads(json.dumps(self.valid_map))
        mutated["difficulties"]["Easy"]["steps"][3]["cost_estimate"] = 1000000

        ok, errs, _, _ = validate_strategy(mutated["difficulties"]["Easy"], map_context=mutated, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("exceeds max available cash" in err for err in errs))

    def test_cost_zero_tampering_prevented_by_canonical_pricing(self):
        # Finding 2: Tampering all step cost_estimate to 0 must NOT bypass economic cash ceiling
        # Let's insert a $20,000 Super Monkey upgrade on Round 6 with cost_estimate: 0
        mutated = json.loads(json.dumps(self.valid_map))
        mutated["difficulties"]["Easy"]["steps"].insert(2, {
            "step_number": 20, "round": 6, "action": "Place", "tower": "Super Monkey",
            "upgrade": "3-0-0", "placement": "Center", "targeting": "First",
            "cost_estimate": 0, "details": "tampered free super monkey", "timing": "before_round"
        })
        ok, errs, _, _ = validate_strategy(mutated["difficulties"]["Easy"], map_context=mutated, diff_name="Easy")
        self.assertFalse(ok, "Validation must calculate canonical purchase cost and reject unaffordable Super Monkey on R6")
        self.assertTrue(any("exceeds max available cash" in err for err in errs))

    def test_catches_excessive_opening_cost(self):
        mutated = json.loads(json.dumps(self.valid_map))
        mutated["difficulties"]["Easy"]["steps"][0]["cost_estimate"] = 700

        ok, errs, _, _ = validate_strategy(mutated["difficulties"]["Easy"], map_context=mutated, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("exceeds $650 starting cash" in err for err in errs))

    def test_catches_downgrade_attempt(self):
        mutated = json.loads(json.dumps(self.valid_map))
        mutated["difficulties"]["Easy"]["steps"][2]["upgrade"] = "0-2-0"
        mutated["difficulties"]["Easy"]["steps"].append({
            "step_number": 6, "round": 38,
            "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-1-0",
            "placement": "B", "targeting": "First", "cost_estimate": 100, "details": "d",
            "timing": "before_round"
        })
        ok, errs, _, _ = validate_strategy(mutated["difficulties"]["Easy"], map_context=mutated, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("drops levels" in err for err in errs))

    def test_malformed_data_diagnostics_without_crashing(self):
        # Finding 4: Null step, string round "8", null tower produce diagnostics rather than crashing
        strat = json.loads(json.dumps(self.valid_map["difficulties"]["Easy"]))

        # 1. Null step
        strat["steps"][1] = None
        ok, errs, _, _ = validate_strategy(strat, map_context=self.valid_map, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("steps[1] must be a JSON dictionary object" in err for err in errs))

        # 2. String round "8"
        strat["steps"][1] = {"step_number": 2, "round": "8", "action": "Place", "tower": "Dart Monkey"}
        ok, errs, _, _ = validate_strategy(strat, map_context=self.valid_map, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("must be an integer" in err for err in errs))

        # 3. Null tower
        strat["steps"][1] = {"step_number": 2, "round": 8, "action": "Place", "tower": None}
        ok, errs, _, _ = validate_strategy(strat, map_context=self.valid_map, diff_name="Easy")
        self.assertFalse(ok)
        self.assertTrue(any("must be a non-empty string" in err for err in errs))

    def test_sale_70_percent_refund_tracking(self):
        # Finding 7: Selling a tower refunds 70% of accumulated recorded investment
        eng = TowerReplayEngine(difficulty="Easy")
        # Place Dart Monkey ($170 on Easy)
        s1 = {"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0"}
        eng.apply_step(s1, 1)

        # Upgrade Dart Monkey to 0-2-3 ($970 upgrade on Easy)
        # Total invested: $170 + $970 = $1,140
        s2 = {"step_number": 2, "round": 10, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-2-3"}
        eng.apply_step(s2, 2)

        inst = list(eng.active_towers.values())[0]
        self.assertEqual(inst.total_invested, 1140)

        # Sell Dart Monkey
        s3 = {"step_number": 3, "round": 15, "action": "Sell", "tower": "Dart Monkey", "cost_estimate": 0}
        ok, err = eng.apply_step(s3, 3)
        self.assertTrue(ok)
        expected_refund = int(round(1140 * 0.70))  # 798
        self.assertEqual(eng.cumulative_refunds, expected_refund)

    def test_ability_validation_rejects_imaginary_weapon(self):
        # Finding 6: Imaginary Hero Weapon without hero or tower must be rejected
        eng = TowerReplayEngine(difficulty="Easy")
        step = {"step_number": 1, "round": 10, "action": "Ability", "tower": "Imaginary Hero Weapon"}
        ok, err = eng.apply_step(step, 1)
        self.assertFalse(ok)
        self.assertIn("references unplaced or unavailable", err)


class TestDataManager(unittest.TestCase):
    def test_datamanager_save_and_overrides(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = os.path.join(tmp_dir, "guides.json")
            ov_path = os.path.join(tmp_dir, "user_overrides.json")

            valid_strat = {
                "difficulty": "Easy",
                "mode": "Standard",
                "rounds": "1-40",
                "status": "Verified",
                "recommended_hero": "Sauda",
                "starting_cash": 650,
                "overview": "Overview text.",
                "camo_handling": "Camo text.",
                "lead_handling": "Lead text.",
                "moab_handling": "MOAB text.",
                "why_it_works": "Why text.",
                "steps": [
                    {"step_number": 1, "step_id": "mm_s1", "round": 1, "action": "Place", "tower": "Sauda", "upgrade": "0-0-0", "timing": "before_round"},
                    {"step_number": 2, "step_id": "mm_s2", "round": 6, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"},
                    {"step_number": 3, "step_id": "mm_s3", "round": 12, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-2-2", "timing": "before_round"},
                    {"step_number": 4, "step_id": "mm_s4", "round": 22, "action": "Place", "tower": "Bomb Shooter", "upgrade": "2-0-3", "timing": "before_round"},
                    {"step_number": 5, "step_id": "mm_s5", "round": 35, "action": "Place", "tower": "Bomb Shooter", "upgrade": "0-3-2", "timing": "before_round"}
                ]
            }
            init_data = {
                "version": "1.3.0",
                "maps": {
                    "monkey_meadow": {
                        "name": "Monkey Meadow",
                        "difficulties": {
                            "Easy": valid_strat
                        }
                    }
                }
            }
            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(init_data, f)

            dm = DataManager(filepath=db_path, show_dialogs=False)
            dm.overrides_filepath = ov_path

            # Save override
            import copy
            edited_strat = copy.deepcopy(valid_strat)
            edited_strat["status"] = "Playtested"
            saved = dm.save_override("monkey_meadow", "Easy", edited_strat)
            self.assertTrue(saved)
            self.assertTrue(os.path.exists(ov_path))

            # Reload and verify override merged
            dm2 = DataManager(filepath=db_path, show_dialogs=False)
            dm2.overrides_filepath = ov_path
            dm2.load()
            strat = dm2.get_map("monkey_meadow")["difficulties"]["Easy"]
            self.assertEqual(strat["status"], "Playtested")

    def test_datamanager_handles_write_failure(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = os.path.join(tmp_dir, "guides.json")
            with open(db_path, "w", encoding="utf-8") as f:
                json.dump({"maps": {}}, f)

            dm = DataManager(filepath=db_path, show_dialogs=False)
            # Inject write failure by replacing os.replace with an exception
            with patch("os.replace", side_effect=OSError("Disk write error")):
                res = dm.save()
                self.assertFalse(res, "DataManager.save() must return False on write failure")
                self.assertIsNotNone(dm.last_save_error)


class TestSettingsManager(unittest.TestCase):
    def test_settings_save_and_step_id_progress(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "settings.json")
            sm = SettingsManager(filepath=set_path)

            # Test progress keying by step_id across difficulties
            sm.set_step_progress("monkey_meadow", "monkey_meadow_easy_s1", True, diff="Easy")
            sm.set_step_progress("monkey_meadow", "monkey_meadow_easy_s2", True, diff="Easy")

            easy_prog = sm.get_progress("monkey_meadow", diff="Easy")
            med_prog = sm.get_progress("monkey_meadow", diff="Medium")
            hard_prog = sm.get_progress("monkey_meadow", diff="Hard")

            self.assertEqual(easy_prog, {"monkey_meadow_easy_s1", "monkey_meadow_easy_s2"})
            self.assertEqual(med_prog, set(), "Medium progress must be isolated from Easy")
            self.assertEqual(hard_prog, set(), "Hard progress must be isolated from Easy")

    def test_settings_handles_write_failure(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "settings.json")
            sm = SettingsManager(filepath=set_path)
            with patch("os.replace", side_effect=OSError("Write permission denied")):
                res = sm.save()
                self.assertFalse(res, "SettingsManager.save() must return False on failure")
                self.assertIsNotNone(sm.last_save_error)


class TestHTMLExportSanitization(unittest.TestCase):
    def test_actual_html_export_escapes_xss_payload(self):
        # Verify export_printable_html sanitizes malicious inputs in actual generated files
        malicious_map = {
            "name": "Map <script>alert('map_xss')</script>",
            "category": "Beginner",
            "terrain": "Grass & <iframe src='evil.com'></iframe>",
            "lanes": "Single Lane",
            "water": False
        }
        malicious_strat = {
            "difficulty": "Easy",
            "rounds": "1-40",
            "status": "Verified",
            "recommended_hero": "Sauda <img src=x onerror=alert(1)>",
            "overview": "Overview with <style>body{display:none}</style>",
            "camo_handling": "Camo <script>x=1</script>",
            "lead_handling": "Lead & bloons",
            "moab_handling": "MOAB <svg onload=alert(2)>",
            "why_it_works": "Why <a href='javascript:alert(3)'>click</a>",
            "steps": [
                {
                    "step_number": 1,
                    "round": 1,
                    "action": "Place",
                    "tower": "Dart <script>evil()</script>",
                    "upgrade": "0-0-0",
                    "targeting": "First",
                    "cost_estimate": 170,
                    "placement": "Near <script>track</script>",
                    "details": "Details & <img onerror=hack() src='bad'>"
                }
            ]
        }

        # Initialize mock Tk app headlessly
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_file = os.path.join(tmp_dir, "test_export.html")
            with patch("webbrowser.open"), patch("tkinter.messagebox.showinfo"), patch("tkinter.messagebox.showerror"):
                # Call export_printable_html logic directly
                app = BTD6GuideApp.__new__(BTD6GuideApp)
                app.data_manager = DataManager(show_dialogs=False)
                app.get_current_map_id = lambda: "test_map"

                # We patch os.path.join to write to our tmp directory
                orig_join = os.path.join
                def custom_join(*args):
                    if len(args) == 2 and args[1].endswith(".html"):
                        return out_file
                    return orig_join(*args)

                with patch("os.path.join", side_effect=custom_join):
                    app.export_printable_html(strat=malicious_strat, map_data=malicious_map)

                self.assertTrue(os.path.exists(out_file), "Exported HTML file must be created")
                with open(out_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Verify all script tags and payloads were HTML-escaped
                self.assertNotIn("<script>", content)
                self.assertIn("&lt;script&gt;alert(&#x27;map_xss&#x27;)&lt;/script&gt;", content)
                self.assertNotIn("<iframe", content)
                self.assertIn("&lt;iframe", content)
                self.assertNotIn("<img src=x", content)
                self.assertIn("&lt;img src=x", content)
                self.assertNotIn("<style>body{display:none}</style>", content)
                self.assertIn("&lt;style&gt;body{display:none}&lt;/style&gt;", content)


class TestReviewFindingsAndHeroIntelligence(unittest.TestCase):
    """
    Direct regression tests for all 8 findings from Suggestions_for_Coding.txt
    and the comprehensive Map Hero Intelligence feature.
    """

    def test_item1_editor_draft_construction_and_save(self):
        """Finding 1: Editor constructs valid draft with starting_cash and mid, successfully saving changes."""
        dm = DataManager(show_dialogs=False)
        mdata = dm.get_map("monkey_meadow")
        self.assertIsNotNone(mdata)
        strat = mdata["difficulties"]["Easy"]

        # Simulate editor get_draft_strategy
        import copy
        draft = copy.deepcopy(strat)
        draft["overview"] = "Updated tactical overview for test."
        if "starting_cash" not in draft:
            draft["starting_cash"] = 650

        # Test validation of draft
        is_valid, errs, _, _ = validate_strategy(draft, map_context=mdata, diff_name="Easy")
        self.assertTrue(is_valid, f"Draft strategy must pass validation: {errs}")

        with tempfile.TemporaryDirectory() as tmp_dir:
            dm_test = DataManager(show_dialogs=False)
            dm_test.overrides_filepath = os.path.join(tmp_dir, "test_overrides.json")
            mid = "monkey_meadow"
            saved = dm_test.save_override(mid, "Easy", draft)
            self.assertTrue(saved, "save_override with mid must succeed")
            self.assertEqual(dm_test.database["maps"][mid]["difficulties"]["Easy"]["overview"], "Updated tactical overview for test.")

    def test_item2_historical_threat_coverage_with_delayed_upgrade_and_sales(self):
        """Finding 2: Threat validation must use historical round snapshot, not future upgrades or sold towers."""
        # 1. Place Dart Monkey at R1; purchase Camo detection (Enhanced Eyesight 0-0-2) at R30
        eng1 = TowerReplayEngine(difficulty="Easy")
        eng1.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)
        eng1.apply_step({"step_number": 2, "round": 30, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-0-2", "timing": "before_round"}, 1)
        cov24_1 = eng1.evaluate_threat_coverage(24)
        self.assertFalse(cov24_1["camo"], "At Round 24, Dart Monkey 0-0-0 must NOT report Camo detection")
        cov30_1 = eng1.evaluate_threat_coverage(30)
        self.assertTrue(cov30_1["camo"], "At Round 30, Dart Monkey 0-0-2 must report Camo detection")

        # 2. Place Ninja at R1; sell it at R2
        eng2 = TowerReplayEngine(difficulty="Easy")
        eng2.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Ninja Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)
        eng2.apply_step({"step_number": 2, "round": 2, "action": "Sell", "tower": "Ninja Monkey", "timing": "before_round"}, 1)
        cov24_2 = eng2.evaluate_threat_coverage(24)
        self.assertFalse(cov24_2["camo"], "At Round 24, sold Ninja Monkey must NOT report Camo detection")

    def test_item3_transactional_replay_rollback_on_unaffordable_action(self):
        """Finding 3: Rejected actions must leave board, towers, investment, and history unchanged."""
        eng = TowerReplayEngine(difficulty="Easy", start_round=1, max_round=40)
        unaffordable_step = {
            "step_number": 1, "round": 1, "action": "Place", "tower": "Super Monkey",
            "upgrade": "0-0-0", "placement": "Center", "targeting": "First",
            "cost_estimate": 8000, "timing": "before_round"
        }
        ok, err = eng.apply_step(unaffordable_step, step_index=0)
        self.assertFalse(ok, "Unaffordable step must fail apply_step")
        self.assertEqual(len(eng.active_towers), 0, "active_towers must remain empty after failed purchase")
        self.assertEqual(len(eng.all_towers), 0, "all_towers must remain empty after failed purchase")
        self.assertEqual(eng.cumulative_cost_spent, 0, "cumulative_cost_spent must remain 0")
        self.assertEqual(len(eng.step_history), 0, "step_history must remain empty after failed purchase")

        # Radar check: must not report Lead ready
        readiness = check_strategy_defense_readiness(28, [unaffordable_step])
        self.assertFalse(readiness["lead_ready"], "Radar must not count capabilities from unaffordable actions")

    def test_item4_tower_id_enforcement_and_exact_hero_names(self):
        """Finding 4: Enforce persistent tower IDs, reject duplicate IDs, type mismatches, and invented heroes."""
        eng = TowerReplayEngine(difficulty="Easy")
        # Place Dart Monkey with explicit ID t1
        s1 = {"step_number": 1, "tower_id": "t1", "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        ok, _ = eng.apply_step(s1, 0)
        self.assertTrue(ok)

        # 1. Reject duplicate placement with same ID t1
        s_dup = {"step_number": 2, "tower_id": "t1", "round": 2, "action": "Place", "tower": "Tack Shooter", "upgrade": "0-0-0", "timing": "before_round"}
        ok, err = eng.apply_step(s_dup, 1)
        self.assertFalse(ok)
        self.assertIn("duplicate tower_id 't1'", err)

        # 2. Reject Bomb Shooter upgrade referencing Dart Monkey's ID t1
        s_mismatch = {"step_number": 2, "tower_id": "t1", "round": 5, "action": "Upgrade", "tower": "Bomb Shooter", "upgrade": "0-3-0", "timing": "before_round"}
        ok, err = eng.apply_step(s_mismatch, 1)
        self.assertFalse(ok)
        self.assertIn("Bomb Shooter", err)

        # 3. Reject invented hero name
        s_hero = {"step_number": 2, "round": 5, "action": "Place", "tower": "Quincy Imaginary Cannon", "upgrade": "0-0-0", "timing": "before_round"}
        ok, err = eng.apply_step(s_hero, 1)
        self.assertFalse(ok)
        self.assertIn("unrecognized or invented", err)

    def test_item5_atomic_single_file_override_failure_safety(self):
        """Finding 5: Injected override save failure leaves live state, user_overrides.json, and guides.json intact."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = os.path.join(tmp_dir, "guides.json")
            ov_path = os.path.join(tmp_dir, "user_overrides.json")
            orig_data = {
                "version": "1.3.0",
                "maps": {
                    "monkey_meadow": {
                        "name": "Monkey Meadow",
                        "difficulties": {
                            "Easy": {"status": "Verified", "overview": "Original Overview"}
                        }
                    }
                }
            }
            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(orig_data, f)

            dm = DataManager(filepath=db_path, show_dialogs=False)
            dm.overrides_filepath = ov_path

            # Inject failure when replacing user_overrides.json
            with patch("os.replace", side_effect=OSError("Disk write error")):
                res = dm.save_override("monkey_meadow", "Easy", {"status": "Playtested", "overview": "Tampered"})
                self.assertFalse(res, "save_override must return False on write failure")

            # Verify in-memory state and disk files were NOT modified
            self.assertEqual(dm.database["maps"]["monkey_meadow"]["difficulties"]["Easy"]["overview"], "Original Overview")
            self.assertFalse(os.path.exists(ov_path), "user_overrides.json must not exist if write failed")
            with open(db_path, "r", encoding="utf-8") as f:
                disk_db = json.load(f)
            self.assertEqual(disk_db["maps"]["monkey_meadow"]["difficulties"]["Easy"]["overview"], "Original Overview")

    def test_item6_step_id_preservation_and_progress_tracking(self):
        """Finding 6: Step IDs are preserved when saving steps, and progress completion checks step_id."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "settings.json")
            sm = SettingsManager(filepath=set_path)
            mid = "monkey_meadow"
            diff = "Easy"

            # Setting progress by step_id
            sm.set_step_progress(mid, "monkey_meadow_easy_s1", True, diff=diff)
            prog = sm.get_progress(mid, diff=diff)
            self.assertIn("monkey_meadow_easy_s1", prog)

            # Unsetting clears it
            sm.set_step_progress(mid, "monkey_meadow_easy_s1", False, diff=diff)
            self.assertNotIn("monkey_meadow_easy_s1", sm.get_progress(mid, diff=diff))

    def test_item7_explicit_timing_and_pop_cash_formula(self):
        """Finding 7: Cash during round strictly includes pop cash only and excludes end-of-round bonus."""
        pop_cash_11 = calculate_round_pop_cash(11)
        tot_inc_11 = calculate_round_income(11)
        self.assertLess(pop_cash_11, tot_inc_11, "Pop cash must not include end-of-round bonus")

        cash_before = get_cash_available("Easy", 11, "before_round")
        cash_during = get_cash_available("Easy", 11, "during_round")
        cash_after = get_cash_available("Easy", 11, "after_round")
        self.assertLess(cash_before, cash_during)
        self.assertLess(cash_during, cash_after)
        self.assertEqual(cash_during - cash_before, pop_cash_11)

    def test_item8_boundary_database_loading_resilience(self):
        """Finding 8: Malformed root database structures are safely rejected without uncaught crashes."""
        bad_inputs = [[], {"maps": []}, {"maps": None}, "invalid string", 12345]
        for bad_in in bad_inputs:
            ok, errs, _, _ = validate_database(data=bad_in)
            self.assertFalse(ok, f"Malformed input {bad_in} must be rejected")
            self.assertTrue(len(errs) > 0, "Errors must describe the boundary violation")

    def test_map_hero_intelligence_covers_all_87_maps(self):
        """Verify optimal hero intelligence covers all 87 maps across all 16 canonical heroes."""
        self.assertEqual(len(MAP_HERO_INTELLIGENCE), 87)
        dm = DataManager(show_dialogs=False)
        maps = dm.get_maps()
        self.assertEqual(len(maps), 87)

        heroes_represented = set()
        for mid, mdata in maps.items():
            best_hero = mdata.get("best_hero")
            self.assertIsNotNone(best_hero)
            self.assertIn(best_hero, HEROES_DATABASE)
            self.assertTrue(len(mdata.get("best_hero_reason", "")) > 10)
            self.assertTrue(len(mdata.get("hero_alternatives", [])) >= 2)
            self.assertTrue(len(mdata.get("hero_synergies", "")) > 5)
            heroes_represented.add(best_hero)

        # All 16 heroes must be represented across the 87 maps
        self.assertEqual(len(heroes_represented), 16, f"Expected all 16 heroes represented, found {len(heroes_represented)}")
        # Sauda must not be assigned to an excessive number of maps
        sauda_count = sum(1 for m in maps.values() if m.get("best_hero") == "Sauda")
        self.assertLessEqual(sauda_count, 20, f"Sauda was assigned to {sauda_count} maps (expected <= 20)")


class TestRemainingSuggestionsRegressions(unittest.TestCase):
    """
    Focused regressions for the latest review findings:
    - Actual Add Step UI callback execution without NameError
    - Single-counted refunds preventing unaffordable purchases
    - Phase-aware historical coverage (after_round cannot defend combat phase)
    - Enforced phase ordering within rounds
    - Replay transaction rollback preserving all mutable state
    - Robust candidate database nested validation preventing AttributeError
    - Radar difficulty awareness and replay error propagation
    - Strict ceramic capability requiring ceramic crowd control rather than lead popping
    - Exclusively canonical pricing preventing investment inflation
    """

    def test_actual_add_step_callback_succeeds(self):
        """Recommendation 1: Actual Add Step and Save Step UI callbacks execute without NameError."""
        import tkinter as tk
        app = BTD6GuideApp()
        app.withdraw()
        try:
            app.selected_map_name.set("Monkey Meadow")
            app.open_edit_guide_dialog()

            # Locate editor window
            editors = [w for w in app.winfo_children() if isinstance(w, tk.Toplevel)]
            self.assertTrue(len(editors) > 0, "Strategy editor window must open")
            editor = editors[0]

            def find_buttons(widget):
                res = []
                if isinstance(widget, tk.Button):
                    res.append(widget)
                for c in widget.winfo_children():
                    res.extend(find_buttons(c))
                return res

            btns = find_buttons(editor)
            add_btns = [b for b in btns if "Add New Step" in b.cget("text")]
            self.assertTrue(len(add_btns) > 0, "Must find '➕ Add New Step' button")
            add_btns[0].invoke()

            # Locate step editor modal dialog
            dialogs = [w for w in editor.winfo_children() if isinstance(w, tk.Toplevel)]
            self.assertTrue(len(dialogs) > 0, "Step editor dialog must open")
            dialog = dialogs[0]

            dialog_btns = find_buttons(dialog)
            save_btns = [b for b in dialog_btns if "Save Step" in b.cget("text")]
            self.assertTrue(len(save_btns) > 0, "Must find '✔ Save Step' button")

            # Invoking save_step must generate step_id using uuid without NameError
            save_btns[0].invoke()
        finally:
            app.destroy()

    def test_refunds_cannot_finance_otherwise_unaffordable_purchase(self):
        """Recommendation 2: Refunds must be counted once; net spending cannot exceed available cash."""
        eng = TowerReplayEngine(difficulty="Medium", start_round=1, max_round=40)
        # Step 1: Place Dart Monkey at R1 ($200)
        ok1, err1 = eng.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)
        self.assertTrue(ok1, f"Step 1 failed: {err1}")

        # Step 2: Sell Dart Monkey at R2 for 70% refund ($140)
        ok2, err2 = eng.apply_step({"step_number": 2, "round": 2, "action": "Sell", "tower": "Dart Monkey", "timing": "before_round"}, 1)
        self.assertTrue(ok2, f"Step 2 failed: {err2}")
        self.assertEqual(eng.cumulative_refunds, 140)

        # Step 3: Attempt to buy an $800 Monkey Ace before R2
        # Cumulative spent would be $200 + $800 = $1,000.
        # Cash available before R2: $650 starting + $121 round 1 income + $140 refund = $911.
        # $1,000 > $911: must be rejected!
        ok3, err3 = eng.apply_step({"step_number": 3, "round": 2, "action": "Place", "tower": "Monkey Ace", "upgrade": "0-0-0", "timing": "before_round"}, 2)
        self.assertFalse(ok3, "Monkey Ace ($800) must be rejected because $1000 spent exceeds $911 available cash")
        self.assertIn("exceeds max available cash", err3)

        # Step 4: A purchase within budget ($350 Sniper Monkey -> $550 spent <= $911) must succeed
        ok4, err4 = eng.apply_step({"step_number": 3, "round": 2, "action": "Place", "tower": "Sniper Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 2)
        self.assertTrue(ok4, f"Affordable purchase should succeed: {err4}")

    def test_after_round_upgrade_cannot_satisfy_opening_defense(self):
        """Recommendation 3: An after_round upgrade cannot satisfy that round's combat defense."""
        eng = TowerReplayEngine(difficulty="Easy", start_round=1, max_round=40)
        # Place Dart Monkey at R1
        eng.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)

        # Upgrade to Camo (0-0-2) AFTER Round 24
        eng.apply_step({"step_number": 2, "round": 24, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-0-2", "timing": "after_round"}, 1)

        # R24 combat phase occurs before after_round, so Camo must be False for R24
        cov24 = eng.evaluate_threat_coverage(24, at_timing="during_round")
        self.assertFalse(cov24["camo"], "Camo upgrade after Round 24 must not defend Round 24 combat")

        # R25 combat phase occurs after R24 after_round, so Camo must be True for R25
        cov25 = eng.evaluate_threat_coverage(25, at_timing="during_round")
        self.assertTrue(cov25["camo"], "Camo upgrade after Round 24 must be active for Round 25")

    def test_phase_order_enforced_within_round(self):
        """Recommendation 3b: Chronology within a round must enforce before_round -> during_round -> after_round."""
        eng = TowerReplayEngine(difficulty="Easy", start_round=1, max_round=40)
        eng.apply_step({"step_number": 1, "round": 10, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "during_round"}, 0)

        # Attempting before_round after during_round in Round 10 must be rejected
        ok, err = eng.apply_step({"step_number": 2, "round": 10, "action": "Place", "tower": "Tack Shooter", "upgrade": "0-0-0", "timing": "before_round"}, 1)
        self.assertFalse(ok)
        self.assertIn("timing 'before_round' regressed from previous timing 'during_round' in Round 10", err)

    def test_rejected_actions_leave_all_replay_state_unchanged(self):
        """Recommendation 4: Failed actions must leave board, chronology, spending, refunds, and history untouched."""
        eng = TowerReplayEngine(difficulty="Easy", start_round=1, max_round=40)
        eng.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)

        snap_round = eng.last_round
        snap_timing = eng.last_timing
        snap_spent = eng.cumulative_cost_spent
        snap_refunds = eng.cumulative_refunds
        snap_active = dict(eng.active_towers)
        snap_all = dict(eng.all_towers)
        snap_history_len = len(eng.step_history)

        # Attempt illegal invented tower at Round 30
        bad_step = {"step_number": 2, "round": 30, "action": "Place", "tower": "Fictional Plasma Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        ok, err = eng.apply_step(bad_step, 1)
        self.assertFalse(ok)

        # Verify exact transactional invariance
        self.assertEqual(eng.last_round, snap_round, "last_round must NOT advance upon rejected action")
        self.assertEqual(eng.last_timing, snap_timing)
        self.assertEqual(eng.cumulative_cost_spent, snap_spent)
        self.assertEqual(eng.cumulative_refunds, snap_refunds)
        self.assertEqual(eng.active_towers, snap_active)
        self.assertEqual(eng.all_towers, snap_all)
        self.assertEqual(len(eng.step_history), snap_history_len)

        # Subsequent valid action at Round 2 must succeed (proving last_round did not stay at 30)
        ok2, err2 = eng.apply_step({"step_number": 2, "round": 2, "action": "Place", "tower": "Tack Shooter", "upgrade": "0-0-0", "timing": "before_round"}, 1)
        self.assertTrue(ok2, f"Round 2 step must succeed: {err2}")

    def test_invalid_nested_database_data_rejected_before_rendering(self):
        """Recommendation 5: Nested null or malformed map dictionaries in database are rejected before assignment."""
        malformed_structures = [
            {"maps": {"bad_map": None}},
            {"maps": {"bad_map": {"difficulties": "not_a_dict"}}},
            {"maps": {"bad_map": {"difficulties": {"Easy": "not_a_dict"}}}},
            {"maps": {"bad_map": 12345}},
        ]
        for bad_data in malformed_structures:
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
                json.dump(bad_data, f)
                tmp_path = f.name
            try:
                dm = DataManager(filepath=tmp_path, show_dialogs=False)
                # load() must fail and record a descriptive load error
                self.assertIsNotNone(dm.last_load_error)
                # get_statistics() must not raise AttributeError
                total, playtested, struct_val, needs_rev, counts = dm.get_statistics()
                self.assertIsInstance(total, int)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

    def test_radar_receives_difficulty_and_reports_replay_errors(self):
        """Recommendation 6: check_strategy_defense_readiness respects difficulty and surfaces replay errors."""
        # On Hard difficulty, Round 1 action is outside legal round range [3, 100]
        step_r1 = {"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        readiness_hard = check_strategy_defense_readiness(10, [step_r1], difficulty="Hard")
        self.assertFalse(readiness_hard["is_valid"])
        self.assertTrue(len(readiness_hard["replay_errors"]) > 0)
        self.assertTrue(any("outside legal range [3, 100]" in e for e in readiness_hard["replay_errors"]))

        # On Medium difficulty, Round 1 is within legal range [1, 100]
        readiness_med = check_strategy_defense_readiness(10, [step_r1], difficulty="Medium")
        self.assertTrue(readiness_med["is_valid"])
        self.assertEqual(len(readiness_med["replay_errors"]), 0)

    def test_ceramic_readiness_cannot_be_satisfied_solely_by_lead_popping(self):
        """Recommendation 7: Lone Bomb Shooter (0-0-0) pops Lead but must NOT satisfy Ceramic readiness."""
        eng = TowerReplayEngine(difficulty="Hard", start_round=3, max_round=80)
        eng.apply_step({"step_number": 1, "round": 3, "action": "Place", "tower": "Bomb Shooter", "upgrade": "0-0-0", "timing": "before_round"}, 0)

        cov63 = eng.evaluate_threat_coverage(63)
        self.assertTrue(cov63["lead"], "Bomb Shooter 0-0-0 pops Lead")
        self.assertFalse(cov63["ceramic"], "Bomb Shooter 0-0-0 must NOT satisfy Ceramic readiness solely by popping Lead")

        # Upgrading to Recursive Cluster (2-0-4) provides heavy ceramic CC
        eng.apply_step({"step_number": 2, "round": 63, "action": "Upgrade", "tower": "Bomb Shooter", "upgrade": "2-0-4", "timing": "before_round"}, 1)
        cov63_upg = eng.evaluate_threat_coverage(63)
        self.assertTrue(cov63_upg["ceramic"], "Recursive Cluster 2-0-4 must satisfy Ceramic readiness")

    def test_canonical_pricing_not_inflated_by_supplied_estimate(self):
        """Recommendation 8: Supplied estimates cannot inflate simulated spending or refund accounting."""
        eng = TowerReplayEngine(difficulty="Medium", start_round=1, max_round=40)
        # Place Dart Monkey ($200 canonical on Medium) with arbitrary $500 estimate
        eng.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "cost_estimate": 500, "timing": "before_round"}, 0)
        self.assertEqual(eng.cumulative_cost_spent, 200, "Cumulative cost spent must use canonical cost ($200), not supplied estimate ($500)")
        self.assertEqual(eng.active_towers["dart_monkey_1"].total_invested, 200, "Tower total_invested must use canonical cost")

        # Sell Dart Monkey: refund must be exactly 70% of $200 = $140, NOT 70% of $500 ($350)
        eng.apply_step({"step_number": 2, "round": 2, "action": "Sell", "tower": "Dart Monkey", "timing": "before_round"}, 1)
        self.assertEqual(eng.cumulative_refunds, 140, "Refund must be 70% of canonical investment ($140)")


class TestExtendedCapabilitiesAndEngineDisambiguation(unittest.TestCase):
    """
    Unit and regression tests verifying:
    - Complete tactical capability coverage for all 16 heroes and remaining towers
    - Upgrade candidate disambiguation prioritizing the advanced tower along the path
    - Editor save assigns explicit tower IDs across all steps
    - SettingsManager resilience against corrupted non-dict files
    - Safe map ID fallback for HTML printable cheat sheets
    """

    def test_all_16_heroes_capabilities_handled(self):
        """All 16 heroes return valid tactical capabilities based on hero level milestones."""
        heroes = [
            "Sauda", "Quincy", "Gwendolin", "Obyn Greenfoot", "Striker Jones",
            "Etienne", "Admiral Brickell", "Psi", "Captain Churchill", "Churchill",
            "Benjamin", "Ezili", "Pat Fusty", "Adora", "Geraldo", "Corvus", "Rosalia"
        ]
        for h in heroes:
            caps_lv1 = get_tower_capabilities(h, (0, 0, 0), hero_level=1)
            self.assertIsInstance(caps_lv1, dict)
            self.assertIn("camo", caps_lv1)
            self.assertIn("lead", caps_lv1)
            self.assertIn("moab_damage", caps_lv1)

        # Ezili: innate camo at lv1, lead at lv4, moab/bfb/zomg at lv10
        ezili_lv1 = get_tower_capabilities("Ezili", (0, 0, 0), hero_level=1)
        self.assertTrue(ezili_lv1["camo"])
        self.assertFalse(ezili_lv1["lead"])
        ezili_lv4 = get_tower_capabilities("Ezili", (0, 0, 0), hero_level=4)
        self.assertTrue(ezili_lv4["lead"])
        ezili_lv10 = get_tower_capabilities("Ezili", (0, 0, 0), hero_level=10)
        self.assertTrue(ezili_lv10["moab_damage"])
        self.assertTrue(ezili_lv10["zomg_damage"])

        # Captain Churchill / Churchill: innate lead, camo at lv6, moab at lv3
        church_lv1 = get_tower_capabilities("Captain Churchill", (0, 0, 0), hero_level=1)
        self.assertTrue(church_lv1["lead"])
        self.assertFalse(church_lv1["camo"])
        church_lv3 = get_tower_capabilities("Captain Churchill", (0, 0, 0), hero_level=3)
        self.assertTrue(church_lv3["moab_damage"])
        self.assertTrue(church_lv3["ceramic_cc"])
        church_lv6 = get_tower_capabilities("Captain Churchill", (0, 0, 0), hero_level=6)
        self.assertTrue(church_lv6["camo"])

        # Pat Fusty: lead at lv2, moab at lv3, bfb at lv10
        pat_lv2 = get_tower_capabilities("Pat Fusty", (0, 0, 0), hero_level=2)
        self.assertTrue(pat_lv2["lead"])
        self.assertTrue(pat_lv2["ceramic_cc"])
        pat_lv10 = get_tower_capabilities("Pat Fusty", (0, 0, 0), hero_level=10)
        self.assertTrue(pat_lv10["bfb_damage"])

    def test_engineer_monkey_and_beast_handler_capabilities(self):
        """Engineer Monkey and Beast Handler tactical capabilities are accurately evaluated."""
        # Cleansing Foam (0-2-0) gives camo, lead, and grants_camo
        eng_foam = get_tower_capabilities("Engineer Monkey", (0, 2, 0))
        self.assertTrue(eng_foam["camo"])
        self.assertTrue(eng_foam["lead"])
        self.assertTrue(eng_foam["grants_camo"])

        # Sentry Expert (4-0-0) gives lead and moab
        eng_sent = get_tower_capabilities("Engineer Monkey", (4, 0, 0))
        self.assertTrue(eng_sent["lead"])
        self.assertTrue(eng_sent["moab_damage"])

        # Bloon Trap (0-0-4) gives ceramic CC; XXL Trap (0-0-5) gives bfb & zomg
        eng_trap = get_tower_capabilities("Engineer Monkey", (0, 0, 4))
        self.assertTrue(eng_trap["ceramic_cc"])
        eng_xxl = get_tower_capabilities("Engineer Monkey", (0, 0, 5))
        self.assertTrue(eng_xxl["bfb_damage"])
        self.assertTrue(eng_xxl["zomg_damage"])

        # Beast Handler: Horned Owl (0-3-0) detects Camo, Great White (2-0-0) deals MOAB damage
        bh_owl = get_tower_capabilities("Beast Handler", (0, 3, 0))
        self.assertTrue(bh_owl["camo"])
        bh_shark = get_tower_capabilities("Beast Handler", (2, 0, 0))
        self.assertTrue(bh_shark["moab_damage"])
        bh_meg = get_tower_capabilities("Beast Handler", (5, 0, 0))
        self.assertTrue(bh_meg["zomg_damage"])

    def test_upgrade_disambiguation_favors_advanced_tower(self):
        """When multiple unassigned towers exist, an upgrade step targets the tower furthest along that path."""
        eng = TowerReplayEngine(difficulty="Easy", start_round=1, max_round=40)
        # Place Dart 1 at R1 (0-0-0)
        eng.apply_step({"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 0)
        # Place Dart 2 at R2 (0-0-0)
        eng.apply_step({"step_number": 2, "round": 2, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}, 1)
        # Upgrade Dart 2 specifically to 0-0-2
        eng.apply_step({"step_number": 3, "round": 3, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-0-2", "tower_id": "dart_monkey_2", "timing": "before_round"}, 2)

        # Now apply an unassigned upgrade step to 0-2-2
        eng.apply_step({"step_number": 4, "round": 4, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-2-2", "timing": "before_round"}, 3)

        # Dart 2 had 2 tiers already; it must be the tower upgraded to 0-2-2! Dart 1 remains 0-0-0
        self.assertEqual(eng.active_towers["dart_monkey_2"].upgrade, (0, 2, 2))
        self.assertEqual(eng.active_towers["dart_monkey_1"].upgrade, (0, 0, 0))

    def test_assign_explicit_tower_ids_on_draft_steps(self):
        """assign_explicit_tower_ids assigns persistent tower IDs to unassigned steps."""
        draft = {
            "difficulty": "Easy",
            "steps": [
                {"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0"},
                {"step_number": 2, "round": 5, "action": "Upgrade", "tower": "Dart Monkey", "upgrade": "0-0-2"}
            ]
        }
        assign_explicit_tower_ids(draft, "monkey_meadow", "Easy")
        self.assertEqual(draft["steps"][0].get("tower_id"), "monkey_meadow_easy_t1")
        self.assertEqual(draft["steps"][1].get("tower_id"), "monkey_meadow_easy_t1")

    def test_settings_manager_corrupted_json_resilience(self):
        """SettingsManager safely handles corrupted non-dictionary JSON without throwing uncaught exceptions."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "corrupted_settings.json")
            # Write a JSON list instead of a dict
            with open(set_path, "w", encoding="utf-8") as f:
                json.dump(["corrupted", "list"], f)

            sm = SettingsManager(filepath=set_path)
            self.assertIsNotNone(sm.last_save_error)
            self.assertIn("root JSON must be a dictionary", str(sm.last_save_error))
            self.assertEqual(sm.data["last_map_id"], "monkey_meadow")

    def test_export_printable_html_safe_mid_fallback(self):
        """export_printable_html creates valid filename when mid is None."""
        app = BTD6GuideApp.__new__(BTD6GuideApp)
        app.data_manager = DataManager(show_dialogs=False)
        app.get_current_map_id = lambda: None

        sample_strat = {
            "difficulty": "Easy",
            "rounds": "1-40",
            "recommended_hero": "Sauda",
            "overview": "Overview test",
            "camo_handling": "Camo test",
            "lead_handling": "Lead test",
            "moab_handling": "MOAB test",
            "why_it_works": "Why test",
            "steps": [
                {"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
            ]
        }
        sample_map = {"name": "Test Map Name", "category": "Beginner"}

        with tempfile.TemporaryDirectory() as tmp_dir:
            orig_join = os.path.join
            def fake_join(*args):
                if len(args) == 2 and str(args[1]).endswith(".html"):
                    return orig_join(tmp_dir, args[1])
                return orig_join(*args)

            from unittest.mock import patch
            with patch("os.path.join", side_effect=fake_join), patch("webbrowser.open"), patch("tkinter.messagebox.showinfo"):
                app.export_printable_html(strat=sample_strat, map_data=sample_map)

            expected_file = os.path.join(tmp_dir, "test_map_name_easy_guide.html")
            self.assertTrue(os.path.exists(expected_file), f"File {expected_file} must exist")


class TestMonkeyKnowledgeAndCommunitySharing(unittest.TestCase):
    """
    Unit and integration tests covering:
    - Monkey Knowledge More Cash (+200 starting cash in non-CHIMPS)
    - Free Dart Monkey perk (0-0-0 first Dart Monkey costs $0)
    - CHIMPS mode strict MK exemption (remains 650 starting cash, no free dart)
    - Community guide export to .btd6guide JSON payload
    - Community guide import, schema validation, tower ID assignment, and override activation
    - Walkthrough auto-advance and navigation hotkey integration
    """

    def test_monkey_knowledge_starting_cash_and_free_dart(self):
        """MK grants +$200 starting cash and makes the first 0-0-0 Dart Monkey free."""
        # Baseline (No MK)
        eng_no_mk = TowerReplayEngine(difficulty="Medium", start_round=1, max_round=40, monkey_knowledge=False)
        step_dart1 = {"step_number": 1, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        ok1, _ = eng_no_mk.apply_step(step_dart1, 0)
        self.assertTrue(ok1)
        self.assertEqual(eng_no_mk.cumulative_cost_spent, 200, "Without MK, Dart Monkey costs canonical $200")

        # With MK (More Cash + Free Dart)
        eng_mk = TowerReplayEngine(difficulty="Medium", start_round=1, max_round=40, monkey_knowledge=True)
        ok2, _ = eng_mk.apply_step(step_dart1, 0)
        self.assertTrue(ok2)
        self.assertEqual(eng_mk.cumulative_cost_spent, 0, "With MK, first 0-0-0 Dart Monkey is free ($0)")
        self.assertTrue(eng_mk.free_dart_used)

        # Second Dart Monkey costs normal canonical cost ($200)
        step_dart2 = {"step_number": 2, "round": 1, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        ok3, _ = eng_mk.apply_step(step_dart2, 1)
        self.assertTrue(ok3)
        self.assertEqual(eng_mk.cumulative_cost_spent, 200, "Second Dart Monkey must cost canonical $200")

    def test_monkey_knowledge_disabled_on_chimps(self):
        """CHIMPS mode strictly disables all Monkey Knowledge benefits."""
        eng_chimps = TowerReplayEngine(difficulty="CHIMPS", start_round=6, max_round=100, monkey_knowledge=True)
        self.assertFalse(eng_chimps.monkey_knowledge, "CHIMPS must force monkey_knowledge to False")
        step_dart = {"step_number": 1, "round": 6, "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "timing": "before_round"}
        ok, _ = eng_chimps.apply_step(step_dart, 0)
        self.assertTrue(ok)
        self.assertEqual(eng_chimps.cumulative_cost_spent, 200, "On CHIMPS, Dart Monkey is not free")

    def test_community_guide_export_and_import_cycle(self):
        """Exporting a strategy to .btd6guide and re-importing preserves structure, validates, and activates."""
        app = BTD6GuideApp.__new__(BTD6GuideApp)
        app.settings = SettingsManager()
        app.data_manager = DataManager(show_dialogs=False)
        app.get_current_map_id = lambda: "monkey_meadow"
        app.get_selected_diff_key = lambda: "Easy"
        app.selected_map_name = unittest.mock.MagicMock()
        app.selected_difficulty = unittest.mock.MagicMock()
        app.render_guide = unittest.mock.MagicMock()

        map_data = app.data_manager.get_map("monkey_meadow")
        strat = map_data["difficulties"]["Easy"]

        with tempfile.TemporaryDirectory() as tmp_dir:
            guide_file = os.path.join(tmp_dir, "test_share.btd6guide")

            from unittest.mock import patch
            with patch("tkinter.filedialog.asksaveasfilename", return_value=guide_file), patch("tkinter.messagebox.showinfo"):
                app.export_strategy_file()

            self.assertTrue(os.path.exists(guide_file), "Exported .btd6guide file must exist on disk")
            with open(guide_file, "r", encoding="utf-8") as f:
                payload = json.load(f)

            self.assertEqual(payload.get("format"), "btd6guide")
            self.assertEqual(payload.get("map_id"), "monkey_meadow")
            self.assertEqual(payload.get("difficulty"), "Easy")
            self.assertTrue(len(payload["strategy"]["steps"]) >= 5)

            test_ov_file = os.path.join(tmp_dir, "user_overrides.json")
            app.data_manager.overrides_filepath = test_ov_file
            payload["strategy"]["overview"] = "Community Modified Overview!"

            with open(guide_file, "w", encoding="utf-8") as f:
                json.dump(payload, f)

            with patch("tkinter.filedialog.askopenfilename", return_value=guide_file), \
                 patch("tkinter.messagebox.askyesno", return_value=True), \
                 patch("tkinter.messagebox.showinfo"):
                app.import_strategy_file()

            self.assertEqual(
                app.data_manager.database["maps"]["monkey_meadow"]["difficulties"]["Easy"]["overview"],
                "Community Modified Overview!"
            )
            self.assertTrue(os.path.exists(test_ov_file))

    def test_settings_manager_monkey_knowledge_toggle(self):
        """SettingsManager stores and toggles monkey_knowledge state."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "settings.json")
            sm = SettingsManager(filepath=set_path)
            self.assertTrue(sm.is_monkey_knowledge())

            sm.set_monkey_knowledge(False)
            self.assertFalse(sm.is_monkey_knowledge())

            # Reload to verify persistence
            sm2 = SettingsManager(filepath=set_path)
            self.assertFalse(sm2.is_monkey_knowledge())


class TestCleanDatabasePassesAllInvariants(unittest.TestCase):
    def test_guides_database_100_percent_pass(self):
        success, errors, warnings, stats = validate_database()
        if errors:
            self.fail(f"Production guides.json failed validation with {len(errors)} errors:\n" + "\n".join(errors[:10]))
        self.assertTrue(success)
        self.assertEqual(stats["total_maps"], 87)
        self.assertEqual(stats["difficulty_counts"]["Easy"], 87)
        self.assertEqual(stats["difficulty_counts"]["Medium"], 87)
        self.assertEqual(stats["difficulty_counts"]["Hard"], 87)


class TestSuggestionsForCodingRegressions(unittest.TestCase):
    """
    Validates all 5 points and prioritized regression requirements from Suggestions_for_Coding.txt:
    1. A Monkey Knowledge-dependent guide survives save, reload, and export/import.
    2. Malformed imports return diagnostics without exceptions.
    3. Mixed explicit/generated tower IDs never collide.
    4. Every accepted strategy is safe for rendering and replay (strict field schemas).
    5. Draft imports remain drafts after restarting.
    6. Saved and shared guides record their execution assumptions (requirements, starting cash, game version).
    """

    def _create_valid_medium_strategy(self, starting_cash=650, mk_req=False):
        steps = [
            {"step_number": 1, "round": 1, "timing": "before_round", "action": "Place", "tower": "Dart Monkey", "upgrade": "0-0-0", "cost_estimate": 215, "placement": "Center"},
            {"step_number": 2, "round": 4, "timing": "before_round", "action": "Place", "tower": "Ninja Monkey", "upgrade": "0-0-0", "cost_estimate": 540, "placement": "Near entrance"},
            {"step_number": 3, "round": 10, "timing": "before_round", "action": "Upgrade", "tower": "Ninja Monkey", "upgrade": "1-0-1", "cost_estimate": 430, "placement": "Near entrance"},
            {"step_number": 4, "round": 18, "timing": "before_round", "action": "Upgrade", "tower": "Ninja Monkey", "upgrade": "3-0-1", "cost_estimate": 920, "placement": "Near entrance"},
            {"step_number": 5, "round": 24, "timing": "before_round", "action": "Upgrade", "tower": "Ninja Monkey", "upgrade": "4-0-1", "cost_estimate": 2970, "placement": "Near entrance"},
            {"step_number": 6, "round": 27, "timing": "before_round", "action": "Place", "tower": "Alchemist", "upgrade": "2-0-0", "cost_estimate": 1405, "placement": "Near Ninja"},
            {"step_number": 7, "round": 36, "timing": "before_round", "action": "Upgrade", "tower": "Alchemist", "upgrade": "3-0-0", "cost_estimate": 1350, "placement": "Near Ninja"},
            {"step_number": 8, "round": 40, "timing": "before_round", "action": "Place", "tower": "Bomb Shooter", "upgrade": "0-3-0", "cost_estimate": 1930, "placement": "Bend"}
        ]
        strat = {
            "difficulty": "Medium",
            "mode": "Standard",
            "rounds": "1-60",
            "status": "Verified",
            "recommended_hero": "Sauda",
            "starting_cash": starting_cash,
            "overview": "Tactical medium test strategy.",
            "camo_handling": "Ninja 4-0-1",
            "lead_handling": "Alchemist 2-0-0 buff",
            "moab_handling": "Bomb Shooter 0-3-0 Mauler",
            "why_it_works": "Synergized defense.",
            "steps": steps
        }
        if mk_req:
            strat["requirements"] = {
                "monkey_knowledge": True,
                "more_starting_cash": True,
                "free_dart_monkey": False,
                "required_starting_cash": 850,
                "game_version": "v45.0"
            }
        return strat

    def test_item1_monkey_knowledge_strategy_survives_save_and_reload(self):
        """1. A Monkey Knowledge-dependent guide survives save, reload, and export/import."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = os.path.join(tmp_dir, "guides.json")
            ov_path = os.path.join(tmp_dir, "user_overrides.json")

            # Medium strategy with Gwendolin ($725 opening spend, starting cash $850)
            strat = self._create_valid_medium_strategy(starting_cash=850, mk_req=True)
            strat["steps"][0] = {
                "step_number": 1,
                "round": 1,
                "timing": "before_round",
                "action": "Place",
                "tower": "Gwendolin",
                "upgrade": "0-0-0",
                "cost_estimate": 725,
                "placement": "Center"
            }
            strat["steps"][1]["timing"] = "during_round"
            strat["steps"][4]["round"] = 26
            strat["steps"][5]["round"] = 30
            strat["steps"][6]["round"] = 37
            strat["recommended_hero"] = "Gwendolin"

            # Base database with default Sauda strategy
            base_db = {
                "version": "1.3.0",
                "maps": {
                    "monkey_meadow": {
                        "name": "Monkey Meadow",
                        "category": "Beginner",
                        "difficulties": {
                            "Medium": self._create_valid_medium_strategy(starting_cash=650, mk_req=False)
                        }
                    }
                }
            }
            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(base_db, f)

            dm = DataManager(filepath=db_path, show_dialogs=False)
            dm.overrides_filepath = ov_path

            # Save the MK override
            saved = dm.save_override("monkey_meadow", "Medium", strat)
            self.assertTrue(saved, "Failed to save Monkey Knowledge override")

            # Reload a fresh DataManager instance (loader defaults to MK=False)
            dm_reloaded = DataManager(filepath=db_path, show_dialogs=False)
            dm_reloaded.overrides_filepath = ov_path
            dm_reloaded.load()

            # Verify the MK override survived loading and is active
            active_strat = dm_reloaded.database["maps"]["monkey_meadow"]["difficulties"]["Medium"]
            self.assertEqual(active_strat["recommended_hero"], "Gwendolin")
            self.assertEqual(active_strat["starting_cash"], 850)
            self.assertIn("monkey_meadow", dm_reloaded.user_overrides)

            # Subsequent save does not overwrite or drop the MK override
            dm_reloaded.save()
            dm_third = DataManager(filepath=db_path, show_dialogs=False)
            dm_third.overrides_filepath = ov_path
            dm_third.load()
            self.assertEqual(
                dm_third.database["maps"]["monkey_meadow"]["difficulties"]["Medium"]["recommended_hero"],
                "Gwendolin"
            )

    def test_item2_malformed_imports_return_diagnostics_without_exceptions(self):
        """2. Malformed imports return diagnostics without exceptions."""
        # Test steps is None
        bad_strat1 = self._create_valid_medium_strategy()
        bad_strat1["steps"] = None
        ok1, errs1 = validate_strategy_schema(bad_strat1)
        self.assertFalse(ok1)
        self.assertTrue(any("steps" in e.lower() for e in errs1))

        # Test step with tower is None
        bad_strat2 = self._create_valid_medium_strategy()
        bad_strat2["steps"][0]["tower"] = None
        ok2, errs2 = validate_strategy_schema(bad_strat2)
        self.assertFalse(ok2)
        self.assertTrue(any("tower" in e.lower() for e in errs2))

        # Test assign_explicit_tower_ids does not crash on None tower
        strat_with_none_tower = {"steps": [{"action": "Place", "tower": None}]}
        try:
            assign_explicit_tower_ids(strat_with_none_tower, "test_map", "Medium")
        except Exception as e:
            self.fail(f"assign_explicit_tower_ids raised exception on None tower: {e}")

        # Test non-dict step
        bad_strat3 = self._create_valid_medium_strategy()
        bad_strat3["steps"][0] = "invalid_step_string"
        ok3, errs3 = validate_strategy_schema(bad_strat3)
        self.assertFalse(ok3)

        # Test boolean step_number or round
        bad_strat4 = self._create_valid_medium_strategy()
        bad_strat4["steps"][0]["round"] = True
        ok4, errs4 = validate_strategy_schema(bad_strat4)
        self.assertFalse(ok4)

    def test_item3_mixed_explicit_and_generated_tower_ids_never_collide(self):
        """3. Mixed explicit and generated tower IDs never collide."""
        engine = TowerReplayEngine(difficulty="Medium", start_round=1, max_round=40)

        # 1. Place a Dart Monkey with explicit ID 'dart_monkey_1'
        step1 = {
            "step_number": 1,
            "round": 1,
            "timing": "before_round",
            "action": "Place",
            "tower": "Dart Monkey",
            "upgrade": "0-0-0",
            "tower_id": "dart_monkey_1",
            "cost_estimate": 215,
            "placement": "Center"
        }
        ok1, err1 = engine.apply_step(step1)
        self.assertTrue(ok1, f"Step 1 failed: {err1}")

        # 2. Place another Dart Monkey WITHOUT an ID
        step2 = {
            "step_number": 2,
            "round": 1,
            "timing": "before_round",
            "action": "Place",
            "tower": "Dart Monkey",
            "upgrade": "0-0-0",
            "cost_estimate": 215,
            "placement": "Top"
        }
        ok2, err2 = engine.apply_step(step2)
        self.assertTrue(ok2, f"Step 2 failed: {err2}")

        # 3. Both placements succeed and the board contains TWO distinct towers
        self.assertEqual(len(engine.active_towers), 2)
        self.assertEqual(len(engine.all_towers), 2)
        self.assertIn("dart_monkey_1", engine.active_towers)
        self.assertIn("dart_monkey_2", engine.active_towers)
        self.assertNotEqual(
            engine.active_towers["dart_monkey_1"].placement,
            engine.active_towers["dart_monkey_2"].placement
        )

        # Test assign_explicit_tower_ids collision avoidance
        strat = {
            "steps": [
                {"action": "Place", "tower": "Dart Monkey", "tower_id": "map_easy_t1"},
                {"action": "Place", "tower": "Dart Monkey"}
            ]
        }
        assign_explicit_tower_ids(strat, "map", "Easy")
        self.assertEqual(strat["steps"][0]["tower_id"], "map_easy_t1")
        self.assertEqual(strat["steps"][1]["tower_id"], "map_easy_t2")

    def test_item4_strict_field_type_and_schema_validation(self):
        """4. Every accepted strategy is safe for rendering and replay (strict field validation)."""
        # A list-valued tower_id is rejected gracefully without unhandled exception
        bad_t_id = self._create_valid_medium_strategy()
        bad_t_id["steps"][0]["tower_id"] = ["dart_1"]
        ok, errs = validate_strategy_schema(bad_t_id)
        self.assertFalse(ok)
        self.assertTrue(any("tower_id" in e for e in errs))

        # A numeric placement is rejected
        bad_place = self._create_valid_medium_strategy()
        bad_place["steps"][0]["placement"] = 12345
        ok, errs = validate_strategy_schema(bad_place)
        self.assertFalse(ok)
        self.assertTrue(any("placement" in e for e in errs))

        # A list-valued step_id is rejected
        bad_s_id = self._create_valid_medium_strategy()
        bad_s_id["steps"][0]["step_id"] = ["step_1"]
        ok, errs = validate_strategy_schema(bad_s_id)
        self.assertFalse(ok)
        self.assertTrue(any("step_id" in e for e in errs))

        # Duplicate step_id is rejected
        dup_s_id = self._create_valid_medium_strategy()
        dup_s_id["steps"][0]["step_id"] = "same_id"
        dup_s_id["steps"][1]["step_id"] = "same_id"
        ok, errs = validate_strategy_schema(dup_s_id)
        self.assertFalse(ok)
        self.assertTrue(any("duplicate step_id" in e for e in errs))

        # "Various" is rejected for an Upgrade action
        bad_upg = self._create_valid_medium_strategy()
        bad_upg["steps"][2]["upgrade"] = "Various"
        ok, errs = validate_strategy_schema(bad_upg)
        self.assertFalse(ok)
        self.assertTrue(any("upgrade" in e.lower() for e in errs))

        # Database loader rejects candidate with list-valued tower_id
        candidate_db = {
            "version": "1.3.0",
            "maps": {
                "test_map": {
                    "name": "Test Map",
                    "difficulties": {
                        "Medium": bad_t_id
                    }
                }
            }
        }
        with tempfile.TemporaryDirectory() as tmp_dir:
            fpath = os.path.join(tmp_dir, "test_guides.json")
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(candidate_db, f)
            dm = DataManager(filepath=fpath, show_dialogs=False)
            self.assertFalse(dm.load())

    def test_item5_draft_imports_remain_drafts_after_restart(self):
        """5. Draft imports remain drafts after restarting."""
        # Strategy lacking camo handling (tactical warning, but replay/economic valid)
        draft_strat = self._create_valid_medium_strategy()
        # Remove camo upgrading step so it lacks Camo on R24
        draft_strat["steps"][4] = {
            "step_number": 5, "round": 24, "timing": "before_round",
            "action": "Place", "tower": "Bomb Shooter", "upgrade": "0-1-0",
            "cost_estimate": 650, "placement": "Bend"
        }
        draft_strat["status"] = "Draft"

        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = os.path.join(tmp_dir, "guides.json")
            ov_path = os.path.join(tmp_dir, "user_overrides.json")

            base_db = {
                "version": "1.3.0",
                "maps": {
                    "monkey_meadow": {
                        "name": "Monkey Meadow",
                        "difficulties": {
                            "Medium": self._create_valid_medium_strategy()
                        }
                    }
                }
            }
            with open(db_path, "w", encoding="utf-8") as f:
                json.dump(base_db, f)

            dm = DataManager(filepath=db_path, show_dialogs=False)
            dm.overrides_filepath = ov_path

            # Save draft override
            saved = dm.save_override("monkey_meadow", "Medium", draft_strat)
            self.assertTrue(saved)

            # Reload fresh DataManager
            dm_reloaded = DataManager(filepath=db_path, show_dialogs=False)
            dm_reloaded.overrides_filepath = ov_path
            dm_reloaded.load()

            loaded_strat = dm_reloaded.database["maps"]["monkey_meadow"]["difficulties"]["Medium"]
            self.assertEqual(loaded_strat["status"], "Draft")
            self.assertIn("monkey_meadow", dm_reloaded.user_overrides)

    def test_item6_exported_strategy_records_assumptions(self):
        """6. Saved and shared guides record their execution assumptions."""
        strat = self._create_valid_medium_strategy(starting_cash=850, mk_req=True)
        map_data = {
            "name": "Monkey Meadow",
            "category": "Beginner",
            "terrain": "Grass",
            "lanes": "Single Track",
            "water": False
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            set_path = os.path.join(tmp_dir, "settings.json")
            sm = SettingsManager(filepath=set_path)
            app = BTD6GuideApp.__new__(BTD6GuideApp)
            app.settings = sm
            app.data_manager = DataManager(filepath=os.path.join(tmp_dir, "guides.json"), show_dialogs=False)
            app.get_current_map_id = lambda: "monkey_meadow"
            app.get_current_strategy = lambda md: strat
            app.clipboard_clear = lambda: None
            copied_text = []
            app.clipboard_append = lambda txt: copied_text.append(txt)
            app.update = lambda: None

            # Test Markdown export
            with patch("tkinter.messagebox.showinfo"):
                app.export_markdown_to_clipboard(strat=strat, map_data=map_data)
            self.assertTrue(len(copied_text) > 0)
            md = copied_text[0]
            self.assertIn("Requirements:", md)
            self.assertIn("Starting Cash: $850", md)
            self.assertIn("Monkey Knowledge: Enabled", md)

            # Test HTML export
            with patch("tkinter.messagebox.showinfo"), \
                 patch("webbrowser.open"):
                app.export_printable_html(strat=strat, map_data=map_data)
                html_filename = "monkey_meadow_medium_guide.html"
                html_path = os.path.join(os.path.dirname(__file__), html_filename)
                self.assertTrue(os.path.exists(html_path))
                with open(html_path, "r", encoding="utf-8") as f:
                    written = f.read()
                self.assertIn("$850", written)
                self.assertIn("Monkey Knowledge", written)
                self.assertIn("Game Version", written)
                if os.path.exists(html_path):
                    os.remove(html_path)


if __name__ == "__main__":
    unittest.main()

