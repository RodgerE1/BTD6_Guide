# Bloons TD 6 — Complete Offline Strategy Guide

A fully functional Windows desktop application built with Python 3 and Tkinter that provides detailed, round-by-round strategies for **every official map in Bloons TD 6 on Easy (R1–40), Medium (R1–60), and Hard (R3–80) difficulties**.

---

## 🎯 Primary Features

- **100% Complete Map Coverage**: Detailed, customized strategies for all **87 official BTD6 maps** across Beginner, Intermediate, Advanced, and Expert tiers.
- **Multi-Tier Difficulty Architecture**: Complete coverage across **Easy (R1–40)**, **Medium (R1–60)**, and **Hard (R3–80)** modes (261 total strategies). Easy strategies are fully verified; Medium and Hard strategies are structurally validated and economically simulated against canonical rules, with a dynamic status badge system (`Playtested`, `Verified`, `Structurally Validated`, `Needs Review`).
- **🦸 Full 16-Hero Intelligence & Recommendation Engine**: Complete tactical profiles for all 16 official heroes (Sauda, Quincy, Gwen, Striker Jones, Obyn, Churchill, Benjamin, Ezili, Pat Fusty, Brickell, Etienne, Psi, Geraldo, Corvus, Rosalia, Adora). Every map features an **Optimal Hero Intelligence** card with tactical justification, alternatives, and synergies. Includes a searchable **Hero Roster Dialog (`🦸 Heroes`)**.
- **📡 Bloon Threat Radar & Wave Inspector (`R`)**: Interactive round-by-round wave inspector (Rounds 1–100) displaying exact bloon counts, RBE (Red Bloon Equivalent), cash generated, speed multipliers, and threat alert tags. Features **Live Defense Verification** checking whether your active strategy has countermeasures ready for Camo, Lead, Ceramics, MOABs, BFBs, and ZOMGs based on canonical tower replay.
- **🛠️ Visual Step Builder & Strategy Editor**: Intuitive form-based step card editor with `[➕ Add]`, `[✏️ Edit]`, `[🗑️ Delete]`, and `[⬆️/⬇️ Reorder]` buttons, interactive 3-tier upgrade path spinners, and dual-mode editing (Visual Form or Raw JSON). User edits are saved to `user_overrides.json` to persist safely across database regenerations.
- **🧠 Monkey Knowledge (MK) Mode Switch (`M`)**: Seamlessly toggle between standard baseline rules and Monkey Knowledge play. Accurately simulates *More Cash* (+$200 starting cash in non-CHIMPS modes) and the *Free Dart Monkey* perk ($0 first Dart Monkey). CHIMPS mode automatically enforces strict zero-MK rules.
- **📁 Community Guide File Export & Import (`.btd6guide`)**: One-click **"Export Guide"** saves self-contained `.btd6guide` JSON strategy packages, while **"Import Guide"** allows players to load, validate, and activate community strategies into local overrides instantly.
- **📋 1-Click Community Sharing & Printable HTML**: Export the active strategy (or live editor draft) with one click directly to formatted Markdown (for Reddit/Discord) or generate a clean, responsive, self-contained **Printable HTML Cheat Sheet** with full HTML entity sanitization opened directly in your browser.
- **Round-by-Round Tactical Instructions**: Exact tower purchases, precise upgrade paths (e.g. `[ 2 • 0 • 4 ]`), specific landmark placements, targeting priorities (`First`, `Strong`, `Close`), and standard difficulty costs.
- **🗗 Compact "Always-On-Top" Gaming Overlay HUD Mode (`F11`)**: Shrinks the app into a sleek, non-intrusive floating HUD widget that stays pinned on top of your BTD6 game. Follow steps and advance with hotkeys without ever Alt-Tabbing!
- **🗺️ Interactive Tactical Placement Minimap**: Visual track flow diagram with clickable numbered pins showing tower placements along the track curves and chokepoints.
- **Dedicated Threat Checkpoints**: Clear countermeasures for **Camo Bloons** (R24, R33, R36, R37, R42, R59), **Lead Bloons** (R28, R30, R37, R45, R59), the **Round 40 MOAB**, the **Round 60 BFB**, **Ceramic rushes** (R63, R76, R78), and the **Round 80 ZOMG**.
- **Interactive Walkthrough Mode & Hotkeys**: Step through rounds in real-time with `[◀ Previous]` and `[Next ▶]` buttons, completion checkboxes, smooth auto-scrolling to the active step, and application-local keyboard shortcuts (active whenever the desktop application window or the compact Gaming HUD overlay is focused):
  - `F11`: Toggle between Full App and Compact Gaming HUD.
  - `Right Arrow` / `Space` / `Return` / `N`: Advance to next step, mark completed, and auto-scroll.
  - `Left Arrow` / `BackSpace` / `P`: Return to previous step and auto-scroll.
  - `M`: Toggle Monkey Knowledge mode (ON / OFF).
  - `R`: Open Bloon Threat Radar & Wave Inspector.
  - `T`: Toggle Always-On-Top pin.
  - `Escape`: Return from HUD Mode to Full App.
