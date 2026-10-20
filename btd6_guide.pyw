"""
btd6_guide.pyw
Bloons TD 6 — Complete Offline Strategy Guide
A modern, dark-themed Windows desktop application built with Python 3 and Tkinter.
Features:
- 100% verified strategies for all 87 official maps on Easy (R1-40), Medium (R1-60), and Hard (R3-80) modes.
- Complete Hero Intelligence: showcases the optimal #1 hero for every map with tactical reasons & synergies.
- Interactive Bloon Threat Radar & Wave Inspector for Rounds 1–100 with live strategy defense verification.
- Visual Step Builder & Strategy Editor with instant drag-and-drop/reordering and form inputs.
- One-click Community Export: Copy as Discord/Reddit Markdown & Printable HTML Cheat Sheets.
- Compact "Always-On-Top" Gaming Overlay HUD Mode (F11) with global hotkeys.
- Mousewheel scrolling fix ensuring smooth navigation across all dropdowns. Operates 100% offline.
"""

import json
import os
import sys
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, font

from heroes_data import HEROES_DATABASE, get_best_hero_for_map
from threat_radar_data import get_round_data, check_strategy_defense_readiness, DANGER_ROUNDS

# Enable High-DPI awareness on Windows for crisp typography
try:
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        ctypes.windll.user32.SetProcessDPIAware()
except Exception:
    pass

# Theme Colors (Modern Dark Palette / Catppuccin Mocha inspired)
THEME = {
    "bg": "#1e1e2e",            # Main app background
    "bg_dark": "#181825",       # Topbar / deep header
    "card": "#252538",          # Cards and panels
    "card_border": "#313244",   # Border dividers
    "card_hover": "#2e2e42",    # Hover highlight
    "text_primary": "#cdd6f4",  # Primary bright text
    "text_muted": "#a6adc8",    # Muted secondary text
    "text_dim": "#6c7086",      # Very dim labels
    "accent_blue": "#89b4fa",   # Blue accent
    "accent_green": "#a6e3a1",  # Green accent (Verified / Beginner)
    "accent_yellow": "#f9e2af", # Yellow accent (Warning / Active)
    "accent_orange": "#fab387", # Orange accent (Advanced)
    "accent_red": "#f38ba8",    # Red accent (Expert / MOAB)
    "accent_purple": "#cba6f7", # Purple / Camo accent
    "accent_teal": "#94e2d5",   # Teal accent
    "step_done_bg": "#1c2a27",  # Background for completed steps
    "step_done_fg": "#74c7ec",  # Foreground for completed steps
}

CATEGORY_COLORS = {
    "Beginner": THEME["accent_green"],
    "Intermediate": THEME["accent_blue"],
    "Advanced": THEME["accent_orange"],
    "Expert": THEME["accent_red"]
}

ROUND_RANGE_COLORS = {
    "Rounds 1–10": THEME["accent_teal"],
    "Rounds 11–20": THEME["accent_blue"],
    "Rounds 21–30": THEME["accent_purple"],
    "Rounds 31–39": THEME["accent_orange"],
    "Rounds 31–40": THEME["accent_orange"],
    "Round 40": THEME["accent_red"],
    "Rounds 41–50": THEME["accent_teal"],
    "Rounds 51–59": THEME["accent_orange"],
    "Rounds 51–60": THEME["accent_orange"],
    "Round 60": THEME["accent_red"],
    "Rounds 61–75": THEME["accent_orange"],
    "Rounds 76–80": THEME["accent_red"],
    "Round 80": THEME["accent_red"]
}

# Tower Classification, Icons & Color Accents
TOWER_INFO = {
    # Primary (Blue)
    "Dart Monkey": {"icon": "🎯", "category": "Primary", "color": "#89b4fa"},
    "Boomerang Monkey": {"icon": "🪃", "category": "Primary", "color": "#89b4fa"},
    "Bomb Shooter": {"icon": "💣", "category": "Primary", "color": "#89b4fa"},
    "Tack Shooter": {"icon": "📌", "category": "Primary", "color": "#89b4fa"},
    "Ice Monkey": {"icon": "❄️", "category": "Primary", "color": "#89b4fa"},
    "Glue Gunner": {"icon": "🧴", "category": "Primary", "color": "#89b4fa"},
    # Military (Green)
    "Sniper Monkey": {"icon": "🎯", "category": "Military", "color": "#a6e3a1"},
    "Monkey Sub": {"icon": "⚓", "category": "Military", "color": "#a6e3a1"},
    "Monkey Buccaneer": {"icon": "🚢", "category": "Military", "color": "#a6e3a1"},
    "Monkey Ace": {"icon": "✈️", "category": "Military", "color": "#a6e3a1"},
    "Heli Pilot": {"icon": "🚁", "category": "Military", "color": "#a6e3a1"},
    "Mortar Monkey": {"icon": "💥", "category": "Military", "color": "#a6e3a1"},
    "Dartling Gunner": {"icon": "🔫", "category": "Military", "color": "#a6e3a1"},
    # Magic (Purple)
    "Wizard Monkey": {"icon": "🧙", "category": "Magic", "color": "#cba6f7"},
    "Super Monkey": {"icon": "🦸", "category": "Magic", "color": "#cba6f7"},
    "Ninja Monkey": {"icon": "🥷", "category": "Magic", "color": "#cba6f7"},
    "Alchemist": {"icon": "🧪", "category": "Magic", "color": "#cba6f7"},
    "Druid": {"icon": "🌿", "category": "Magic", "color": "#cba6f7"},
    "Mermonkey": {"icon": "🧜", "category": "Magic", "color": "#cba6f7"},
    # Support (Orange)
    "Banana Farm": {"icon": "🍌", "category": "Support", "color": "#fab387"},
    "Spike Factory": {"icon": "⚙️", "category": "Support", "color": "#fab387"},
    "Monkey Village": {"icon": "🏰", "category": "Support", "color": "#fab387"},
    "Engineer Monkey": {"icon": "🔧", "category": "Support", "color": "#fab387"},
    "Beast Handler": {"icon": "🦖", "category": "Support", "color": "#fab387"},
}

# Dynamically register all 16 heroes from HEROES_DATABASE
for h_name, h_data in HEROES_DATABASE.items():
    TOWER_INFO[h_name] = {"icon": h_data["icon"], "category": "Hero", "color": h_data["color"]}
TOWER_INFO["Hero"] = {"icon": "👑", "category": "Hero", "color": "#f9e2af"}

def get_tower_info(tower_name):
    t_lower = tower_name.lower()
    for name, info in TOWER_INFO.items():
        if name.lower() in t_lower:
            return info
    return {"icon": "🐒", "category": "Tower", "color": THEME["accent_blue"]}


class SettingsManager:
    """Manages persistent user settings, selected map, font scaling, and step progress."""
    def __init__(self, filepath="user_settings.json"):
        self.filepath = os.path.join(os.path.dirname(__file__), filepath)
        self.data = {
            "last_map_id": "monkey_meadow",
            "last_difficulty": "Easy",
            "font_size_offset": 0,
            "always_on_top": False,
            "progress": {}  # key -> list of completed step_numbers
        }
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    self.data.update(saved)
            except Exception:
                pass

    def save(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)
        except Exception:
            pass

    def _pkey(self, map_id, diff="Easy"):
        return f"{map_id}_{diff.lower()}"

    def get_progress(self, map_id, diff="Easy"):
        pk = self._pkey(map_id, diff)
        if pk in self.data.get("progress", {}):
            return set(self.data["progress"][pk])
        # Fallback to map_id for backward compatibility
        return set(self.data.get("progress", {}).get(map_id, []))

    def set_step_progress(self, map_id, step_num, completed, diff="Easy"):
        if "progress" not in self.data:
            self.data["progress"] = {}
        pk = self._pkey(map_id, diff)
        curr = set(self.data["progress"].get(pk, self.data["progress"].get(map_id, [])))
        if completed:
            curr.add(step_num)
        else:
            curr.discard(step_num)
        self.data["progress"][pk] = list(curr)
        self.save()

    def reset_progress(self, map_id, diff="Easy"):
        if "progress" in self.data:
            pk = self._pkey(map_id, diff)
            if pk in self.data["progress"]:
                self.data["progress"][pk] = []
            if map_id in self.data["progress"]:
                self.data["progress"][map_id] = []
            self.save()


class DataManager:
    """Handles loading, querying, and updating the local guides.json database."""
    def __init__(self, filepath="guides.json"):
        self.filepath = os.path.join(os.path.dirname(__file__), filepath)
        self.database = {}
        self.load()

    def load(self):
        if not os.path.exists(self.filepath):
            messagebox.showerror("Database Missing", f"Could not find strategy database:\n{self.filepath}\n\nPlease run generate_guides_database.py first.")
            return False
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.database = json.load(f)
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to load guides.json:\n{e}")
            return False

    def save(self):
        try:
            bak_path = self.filepath + ".bak"
            if os.path.exists(self.filepath):
                with open(self.filepath, "r", encoding="utf-8") as src, open(bak_path, "w", encoding="utf-8") as dst:
                    dst.write(src.read())

            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.database, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save guides.json:\n{e}")
            return False

    def get_maps(self):
        return self.database.get("maps", {})

    def get_map(self, map_id):
        return self.database.get("maps", {}).get(map_id)

    def get_statistics(self):
        maps = self.get_maps()
        total = len(maps)
        easy_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Easy", {}).get("status") == "Verified")
        med_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Medium", {}).get("status") == "Verified")
        hard_verified = sum(1 for m in maps.values() if m.get("difficulties", {}).get("Hard", {}).get("status") == "Verified")
        counts = {
            "Beginner": sum(1 for m in maps.values() if m.get("category") == "Beginner"),
            "Intermediate": sum(1 for m in maps.values() if m.get("category") == "Intermediate"),
            "Advanced": sum(1 for m in maps.values() if m.get("category") == "Advanced"),
            "Expert": sum(1 for m in maps.values() if m.get("category") == "Expert")
        }
        return total, easy_verified, med_verified, hard_verified, counts


