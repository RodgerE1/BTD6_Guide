# Project: Bloons TD 6 — Complete Offline Strategy Guide

Build a fully functional Windows desktop application in Python 3 that provides detailed, round-by-round strategies for **every map in Bloons TD 6 on Easy / Standard difficulty**.

You are acting as the developer. **Do the work directly in the current Antigravity IDE workspace.** Create the files, research the strategies, populate the database, test the program, and fix any problems you discover.

Do not simply explain how to build the program or provide code for me to copy.

## 1. Primary Objective

Create an offline BTD6 strategy guide where I can:

- Select any BTD6 map using a drop-down menu.
- Select a difficulty using another drop-down menu.
- Read a detailed, step-by-step strategy for completing that map.
- Follow the guide while playing without needing an internet connection.
- Add and edit strategies later.

**Initial release: Every existing BTD6 map, Easy / Standard mode only, Rounds 1–40.**

Research the current complete map list, including Beginner, Intermediate, Advanced, and Expert maps. Do not rely on an outdated hardcoded list.

Include every available official map, not just popular or easy ones.

The database and application architecture must support Medium, Hard, Impoppable, CHIMPS, and additional modes later, but do not spend time generating those strategies yet.

## 2. Research and Generate Strategies

Research each map individually using reliable BTD6 references, community strategies, the Bloons Wiki, and current gameplay information where accessible.

For EACH map, generate a useful, detailed Easy / Standard strategy.

Every strategy should include:

- Recommended starting hero, if appropriate.
- First tower to purchase and its placement.
- Which towers to place on each subsequent step.
- Exact upgrade paths, such as 3-0-2 or 4-2-0.
- The round by which each tower or upgrade should be purchased.
- Clear tower positioning using landmarks and track entrances/exits.
- Targeting priorities where important (First, Strong, Last, Close).
- Special handling for Camo Bloons, Lead Bloons, and the Round 40 MOAB.
- A final explanation of why the strategy works.

Use clear instructions rather than vague advice.

For example:

**Round 1:** Place a Dart Monkey (0-0-0) near the first track intersection. Set targeting to First.

**Round 8:** Upgrade the Dart Monkey to 2-0-0.

**Round 15:** Place a Sniper Monkey on an available static platform.

**Round 28:** Ensure Lead Bloon popping capability is available.

**Round 40:** Explain the exact defense needed for the MOAB and its children.

These are formatting examples, NOT an actual strategy to copy.

Do not invent purchases, upgrade paths, prices, or placements.

Account for starting cash, income, hero prices, map placement restrictions, available line of sight, and upgrade costs on Easy difficulty. Do not recommend purchases earlier than they can realistically be afforded.

Research and correct any questionable strategies from previous examples rather than blindly copying them.

Favor reliable, relatively simple strategies with minimal micromanagement.

If a guide cannot be verified adequately, flag it clearly as needing review rather than presenting an invented strategy as tested.

## 3. Application Interface

Create a modern, dark-themed desktop GUI using Python 3 and Tkinter.

Suggested features:

- Dark background (#1e1e2e).
- Map selection drop-down, alphabetically sorted.
- Difficulty selection drop-down.
- Map category displayed prominently.
- Large, readable text with adjustable font size.
- Scrollable guide display.
- Bold tower names.
- Colored round headings.
- Highlighted tower upgrades (3-0-2).
- Search or filtering for map names.
- Buttons for Previous Step and Next Step.
- Optional checkbox to mark steps as completed.
- A Reset Progress button.
- An Edit Guide button.
- A Reload Database button.

The selected map and difficulty should be remembered when the application is reopened.

Include a status indicator showing how many maps have completed guides and how many need review.

## 4. Guide Formatting

Organize each guide into sensible round ranges, such as:

### Rounds 1–10: Opening Defense
Explain initial placement and starting upgrades.

### Rounds 11–20: Expanding Defense
Explain which towers and upgrades are needed.

### Rounds 21–30: Camo and Lead Preparation
Explain important Bloon types and countermeasures.

### Rounds 31–39: Final Preparation
Explain defensive improvements and MOAB preparation.

### Round 40: MOAB Battle
Give exact instructions for completing the final round.

The actual steps and round ranges should reflect each map's strategy. Do not blindly repeat identical generic strategies for every map.

## 5. Local Database

Store all map information and strategies locally in `guides.json`, or in a better structured local database if justified.

Each map should have:

- Map name
- Map category
- Difficulty
- Overview
- Strategy steps
- Tower placements
- Upgrades
- Round requirements
- Research sources
- Verification/review status

Design the database so additional difficulties and strategies can be added without rewriting the application.

Preserve existing data when adding new guides.

Provide a way to edit individual guides directly inside the application.

## 6. Offline Requirements

After installation and initial data generation:

- The application must operate completely offline.
- All generated Easy guides must be stored locally.
- No Gemini API connection is required to read guides.
- No account or subscription is necessary to use the viewer.
- No cloud database is required.

Online research during the initial development process is permitted.

If online guide generation is added for future expansion, it must be an optional feature and must never interfere with offline operation.

## 7. Completeness Requirements

**Do not stop after creating two or three example maps.**

Work through the entire current BTD6 map list.

Use a generation and validation pipeline if that is more efficient than writing every strategy manually.

Process maps in batches if needed, saving progress after each batch.

The application must distinguish between complete guides, drafts needing review, and missing guides.

Do not mark an empty or placeholder guide as complete.

Before declaring the project finished:

1. Compare the database against the complete current BTD6 map list.
2. Identify missing maps.
3. Confirm every map appears in the drop-down menu.
4. Confirm every map has an Easy strategy entry.
5. Check upgrade-path validity and apparent economic feasibility.
6. Identify unverified strategies clearly.
7. Make sure the application reads every guide without errors.
8. Confirm that switching maps and editing guides works correctly.

Do not claim that a strategy was playtested unless it was actually tested in the game.

## 8. Files and Testing

Create the following files inside the current workspace:

- `btd6_guide.pyw` — Main Windows desktop application.
- `guides.json` — Complete local map and strategy database.
- `README.md` — Instructions for running and updating the application.
- `validate_guides.py` — Validation script checking guide coverage, completeness, and data integrity.
- Additional source files as needed.

Use Python 3. Prefer standard-library dependencies where practical.

Run syntax and validation tests and launch the GUI if the environment supports graphical execution.

Resolve any errors found.

Do not overwrite valuable existing project data without preserving it.

## 9. Future Expansion

Build the application with future support for:

- Medium strategies (Rounds 1–60).
- Hard strategies (Rounds 3–80).
- Impoppable.
- CHIMPS.
- Additional map releases.
- Multiple alternative strategies for the same map.
- Strategy updates when tower costs or game mechanics change.

Do not generate these additional difficulties yet.

## 10. Final Deliverable

I want a working desktop application, not a prototype or partial code example.

When finished, provide a concise report containing:

- Total official maps identified.
- Total Easy guides generated.
- Number of guides verified through available evidence.
- Number still requiring gameplay verification.
- Any maps or guides not completed.
- Test results.
- Exact application launch instructions.

**Begin developing the project now. Research every official map and complete as much of the full Easy strategy database as possible. Prioritize accurate, usable guides over unsupported claims of completeness. Do not stop at a two-map demonstration.**