- **Drop-Down Mousewheel Isolation**: Mousewheel scrolling over dropdown boxes scrolls the dropdown menu cleanly without moving the underlying window canvas.
- **Category Filtering & Live Search**: Instant filtering by category (Beginner, Intermediate, Advanced, Expert) and real-time map name search.
- **Persistent User Settings**: Automatically remembers your last selected map, difficulty, font size, always-on-top preference, and step completion progress (keyed by persistent `step_id`) across restarts in `user_settings.json`.
- **100% Offline & Zero Dependencies**: Built using the Python standard library and Tkinter. Runs on any Windows machine with Python 3 installed—no internet connection, cloud databases, or `pip install` commands required.

---

## 🚀 How to Run the Application

### Option A: Double-Click (Recommended on Windows)
Simply double-click the application file directly from File Explorer:
```
btd6_guide.pyw
```
*(The `.pyw` extension runs Python applications directly as a desktop window without opening a command prompt).*

### Option B: From the Terminal / PowerShell
Open PowerShell or Command Prompt in the project folder and run:
```bash
python btd6_guide.pyw
```

---

## 📊 Map & Guide Statistics

| Category | Total Maps | Easy (R1–40) | Medium (R1–60) | Hard (R3–80) | Total Strategies |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Beginner** | 26 | 26 / 26 (Verified) | 26 / 26 (Validated) | 26 / 26 (Validated) | **78 / 78** |
| **Intermediate** | 26 | 26 / 26 (Verified) | 26 / 26 (Validated) | 26 / 26 (Validated) | **78 / 78** |
| **Advanced** | 22 | 22 / 22 (Verified) | 22 / 22 (Validated) | 22 / 22 (Validated) | **66 / 66** |
| **Expert** | 13 | 13 / 13 (Verified) | 13 / 13 (Validated) | 13 / 13 (Validated) | **39 / 39** |
| **Total** | **87** | **87 / 87 Verified** | **87 / 87 Validated** | **87 / 87 Validated** | **261 / 261** |

> **Verification Status Note**: 100% of all 261 strategies pass programmatic invariant verification (strictly legal crosspaths, canonical pricing feasibility, timing-aware cash bounds, no orphan upgrades, and round-by-round threat readiness). All 87 Easy strategies are marked **Verified**; Medium and Hard strategies are marked **Structurally Validated**, with the **Playtested** badge reserved for strategies with confirmed empirical playthroughs.

---

## 🎮 Hotkey Quick Reference

> *Note: Hotkeys are application-local and active whenever the main application window or the compact Gaming HUD overlay is focused.*

| Shortcut | Action |
| :--- | :--- |
| **`F11`** | Toggle between Full Desktop App and Compact Gaming HUD |
| **`Right Arrow`** / **`Space`** | Advance to next step and mark completed |
| **`Left Arrow`** | Return to previous step |
| **`R`** | Open Bloon Threat Radar & Wave Inspector |
| **`T`** | Toggle Always-On-Top Pin on / off |
| **`Escape`** | Return from HUD Mode back to Full Desktop App |

---

## 🛠️ Project Structure