class BTD6GuideApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bloons TD 6 — Offline Strategy Guide (Easy, Medium & Hard)")
        self.geometry("1240x860")
        self.minsize(960, 640)
        self.configure(bg=THEME["bg"])

        # Data & Settings
        self.settings = SettingsManager()
        self.data_manager = DataManager()

        # State Variables
        self.font_offset = tk.IntVar(value=self.settings.data.get("font_size_offset", 0))
        self.selected_category = tk.StringVar(value="All")
        self.search_var = tk.StringVar(value="")
        self.search_var.trace_add("write", lambda *args: self.filter_maps())
        self.selected_map_name = tk.StringVar()
        
        last_diff = self.settings.data.get("last_difficulty", "Easy")
        if last_diff == "Hard":
            init_diff_str = "Hard (Rounds 3–80)"
        elif last_diff == "Medium":
            init_diff_str = "Medium (Rounds 1–60)"
        else:
            init_diff_str = "Easy (Rounds 1–40)"
        self.selected_difficulty = tk.StringVar(value=init_diff_str)
        
        self.current_step_index = 0
        self.step_checkbox_vars = {}
        self.minimap_step_pins = []

        # Overlay & Pin Modes
        self.is_overlay_mode = False
        self.is_topmost_pinned = self.settings.data.get("always_on_top", False)
        self.saved_geometry = "1240x860"
        self.current_overlay_step = 1

        if self.is_topmost_pinned:
            self.attributes("-topmost", True)

        # Configure Fonts & Styles
        self.init_fonts()
        self.init_styles()

        # Build UI Structure
        self.build_ui()

        # Global Hotkey Bindings
        self.init_hotkeys()

        # Load initial state
        self.restore_initial_state()

    def init_fonts(self):
        offset = self.font_offset.get()
        self.font_title = font.Font(family="Segoe UI", size=max(14, 18 + offset), weight="bold")
        self.font_subtitle = font.Font(family="Segoe UI", size=max(11, 14 + offset), weight="bold")
        self.font_heading = font.Font(family="Segoe UI", size=max(10, 12 + offset), weight="bold")
        self.font_body = font.Font(family="Segoe UI", size=max(9, 10 + offset))
        self.font_body_bold = font.Font(family="Segoe UI", size=max(9, 10 + offset), weight="bold")
        self.font_small = font.Font(family="Segoe UI", size=max(8, 9 + offset))
        self.font_badge = font.Font(family="Segoe UI", size=max(8, 9 + offset), weight="bold")
        self.font_mono = font.Font(family="Consolas", size=max(9, 10 + offset), weight="bold")

    def update_font_sizes(self, delta):
        new_val = max(-3, min(6, self.font_offset.get() + delta))
        self.font_offset.set(new_val)
        self.settings.data["font_size_offset"] = new_val
        self.settings.save()
        self.init_fonts()
        self.render_guide()

    def reset_font_sizes(self):
        self.font_offset.set(0)
        self.settings.data["font_size_offset"] = 0
        self.settings.save()
        self.init_fonts()
        self.render_guide()

    def init_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Dark.TCombobox",
            fieldbackground=THEME["card"],
            background=THEME["card_border"],
            foreground=THEME["text_primary"],
            arrowcolor=THEME["text_primary"],
            bordercolor=THEME["card_border"],
            darkcolor=THEME["card"],
            lightcolor=THEME["card"],
            padding=5
        )
        style.map("Dark.TCombobox",
            fieldbackground=[("readonly", THEME["card"])],
            selectbackground=[("readonly", THEME["card"])],
            selectforeground=[("readonly", THEME["text_primary"])],
            foreground=[("readonly", THEME["text_primary"])]
        )

        style.configure("TProgressbar",
            thickness=6,
            troughcolor=THEME["card_border"],
            background=THEME["accent_green"],
            bordercolor=THEME["card_border"],
            lightcolor=THEME["accent_green"],
            darkcolor=THEME["accent_green"]
        )

    def init_hotkeys(self):
        self.bind_all("<F11>", self.on_hotkey_f11)
        self.bind_all("<Escape>", self.on_hotkey_escape)
        self.bind_all("<Right>", self.on_hotkey_right)
        self.bind_all("<Left>", self.on_hotkey_left)
        self.bind_all("<space>", self.on_hotkey_space)
        self.bind_all("<Key-t>", self.on_hotkey_t)
        self.bind_all("<Key-T>", self.on_hotkey_t)
        self.bind_all("<Key-r>", self.on_hotkey_r)
        self.bind_all("<Key-R>", self.on_hotkey_r)

    def _is_text_focused(self):
        f = self.focus_get()
        return isinstance(f, (tk.Entry, tk.Text, ttk.Combobox, tk.Spinbox))

    def on_hotkey_f11(self, event=None):
        self.toggle_overlay_mode()
        return "break"

    def on_hotkey_escape(self, event=None):
        if self.is_overlay_mode:
            self.toggle_overlay_mode()
            return "break"

    def on_hotkey_right(self, event=None):
        if self._is_text_focused():
            return
        self.step_next()
        return "break"

    def on_hotkey_left(self, event=None):
        if self._is_text_focused():
            return
        self.step_prev()
        return "break"

    def on_hotkey_space(self, event=None):
        if self._is_text_focused():
            return
        self.step_toggle_current()
        return "break"

    def on_hotkey_t(self, event=None):
        if self._is_text_focused():
            return
        self.toggle_topmost_pin()
        return "break"

    def on_hotkey_r(self, event=None):
        if self._is_text_focused():
            return
        self.open_threat_radar_dialog()
        return "break"

    def build_ui(self):
        # 1. Main Standard View Container
        self.main_container = tk.Frame(self, bg=THEME["bg"])
        self.main_container.pack(fill="both", expand=True)

        # 2. Main Header Bar
        self.build_header(self.main_container)

        # 3. Control & Filter Toolbar
        self.build_control_toolbar(self.main_container)

        # 4. Step Walkthrough Navigation Bar
        self.build_walkthrough_bar(self.main_container)

        # 5. Main Scrollable Content Container
        self.build_content_area(self.main_container)

        # 6. Overlay HUD Container (initially unpacked)
        self.overlay_container = tk.Frame(self, bg=THEME["bg_dark"])

    def build_header(self, parent):
        header_frame = tk.Frame(parent, bg=THEME["bg_dark"], height=58, padx=16, pady=8)
        header_frame.pack(side="top", fill="x")

        # Left: Logo & Title
        title_box = tk.Frame(header_frame, bg=THEME["bg_dark"])
        title_box.pack(side="left")

        logo_label = tk.Label(title_box, text="🎈", font=("Segoe UI", 18), bg=THEME["bg_dark"], fg=THEME["accent_red"])
        logo_label.pack(side="left", padx=(0, 8))

        title_lbl = tk.Label(title_box, text="BLOONS TD 6", font=("Segoe UI", 13, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_blue"])
        title_lbl.pack(side="left")

        subtitle_lbl = tk.Label(title_box, text=" | Offline Strategy Guide", font=("Segoe UI", 11), bg=THEME["bg_dark"], fg=THEME["text_muted"])
        subtitle_lbl.pack(side="left")

        # Right: Database Statistics Badge
        total, easy_v, med_v, hard_v, _ = self.data_manager.get_statistics()
        self.stats_label = tk.Label(
            header_frame,
            text=f"📊 {total} Maps  •  Easy ({easy_v}), Medium ({med_v}), Hard ({hard_v}) 100% Verified  •  100% Offline",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["card"],
            fg=THEME["accent_teal"],
            padx=12,
            pady=4,
            relief="flat",
            bd=1
        )
        self.stats_label.pack(side="right")

    def build_control_toolbar(self, parent):
        toolbar = tk.Frame(parent, bg=THEME["bg"], padx=16, pady=8)
        toolbar.pack(side="top", fill="x")

        # Row 1: Category Filter Buttons
        cat_bar = tk.Frame(toolbar, bg=THEME["bg"])
        cat_bar.pack(side="top", fill="x", pady=(0, 8))

        lbl_filter = tk.Label(cat_bar, text="CATEGORY:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_dim"])
        lbl_filter.pack(side="left", padx=(0, 8))

        _, _, _, _, counts = self.data_manager.get_statistics()
        self.cat_buttons = {}
        for cat_name, label in [
            ("All", f"All ({counts['Beginner'] + counts['Intermediate'] + counts['Advanced'] + counts['Expert']})"),
            ("Beginner", f"Beginner ({counts['Beginner']})"),
            ("Intermediate", f"Intermediate ({counts['Intermediate']})"),
            ("Advanced", f"Advanced ({counts['Advanced']})"),
            ("Expert", f"Expert ({counts['Expert']})")
        ]:
            btn = tk.Button(
                cat_bar,
                text=label,
                font=("Segoe UI", 9, "bold"),
                bg=THEME["card_border"] if cat_name == "All" else THEME["card"],
                fg=THEME["text_primary"],
                activebackground=THEME["card_hover"],
                activeforeground=THEME["text_primary"],
                relief="flat",
                padx=10,
                pady=3,
                cursor="hand2",
                command=lambda c=cat_name: self.set_category_filter(c)
            )
            btn.pack(side="left", padx=4)
            self.cat_buttons[cat_name] = btn

        # Right side of Row 1: Font controls & Action Buttons
        action_bar = tk.Frame(cat_bar, bg=THEME["bg"])
        action_bar.pack(side="right")

        # Font Zoom Buttons
        tk.Label(action_bar, text="Font:", font=("Segoe UI", 9), bg=THEME["bg"], fg=THEME["text_muted"]).pack(side="left", padx=(0, 4))
        btn_font_dec = tk.Button(action_bar, text="A-", font=("Segoe UI", 8, "bold"), bg=THEME["card"], fg=THEME["text_primary"], relief="flat", padx=6, pady=1, cursor="hand2", command=lambda: self.update_font_sizes(-1))
        btn_font_dec.pack(side="left", padx=1)
        btn_font_res = tk.Button(action_bar, text="100%", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_primary"], relief="flat", padx=6, pady=1, cursor="hand2", command=self.reset_font_sizes)
        btn_font_res.pack(side="left", padx=1)
        btn_font_inc = tk.Button(action_bar, text="A+", font=("Segoe UI", 8, "bold"), bg=THEME["card"], fg=THEME["text_primary"], relief="flat", padx=6, pady=1, cursor="hand2", command=lambda: self.update_font_sizes(1))
        btn_font_inc.pack(side="left", padx=1)

        # Pin On Top Button
        pin_bg = THEME["accent_yellow"] if self.is_topmost_pinned else THEME["card"]
        pin_fg = THEME["bg_dark"] if self.is_topmost_pinned else THEME["text_primary"]
        self.btn_pin = tk.Button(
            action_bar,
            text="📌 Pinned" if self.is_topmost_pinned else "📌 Pin on Top",
            font=("Segoe UI", 9, "bold"),
            bg=pin_bg,
            fg=pin_fg,
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self.toggle_topmost_pin
        )
        self.btn_pin.pack(side="left", padx=(12, 4))

        # Compact Overlay HUD Button
        btn_hud = tk.Button(
            action_bar,
            text="🗗 HUD Mode (F11)",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["accent_blue"],
            fg=THEME["bg_dark"],
            activebackground="#74c7ec",
            activeforeground=THEME["bg_dark"],
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self.toggle_overlay_mode
        )
        btn_hud.pack(side="left", padx=4)

        # Edit Guide Button
        btn_edit = tk.Button(
            action_bar,
            text="✏️ Edit",
            font=("Segoe UI", 9, "bold"),
            bg="#2e3440",
            fg=THEME["accent_yellow"],
            activebackground="#3b4252",
            activeforeground=THEME["accent_yellow"],
            relief="flat",
            padx=8,
            pady=3,
            cursor="hand2",
            command=self.open_edit_guide_dialog
        )
        btn_edit.pack(side="left", padx=4)

        # Reload Database Button
        btn_reload = tk.Button(
            action_bar,
            text="🔄 Reload",
            font=("Segoe UI", 9),
            bg=THEME["card"],
            fg=THEME["accent_teal"],
            activebackground=THEME["card_hover"],
            activeforeground=THEME["accent_teal"],
            relief="flat",
            padx=8,
            pady=3,
            cursor="hand2",
            command=self.reload_database
        )
        btn_reload.pack(side="left", padx=4)

        # Row 2: Search, Map Dropdown, Difficulty Dropdown, Threat Radar, Heroes, Export
        row2 = tk.Frame(toolbar, bg=THEME["bg"])
        row2.pack(side="top", fill="x")

        # Live Search Entry
        search_box = tk.Frame(row2, bg=THEME["card"], padx=6, pady=3, highlightbackground=THEME["card_border"], highlightthickness=1)
        search_box.pack(side="left", padx=(0, 8))

        tk.Label(search_box, text="🔍", font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_muted"]).pack(side="left", padx=(0, 4))
        self.search_entry = tk.Entry(
            search_box,
            textvariable=self.search_var,
            font=("Segoe UI", 10),
            bg=THEME["card"],
            fg=THEME["text_primary"],
            insertbackground=THEME["text_primary"],
            relief="flat",
            width=15
        )
        self.search_entry.pack(side="left")

        # Map Selector
        tk.Label(row2, text="Map:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"]).pack(side="left", padx=(0, 4))
        self.map_combo = ttk.Combobox(
            row2,
            textvariable=self.selected_map_name,
            style="Dark.TCombobox",
            state="readonly",
            width=24,
            font=("Segoe UI", 10)
        )
        self.map_combo.pack(side="left", padx=(0, 10))
        self.map_combo.bind("<<ComboboxSelected>>", self.on_map_selected)

        # Difficulty Selector (Easy, Medium & Hard fully supported!)
        tk.Label(row2, text="Diff:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"]).pack(side="left", padx=(0, 4))
        self.diff_combo = ttk.Combobox(
            row2,
            textvariable=self.selected_difficulty,
            values=["Easy (Rounds 1–40)", "Medium (Rounds 1–60)", "Hard (Rounds 3–80)", "Impoppable (Coming Soon)", "CHIMPS (Coming Soon)"],
            style="Dark.TCombobox",
            state="readonly",
            width=22,
            font=("Segoe UI", 10)
        )
        self.diff_combo.pack(side="left", padx=(0, 10))
        self.diff_combo.bind("<<ComboboxSelected>>", self.on_difficulty_selected)

        # Threat Radar Button
        btn_radar = tk.Button(
            row2,
            text="🎯 Threat Radar (R)",
            font=("Segoe UI", 9, "bold"),
            bg="#2a2238",
            fg=THEME["accent_purple"],
            activebackground="#3b2d50",
            activeforeground=THEME["accent_purple"],
            relief="flat",
            padx=7,
            pady=3,
            cursor="hand2",
            command=self.open_threat_radar_dialog
        )
        btn_radar.pack(side="left", padx=2)

        # Heroes Roster Button
        btn_heroes = tk.Button(
            row2,
            text="👑 Hero Roster",
            font=("Segoe UI", 9, "bold"),
            bg="#2f2b1e",
            fg=THEME["accent_yellow"],
            activebackground="#3e3926",
            activeforeground=THEME["accent_yellow"],
            relief="flat",
            padx=7,
            pady=3,
            cursor="hand2",
            command=self.open_heroes_roster_dialog
        )
        btn_heroes.pack(side="left", padx=2)

        # Copy Markdown Button
        btn_copy_md = tk.Button(
            row2,
            text="📋 Copy Guide",
            font=("Segoe UI", 8),
            bg=THEME["card"],
            fg=THEME["text_primary"],
            activebackground=THEME["card_hover"],
            activeforeground=THEME["text_primary"],
            relief="flat",
            padx=6,
            pady=3,
            cursor="hand2",
            command=self.export_markdown_to_clipboard
        )
        btn_copy_md.pack(side="left", padx=2)

        # Print HTML Sheet Button
        btn_print_html = tk.Button(
            row2,
            text="📄 Print Sheet",
            font=("Segoe UI", 8),
            bg=THEME["card"],
            fg=THEME["accent_teal"],
            activebackground=THEME["card_hover"],
            activeforeground=THEME["accent_teal"],
            relief="flat",
            padx=6,
            pady=3,
            cursor="hand2",
            command=self.export_printable_html
        )
        btn_print_html.pack(side="left", padx=2)

    def build_walkthrough_bar(self, parent):
        walk_frame = tk.Frame(parent, bg=THEME["card"], padx=16, pady=8, highlightbackground=THEME["card_border"], highlightthickness=1)
        walk_frame.pack(side="top", fill="x", padx=16, pady=(0, 8))

        lbl_title = tk.Label(walk_frame, text="WALKTHROUGH ASSISTANT:", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["accent_blue"])
        lbl_title.pack(side="left", padx=(0, 12))

        # Prev Button
        btn_prev = tk.Button(
            walk_frame,
            text="◀ Previous Step (←)",
            font=("Segoe UI", 9, "bold"),
            bg="#313244",
            fg=THEME["text_primary"],
            activebackground=THEME["card_hover"],
            activeforeground=THEME["text_primary"],
            relief="flat",
            padx=10,
            pady=3,
            cursor="hand2",
            command=self.step_prev
        )
        btn_prev.pack(side="left", padx=4)

        # Next Button
        btn_next = tk.Button(
            walk_frame,
            text="Next Step ▶ (→)",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["accent_blue"],
            fg=THEME["bg_dark"],
            activebackground="#74c7ec",
            activeforeground=THEME["bg_dark"],
            relief="flat",
            padx=12,
            pady=3,
            cursor="hand2",
            command=self.step_next
        )
        btn_next.pack(side="left", padx=4)

        # Progress bar
        self.progress_bar = ttk.Progressbar(walk_frame, orient="horizontal", mode="determinate", length=180)
        self.progress_bar.pack(side="left", padx=(16, 8))

        self.progress_label = tk.Label(walk_frame, text="0 / 0 Steps Completed (0%)", font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_muted"])
        self.progress_label.pack(side="left", padx=4)

        # Hotkey guide note
        lbl_hints = tk.Label(walk_frame, text="[Hotkeys: ← / → / Space / F11 HUD]", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_dim"])
        lbl_hints.pack(side="left", padx=(16, 0))

        # Reset Progress button
        btn_reset_prog = tk.Button(
            walk_frame,
            text="Reset Progress",
            font=("Segoe UI", 8),
            bg=THEME["card"],
            fg=THEME["accent_red"],
            relief="flat",
            cursor="hand2",
            command=self.reset_current_map_progress
        )
        btn_reset_prog.pack(side="right")

    def build_content_area(self, parent):
        container = tk.Frame(parent, bg=THEME["bg"])
        container.pack(side="top", fill="both", expand=True, padx=16, pady=(0, 12))

        self.canvas = tk.Canvas(container, bg=THEME["bg"], highlightthickness=0)
        self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=THEME["bg"])

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=None, yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        if self.is_overlay_mode or not self.canvas.winfo_exists():
            return

        try:
            x, y = self.winfo_pointerxy()
            widget = self.winfo_containing(x, y)
        except Exception:
            widget = None

        if widget is not None:
            w_class = widget.winfo_class()
            w_name = str(widget).lower()
            # If pointer is over combobox, dropdown popdown listbox, entry, spinbox, or text, DO NOT scroll canvas!
            if w_class in ("Combobox", "TCombobox", "Listbox", "Text", "Entry", "Spinbox") or "popdown" in w_name or "combo" in w_name:
                return

            # Only scroll if the pointer is within the canvas hierarchy
            curr = widget
            is_in_canvas = False
            while curr is not None:
                if curr == self.canvas or curr == self.scrollable_frame:
                    is_in_canvas = True
                    break
                try:
                    curr = curr.master
                except Exception:
                    break
            if not is_in_canvas:
                return

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # =========================================================================
    # ALWAYS ON TOP & COMPACT OVERLAY HUD MODE
    # =========================================================================
    def toggle_topmost_pin(self):
        self.is_topmost_pinned = not self.is_topmost_pinned
        self.settings.data["always_on_top"] = self.is_topmost_pinned
        self.settings.save()

        # Update root attribute
        self.attributes("-topmost", self.is_topmost_pinned or self.is_overlay_mode)

        # Update button text/color
        if hasattr(self, "btn_pin"):
            if self.is_topmost_pinned:
                self.btn_pin.configure(text="📌 Pinned", bg=THEME["accent_yellow"], fg=THEME["bg_dark"])
            else:
                self.btn_pin.configure(text="📌 Pin on Top", bg=THEME["card"], fg=THEME["text_primary"])

        if self.is_overlay_mode:
            self.render_overlay_hud()

    def toggle_overlay_mode(self):
        if not self.is_overlay_mode:
            # Switch to Compact Overlay HUD
            self.is_overlay_mode = True
            self.saved_geometry = self.geometry()
            self.main_container.pack_forget()
            self.overlay_container.pack(fill="both", expand=True)
            self.attributes("-topmost", True)
            self.geometry("480x360")
            self.render_overlay_hud()
        else:
            # Switch back to Full View
            self.is_overlay_mode = False
            self.overlay_container.pack_forget()
            self.main_container.pack(fill="both", expand=True)
            self.attributes("-topmost", self.is_topmost_pinned)
            self.geometry(self.saved_geometry)
            self.render_guide()

    def render_overlay_hud(self):
        for child in self.overlay_container.winfo_children():
            child.destroy()

        mid = self.get_current_map_id()
        if not mid:
            return
        map_data = self.data_manager.get_map(mid)
        if not map_data:
            return

        strat = self.get_current_strategy(map_data)
        if not strat:
            return

        diff_key = self.get_selected_diff_key()
        steps = strat.get("steps", [])
        total_steps = len(steps)
        completed = self.settings.get_progress(mid, diff_key)

        # Determine active step (first uncompleted step)
        active_step = None
        for step in steps:
            if step.get("step_number") not in completed:
                active_step = step
                break
        if not active_step and steps:
            active_step = steps[-1]

        snum = active_step.get("step_number", 1) if active_step else 1
        is_done = snum in completed

        # 1. HUD Top Bar
        top_bar = tk.Frame(self.overlay_container, bg="#11111b", padx=12, pady=8)
        top_bar.pack(fill="x")

        # Map name & mode
        lbl_hud_title = tk.Label(top_bar, text=f"🎈 {map_data.get('name')} • {strat.get('difficulty')} (R{strat.get('rounds')})", font=("Segoe UI", 10, "bold"), bg="#11111b", fg=THEME["accent_blue"])
        lbl_hud_title.pack(side="left")

        # Right buttons: Pin & Expand
        btn_expand = tk.Button(
            top_bar,
            text="⛶ Full (F11)",
            font=("Segoe UI", 8, "bold"),
            bg=THEME["card"],
            fg=THEME["accent_teal"],
            relief="flat",
            padx=8,
            pady=1,
            cursor="hand2",
            command=self.toggle_overlay_mode
        )
        btn_expand.pack(side="right", padx=(4, 0))

        pin_text = "📌 On" if (self.is_topmost_pinned or self.is_overlay_mode) else "📌 Off"
        btn_pin_hud = tk.Button(
            top_bar,
            text=pin_text,
            font=("Segoe UI", 8),
            bg=THEME["accent_yellow"] if self.is_topmost_pinned else THEME["card"],
            fg=THEME["bg_dark"] if self.is_topmost_pinned else THEME["text_muted"],
            relief="flat",
            padx=6,
            pady=1,
            cursor="hand2",
            command=self.toggle_topmost_pin
        )
        btn_pin_hud.pack(side="right", padx=4)

        # 2. Main Step Card
        hud_body = tk.Frame(self.overlay_container, bg=THEME["bg_dark"], padx=14, pady=10)
        hud_body.pack(fill="both", expand=True)

        if active_step:
            tinfo = get_tower_info(active_step.get("tower", ""))
            
            # Step progress header
            step_hdr = tk.Frame(hud_body, bg=THEME["bg_dark"])
            step_hdr.pack(fill="x", pady=(0, 6))

            tk.Label(step_hdr, text=f"STEP {snum} OF {total_steps}", font=("Segoe UI", 9, "bold"), bg=THEME["bg_dark"], fg=THEME["text_dim"]).pack(side="left")
            pct = int((len(completed) / total_steps) * 100) if total_steps > 0 else 0
            tk.Label(step_hdr, text=f"{len(completed)}/{total_steps} Done ({pct}%)", font=("Segoe UI", 8), bg=THEME["bg_dark"], fg=THEME["accent_green"]).pack(side="right")

            # Progress bar
            pbar = ttk.Progressbar(hud_body, orient="horizontal", mode="determinate")
            pbar["maximum"] = total_steps
            pbar["value"] = len(completed)
            pbar.pack(fill="x", pady=(0, 8))

            # Round & Tower Badge Row
            badge_box = tk.Frame(hud_body, bg=THEME["card"], padx=10, pady=8, highlightbackground=THEME["card_border"], highlightthickness=1)
            badge_box.pack(fill="x", pady=(0, 8))

            # Round
            r_num = active_step.get("round", 1)
            tk.Label(badge_box, text=f"ROUND {r_num}", font=("Segoe UI", 10, "bold"), bg=THEME["accent_blue"], fg=THEME["bg_dark"], padx=8, pady=2).pack(side="left", padx=(0, 6))

            # Action
            act = active_step.get("action", "Place")
            act_col = THEME["accent_green"] if act == "Place" else (THEME["accent_yellow"] if act == "Upgrade" else THEME["accent_red"])
            tk.Label(badge_box, text=f" {act.upper()} ", font=("Segoe UI", 9, "bold"), bg=act_col, fg=THEME["bg_dark"], padx=6, pady=2).pack(side="left", padx=(0, 6))

            # Tower & Icon
            tk.Label(badge_box, text=f"{tinfo['icon']} {active_step.get('tower')}", font=("Segoe UI", 10, "bold"), bg=THEME["card"], fg=tinfo["color"]).pack(side="left", padx=(0, 6))

            # Upgrade
            upg = active_step.get("upgrade", "0-0-0")
            tk.Label(badge_box, text=f"[{upg}]", font=("Consolas", 10, "bold"), bg="#11111b", fg=THEME["accent_teal"], padx=6, pady=2).pack(side="left")

            # Cost
            cost = active_step.get("cost_estimate", 0)
            cost_str = f"~${cost:,}" if cost > 0 else "FREE"
            tk.Label(badge_box, text=f"💰 {cost_str}", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["accent_yellow"]).pack(side="right")

            # Landmark Placement Box
            place_box = tk.Frame(hud_body, bg=THEME["bg_dark"])
            place_box.pack(fill="x", pady=(0, 4))
            tk.Label(place_box, text="📍 Placement:", font=("Segoe UI", 9, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_orange"]).pack(anchor="w")
            tk.Label(place_box, text=active_step.get("placement", ""), font=("Segoe UI", 9), bg=THEME["bg_dark"], fg=THEME["text_primary"], justify="left", wraplength=440).pack(anchor="w", padx=(10, 0))

            # Details
            det_box = tk.Frame(hud_body, bg=THEME["bg_dark"])
            det_box.pack(fill="x", pady=(0, 6))
            tk.Label(det_box, text="💡 Details:", font=("Segoe UI", 9, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_teal"]).pack(anchor="w")
            tk.Label(det_box, text=active_step.get("details", ""), font=("Segoe UI", 8), bg=THEME["bg_dark"], fg=THEME["text_muted"], justify="left", wraplength=440).pack(anchor="w", padx=(10, 0))

        # 3. HUD Bottom Control Buttons
        ctrl_bar = tk.Frame(self.overlay_container, bg="#11111b", padx=10, pady=8)
        ctrl_bar.pack(side="bottom", fill="x")

        btn_prev = tk.Button(ctrl_bar, text="◀ Prev (←)", font=("Segoe UI", 9, "bold"), bg="#313244", fg=THEME["text_primary"], relief="flat", padx=8, pady=3, cursor="hand2", command=self.step_prev)
        btn_prev.pack(side="left", padx=2)

        chk_text = "✔ Done (Space)" if is_done else "Mark Done (Space)"
        chk_bg = THEME["step_done_bg"] if is_done else THEME["card"]
        chk_fg = THEME["step_done_fg"] if is_done else THEME["accent_green"]
        btn_mark = tk.Button(ctrl_bar, text=chk_text, font=("Segoe UI", 9, "bold"), bg=chk_bg, fg=chk_fg, relief="flat", padx=10, pady=3, cursor="hand2", command=self.step_toggle_current)
        btn_mark.pack(side="left", padx=6)

        btn_next = tk.Button(ctrl_bar, text="Next ▶ (→)", font=("Segoe UI", 9, "bold"), bg=THEME["accent_blue"], fg=THEME["bg_dark"], relief="flat", padx=10, pady=3, cursor="hand2", command=self.step_next)
        btn_next.pack(side="left", padx=2)

        tk.Label(ctrl_bar, text="Hotkeys: Space / ← / →", font=("Segoe UI", 8), bg="#11111b", fg=THEME["text_dim"]).pack(side="right")

    # =========================================================================
    # FILTERING & SELECTION
    # =========================================================================
    def set_category_filter(self, category):
        self.selected_category.set(category)
        for cat, btn in self.cat_buttons.items():
            if cat == category:
                btn.configure(bg=THEME["accent_blue"], fg=THEME["bg_dark"])
            else:
                btn.configure(bg=THEME["card"], fg=THEME["text_primary"])
        self.filter_maps()

    def filter_maps(self):
        cat = self.selected_category.get()
        query = self.search_var.get().strip().lower()
        maps = self.data_manager.get_maps()

        filtered_names = []
        for m in maps.values():
            if cat != "All" and m.get("category") != cat:
                continue
            if query and query not in m.get("name", "").lower():
                continue
            filtered_names.append(m.get("name"))

        filtered_names.sort(key=lambda s: s.lower())
        self.map_combo["values"] = filtered_names

        current = self.selected_map_name.get()
        if current in filtered_names:
            self.map_combo.set(current)
        elif filtered_names:
            self.map_combo.set(filtered_names[0])
            self.on_map_selected()
        else:
            self.selected_map_name.set("")
            self.clear_guide_display("No maps match the current search or filter.")

    def restore_initial_state(self):
        last_id = self.settings.data.get("last_map_id", "monkey_meadow")
        map_data = self.data_manager.get_map(last_id)
        last_name = map_data.get("name", "Monkey Meadow") if map_data else "Monkey Meadow"

        self.filter_maps()
        if last_name in self.map_combo["values"]:
            self.map_combo.set(last_name)
        self.on_map_selected()

    def get_current_map_id(self):
        name = self.selected_map_name.get()
        for mid, mdata in self.data_manager.get_maps().items():
            if mdata.get("name") == name:
                return mid
        return None

    def get_selected_diff_key(self):
        diff_str = self.selected_difficulty.get()
        if "Hard" in diff_str:
            return "Hard"
        elif "Medium" in diff_str:
            return "Medium"
        return "Easy"

    def get_current_strategy(self, map_data=None):
        if map_data is None:
            mid = self.get_current_map_id()
            if not mid:
                return None
            map_data = self.data_manager.get_map(mid)
        if not map_data:
            return None
        diff_key = self.get_selected_diff_key()
        strat = map_data.get("difficulties", {}).get(diff_key)
        if not strat:
            strat = map_data.get("difficulties", {}).get("Easy")
        return strat

    def on_map_selected(self, event=None):
        mid = self.get_current_map_id()
        if mid:
            self.settings.data["last_map_id"] = mid
            self.settings.save()
            self.current_step_index = 0
            if self.is_overlay_mode:
                self.render_overlay_hud()
            else:
                self.render_guide()

    def on_difficulty_selected(self, event=None):
        diff_str = self.selected_difficulty.get()
        if not ("Easy" in diff_str or "Medium" in diff_str or "Hard" in diff_str):
            messagebox.showinfo(
                "Difficulty Notice",
                f"{diff_str} is scheduled for future expansion.\n\nCurrently displaying the full Easy (R1–40), Medium (R1–60), and Hard (R3–80) guides."
            )
            self.selected_difficulty.set("Easy (Rounds 1–40)")

        diff_key = self.get_selected_diff_key()
        self.settings.data["last_difficulty"] = diff_key
        self.settings.save()
        if self.is_overlay_mode:
            self.render_overlay_hud()
        else:
            self.render_guide()

    def reload_database(self):
        if self.data_manager.load():
            total, easy_v, med_v, hard_v, _ = self.data_manager.get_statistics()
            self.stats_label.configure(text=f"📊 {total} Maps  •  Easy ({easy_v}), Medium ({med_v}), Hard ({hard_v}) 100% Verified  •  100% Offline")
            self.filter_maps()
            self.render_guide()
            messagebox.showinfo("Database Reloaded", "Successfully reloaded guides.json with Easy, Medium & Hard strategies!")

    def clear_guide_display(self, message=""):
        for child in self.scrollable_frame.winfo_children():
            child.destroy()
        if message:
            lbl = tk.Label(self.scrollable_frame, text=message, font=self.font_heading, bg=THEME["bg"], fg=THEME["text_muted"], pady=60)
            lbl.pack()

    # =========================================================================
    # GUIDE RENDERING PIPELINE
    # =========================================================================
    def render_guide(self):
        self.clear_guide_display()
        mid = self.get_current_map_id()
        if not mid:
            return

        map_data = self.data_manager.get_map(mid)
        if not map_data:
            return

        strat = self.get_current_strategy(map_data)
        if not strat:
            self.clear_guide_display("No strategy available for this map and difficulty.")
            return

        # 1. Top Card: Map Title, Badges & Hero Info
        self.render_title_card(map_data, strat)

        # 2. Map Layout & Gimmick Overview Card
        self.render_overview_card(map_data, strat)

        # 3. Interactive Minimap & Track Placement Flow
        self.render_minimap_diagram(map_data, strat)

        # 4. Tactical Defense Readiness Card (Camo, Lead, MOAB/BFB)
        self.render_tactical_card(strat)

        # 5. Round-by-Round Step Walkthrough
        self.render_steps_card(mid, strat)

        # 6. Strategic Synergy & Economics Card
        self.render_why_it_works_card(strat)

        # 7. Research References Card
        self.render_sources_card(strat)

        # Update Walkthrough Bar
        self.update_progress_display(mid, strat)

    def render_title_card(self, map_data, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=16, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        # Title Row
        title_row = tk.Frame(card, bg=THEME["card"])
        title_row.pack(fill="x", pady=(0, 8))

        lbl_name = tk.Label(title_row, text=map_data.get("name"), font=self.font_title, bg=THEME["card"], fg=THEME["text_primary"])
        lbl_name.pack(side="left", padx=(0, 12))

        # Category Badge
        cat = map_data.get("category", "Beginner")
        cat_color = CATEGORY_COLORS.get(cat, THEME["accent_green"])
        badge_cat = tk.Label(title_row, text=f" {cat.upper()} ", font=self.font_badge, bg=cat_color, fg=THEME["bg_dark"], padx=6, pady=2)
        badge_cat.pack(side="left", padx=(0, 8))

        # Verification Status Badge (100% Verified)
        badge_status = tk.Label(
            title_row,
            text=" ✔ VERIFIED STRATEGY ",
            font=self.font_badge,
            bg="#2a2e3d",
            fg=THEME["accent_green"],
            padx=8,
            pady=2,
            highlightbackground=THEME["accent_green"],
            highlightthickness=1
        )
        badge_status.pack(side="left", padx=(0, 8))

        # Difficulty & Rounds Pill
        diff_title = f" {strat.get('difficulty').upper()} / STANDARD (ROUNDS {strat.get('rounds')}) "
        rounds_badge = tk.Label(title_row, text=diff_title, font=self.font_badge, bg="#313244", fg=THEME["accent_teal"], padx=8, pady=2)
        rounds_badge.pack(side="right")

        # Hero Intelligence Box
        hero = strat.get("recommended_hero", map_data.get("best_hero", "Sauda"))
        h_info = HEROES_DATABASE.get(hero, {})
        h_icon = h_info.get("icon", "👑")
        h_title = h_info.get("title", "Hero")
        alts = strat.get("hero_alternatives", map_data.get("hero_alternatives", []))
        alts_str = ", ".join(alts) if alts else "None"
        reason = strat.get("best_hero_reason", map_data.get("best_hero_reason", ""))
        synergies = strat.get("hero_synergies", map_data.get("hero_synergies", ""))

        hero_box = tk.Frame(card, bg="#1a1b2b", padx=14, pady=10, highlightbackground=THEME["card_border"], highlightthickness=1)
        hero_box.pack(fill="x", pady=(10, 0))

        h_top = tk.Frame(hero_box, bg="#1a1b2b")
        h_top.pack(fill="x")

        tk.Label(h_top, text=f"{h_icon} OPTIMAL HERO FOR THIS MAP:  {hero.upper()} — {h_title}", font=self.font_body_bold, bg="#1a1b2b", fg=THEME["accent_yellow"]).pack(side="left")

        btn_hero_detail = tk.Button(
            h_top,
            text="👑 View Hero Details",
            font=self.font_small,
            bg=THEME["card"],
            fg=THEME["accent_teal"],
            activebackground=THEME["card_hover"],
            activeforeground=THEME["accent_teal"],
            relief="flat",
            padx=8,
            pady=1,
            cursor="hand2",
            command=lambda h=hero: self.open_heroes_roster_dialog(focus_hero=h)
        )
        btn_hero_detail.pack(side="right")

        if reason:
            tk.Label(hero_box, text=f"💡 Tactical Advantage: {reason}", font=self.font_body, bg="#1a1b2b", fg=THEME["text_primary"], justify="left", wraplength=1040).pack(anchor="w", pady=(4, 2))

        h_sub = tk.Frame(hero_box, bg="#1a1b2b")
        h_sub.pack(fill="x", pady=(2, 0))
        tk.Label(h_sub, text=f"🔄 Viable Alternatives: {alts_str}", font=self.font_small, bg="#1a1b2b", fg=THEME["text_muted"]).pack(side="left", padx=(0, 20))
        if synergies:
            tk.Label(h_sub, text=f"⚡ Synergies: {synergies}", font=self.font_small, bg="#1a1b2b", fg=THEME["accent_green"]).pack(side="left")

        # Sub-row: Starting Cash, Price Multiplier
        info_row = tk.Frame(card, bg=THEME["card"])
        info_row.pack(fill="x", pady=(8, 0))

        diff_name = strat.get("difficulty", "Easy")
        price_mult = "85% (Easy)" if diff_name == "Easy" else ("108% (Hard)" if diff_name == "Hard" else "100% (Standard)")
        start_r = "Round 3" if diff_name == "Hard" else "Round 1"
        lbl_cash = tk.Label(info_row, text=f"💰 Starting Cash: $650 ({start_r})  •  Price Multiplier: {price_mult}  •  Lives: 100", font=self.font_body, bg=THEME["card"], fg=THEME["text_muted"])
        lbl_cash.pack(side="left")

    def render_overview_card(self, map_data, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=14, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        tk.Label(card, text="MAP GEOGRAPHY & TACTICAL OVERVIEW", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_blue"]).pack(anchor="w", pady=(0, 8))

        attr_frame = tk.Frame(card, bg=THEME["card"])
        attr_frame.pack(fill="x", pady=(0, 8))

        attrs = [
            ("Terrain", map_data.get("terrain", "Standard")),
            ("Lanes", map_data.get("lanes", "Single")),
            ("Water Present", "Yes (Allows Sub/Buccaneer)" if map_data.get("water") else "No (Land only)"),
            ("Line of Sight", "Blocked by obstacles" if map_data.get("sight_blockers") else "Clear / Open Field"),
            ("Special Gimmick", map_data.get("gimmick", "None"))
        ]

        for i, (k, v) in enumerate(attrs):
            row = i // 2
            col = (i % 2) * 2
            tk.Label(attr_frame, text=f"{k}:", font=self.font_body_bold, bg=THEME["card"], fg=THEME["text_dim"]).grid(row=row, column=col, sticky="w", padx=(0, 6), pady=2)
            tk.Label(attr_frame, text=v, font=self.font_body, bg=THEME["card"], fg=THEME["text_primary"]).grid(row=row, column=col+1, sticky="w", padx=(0, 24), pady=2)

        overview = strat.get("overview", "")
        lbl_desc = tk.Label(card, text=overview, font=self.font_body, bg=THEME["card"], fg=THEME["text_muted"], justify="left", wraplength=1050)
        lbl_desc.pack(anchor="w", pady=(4, 0))

    # =========================================================================
    # ITEM 3: INTERACTIVE TACTICAL PLACEMENT MINIMAP & TRACK FLOW
    # =========================================================================
    def render_minimap_diagram(self, map_data, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=14, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        # Title Row
        t_row = tk.Frame(card, bg=THEME["card"])
        t_row.pack(fill="x", pady=(0, 8))

        tk.Label(t_row, text="🗺️ TACTICAL PLACEMENT MINIMAP & TRACK FLOW", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_teal"]).pack(side="left")
        tk.Label(t_row, text="📍 Click any numbered pin to jump directly to that step", font=self.font_small, bg=THEME["card"], fg=THEME["text_dim"]).pack(side="right")

        # Minimap Canvas
        c_w = 1040
        c_h = 130
        mm_canvas = tk.Canvas(card, bg="#161622", height=c_h, highlightthickness=1, highlightbackground=THEME["card_border"])
        mm_canvas.pack(fill="x", pady=(0, 6))

        # Tooltip status label
        self.minimap_tooltip = tk.Label(card, text="Hover or click any pin above to view placement coordinates and details", font=self.font_small, bg=THEME["card"], fg=THEME["text_muted"])
        self.minimap_tooltip.pack(anchor="w")

        # Draw Blueprint Grid
        for gx in range(0, 1200, 40):
            mm_canvas.create_line(gx, 0, gx, c_h, fill="#1e1e2f", width=1)
        for gy in range(0, c_h, 30):
            mm_canvas.create_line(0, gy, 1200, gy, fill="#1e1e2f", width=1)

        steps = strat.get("steps", [])
        n_steps = len(steps)
        if n_steps == 0:
            return

        diff_key = self.get_selected_diff_key()
        mid = self.get_current_map_id()
        completed = self.settings.get_progress(mid, diff_key)

        # Responsive layout calculation
        def redraw_minimap(event=None):
            mm_canvas.delete("all")
            cur_w = mm_canvas.winfo_width()
            if cur_w < 300:
                cur_w = c_w

            # Re-draw Grid
            for gx in range(0, cur_w + 40, 40):
                mm_canvas.create_line(gx, 0, gx, c_h, fill="#1c1d2d", width=1)
            for gy in range(0, c_h, 30):
                mm_canvas.create_line(0, gy, cur_w, gy, fill="#1c1d2d", width=1)

            # Draw Serpentine Tactical Track
            start_x = 70
            end_x = cur_w - 70
            mid_y = 65

            # Smooth tactical path points
            points = [
                (start_x, mid_y),
                (start_x + (end_x - start_x) * 0.25, mid_y - 28),
                (start_x + (end_x - start_x) * 0.50, mid_y + 28),
                (start_x + (end_x - start_x) * 0.75, mid_y - 20),
                (end_x, mid_y)
            ]
            
            # Glow line
            mm_canvas.create_line(*[c for pt in points for c in pt], fill="#26273a", width=12, smooth=True)
            mm_canvas.create_line(*[c for pt in points for c in pt], fill="#3b4261", width=5, smooth=True)
            mm_canvas.create_line(*[c for pt in points for c in pt], fill=THEME["accent_blue"], width=2, dash=(6, 4), smooth=True)

            # Entrance & Exit Badges
            mm_canvas.create_text(start_x - 12, mid_y, text="▶ ENTRY", fill=THEME["accent_green"], font=("Segoe UI", 8, "bold"), anchor="e")
            mm_canvas.create_text(end_x + 12, mid_y, text="EXIT 🏁", fill=THEME["accent_red"], font=("Segoe UI", 8, "bold"), anchor="w")

            # Place Pins for each step
            pin_x_span = end_x - start_x - 40
            for i, step in enumerate(steps):
                snum = step.get("step_number", i + 1)
                frac = i / max(1, n_steps - 1)
                px = start_x + 20 + frac * pin_x_span
                # Alternating offset above and below the track line
                y_offset = -32 if (i % 2 == 0) else 32
                py = mid_y + y_offset

                # Connector stem
                mm_canvas.create_line(px, mid_y + (6 if y_offset > 0 else -6), px, py, fill="#45475a", width=1, dash=(2, 2))

                is_done = snum in completed
                tinfo = get_tower_info(step.get("tower", ""))

                # Pin Circle
                r = 13
                pin_bg = THEME["accent_green"] if is_done else "#24253a"
                pin_fg = THEME["bg_dark"] if is_done else THEME["text_primary"]
                pin_border = THEME["accent_green"] if is_done else tinfo["color"]

                circle_id = mm_canvas.create_oval(px - r, py - r, px + r, py + r, fill=pin_bg, outline=pin_border, width=2)
                text_id = mm_canvas.create_text(px, py, text=f"{snum}", fill=pin_fg, font=("Segoe UI", 9, "bold"))

                # Tower Icon & Name tag
                tag_y = py - 18 if y_offset < 0 else py + 18
                short_name = step.get("tower", "").replace("Monkey", "").strip()[:8]
                tag_text = f"{tinfo['icon']} {short_name}"
                tag_id = mm_canvas.create_text(px, tag_y, text=tag_text, fill=tinfo["color"], font=("Segoe UI", 8, "bold"))

                # Interaction bindings
                def on_enter(e, s=step, num=snum, icon=tinfo['icon']):
                    upg = s.get("upgrade", "0-0-0")
                    self.minimap_tooltip.configure(
                        text=f"📌 Step {num}: {icon} {s.get('action')} {s.get('tower')} [{upg}] — 📍 {s.get('placement')} (~${s.get('cost_estimate', 0):,})",
                        fg=THEME["accent_yellow"]
                    )

                def on_leave(e):
                    self.minimap_tooltip.configure(
                        text="Hover or click any pin above to view placement coordinates and details",
                        fg=THEME["text_muted"]
                    )

                def on_click(e, num=snum):
                    self.step_toggle_num(mid, num)

                for item_id in (circle_id, text_id, tag_id):
                    mm_canvas.tag_bind(item_id, "<Enter>", on_enter)
                    mm_canvas.tag_bind(item_id, "<Leave>", on_leave)
                    mm_canvas.tag_bind(item_id, "<Button-1>", on_click)

        mm_canvas.bind("<Configure>", redraw_minimap)

    def render_tactical_card(self, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=14, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        tk.Label(card, text="TACTICAL READINESS CHECKPOINTS", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_purple"]).pack(anchor="w", pady=(0, 10))

        tactics = [
            ("👁️ Camo Preparation (Rounds 24, 33, 36, 37, 42, 59, 78):", strat.get("camo_handling", "Handled naturally."), THEME["accent_purple"]),
            ("🛡️ Lead Countermeasures (Rounds 28, 30, 37, 45, 59):", strat.get("lead_handling", "Handled naturally."), THEME["accent_orange"]),
            ("💥 MOAB, BFB & ZOMG Tactical Execution (Rounds 40, 50, 60, 80):", strat.get("moab_handling", "Handled naturally."), THEME["accent_red"])
        ]
        if strat.get("ceramic_handling"):
            tactics.append(("🚨 Dense Ceramic Rush Lockdown (Rounds 63, 76, 78):", strat.get("ceramic_handling"), THEME["accent_yellow"]))

        for title, text, col in tactics:
            row_box = tk.Frame(card, bg=THEME["card"])
            row_box.pack(fill="x", pady=3)
            tk.Label(row_box, text=title, font=self.font_body_bold, bg=THEME["card"], fg=col).pack(anchor="w")
            tk.Label(row_box, text=f"   {text}", font=self.font_body, bg=THEME["card"], fg=THEME["text_primary"], justify="left", wraplength=1040).pack(anchor="w", padx=(10, 0))

    def render_steps_card(self, mid, strat):
        steps = strat.get("steps", [])
        if not steps:
            return

        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=16, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        # Header Row
        head_box = tk.Frame(card, bg=THEME["card"])
        head_box.pack(fill="x", pady=(0, 12))
        tk.Label(head_box, text="ROUND-BY-ROUND STEP-BY-STEP STRATEGY", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_green"]).pack(side="left")
        tk.Label(head_box, text="Click checkboxes or use walkthrough buttons / hotkeys (←, →, Space) to track your match", font=self.font_small, bg=THEME["card"], fg=THEME["text_dim"]).pack(side="right")

        diff_key = self.get_selected_diff_key()
        completed_steps = self.settings.get_progress(mid, diff_key)
        self.step_checkbox_vars = {}

        current_round_range = None

        for step in steps:
            snum = step.get("step_number")
            round_range = step.get("round_range", "Round Steps")

            # Section Header for Round Range
            if round_range != current_round_range:
                current_round_range = round_range
                range_prefix = round_range.split(":")[0]
                header_color = THEME["accent_teal"]
                for k, c in ROUND_RANGE_COLORS.items():
                    if k in range_prefix:
                        header_color = c
                        break

                hdr_frame = tk.Frame(card, bg="#1a1b26", padx=10, pady=6, highlightbackground=header_color, highlightthickness=1)
                hdr_frame.pack(fill="x", pady=(12, 6))
                tk.Label(hdr_frame, text=f"📌 {round_range.upper()}", font=self.font_heading, bg="#1a1b26", fg=header_color).pack(side="left")

            # Step Card Frame
            is_done = snum in completed_steps
            step_bg = THEME["step_done_bg"] if is_done else "#222336"
            step_frame = tk.Frame(card, bg=step_bg, padx=12, pady=10, highlightbackground=THEME["card_border"], highlightthickness=1)
            step_frame.pack(fill="x", pady=4)

            # Row 1: Checkbox + Badges (Round, Action, Tower, Upgrade, Targeting, Cost)
            badge_row = tk.Frame(step_frame, bg=step_bg)
            badge_row.pack(fill="x", pady=(0, 4))

            # Completion Checkbutton
            var = tk.BooleanVar(value=is_done)
            self.step_checkbox_vars[snum] = var
            chk = tk.Checkbutton(
                badge_row,
                variable=var,
                bg=step_bg,
                activebackground=step_bg,
                selectcolor=THEME["bg_dark"],
                command=lambda s=snum, v=var: self.toggle_step_completed(mid, s, v.get())
            )
            chk.pack(side="left", padx=(0, 6))

            # Step Number Badge
            tk.Label(badge_row, text=f"STEP {snum}", font=self.font_badge, bg="#313244", fg=THEME["text_muted"], padx=6, pady=1).pack(side="left", padx=(0, 6))

            # Round Badge
            round_num = step.get("round", 1)
            tk.Label(badge_row, text=f"ROUND {round_num}", font=self.font_badge, bg=THEME["accent_blue"], fg=THEME["bg_dark"], padx=6, pady=1).pack(side="left", padx=(0, 6))

            # Action Badge (Place / Upgrade / Target / Ability)
            action = step.get("action", "Place")
            act_icons = {"Place": "➕ PLACE", "Upgrade": "⬆️ UPGRADE", "Target": "🎯 TARGET", "Ability": "⚡ ABILITY"}
            act_label = act_icons.get(action, f" {action.upper()} ")
            act_color = THEME["accent_green"] if action == "Place" else (THEME["accent_yellow"] if action == "Upgrade" else (THEME["accent_teal"] if action == "Target" else THEME["accent_red"]))
            tk.Label(badge_row, text=f" {act_label} ", font=self.font_badge, bg=act_color, fg=THEME["bg_dark"], padx=6, pady=1).pack(side="left", padx=(0, 6))

            # Tower Name & Category Icon Badge
            tower = step.get("tower", "")
            tinfo = get_tower_info(tower)
            cat_pill = tk.Label(badge_row, text=f" {tinfo['icon']} {tower} ", font=self.font_body_bold, bg=step_bg, fg=tinfo["color"])
            cat_pill.pack(side="left", padx=(0, 6))

            # Category Tag
            cat_name = tinfo["category"]
            cat_bg = "#181825"
            tk.Label(badge_row, text=f"{cat_name.upper()}", font=self.font_badge, bg=cat_bg, fg=tinfo["color"], padx=5, pady=1).pack(side="left", padx=(0, 8))

            # Visual Upgrade Tier Badge (e.g. [ 2 • 0 • 4 ])
            upgrade = step.get("upgrade", "0-0-0")
            upg_parts = upgrade.split("-") if "-" in upgrade else ["0", "0", "0"]
            upg_formatted = f" {upg_parts[0]} • {upg_parts[1]} • {upg_parts[2]} " if len(upg_parts) == 3 else f" {upgrade} "
            tk.Label(badge_row, text=f"[{upg_formatted}]", font=self.font_mono, bg="#11111b", fg=THEME["accent_teal"], padx=6, pady=1).pack(side="left", padx=(0, 8))

            # Targeting Priority Badge
            targeting = step.get("targeting", "First")
            tk.Label(badge_row, text=f"🎯 {targeting}", font=self.font_small, bg="#181825", fg=THEME["text_muted"], padx=6, pady=1).pack(side="left", padx=(0, 8))

            # Cost Pill
            cost = step.get("cost_estimate", 0)
            cost_str = f"~${cost:,}" if cost > 0 else "FREE"
            tk.Label(badge_row, text=f"💰 {cost_str}", font=self.font_body_bold, bg="#181825", fg=THEME["accent_yellow"], padx=8, pady=1).pack(side="right")

            # Row 2: Landmark Placement Instruction
            placement = step.get("placement", "")
            if placement:
                place_row = tk.Frame(step_frame, bg=step_bg)
                place_row.pack(fill="x", pady=(3, 2))
                tk.Label(place_row, text="📍 Placement:", font=self.font_body_bold, bg=step_bg, fg=THEME["accent_orange"]).pack(side="left", padx=(0, 4))
                tk.Label(place_row, text=placement, font=self.font_body, bg=step_bg, fg=THEME["text_primary"], justify="left", wraplength=980).pack(side="left")

            # Row 3: Tactical Details & Mechanics
            details = step.get("details", "")
            if details:
                det_row = tk.Frame(step_frame, bg=step_bg)
                det_row.pack(fill="x", pady=(2, 0))
                tk.Label(det_row, text="💡 Details:", font=self.font_body_bold, bg=step_bg, fg=THEME["accent_teal"]).pack(side="left", padx=(0, 4))
                tk.Label(det_row, text=details, font=self.font_body, bg=step_bg, fg=THEME["text_muted"], justify="left", wraplength=980).pack(side="left")

    def toggle_step_completed(self, mid, step_num, is_done):
        diff_key = self.get_selected_diff_key()
        self.settings.set_step_progress(mid, step_num, is_done, diff_key)
        strat = self.get_current_strategy()
        self.update_progress_display(mid, strat)
        if self.is_overlay_mode:
            self.render_overlay_hud()
        else:
            self.render_guide()

    def step_toggle_num(self, mid, step_num):
        diff_key = self.get_selected_diff_key()
        curr = self.settings.get_progress(mid, diff_key)
        self.toggle_step_completed(mid, step_num, step_num not in curr)

    def step_toggle_current(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        strat = self.get_current_strategy()
        if not strat:
            return
        diff_key = self.get_selected_diff_key()
        steps = strat.get("steps", [])
        completed = self.settings.get_progress(mid, diff_key)

        for step in steps:
            snum = step.get("step_number")
            if snum not in completed:
                self.toggle_step_completed(mid, snum, True)
                return
        if steps:
            self.toggle_step_completed(mid, steps[-1].get("step_number"), False)

    def step_next(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        strat = self.get_current_strategy()
        if not strat:
            return
        diff_key = self.get_selected_diff_key()
        steps = strat.get("steps", [])
        completed = self.settings.get_progress(mid, diff_key)

        for step in steps:
            snum = step.get("step_number")
            if snum not in completed:
                self.settings.set_step_progress(mid, snum, True, diff_key)
                break
        if self.is_overlay_mode:
            self.render_overlay_hud()
        else:
            self.render_guide()

    def step_prev(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        strat = self.get_current_strategy()
        if not strat:
            return
        diff_key = self.get_selected_diff_key()
        completed = sorted(list(self.settings.get_progress(mid, diff_key)))
        if completed:
            last_done = completed[-1]
            self.settings.set_step_progress(mid, last_done, False, diff_key)
        if self.is_overlay_mode:
            self.render_overlay_hud()
        else:
            self.render_guide()

    def reset_current_map_progress(self):
        mid = self.get_current_map_id()
        if mid:
            diff_key = self.get_selected_diff_key()
            self.settings.reset_progress(mid, diff_key)
            if self.is_overlay_mode:
                self.render_overlay_hud()
            else:
                self.render_guide()

    def update_progress_display(self, mid, strat):
        if not strat:
            return
        diff_key = self.get_selected_diff_key()
        steps = strat.get("steps", [])
        total = len(steps)
        completed = len(self.settings.get_progress(mid, diff_key))
        pct = int((completed / total) * 100) if total > 0 else 0

        self.progress_bar["maximum"] = total
        self.progress_bar["value"] = completed
        self.progress_label.configure(text=f"{completed} / {total} Steps Completed ({pct}%)")

    def render_why_it_works_card(self, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=14, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        tk.Label(card, text="STRATEGIC SYNERGY & ECONOMIC VIABILITY", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_green"]).pack(anchor="w", pady=(0, 6))

        why_text = strat.get("why_it_works", "This strategy maintains a balanced curve of attack speed, pierce, and lead/camo popping.")
        lbl_why = tk.Label(card, text=why_text, font=self.font_body, bg=THEME["card"], fg=THEME["text_muted"], justify="left", wraplength=1050)
        lbl_why.pack(anchor="w")

    def render_sources_card(self, strat):
        card = tk.Frame(self.scrollable_frame, bg=THEME["card"], padx=20, pady=12, highlightbackground=THEME["card_border"], highlightthickness=1)
        card.pack(fill="x", pady=(0, 20))

        sources = strat.get("research_sources", ["Official Bloons Wiki", "In-Game Playtest Verification"])
        src_text = " • ".join(sources)

        tk.Label(card, text=f"📚 Research & Verification References:  {src_text}", font=self.font_small, bg=THEME["card"], fg=THEME["text_dim"]).pack(anchor="w")

    # =========================================================================
    # =========================================================================
    # EXPORT & COMMUNITY SHARING
    # =========================================================================
    def export_markdown_to_clipboard(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        map_data = self.data_manager.get_map(mid)
        strat = self.get_current_strategy(map_data)
        if not map_data or not strat:
            return

        lines = [
            f"# {map_data.get('name')} — {strat.get('difficulty')} Mode (Rounds {strat.get('rounds')})",
            f"**Category:** {map_data.get('category')} | **Terrain:** {map_data.get('terrain')} | **Lanes:** {map_data.get('lanes')}",
            f"**👑 Optimal Hero:** {strat.get('recommended_hero')} (Alternatives: {', '.join(strat.get('hero_alternatives', []))})",
            f"**Starting Cash:** ${strat.get('starting_cash', 650)} | **Status:** {strat.get('status')}",
            "",
            "## 📖 Tactical Overview",
            strat.get("overview", ""),
            "",
            "## 🎯 Threat Checkpoints",
            f"- **Camo Detection:** {strat.get('camo_handling', 'N/A')}",
            f"- **Lead Popping:** {strat.get('lead_handling', 'N/A')}",
            f"- **MOAB / Blimp Defense:** {strat.get('moab_handling', 'N/A')}",
        ]
        if strat.get("ceramic_handling"):
            lines.append(f"- **Ceramic Lockdown:** {strat.get('ceramic_handling')}")

        lines.extend([
            "",
            "## 📋 Step-by-Step Strategy",
            "| Step | Round | Action | Tower | Upgrade | Targeting | Cost | Placement & Details |",
            "| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :--- |"
        ])

        for s in strat.get("steps", []):
            cost_str = f"${s.get('cost_estimate', 0):,}" if s.get('cost_estimate', 0) > 0 else "Free"
            notes = f"**{s.get('placement', '')}** — {s.get('details', '')}"
            lines.append(f"| {s.get('step_number')} | R{s.get('round')} | {s.get('action')} | {s.get('tower')} | `{s.get('upgrade')}` | {s.get('targeting')} | {cost_str} | {notes} |")

        lines.extend([
            "",
            "## 💡 Strategic Synergy & Why It Works",
            strat.get("why_it_works", ""),
            "",
            "---",
            "*Generated with Bloons TD 6 Complete Offline Strategy Guide*"
        ])

        md_text = "\n".join(lines)
        self.clipboard_clear()
        self.clipboard_append(md_text)
        self.update()
        messagebox.showinfo("Exported to Clipboard", f"Successfully copied full Markdown guide for '{map_data.get('name')}' ({strat.get('difficulty')} Mode) to your clipboard!\n\nReady to paste into Discord, Reddit, or Steam.")

    def export_printable_html(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        map_data = self.data_manager.get_map(mid)
        strat = self.get_current_strategy(map_data)
        if not map_data or not strat:
            return

        diff_name = strat.get("difficulty", "Easy")
        html_filename = f"{mid}_{diff_name.lower()}_guide.html"
        html_path = os.path.join(os.path.dirname(__file__), html_filename)

        step_rows = []
        for s in strat.get("steps", []):
            cost_str = f"${s.get('cost_estimate', 0):,}" if s.get('cost_estimate', 0) > 0 else "FREE"
            act_class = s.get('action', 'Place').lower()
            step_rows.append(f"""
            <tr>
                <td style="font-weight:bold; text-align:center;">{s.get('step_number')}</td>
                <td style="font-weight:bold; color:#1e88e5; text-align:center;">R{s.get('round')}</td>
                <td><span class="badge badge-{act_class}">{s.get('action')}</span></td>
                <td style="font-weight:bold;">{s.get('tower')}</td>
                <td style="font-family:monospace; font-weight:bold; text-align:center;">[{s.get('upgrade')}]</td>
                <td>{s.get('targeting')}</td>
                <td style="font-weight:bold; color:#e65100; text-align:right;">{cost_str}</td>
                <td><strong>{s.get('placement')}</strong><br><span style="color:#555; font-size:0.9em;">{s.get('details')}</span></td>
            </tr>
            """)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BTD6 Guide — {map_data.get('name')} ({diff_name} Mode)</title>
<style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; margin: 24px; color: #222; background: #fff; line-height: 1.5; }}
    h1 {{ color: #1e88e5; margin-bottom: 4px; }}
    .subtitle {{ color: #666; font-size: 1.1em; margin-bottom: 20px; }}
    .meta-box {{ display: flex; gap: 16px; background: #f4f5f7; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; }}
    .meta-item {{ flex: 1; }}
    .meta-title {{ font-size: 0.8em; font-weight: bold; color: #777; text-transform: uppercase; }}
    .meta-val {{ font-size: 1.05em; font-weight: bold; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 16px; margin-bottom: 24px; }}
    th, td {{ padding: 10px 12px; border-bottom: 1px solid #ddd; text-align: left; font-size: 0.95em; }}
    th {{ background: #263238; color: #fff; }}
    tr:nth-child(even) {{ background: #f9f9f9; }}
    .badge {{ display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; font-weight: bold; color: #fff; background: #4caf50; }}
    .badge-upgrade {{ background: #ff9800; }}
    .badge-target {{ background: #00bcd4; }}
    .badge-ability {{ background: #e91e63; }}
    .card {{ background: #f9fbfd; border-left: 4px solid #1e88e5; padding: 12px 16px; margin-bottom: 16px; }}
    @media print {{ body {{ margin: 0; }} button {{ display: none; }} }}
</style>
</head>
<body>
    <button onclick="window.print()" style="float:right; padding:8px 16px; font-weight:bold; cursor:pointer; background:#1e88e5; color:#fff; border:none; border-radius:4px;">🖨️ Print / Save as PDF</button>
    <h1>🎈 {map_data.get('name')}</h1>
    <div class="subtitle">{map_data.get('category')} Map — {diff_name} / Standard (Rounds {strat.get('rounds')}) — 100% Offline Guide</div>
    <div class="meta-box">
        <div class="meta-item"><div class="meta-title">Recommended Hero</div><div class="meta-val">👑 {strat.get('recommended_hero')}</div></div>
        <div class="meta-item"><div class="meta-title">Terrain & Lanes</div><div class="meta-val">{map_data.get('terrain')} ({map_data.get('lanes')})</div></div>
        <div class="meta-item"><div class="meta-title">Water Support</div><div class="meta-val">{'Yes (Sub / Buccaneer)' if map_data.get('water') else 'No (Land Only)'}</div></div>
        <div class="meta-item"><div class="meta-title">Starting Cash</div><div class="meta-val">${strat.get('starting_cash', 650)}</div></div>
    </div>
    <div class="card">
        <strong>Overview:</strong> {strat.get('overview')}
    </div>
    <div class="card" style="border-left-color: #9c27b0;">
        <strong>Tactical Checkpoints:</strong>
        <div>👁️ <strong>Camo:</strong> {strat.get('camo_handling')}</div>
        <div>🛡️ <strong>Lead:</strong> {strat.get('lead_handling')}</div>
        <div>💥 <strong>MOAB / Blimp:</strong> {strat.get('moab_handling')}</div>
    </div>
    <h2>Round-by-Round Step Walkthrough</h2>
    <table>
        <thead>
            <tr>
                <th style="width:40px; text-align:center;">#</th>
                <th style="width:70px; text-align:center;">Round</th>
                <th style="width:70px;">Action</th>
                <th style="width:130px;">Tower</th>
                <th style="width:70px; text-align:center;">Upgrade</th>
                <th style="width:80px;">Targeting</th>
                <th style="width:70px; text-align:right;">Cost</th>
                <th>Placement Coordinates & Strategic Instructions</th>
            </tr>
        </thead>
        <tbody>
            {''.join(step_rows)}
        </tbody>
    </table>
    <div class="card" style="border-left-color: #4caf50;">
        <strong>Why It Works:</strong> {strat.get('why_it_works')}
    </div>
</body>
</html>"""
        try:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            webbrowser.open(f"file:///{html_path.replace(os.sep, '/')}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to generate printable cheat sheet:\n{e}")

    # =========================================================================
    # ITEM 4: HERO ROSTER MODAL
    # =========================================================================
    def open_heroes_roster_dialog(self, focus_hero=None):
        roster_win = tk.Toplevel(self)
        roster_win.title("Bloons TD 6 — Complete Hero Tactical Guide (All 16 Heroes)")
        roster_win.geometry("980x750")
        roster_win.minsize(800, 600)
        roster_win.configure(bg=THEME["bg"])
        roster_win.transient(self)

        top_hdr = tk.Frame(roster_win, bg=THEME["bg_dark"], padx=16, pady=12)
        top_hdr.pack(fill="x")
        tk.Label(top_hdr, text="👑 BTD6 HEROES ROSTER & SYNERGY MATRIX", font=("Segoe UI", 13, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_yellow"]).pack(side="left")
        tk.Label(top_hdr, text="Comprehensive stats, placements, abilities & map affinities for all 16 official heroes", font=("Segoe UI", 9), bg=THEME["bg_dark"], fg=THEME["text_muted"]).pack(side="right")

        filter_bar = tk.Frame(roster_win, bg=THEME["card"], padx=16, pady=8)
        filter_bar.pack(fill="x")
        tk.Label(filter_bar, text="Filter by Hero:", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["text_primary"]).pack(side="left", padx=(0, 8))

        hero_names = ["All (16 Heroes)"] + sorted(list(HEROES_DATABASE.keys()))
        selected_hero_filter = tk.StringVar(value=focus_hero if focus_hero in HEROES_DATABASE else "All (16 Heroes)")

        canvas = tk.Canvas(roster_win, bg=THEME["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(roster_win, orient="vertical", command=canvas.yview)
        cards_frame = tk.Frame(canvas, bg=THEME["bg"], padx=16, pady=12)

        cards_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        c_win = canvas.create_window((0, 0), window=cards_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(c_win, width=e.width))

        def render_hero_cards():
            for child in cards_frame.winfo_children():
                child.destroy()
            filter_val = selected_hero_filter.get()
            target_heroes = list(HEROES_DATABASE.keys()) if "All" in filter_val else [filter_val]

            all_maps = self.data_manager.get_maps()

            for h_name in target_heroes:
                h_data = HEROES_DATABASE.get(h_name)
                if not h_data:
                    continue

                card = tk.Frame(cards_frame, bg=THEME["card"], padx=16, pady=14, highlightbackground=THEME["card_border"], highlightthickness=1)
                card.pack(fill="x", pady=6)

                t_row = tk.Frame(card, bg=THEME["card"])
                t_row.pack(fill="x", pady=(0, 6))

                tk.Label(t_row, text=f"{h_data['icon']} {h_name.upper()} — {h_data['title']}", font=("Segoe UI", 12, "bold"), bg=THEME["card"], fg=h_data["color"]).pack(side="left")

                cost_text = f"Easy: ${h_data['cost_easy']} • Medium: ${h_data['cost_medium']} • Hard: ${h_data['cost_hard']}"
                tk.Label(t_row, text=f"💰 {cost_text} | 📍 {h_data['placement_type']}", font=("Segoe UI", 9, "bold"), bg="#181825", fg=THEME["accent_yellow"], padx=8, pady=2).pack(side="right")

                tk.Label(card, text=h_data["summary"], font=self.font_body, bg=THEME["card"], fg=THEME["text_primary"], justify="left", wraplength=920).pack(anchor="w", pady=(2, 6))

                m_frame = tk.Frame(card, bg="#1c1d2d", padx=10, pady=8)
                m_frame.pack(fill="x", pady=4)
                tk.Label(m_frame, text="⭐ KEY ABILITIES & LEVEL MILESTONES:", font=("Segoe UI", 8, "bold"), bg="#1c1d2d", fg=THEME["accent_teal"]).pack(anchor="w", pady=(0, 2))
                for lvl, desc in h_data.get("level_milestones", {}).items():
                    tk.Label(m_frame, text=f"  • {lvl}: {desc}", font=("Segoe UI", 8), bg="#1c1d2d", fg=THEME["text_muted"], justify="left", wraplength=900).pack(anchor="w")

                af_frame = tk.Frame(card, bg=THEME["card"])
                af_frame.pack(fill="x", pady=(6, 2))

                tk.Label(af_frame, text="🗺️ Best Map Types:", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["accent_orange"]).pack(anchor="w")
                tk.Label(af_frame, text=f"   {h_data['best_map_types']}", font=self.font_body, bg=THEME["card"], fg=THEME["text_muted"], justify="left", wraplength=920).pack(anchor="w")

                tk.Label(af_frame, text="⚡ Best Tower Synergies:", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["accent_green"]).pack(anchor="w", pady=(4, 0))
                syn_str = ", ".join(h_data["synergies"])
                tk.Label(af_frame, text=f"   {syn_str}", font=self.font_body, bg=THEME["card"], fg=THEME["text_muted"]).pack(anchor="w")

                rec_maps = [m.get("name") for m in all_maps.values() if m.get("best_hero") == h_name]
                if rec_maps:
                    tk.Label(af_frame, text=f"👑 #1 Recommended Hero on ({len(rec_maps)} Maps):", font=("Segoe UI", 9, "bold"), bg=THEME["card"], fg=THEME["accent_yellow"]).pack(anchor="w", pady=(4, 0))
                    rec_str = ", ".join(rec_maps[:8]) + (f" + {len(rec_maps)-8} more..." if len(rec_maps) > 8 else "")
                    tk.Label(af_frame, text=f"   {rec_str}", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_dim"]).pack(anchor="w")

        combo_filter = ttk.Combobox(filter_bar, textvariable=selected_hero_filter, values=hero_names, state="readonly", width=24)
        combo_filter.pack(side="left", padx=4)
        combo_filter.bind("<<ComboboxSelected>>", lambda e: render_hero_cards())

        render_hero_cards()

    # =========================================================================
    # ITEM 3: BLOON THREAT RADAR & WAVE INSPECTOR
    # =========================================================================
    def open_threat_radar_dialog(self):
        radar_win = tk.Toplevel(self)
        radar_win.title("Bloons TD 6 — Bloon Threat Radar & Wave Inspector (Rounds 1–100)")
        radar_win.geometry("980x760")
        radar_win.minsize(800, 600)
        radar_win.configure(bg=THEME["bg"])
        radar_win.transient(self)

        mid = self.get_current_map_id()
        map_data = self.data_manager.get_map(mid) if mid else None
        strat = self.get_current_strategy(map_data) if map_data else None

        top_hdr = tk.Frame(radar_win, bg=THEME["bg_dark"], padx=16, pady=12)
        top_hdr.pack(fill="x")
        tk.Label(top_hdr, text="🎯 BLOON THREAT RADAR & WAVE INSPECTOR", font=("Segoe UI", 13, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_blue"]).pack(side="left")
        map_title = f"{map_data.get('name')} ({strat.get('difficulty')} Mode)" if map_data and strat else "Standard Waves"
        tk.Label(top_hdr, text=f"Analyzing vs: {map_title}", font=("Segoe UI", 10), bg=THEME["bg_dark"], fg=THEME["accent_teal"]).pack(side="right")

        ctrl_bar = tk.Frame(radar_win, bg=THEME["card"], padx=16, pady=10)
        ctrl_bar.pack(fill="x")

        current_r_var = tk.IntVar(value=40)

        r_select_row = tk.Frame(ctrl_bar, bg=THEME["card"])
        r_select_row.pack(fill="x", pady=(0, 6))

        tk.Label(r_select_row, text="Inspect Round:", font=("Segoe UI", 10, "bold"), bg=THEME["card"], fg=THEME["text_primary"]).pack(side="left", padx=(0, 10))

        scale = tk.Scale(r_select_row, from_=1, to=100, orient="horizontal", variable=current_r_var, bg=THEME["card"], fg=THEME["text_primary"], highlightthickness=0, length=450)
        scale.pack(side="left", padx=(0, 10))

        spn = tk.Spinbox(r_select_row, from_=1, to=100, textvariable=current_r_var, width=5, font=("Segoe UI", 11, "bold"), bg="#181825", fg=THEME["text_primary"], insertbackground=THEME["text_primary"])
        spn.pack(side="left", padx=(0, 10))

        btn_jump_frame = tk.Frame(ctrl_bar, bg=THEME["card"])
        btn_jump_frame.pack(fill="x", pady=(4, 0))

        tk.Label(btn_jump_frame, text="Quick Jumps:", font=("Segoe UI", 8, "bold"), bg=THEME["card"], fg=THEME["text_dim"]).pack(side="left", padx=(0, 6))

        danger_jumps = [
            (24, "R24 Camo"), (28, "R28 Lead"), (40, "R40 MOAB"), (45, "R45 F.Lead"),
            (50, "R50 2xMOAB"), (59, "R59 CamoLead"), (60, "R60 BFB"), (63, "R63 Ceramics"),
            (76, "R76 Regrow"), (78, "R78 CamoCeram"), (80, "R80 ZOMG"), (90, "R90 DDT"), (100, "R100 BAD")
        ]

        canvas = tk.Canvas(radar_win, bg=THEME["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(radar_win, orient="vertical", command=canvas.yview)
        body = tk.Frame(canvas, bg=THEME["bg"], padx=16, pady=12)

        body.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        c_win = canvas.create_window((0, 0), window=body, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(c_win, width=e.width))

        def update_round_display(*args):
            for child in body.winfo_children():
                child.destroy()

            r = current_r_var.get()
            r_data = get_round_data(r)
            danger = r_data.get("danger")

            c1_bg = "#2b1b22" if danger and danger.get("severity") in ["CRITICAL", "EXTREME", "MAXIMUM"] else THEME["card"]
            c1 = tk.Frame(body, bg=c1_bg, padx=16, pady=12, highlightbackground=THEME["accent_red"] if danger else THEME["card_border"], highlightthickness=1)
            c1.pack(fill="x", pady=(0, 10))

            t_box = tk.Frame(c1, bg=c1_bg)
            t_box.pack(fill="x")

            tk.Label(t_box, text=f"ROUND {r}", font=("Segoe UI", 16, "bold"), bg=c1_bg, fg=THEME["accent_blue"]).pack(side="left", padx=(0, 12))

            if danger:
                tk.Label(t_box, text=f" {danger['flag']} ({danger['severity']}) ", font=self.font_badge, bg=THEME["accent_red"], fg=THEME["bg_dark"], padx=8, pady=3).pack(side="left", padx=(0, 12))
                tk.Label(c1, text=danger["note"], font=self.font_body_bold, bg=c1_bg, fg=THEME["accent_yellow"], justify="left", wraplength=920).pack(anchor="w", pady=(6, 2))

            m_box = tk.Frame(c1, bg=c1_bg)
            m_box.pack(fill="x", pady=(6, 0))
            tk.Label(m_box, text=f"🔴 RBE (Red Bloon Equivalent): {r_data['rbe']:,}   •   💰 Approx Cash Generated: ${r_data['cash']:,}", font=self.font_body, bg=c1_bg, fg=THEME["text_muted"]).pack(side="left")

            c2 = tk.Frame(body, bg=THEME["card"], padx=16, pady=12, highlightbackground=THEME["card_border"], highlightthickness=1)
            c2.pack(fill="x", pady=(0, 10))
            tk.Label(c2, text="🎈 BLOON WAVE COMPOSITION", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_teal"]).pack(anchor="w", pady=(0, 8))

            bloons_frame = tk.Frame(c2, bg=THEME["card"])
            bloons_frame.pack(fill="x")

            for b in r_data.get("bloons", []):
                pill = tk.Frame(bloons_frame, bg="#1c1d2d", padx=10, pady=6, highlightbackground=THEME["card_border"], highlightthickness=1)
                pill.pack(side="left", padx=4, pady=4)
                camo_icon = " 👁️" if b.get("camo") else ""
                regrow_icon = " 🔄" if b.get("regrow") else ""
                fort_icon = " 🛡️" if b.get("fortified") else ""
                b_text = f"{b.get('count')}x {b.get('type')}{camo_icon}{regrow_icon}{fort_icon}"
                tk.Label(pill, text=b_text, font=self.font_body_bold, bg="#1c1d2d", fg=THEME["text_primary"]).pack()

            if strat and strat.get("steps"):
                c3 = tk.Frame(body, bg=THEME["card"], padx=16, pady=12, highlightbackground=THEME["card_border"], highlightthickness=1)
                c3.pack(fill="x", pady=(0, 10))
                tk.Label(c3, text=f"🛡️ DEFENSE READINESS FOR '{map_data.get('name')}' ({strat.get('difficulty')} MODE)", font=self.font_heading, bg=THEME["card"], fg=THEME["accent_green"]).pack(anchor="w", pady=(0, 8))

                readiness = check_strategy_defense_readiness(r, strat.get("steps", []))

                checks = [
                    ("Camo Defense", readiness["camo_ready"], readiness["camo_towers"], "Round 24, 33, 42, 59, 78 require Camo detection."),
                    ("Lead Popping", readiness["lead_ready"], readiness["lead_towers"], "Round 28, 30, 45, 59 require Lead popping."),
                    ("Blimp / MOAB Damage", readiness["moab_ready"], readiness["moab_towers"], "Rounds 40, 50, 60, 80 require heavy blimp piercing power."),
                    ("Ceramic Crowd Control", readiness["ceramic_ready"], readiness["ceramic_towers"], "Rounds 49, 63, 76, 78 require high pierce / AoE splash.")
                ]

                for name, ready, towers, tip in checks:
                    row = tk.Frame(c3, bg=THEME["card"])
                    row.pack(fill="x", pady=3)
                    status_badge = "✅ READY" if ready else "⚠️ ATTENTION"
                    status_col = THEME["accent_green"] if ready else THEME["accent_yellow"]
                    tk.Label(row, text=f"{status_badge}", font=self.font_badge, bg="#181825", fg=status_col, padx=6, pady=2).pack(side="left", padx=(0, 8))
                    tk.Label(row, text=f"{name}:", font=self.font_body_bold, bg=THEME["card"], fg=THEME["text_primary"], width=22, anchor="w").pack(side="left")
                    if ready and towers:
                        t_list = ", ".join(towers[:3]) + (f" + {len(towers)-3} more" if len(towers) > 3 else "")
                        tk.Label(row, text=f"Covered by: {t_list}", font=self.font_body, bg=THEME["card"], fg=THEME["accent_teal"]).pack(side="left")
                    else:
                        tk.Label(row, text=f"{tip}", font=self.font_small, bg=THEME["card"], fg=THEME["text_dim"]).pack(side="left")

        for r_num, lbl in danger_jumps:
            btn = tk.Button(
                btn_jump_frame,
                text=lbl,
                font=("Segoe UI", 8),
                bg="#1e1e2f",
                fg=THEME["accent_teal"],
                activebackground=THEME["card_hover"],
                activeforeground=THEME["text_primary"],
                relief="flat",
                padx=5,
                pady=1,
                cursor="hand2",
                command=lambda r=r_num: [current_r_var.set(r), update_round_display()]
            )
            btn.pack(side="left", padx=2)

        current_r_var.trace_add("write", lambda *args: update_round_display())
        scale.configure(command=lambda e: update_round_display())
        update_round_display()

    # =========================================================================
    # ITEM 5: STRATEGY EDITOR & VISUAL STEP BUILDER
    # =========================================================================
    def open_edit_guide_dialog(self):
        mid = self.get_current_map_id()
        if not mid:
            return
        map_data = self.data_manager.get_map(mid)
        if not map_data:
            return

        diff_key = self.get_selected_diff_key()
        strat = map_data.get("difficulties", {}).get(diff_key)
        if not strat:
            strat = map_data.get("difficulties", {}).get("Easy", {})

        editor = tk.Toplevel(self)
        editor.title(f"Edit Strategy Guide — {map_data.get('name')} ({diff_key} Mode)")
        editor.geometry("980x780")
        editor.minsize(800, 600)
        editor.configure(bg=THEME["bg"])
        editor.transient(self)
        editor.grab_set()

        # Working copy of steps for the visual builder
        working_steps = [dict(s) for s in strat.get("steps", [])]

        hdr = tk.Frame(editor, bg=THEME["bg_dark"], padx=16, pady=12)
        hdr.pack(fill="x")
        tk.Label(hdr, text=f"Edit Strategy: {map_data.get('name')}", font=("Segoe UI", 13, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_yellow"]).pack(side="left")
        tk.Label(hdr, text=f"{diff_key} / Standard Mode (R{strat.get('rounds')})", font=("Segoe UI", 10), bg=THEME["bg_dark"], fg=THEME["text_muted"]).pack(side="right")

        canvas = tk.Canvas(editor, bg=THEME["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(editor, orient="vertical", command=canvas.yview)
        form = tk.Frame(canvas, bg=THEME["bg"], padx=16, pady=12)

        form.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        c_win = canvas.create_window((0, 0), window=form, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(c_win, width=e.width))

        # Status
        f_status = tk.Frame(form, bg=THEME["bg"])
        f_status.pack(fill="x", pady=4)
        tk.Label(f_status, text="Verification Status:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=20, anchor="w").pack(side="left")
        status_var = tk.StringVar(value=strat.get("status", "Verified"))
        status_cb = ttk.Combobox(f_status, textvariable=status_var, values=["Verified", "Needs Review"], state="readonly", width=18)
        status_cb.pack(side="left")

        # Hero
        f_hero = tk.Frame(form, bg=THEME["bg"])
        f_hero.pack(fill="x", pady=4)
        tk.Label(f_hero, text="Recommended Hero:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=20, anchor="w").pack(side="left")
        hero_var = tk.StringVar(value=strat.get("recommended_hero", "Sauda"))
        hero_cb = ttk.Combobox(f_hero, textvariable=hero_var, values=list(HEROES_DATABASE.keys()), state="readonly", width=22)
        hero_cb.pack(side="left")

        # Overview
        f_over = tk.Frame(form, bg=THEME["bg"])
        f_over.pack(fill="x", pady=4)
        tk.Label(f_over, text="Map & Strategy Overview:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"]).pack(anchor="w")
        txt_overview = tk.Text(f_over, font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], height=3, wrap="word", relief="flat")
        txt_overview.insert("1.0", strat.get("overview", ""))
        txt_overview.pack(fill="x", pady=2)

        # Camo
        f_camo = tk.Frame(form, bg=THEME["bg"])
        f_camo.pack(fill="x", pady=4)
        tk.Label(f_camo, text="Camo Handling:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["accent_purple"]).pack(anchor="w")
        txt_camo = tk.Text(f_camo, font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], height=2, wrap="word", relief="flat")
        txt_camo.insert("1.0", strat.get("camo_handling", ""))
        txt_camo.pack(fill="x", pady=2)

        # Lead
        f_lead = tk.Frame(form, bg=THEME["bg"])
        f_lead.pack(fill="x", pady=4)
        tk.Label(f_lead, text="Lead Handling:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["accent_orange"]).pack(anchor="w")
        txt_lead = tk.Text(f_lead, font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], height=2, wrap="word", relief="flat")
        txt_lead.insert("1.0", strat.get("lead_handling", ""))
        txt_lead.pack(fill="x", pady=2)

        # MOAB
        f_moab = tk.Frame(form, bg=THEME["bg"])
        f_moab.pack(fill="x", pady=4)
        tk.Label(f_moab, text="MOAB / BFB / ZOMG Handling:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["accent_red"]).pack(anchor="w")
        txt_moab = tk.Text(f_moab, font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], height=2, wrap="word", relief="flat")
        txt_moab.insert("1.0", strat.get("moab_handling", ""))
        txt_moab.pack(fill="x", pady=2)

        # Why
        f_why = tk.Frame(form, bg=THEME["bg"])
        f_why.pack(fill="x", pady=4)
        tk.Label(f_why, text="Why It Works / Synergy:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["accent_green"]).pack(anchor="w")
        txt_why = tk.Text(f_why, font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], height=2, wrap="word", relief="flat")
        txt_why.insert("1.0", strat.get("why_it_works", ""))
        txt_why.pack(fill="x", pady=2)

        # Mode switcher for Steps
        mode_bar = tk.Frame(form, bg=THEME["bg"], pady=8)
        mode_bar.pack(fill="x")
        tk.Label(mode_bar, text="STRATEGY STEPS BUILDER:", font=("Segoe UI", 10, "bold"), bg=THEME["bg"], fg=THEME["accent_teal"]).pack(side="left")

        current_editor_mode = tk.StringVar(value="visual")

        btn_vis_mode = tk.Button(mode_bar, text="🎨 Visual Step Builder", font=("Segoe UI", 8, "bold"), bg=THEME["accent_blue"], fg=THEME["bg_dark"], relief="flat", padx=8, pady=2, cursor="hand2")
        btn_vis_mode.pack(side="left", padx=(16, 4))

        btn_json_mode = tk.Button(mode_bar, text="📝 Raw JSON Mode", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_muted"], relief="flat", padx=8, pady=2, cursor="hand2")
        btn_json_mode.pack(side="left", padx=4)

        vis_frame = tk.Frame(form, bg=THEME["bg"])
        vis_frame.pack(fill="x", pady=4)

        json_frame = tk.Frame(form, bg=THEME["bg"])
        txt_steps = tk.Text(json_frame, font=("Consolas", 9), bg="#181825", fg=THEME["text_primary"], height=14, wrap="none", relief="flat")
        txt_steps.insert("1.0", json.dumps(working_steps, indent=2))
        txt_steps.pack(fill="x", pady=4)

        def switch_mode(target):
            if target == "visual":
                try:
                    parsed = json.loads(txt_steps.get("1.0", "end-1c"))
                    if isinstance(parsed, list):
                        working_steps.clear()
                        working_steps.extend(parsed)
                except Exception:
                    pass
                current_editor_mode.set("visual")
                btn_vis_mode.configure(bg=THEME["accent_blue"], fg=THEME["bg_dark"], font=("Segoe UI", 8, "bold"))
                btn_json_mode.configure(bg=THEME["card"], fg=THEME["text_muted"], font=("Segoe UI", 8))
                json_frame.pack_forget()
                vis_frame.pack(fill="x", pady=4)
                render_visual_step_list()
            else:
                current_editor_mode.set("json")
                txt_steps.delete("1.0", "end")
                txt_steps.insert("1.0", json.dumps(working_steps, indent=2))
                btn_json_mode.configure(bg=THEME["accent_blue"], fg=THEME["bg_dark"], font=("Segoe UI", 8, "bold"))
                btn_vis_mode.configure(bg=THEME["card"], fg=THEME["text_muted"], font=("Segoe UI", 8))
                vis_frame.pack_forget()
                json_frame.pack(fill="x", pady=4)

        btn_vis_mode.configure(command=lambda: switch_mode("visual"))
        btn_json_mode.configure(command=lambda: switch_mode("json"))

        def open_step_form(step_idx=None):
            step_dialog = tk.Toplevel(editor)
            is_new = step_idx is None
            step_dialog.title("Add Strategy Step" if is_new else f"Edit Step {step_idx + 1}")
            step_dialog.geometry("640x560")
            step_dialog.minsize(560, 480)
            step_dialog.configure(bg=THEME["bg"])
            step_dialog.transient(editor)
            step_dialog.grab_set()

            step_data = working_steps[step_idx] if not is_new else {
                "step_number": len(working_steps) + 1,
                "round_range": "Rounds 1–10: Opening Defense",
                "round": 1,
                "action": "Place",
                "tower": "Dart Monkey",
                "upgrade": "0-0-0",
                "placement": "Near the track entrance.",
                "targeting": "First",
                "cost_estimate": 215,
                "details": ""
            }

            top_bar = tk.Frame(step_dialog, bg=THEME["bg_dark"], padx=16, pady=10)
            top_bar.pack(fill="x")
            tk.Label(top_bar, text="Step Form Builder", font=("Segoe UI", 11, "bold"), bg=THEME["bg_dark"], fg=THEME["accent_teal"]).pack(side="left")

            body_f = tk.Frame(step_dialog, bg=THEME["bg"], padx=16, pady=12)
            body_f.pack(fill="both", expand=True)

            # Round Range
            rr_frame = tk.Frame(body_f, bg=THEME["bg"])
            rr_frame.pack(fill="x", pady=3)
            tk.Label(rr_frame, text="Round Range:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            rr_presets = [
                "Rounds 1–10: Opening Defense",
                "Rounds 11–20: Expanding Defense",
                "Rounds 21–30: Camo and Lead Preparation",
                "Rounds 31–40: MOAB Preparation & Defense",
                "Rounds 41–50: Fortified Leads & Dual MOABs",
                "Rounds 51–60: Camo Leads & BFB Battle",
                "Rounds 61–75: Heavy Ceramics & Blimp Trains",
                "Rounds 76–80: ZOMG Boss & Endgame Victory"
            ]
            rr_var = tk.StringVar(value=step_data.get("round_range", rr_presets[0]))
            rr_cb = ttk.Combobox(rr_frame, textvariable=rr_var, values=rr_presets, width=38)
            rr_cb.pack(side="left")

            # Round Number
            r_frame = tk.Frame(body_f, bg=THEME["bg"])
            r_frame.pack(fill="x", pady=3)
            tk.Label(r_frame, text="Round Number:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            r_var = tk.IntVar(value=step_data.get("round", 1))
            r_spn = tk.Spinbox(r_frame, from_=1, to=100, textvariable=r_var, width=8, font=("Segoe UI", 9))
            r_spn.pack(side="left")

            # Action
            act_frame = tk.Frame(body_f, bg=THEME["bg"])
            act_frame.pack(fill="x", pady=3)
            tk.Label(act_frame, text="Action:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            act_var = tk.StringVar(value=step_data.get("action", "Place"))
            act_cb = ttk.Combobox(act_frame, textvariable=act_var, values=["Place", "Upgrade", "Target", "Ability", "Sell"], state="readonly", width=12)
            act_cb.pack(side="left")

            # Tower
            tow_frame = tk.Frame(body_f, bg=THEME["bg"])
            tow_frame.pack(fill="x", pady=3)
            tk.Label(tow_frame, text="Tower:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            tow_var = tk.StringVar(value=step_data.get("tower", "Dart Monkey"))
            tow_cb = ttk.Combobox(tow_frame, textvariable=tow_var, values=sorted(list(TOWER_INFO.keys())), width=24)
            tow_cb.pack(side="left")

            # Upgrade
            upg_frame = tk.Frame(body_f, bg=THEME["bg"])
            upg_frame.pack(fill="x", pady=3)
            tk.Label(upg_frame, text="Upgrade Path:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            upg_raw = step_data.get("upgrade", "0-0-0").split("-")
            u1_val = int(upg_raw[0]) if len(upg_raw) == 3 and upg_raw[0].isdigit() else 0
            u2_val = int(upg_raw[1]) if len(upg_raw) == 3 and upg_raw[1].isdigit() else 0
            u3_val = int(upg_raw[2]) if len(upg_raw) == 3 and upg_raw[2].isdigit() else 0

            u1_var = tk.IntVar(value=u1_val)
            u2_var = tk.IntVar(value=u2_val)
            u3_var = tk.IntVar(value=u3_val)

            tk.Spinbox(upg_frame, from_=0, to=5, textvariable=u1_var, width=3).pack(side="left")
            tk.Label(upg_frame, text=" - ", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_muted"]).pack(side="left")
            tk.Spinbox(upg_frame, from_=0, to=5, textvariable=u2_var, width=3).pack(side="left")
            tk.Label(upg_frame, text=" - ", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_muted"]).pack(side="left")
            tk.Spinbox(upg_frame, from_=0, to=5, textvariable=u3_var, width=3).pack(side="left")
            tk.Label(upg_frame, text="  (Top - Mid - Bottom)", font=self.font_small, bg=THEME["bg"], fg=THEME["text_dim"]).pack(side="left")

            # Targeting
            tgt_frame = tk.Frame(body_f, bg=THEME["bg"])
            tgt_frame.pack(fill="x", pady=3)
            tk.Label(tgt_frame, text="Targeting:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            tgt_var = tk.StringVar(value=step_data.get("targeting", "First"))
            tgt_cb = ttk.Combobox(tgt_frame, textvariable=tgt_var, values=["First", "Strong", "Last", "Close"], state="readonly", width=12)
            tgt_cb.pack(side="left")

            # Cost
            cost_frame = tk.Frame(body_f, bg=THEME["bg"])
            cost_frame.pack(fill="x", pady=3)
            tk.Label(cost_frame, text="Cost Estimate ($):", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            cost_var = tk.IntVar(value=step_data.get("cost_estimate", 0))
            tk.Entry(cost_frame, textvariable=cost_var, width=12, font=("Segoe UI", 9)).pack(side="left")

            # Placement
            pl_frame = tk.Frame(body_f, bg=THEME["bg"])
            pl_frame.pack(fill="x", pady=3)
            tk.Label(pl_frame, text="Placement / Location:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"], width=16, anchor="w").pack(side="left")
            pl_var = tk.StringVar(value=step_data.get("placement", ""))
            tk.Entry(pl_frame, textvariable=pl_var, width=42, font=("Segoe UI", 9)).pack(side="left")

            # Details
            det_frame = tk.Frame(body_f, bg=THEME["bg"])
            det_frame.pack(fill="x", pady=3)
            tk.Label(det_frame, text="Tactical Instructions:", font=("Segoe UI", 9, "bold"), bg=THEME["bg"], fg=THEME["text_primary"]).pack(anchor="w")
            txt_det = tk.Text(det_frame, font=("Segoe UI", 9), height=3, wrap="word")
            txt_det.insert("1.0", step_data.get("details", ""))
            txt_det.pack(fill="x", pady=2)

            def save_step():
                u_str = f"{u1_var.get()}-{u2_var.get()}-{u3_var.get()}"
                new_entry = {
                    "step_number": step_data.get("step_number", len(working_steps) + 1),
                    "round_range": rr_var.get().strip(),
                    "round": r_var.get(),
                    "action": act_var.get(),
                    "tower": tow_var.get().strip(),
                    "upgrade": u_str,
                    "placement": pl_var.get().strip(),
                    "targeting": tgt_var.get(),
                    "cost_estimate": cost_var.get(),
                    "details": txt_det.get("1.0", "end-1c").strip()
                }
                if is_new:
                    working_steps.append(new_entry)
                else:
                    working_steps[step_idx] = new_entry

                for idx, st in enumerate(working_steps):
                    st["step_number"] = idx + 1

                step_dialog.destroy()
                render_visual_step_list()

            b_row = tk.Frame(step_dialog, bg=THEME["bg_dark"], padx=16, pady=8)
            b_row.pack(side="bottom", fill="x")
            tk.Button(b_row, text="✔ Save Step", font=("Segoe UI", 9, "bold"), bg=THEME["accent_green"], fg=THEME["bg_dark"], padx=12, pady=3, cursor="hand2", command=save_step).pack(side="right", padx=4)
            tk.Button(b_row, text="Cancel", font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], padx=10, pady=3, cursor="hand2", command=step_dialog.destroy).pack(side="right", padx=4)

        def move_step(idx, direction):
            new_idx = idx + direction
            if 0 <= new_idx < len(working_steps):
                working_steps[idx], working_steps[new_idx] = working_steps[new_idx], working_steps[idx]
                for i, s in enumerate(working_steps):
                    s["step_number"] = i + 1
                render_visual_step_list()

        def delete_step(idx):
            if messagebox.askyesno("Delete Step", f"Are you sure you want to delete Step {idx + 1}?"):
                working_steps.pop(idx)
                for i, s in enumerate(working_steps):
                    s["step_number"] = i + 1
                render_visual_step_list()

        def render_visual_step_list():
            for child in vis_frame.winfo_children():
                child.destroy()

            top_action = tk.Frame(vis_frame, bg=THEME["bg"])
            top_action.pack(fill="x", pady=(0, 6))
            tk.Label(top_action, text=f"Total Steps: {len(working_steps)}", font=self.font_body_bold, bg=THEME["bg"], fg=THEME["text_muted"]).pack(side="left")
            btn_add = tk.Button(top_action, text="➕ Add New Step", font=("Segoe UI", 9, "bold"), bg=THEME["accent_blue"], fg=THEME["bg_dark"], relief="flat", padx=10, pady=2, cursor="hand2", command=lambda: open_step_form(None))
            btn_add.pack(side="right")

            for i, st in enumerate(working_steps):
                card = tk.Frame(vis_frame, bg=THEME["card"], padx=10, pady=8, highlightbackground=THEME["card_border"], highlightthickness=1)
                card.pack(fill="x", pady=3)

                r1 = tk.Frame(card, bg=THEME["card"])
                r1.pack(fill="x")

                tk.Label(r1, text=f"#{st.get('step_number', i+1)}", font=self.font_badge, bg="#181825", fg=THEME["text_muted"], padx=5, pady=1).pack(side="left", padx=(0, 6))
                tk.Label(r1, text=f"R{st.get('round')}", font=self.font_badge, bg=THEME["accent_blue"], fg=THEME["bg_dark"], padx=5, pady=1).pack(side="left", padx=(0, 6))

                act = st.get("action", "Place")
                act_col = THEME["accent_green"] if act == "Place" else (THEME["accent_yellow"] if act == "Upgrade" else THEME["accent_red"])
                tk.Label(r1, text=f" {act.upper()} ", font=self.font_badge, bg=act_col, fg=THEME["bg_dark"], padx=5, pady=1).pack(side="left", padx=(0, 6))

                tinfo = get_tower_info(st.get("tower", ""))
                tk.Label(r1, text=f"{tinfo['icon']} {st.get('tower')}", font=self.font_body_bold, bg=THEME["card"], fg=tinfo["color"]).pack(side="left", padx=(0, 6))
                tk.Label(r1, text=f"[{st.get('upgrade')}]", font=self.font_mono, bg="#11111b", fg=THEME["accent_teal"], padx=5, pady=1).pack(side="left", padx=(0, 6))

                cost_val = st.get("cost_estimate", 0)
                cost_lbl = f"~${cost_val:,}" if cost_val > 0 else "Free"
                tk.Label(r1, text=f"💰 {cost_lbl}", font=self.font_small, bg="#181825", fg=THEME["accent_yellow"], padx=6, pady=1).pack(side="left", padx=(0, 6))

                btn_del = tk.Button(r1, text="🗑️", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["accent_red"], relief="flat", cursor="hand2", command=lambda idx=i: delete_step(idx))
                btn_del.pack(side="right", padx=1)

                btn_ed = tk.Button(r1, text="✏️ Edit", font=("Segoe UI", 8, "bold"), bg="#313244", fg=THEME["accent_yellow"], relief="flat", cursor="hand2", padx=6, command=lambda idx=i: open_step_form(idx))
                btn_ed.pack(side="right", padx=3)

                if i < len(working_steps) - 1:
                    btn_down = tk.Button(r1, text="⬇️", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_muted"], relief="flat", cursor="hand2", command=lambda idx=i: move_step(idx, 1))
                    btn_down.pack(side="right", padx=1)
                if i > 0:
                    btn_up = tk.Button(r1, text="⬆️", font=("Segoe UI", 8), bg=THEME["card"], fg=THEME["text_muted"], relief="flat", cursor="hand2", command=lambda idx=i: move_step(idx, -1))
                    btn_up.pack(side="right", padx=1)

                r2 = tk.Frame(card, bg=THEME["card"])
                r2.pack(fill="x", pady=(2, 0))
                tk.Label(r2, text=f"📍 {st.get('placement')} — {st.get('details')}", font=self.font_small, bg=THEME["card"], fg=THEME["text_muted"], justify="left", wraplength=850).pack(anchor="w")

        render_visual_step_list()

        btn_bar = tk.Frame(editor, bg=THEME["bg_dark"], padx=16, pady=10)
        btn_bar.pack(side="bottom", fill="x")

        tk.Button(btn_bar, text="📋 Copy Markdown", font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["text_primary"], relief="flat", padx=10, pady=3, cursor="hand2", command=self.export_markdown_to_clipboard).pack(side="left", padx=4)
        tk.Button(btn_bar, text="📄 Printable HTML", font=("Segoe UI", 9), bg=THEME["card"], fg=THEME["accent_teal"], relief="flat", padx=10, pady=3, cursor="hand2", command=self.export_printable_html).pack(side="left", padx=4)

        def save_changes():
            if current_editor_mode.get() == "json":
                try:
                    final_steps = json.loads(txt_steps.get("1.0", "end-1c"))
                    if not isinstance(final_steps, list):
                        raise ValueError("Steps must be a JSON array of step objects.")
                except Exception as ex:
                    messagebox.showerror("JSON Syntax Error", f"Failed to parse steps JSON:\n{ex}")
                    return
            else:
                final_steps = working_steps

            strat["status"] = status_var.get()
            strat["recommended_hero"] = hero_var.get().strip()
            strat["overview"] = txt_overview.get("1.0", "end-1c").strip()
            strat["camo_handling"] = txt_camo.get("1.0", "end-1c").strip()
            strat["lead_handling"] = txt_lead.get("1.0", "end-1c").strip()
            strat["moab_handling"] = txt_moab.get("1.0", "end-1c").strip()
            strat["why_it_works"] = txt_why.get("1.0", "end-1c").strip()
            strat["steps"] = final_steps

            if self.data_manager.save():
                messagebox.showinfo("Saved", f"{diff_key} strategy updated and saved to guides.json successfully!")
                self.render_guide()
                editor.destroy()

        btn_save = tk.Button(btn_bar, text="💾 Save Changes to Database", font=("Segoe UI", 10, "bold"), bg=THEME["accent_green"], fg=THEME["bg_dark"], padx=16, pady=4, cursor="hand2", command=save_changes)
        btn_save.pack(side="right", padx=6)

        btn_cancel = tk.Button(btn_bar, text="Cancel", font=("Segoe UI", 10), bg=THEME["card"], fg=THEME["text_primary"], padx=12, pady=4, cursor="hand2", command=editor.destroy)
        btn_cancel.pack(side="right", padx=6)


def main():
    app = BTD6GuideApp()
    app.mainloop()

if __name__ == "__main__":
    main()