- `btd6_guide.pyw` — Main Windows desktop GUI application with HUD overlay, minimap, hero roster, threat radar, and visual step builder.
- `btd6_economy.py` — Canonical BTD6 pricing matrix (23 towers x 3 paths x 5 tiers), monotonic cash model, hero level scaling, and timing-aware cash availability.
- `btd6_replay.py` — Unified tower state replay engine and strategy validator shared across the editor, threat radar, validator, and compiler.
- `heroes_data.py` — Complete tactical database for all 16 heroes + map recommendation intelligence engine.
- `threat_radar_data.py` — Rounds 1–100 bloon wave compositions, RBE, danger alerts, and live defense verification logic.
- `guides.json` — Comprehensive local JSON database containing all 87 maps with Easy, Medium, and Hard strategies (261 total).
- `validate_guides.py` — Automated verification script checking coverage, data integrity, upgrade syntax, and economic sanity for all modes.
- `test_suite.py` — Comprehensive unit test suite covering the economic engine, validation engine, threat radar agreement, settings/data managers, and HTML export sanitization.
- `generate_guides_database.py` — Database compiler script that pre-validates and compiles modular map definitions and `user_overrides.json` into `guides.json`.
- `map_data_hard.py` — Hard difficulty (Rounds 3–80) strategy generator and late-game fortification / ZOMG logic.
- `map_data_medium.py` — Medium difficulty (Rounds 1–60) strategy generator and BFB battle logic.
- `map_data_beginner.py` — Strategy definitions for all 26 Beginner maps.
- `map_data_intermediate.py` — Strategy definitions for all 26 Intermediate maps.
- `map_data_advanced.py` — Strategy definitions for all 22 Advanced maps.
- `map_data_expert.py` — Strategy definitions for all 13 Expert maps.
- `user_settings.json` — Local user preferences (selected map, difficulty, font scaling, completed steps keyed by `step_id`, pin state).
- `user_overrides.json` — Local user strategy customizations that persist safely across database regenerations.

---

## 🧪 Validating the Database & Running Tests

### 1. Invariant Database Verification
To verify data integrity, coverage, upgrade path validity, and economic sanity across Easy, Medium, and Hard modes:
```bash
python validate_guides.py
```

### 2. Comprehensive Unit Test Suite
To run the automated regression test suite:
```bash
python test_suite.py
```

### Validation Checks Performed:
1. **Map Completeness**: Verifies all 87 official maps exist with correct difficulty categorization.
2. **Multi-Difficulty Coverage**: Validates that every map has Easy (R1–40), Medium (R1–60), and Hard (R3–80) verified strategies.
3. **Schema Integrity**: Validates all required fields (`name`, `category`, `terrain`, `lanes`, `water`, `sight_blockers`, `gimmick`, `steps`).
4. **Upgrade Syntax & Legality**: Confirms all upgrades match standard `X-Y-Z` notation and enforce canonical crosspathing rules (max tier 5, max 2 paths upgraded, secondary path max tier 2).
5. **Economic Feasibility**: Replays full tower progression by `tower_id`, calculates canonical purchase and upgrade costs with timing awareness (`before_round`, `during_round`, `after_round`), tracks 70% sell refunds, and enforces opening cash limits ($650).
6. **Threat Preparedness**: Validates Camo defense before Round 24, Lead popping before Round 28, MOAB defense by Round 40, BFB defense by Round 60, Ceramic rush defense before Round 63/76/78, and ZOMG defense by Round 80 using actual replayed tower capabilities.

---

## ✏️ Editing & Updating Guides

You can update strategies in two ways:

1. **Inside the GUI (Recommended)**:
   - Select the desired map and difficulty.
   - Click the **`✏️ Edit`** button in the top toolbar.
   - Use the **Visual Step Builder** to add, edit, remove, or reorder step cards with interactive upgrade spinners.
   - Or toggle to **Raw JSON** mode for direct JSON editing.
   - Click **`💾 Save Changes to Database`**: the editor validates the draft before mutating live state, saves the custom strategy to `user_overrides.json` (so your edits persist even if `generate_guides_database.py` is re-run), and updates `guides.json` atomically with `.bak` backup protection.
2. **Via Source Python Files**:
   - Edit the respective `map_data_<category>.py`, `map_data_medium.py`, or `map_data_hard.py` file.
   - Re-run `python generate_guides_database.py` to regenerate `guides.json`.
   - Click **`🔄 Reload`** in the application to immediately see the changes.

---

## 📤 Sharing Strategies & Exporting

- **Markdown Export**: Click **`📋 Copy Markdown`** in the toolbar to copy a formatted Reddit/Discord-ready strategy guide directly to your clipboard.
- **Printable Cheat Sheet**: Click **`🖨️ Export HTML`** in the toolbar to generate and open a clean, self-contained printable cheat sheet in your browser for dual-monitor or printed reference.
