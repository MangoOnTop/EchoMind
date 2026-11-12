import os
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Enable DPI awareness on Windows for crisp high-resolution rendering
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

# Ensure project root is in sys.path
<<<<<<< HEAD
if getattr(sys, "frozen", False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
else:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

=======
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
>>>>>>> 4bedd04adc7f07915fcd65748dfd626673b8eb53
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.memory_manager import load_memory, save_memory, MEMORY_FILE
from src.engine import process_turn, get_response

# ─── Color Palette (Modern Dark Theme) ─────────────────────────────────────────
PALETTE = {
    "bg_root": "#0B0F17",           # Deep dark background
    "bg_sidebar": "#111827",        # Dark gray sidebar
    "bg_sidebar_card": "#1F2937",   # Elevated card in sidebar
    "border": "#374151",            # Gray 700 border
    "border_light": "#4B5563",      # Gray 600 border for hover
    "chat_bg": "#0F172A",           # Deep slate chat background
    "user_bubble": "#4F46E5",       # Indigo 600
    "user_text": "#FFFFFF",         # White
    "bot_bubble": "#1E293B",        # Slate 800
    "bot_bubble_border": "#334155", # Slate 700
    "bot_text": "#F8FAFC",          # Slate 50
    "accent": "#6366F1",            # Indigo 500
    "accent_hover": "#4338CA",      # Indigo 700
    "accent_emerald": "#10B981",    # Emerald green
    "accent_rose": "#EF4444",       # Rose / Red
    "accent_rose_hover": "#DC2626", # Darker red
    "text_primary": "#F9FAFB",      # Near white
    "text_secondary": "#94A3B8",    # Slate 400
    "text_muted": "#64748B",        # Slate 500
    "chip_bg": "#1E293B",           # Chip background
    "chip_hover": "#334155",        # Chip hover
    "input_bg": "#1E293B",          # Text field background
}

FONT_FAMILY = "Segoe UI" if sys.platform == "win32" else "Helvetica"

class EchoMindGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("EchoMind • AI Rule-Engine & Memory Assistant")
        self.root.geometry("1020x720")
        self.root.minsize(860, 560)
        self.root.configure(bg=PALETTE["bg_root"])

        # Center window on screen
        self.center_window(1020, 720)

        # Load session memory
        self.memory = load_memory()
        save_memory(self.memory)

        # State tracking
        self.message_count = 0

        # Build UI Layout
        self.setup_styles()
        self.build_layout()

        # Populate initial greeting
        self.show_initial_greeting()
        self.update_sidebar_profile()

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self, width, height):
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = max(0, int((screen_w - width) / 2))
        y = max(0, int((screen_h - height) / 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("default")
        # Custom scrollbar styling
        style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background=PALETTE["bg_sidebar_card"],
            darkcolor=PALETTE["bg_sidebar"],
            lightcolor=PALETTE["bg_sidebar"],
            troughcolor=PALETTE["chat_bg"],
            bordercolor=PALETTE["chat_bg"],
            arrowcolor=PALETTE["text_secondary"]
        )

    def build_layout(self):
        # Master grid layout: column 0 = Sidebar (fixed width), column 1 = Chat (expands)
        self.root.grid_columnconfigure(0, weight=0, minsize=300)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.build_sidebar()
        self.build_chat_panel()

    # ─── LEFT SIDEBAR: PROFILE & CONTROLS ─────────────────────────────────────
    def build_sidebar(self):
        sidebar = tk.Frame(self.root, bg=PALETTE["bg_sidebar"], width=300, padx=18, pady=18)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # App Brand Header
        brand_frame = tk.Frame(sidebar, bg=PALETTE["bg_sidebar"])
        brand_frame.pack(fill="x", pady=(0, 16))

        title_row = tk.Frame(brand_frame, bg=PALETTE["bg_sidebar"])
        title_row.pack(anchor="w")

        icon_lbl = tk.Label(title_row, text="🧠", font=(FONT_FAMILY, 20), bg=PALETTE["bg_sidebar"])
        icon_lbl.pack(side="left", padx=(0, 8))

        brand_text_col = tk.Frame(title_row, bg=PALETTE["bg_sidebar"])
        brand_text_col.pack(side="left")

        app_name = tk.Label(
            brand_text_col, text="EchoMind",
            font=(FONT_FAMILY, 15, "bold"), fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar"]
        )
        app_name.pack(anchor="w")

        app_sub = tk.Label(
            brand_text_col, text="Persistent Rule Engine Agent",
            font=(FONT_FAMILY, 9), fg=PALETTE["text_muted"], bg=PALETTE["bg_sidebar"]
        )
        app_sub.pack(anchor="w")

        # Status Pill
        status_frame = tk.Frame(brand_frame, bg=PALETTE["bg_sidebar_card"], padx=10, pady=5)
        status_frame.pack(fill="x", pady=(10, 0))

        status_dot = tk.Label(
            status_frame, text="●", font=(FONT_FAMILY, 10),
            fg=PALETTE["accent_emerald"], bg=PALETTE["bg_sidebar_card"]
        )
        status_dot.pack(side="left", padx=(0, 6))

        self.status_lbl = tk.Label(
            status_frame, text="Online • State Synced",
            font=(FONT_FAMILY, 9, "bold"), fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar_card"]
        )
        self.status_lbl.pack(side="left")

        # ── Profile Card ──
        card_lbl = tk.Label(
            sidebar, text="PERSISTENT MEMORY",
            font=(FONT_FAMILY, 9, "bold"), fg=PALETTE["text_muted"], bg=PALETTE["bg_sidebar"]
        )
        card_lbl.pack(anchor="w", pady=(14, 6))

        self.profile_card = tk.Frame(
            sidebar, bg=PALETTE["bg_sidebar_card"],
            highlightbackground=PALETTE["border"], highlightthickness=1, padx=12, pady=12
        )
        self.profile_card.pack(fill="x")

        # Profile fields
        self.field_labels = {}
        fields = [
            ("👤 Name", "username"),
            ("📍 Location", "location"),
            ("🎮 Fav Game", "fav_game"),
            ("🎨 Fav Hobby", "fav_hobby"),
            ("🔢 Session", "session_count"),
            ("⏱️ Last Saved", "last_saved"),
        ]

        for display, key in fields:
            row = tk.Frame(self.profile_card, bg=PALETTE["bg_sidebar_card"])
            row.pack(fill="x", pady=2)

            name_lbl = tk.Label(
                row, text=display, font=(FONT_FAMILY, 9),
                fg=PALETTE["text_secondary"], bg=PALETTE["bg_sidebar_card"]
            )
            name_lbl.pack(side="left")

            val_lbl = tk.Label(
                row, text="—", font=(FONT_FAMILY, 9, "bold"),
                fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar_card"], anchor="e"
            )
            val_lbl.pack(side="right")
            self.field_labels[key] = val_lbl

        # ── Quick Action Buttons ──
        prompts_hdr = tk.Label(
            sidebar, text="QUICK ACTIONS",
            font=(FONT_FAMILY, 9, "bold"), fg=PALETTE["text_muted"], bg=PALETTE["bg_sidebar"]
        )
        prompts_hdr.pack(anchor="w", pady=(18, 6))

        actions = [
            ("👤 Who Am I?", "Who am I?"),
            ("📍 Where Do I Live?", "Where do I live?"),
            ("🎮 What's My Favorite Game?", "What is my favorite game?"),
            ("🎨 What's My Hobby?", "What is my favorite hobby?"),
            ("🧠 What Did I Say?", "What did I say?"),
            ("❓ Help & Commands", "Help"),
        ]

        for text, prompt in actions:
            btn = tk.Button(
                sidebar, text=text, font=(FONT_FAMILY, 9),
                fg=PALETTE["text_secondary"], bg=PALETTE["bg_sidebar_card"],
                activebackground=PALETTE["border"], activeforeground=PALETTE["text_primary"],
                relief="flat", anchor="w", padx=10, pady=5, cursor="hand2",
                command=lambda p=prompt: self.send_user_message(p)
            )
            btn.pack(fill="x", pady=2)
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=PALETTE["border"], fg=PALETTE["text_primary"]))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=PALETTE["bg_sidebar_card"], fg=PALETTE["text_secondary"]))

        # ── Utility Buttons ──
        bottom_frame = tk.Frame(sidebar, bg=PALETTE["bg_sidebar"])
        bottom_frame.pack(side="bottom", fill="x", pady=(12, 0))

        # View JSON Memory button
        json_btn = tk.Button(
            bottom_frame, text="📄 View JSON Memory", font=(FONT_FAMILY, 9),
            fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar_card"],
            activebackground=PALETTE["border"], activeforeground=PALETTE["text_primary"],
            relief="flat", pady=6, cursor="hand2", command=self.open_memory_viewer
        )
        json_btn.pack(fill="x", pady=(0, 4))
        json_btn.bind("<Enter>", lambda e, b=json_btn: b.configure(bg=PALETTE["border"]))
        json_btn.bind("<Leave>", lambda e, b=json_btn: b.configure(bg=PALETTE["bg_sidebar_card"]))

        # Forget Me / Reset button
        forget_btn = tk.Button(
            bottom_frame, text="🗑️ Forget Me (Reset Profile)", font=(FONT_FAMILY, 9, "bold"),
            fg="#FFFFFF", bg=PALETTE["accent_rose"],
            activebackground=PALETTE["accent_rose_hover"], activeforeground="#FFFFFF",
            relief="flat", pady=6, cursor="hand2", command=self.confirm_forget_me
        )
        forget_btn.pack(fill="x")
        forget_btn.bind("<Enter>", lambda e, b=forget_btn: b.configure(bg=PALETTE["accent_rose_hover"]))
        forget_btn.bind("<Leave>", lambda e, b=forget_btn: b.configure(bg=PALETTE["accent_rose"]))

    # ─── RIGHT PANEL: CHAT FEED & INPUT ───────────────────────────────────────
    def build_chat_panel(self):
        chat_container = tk.Frame(self.root, bg=PALETTE["chat_bg"])
        chat_container.grid(row=0, column=1, sticky="nsew")
        chat_container.grid_rowconfigure(1, weight=1)
        chat_container.grid_columnconfigure(0, weight=1)

        # ── 1. Chat Top Header ──
        header = tk.Frame(
            chat_container, bg=PALETTE["bg_sidebar"],
            highlightbackground=PALETTE["border"], highlightthickness=1, padx=20, pady=12
        )
        header.grid(row=0, column=0, sticky="ew")

        h_left = tk.Frame(header, bg=PALETTE["bg_sidebar"])
        h_left.pack(side="left")

        self.chat_title = tk.Label(
            h_left, text="Active Conversation",
            font=(FONT_FAMILY, 12, "bold"), fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar"]
        )
        self.chat_title.pack(anchor="w")

        self.chat_sub = tk.Label(
            h_left, text="Persistent memory loaded from echomind_memory.json",
            font=(FONT_FAMILY, 9), fg=PALETTE["text_muted"], bg=PALETTE["bg_sidebar"]
        )
        self.chat_sub.pack(anchor="w")

        # Stats Badge on right of header
        self.stats_badge = tk.Label(
            header, text="0 messages", font=(FONT_FAMILY, 9),
            fg=PALETTE["text_secondary"], bg=PALETTE["bg_sidebar_card"], padx=10, pady=4
        )
        self.stats_badge.pack(side="right")

        # Clear Chat Button
        clear_btn = tk.Button(
            header, text="🧹 Clear View", font=(FONT_FAMILY, 9),
            fg=PALETTE["text_secondary"], bg=PALETTE["bg_sidebar"],
            activebackground=PALETTE["border"], relief="flat", cursor="hand2",
            padx=8, pady=2, command=self.clear_chat_display
        )
        clear_btn.pack(side="right", padx=(0, 10))

        # ── 2. Scrollable Chat Canvas ──
        chat_frame = tk.Frame(chat_container, bg=PALETTE["chat_bg"])
        chat_frame.grid(row=1, column=0, sticky="nsew")
        chat_frame.grid_rowconfigure(0, weight=1)
        chat_frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            chat_frame, bg=PALETTE["chat_bg"],
            highlightthickness=0, bd=0
        )
        self.scrollbar = ttk.Scrollbar(
            chat_frame, orient="vertical", command=self.canvas.yview, style="Vertical.TScrollbar"
        )

        self.messages_inner = tk.Frame(self.canvas, bg=PALETTE["chat_bg"])
        self.messages_inner.bind("<Configure>", self.on_frame_configure)

        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.messages_inner, anchor="nw"
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Bind canvas resize to update inner window width
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Bind Mousewheel scrolling
        self.bind_mousewheel(self.canvas)
        self.bind_mousewheel(self.messages_inner)

        # ── 3. Suggestion Chips Bar ──
        chips_frame = tk.Frame(chat_container, bg=PALETTE["chat_bg"], padx=20, pady=5)
        chips_frame.grid(row=2, column=0, sticky="ew")

        chips = [
            ("👋 Hello!", "Hello!"),
            ("🏷️ Set Name", "My name is "),
            ("📍 Set Location", "I live in "),
            ("🎮 Set Game", "My favorite game is "),
            ("❓ Help", "Help"),
        ]

        for label, prompt in chips:
            btn = tk.Button(
                chips_frame, text=label, font=(FONT_FAMILY, 8, "bold"),
                fg=PALETTE["text_secondary"], bg=PALETTE["chip_bg"],
                activebackground=PALETTE["chip_hover"], activeforeground=PALETTE["text_primary"],
                relief="flat", padx=10, pady=3, cursor="hand2",
                command=lambda p=prompt: self.on_chip_click(p)
            )
            btn.pack(side="left", padx=(0, 6))
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=PALETTE["chip_hover"], fg=PALETTE["text_primary"]))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=PALETTE["chip_bg"], fg=PALETTE["text_secondary"]))

        # ── 4. Input Controls Bar ──
        input_bar = tk.Frame(
            chat_container, bg=PALETTE["bg_sidebar"],
            highlightbackground=PALETTE["border"], highlightthickness=1, padx=16, pady=12
        )
        input_bar.grid(row=3, column=0, sticky="ew")

        # Text input field
        self.entry = tk.Entry(
            input_bar, font=(FONT_FAMILY, 11),
            bg=PALETTE["input_bg"], fg=PALETTE["text_primary"],
            insertbackground=PALETTE["text_primary"],
            relief="flat", highlightbackground=PALETTE["border"], highlightthickness=1
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.on_send_pressed())

        # Placeholder management
        self.placeholder_text = "Type a message... (e.g., 'My name is Mahi', 'Who am I?', 'Help')"
        self.set_placeholder()
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)

        # Send Button
        self.send_btn = tk.Button(
            input_bar, text="Send  ➔", font=(FONT_FAMILY, 10, "bold"),
            fg="#FFFFFF", bg=PALETTE["accent"],
            activebackground=PALETTE["accent_hover"], activeforeground="#FFFFFF",
            relief="flat", padx=18, pady=8, cursor="hand2", command=self.on_send_pressed
        )
        self.send_btn.pack(side="right")
        self.send_btn.bind("<Enter>", lambda e: self.send_btn.configure(bg=PALETTE["accent_hover"]))
        self.send_btn.bind("<Leave>", lambda e: self.send_btn.configure(bg=PALETTE["accent"]))

    # ─── Placeholder Management ───────────────────────────────────────────────
    def set_placeholder(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.placeholder_text)
        self.entry.configure(fg=PALETTE["text_muted"])
        self.placeholder_active = True

    def clear_placeholder(self, event=None):
        if getattr(self, "placeholder_active", False):
            self.entry.delete(0, tk.END)
            self.entry.configure(fg=PALETTE["text_primary"])
            self.placeholder_active = False

    def restore_placeholder(self, event=None):
        if not self.entry.get().strip():
            self.set_placeholder()

    def on_chip_click(self, prompt: str):
        self.clear_placeholder()
        if prompt.endswith(" "):
            # Incomplete prompt: fill into input and focus for user to type
            self.entry.delete(0, tk.END)
            self.entry.insert(0, prompt)
            self.entry.focus_set()
            self.entry.icursor(tk.END)
        else:
            # Complete prompt: send immediately
            self.send_user_message(prompt)

    # ─── Scrolling & Resizing ──────────────────────────────────────────────────
    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def bind_mousewheel(self, widget):
        widget.bind("<MouseWheel>", self.on_mousewheel)
        for child in widget.winfo_children():
            self.bind_mousewheel(child)

    def on_mousewheel(self, event):
        if sys.platform == "win32":
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            self.canvas.yview_scroll(int(-1 * event.delta), "units")

    def scroll_to_bottom(self):
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # ─── Chat Bubble Rendering ────────────────────────────────────────────────
    def add_bubble(self, speaker: str, text: str, timestamp: str = None):
        if not timestamp:
            timestamp = datetime.now().strftime("%I:%M %p")

        # Wrapper row inside inner frame
        row = tk.Frame(self.messages_inner, bg=PALETTE["chat_bg"], pady=6, padx=20)
        row.pack(fill="x")

        is_user = (speaker == "user")
        is_system = (speaker == "system")

        if is_system:
            # Centered system announcement pill
            pill = tk.Frame(
                row, bg=PALETTE["bg_sidebar_card"],
                highlightbackground=PALETTE["border"], highlightthickness=1, padx=12, pady=4
            )
            pill.pack(anchor="center")
            lbl = tk.Label(
                pill, text=text, font=(FONT_FAMILY, 8, "italic"),
                fg=PALETTE["text_muted"], bg=PALETTE["bg_sidebar_card"]
            )
            lbl.pack()
            self.scroll_to_bottom()
            return

        # Main bubble frame
        bubble_bg = PALETTE["user_bubble"] if is_user else PALETTE["bot_bubble"]
        bubble_fg = PALETTE["user_text"] if is_user else PALETTE["bot_text"]
        border_color = PALETTE["user_bubble"] if is_user else PALETTE["bot_bubble_border"]

        bubble = tk.Frame(
            row, bg=bubble_bg,
            highlightbackground=border_color, highlightthickness=1,
            padx=14, pady=10
        )
        bubble.pack(anchor="e" if is_user else "w")

        # Header inside bubble (Speaker tag + timestamp)
        header_row = tk.Frame(bubble, bg=bubble_bg)
        header_row.pack(fill="x", pady=(0, 4))

        tag_text = "👤 You" if is_user else "🤖 EchoMind"
        tag_color = "#E0E7FF" if is_user else PALETTE["accent"]

        tag_lbl = tk.Label(
            header_row, text=tag_text, font=(FONT_FAMILY, 9, "bold"),
            fg=tag_color, bg=bubble_bg
        )
        tag_lbl.pack(side="left" if not is_user else "right", padx=(0, 6) if not is_user else (6, 0))

        time_lbl = tk.Label(
            header_row, text=timestamp, font=(FONT_FAMILY, 8),
            fg="#C7D2FE" if is_user else PALETTE["text_muted"], bg=bubble_bg
        )
        time_lbl.pack(side="left" if not is_user else "right")

        # Text content
        # Dynamically calculate wrapping based on window size
        content_lbl = tk.Label(
            bubble, text=text, font=(FONT_FAMILY, 10),
            fg=bubble_fg, bg=bubble_bg, justify="left" if not is_user else "right",
            wraplength=520
        )
        content_lbl.pack(anchor="w" if not is_user else "e")

        self.bind_mousewheel(row)
        self.bind_mousewheel(bubble)
        self.bind_mousewheel(header_row)
        self.bind_mousewheel(content_lbl)

        self.message_count += 1
        self.stats_badge.configure(text=f"{self.message_count} messages")
        self.scroll_to_bottom()

    def show_initial_greeting(self):
        username = self.memory.get("user_profile", {}).get("username")
        if username:
            greeting = f"Welcome back, {username}! How can I help you today?"
            self.add_bubble("system", f"Session restored for {username}")
        else:
            greeting = "Hi, I am EchoMind! What's your name? (Tell me with 'My name is ...' or ask for 'help')"
            self.add_bubble("system", "New session initialized with empty profile")

        self.add_bubble("bot", greeting)

    # ─── Message Handling ─────────────────────────────────────────────────────
    def on_send_pressed(self):
        if getattr(self, "placeholder_active", False):
            return
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)
        self.send_user_message(user_text)

    def send_user_message(self, text: str):
        # 1. Render User Bubble
        self.add_bubble("user", text)

        # 2. Process Turn via Engine
        reply, is_farewell = process_turn(text, self.memory)

        # 3. Render Bot Reply
        self.add_bubble("bot", reply)

        # 4. Refresh Sidebar Profile & State
        self.update_sidebar_profile()

        # 5. Handle Farewell
        if is_farewell:
            self.add_bubble("system", "Session farewell recognized. You may close or continue chatting.")

        # Re-focus input
        self.entry.focus_set()

    def update_sidebar_profile(self):
        prof = self.memory.get("user_profile", {})
        meta = self.memory.get("metadata", {})

        username = prof.get("username")
        location = prof.get("location")
        fav_game = prof.get("fav_game")
        fav_hobby = prof.get("fav_hobby")
        session_count = meta.get("session_count", 1)
        last_saved = meta.get("last_saved") or "Just now"

        self.field_labels["username"].configure(
            text=username if username else "(Not set)",
            fg=PALETTE["text_primary"] if username else PALETTE["text_muted"]
        )
        self.field_labels["location"].configure(
            text=location if location else "(Not set)",
            fg=PALETTE["text_primary"] if location else PALETTE["text_muted"]
        )
        self.field_labels["fav_game"].configure(
            text=fav_game if fav_game else "(Not set)",
            fg=PALETTE["text_primary"] if fav_game else PALETTE["text_muted"]
        )
        self.field_labels["fav_hobby"].configure(
            text=fav_hobby if fav_hobby else "(Not set)",
            fg=PALETTE["text_primary"] if fav_hobby else PALETTE["text_muted"]
        )
        self.field_labels["session_count"].configure(
            text=f"#{session_count}", fg=PALETTE["accent_emerald"]
        )
        self.field_labels["last_saved"].configure(
            text=last_saved.split(" ")[-1] if " " in str(last_saved) else str(last_saved),
            fg=PALETTE["text_secondary"]
        )

        # Update chat header subtitle if name exists
        if username:
            self.chat_title.configure(text=f"Chatting with {username}")
        else:
            self.chat_title.configure(text="Active Conversation")

    # ─── Memory Viewer Dialog ─────────────────────────────────────────────────
    def open_memory_viewer(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Inspect echomind_memory.json")
        dialog.geometry("640x500")
        dialog.configure(bg=PALETTE["bg_root"])
        dialog.transient(self.root)

        hdr = tk.Frame(dialog, bg=PALETTE["bg_sidebar"], padx=16, pady=10)
        hdr.pack(fill="x")

        tk.Label(
            hdr, text="📄 echomind_memory.json Contents",
            font=(FONT_FAMILY, 11, "bold"), fg=PALETTE["text_primary"], bg=PALETTE["bg_sidebar"]
        ).pack(side="left")

        # Reload button
        def reload_json():
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    data = f.read()
                txt.delete("1.0", tk.END)
                txt.insert("1.0", data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load memory file:\n{e}")

        reload_btn = tk.Button(
            hdr, text="🔄 Reload", font=(FONT_FAMILY, 9),
            fg=PALETTE["text_secondary"], bg=PALETTE["bg_sidebar_card"],
            relief="flat", padx=10, pady=2, cursor="hand2", command=reload_json
        )
        reload_btn.pack(side="right")

        # Text area
        txt_frame = tk.Frame(dialog, bg=PALETTE["bg_root"], padx=12, pady=12)
        txt_frame.pack(fill="both", expand=True)

        txt = tk.Text(
            txt_frame, font=("Consolas", 10),
            bg=PALETTE["chat_bg"], fg="#A7F3D0",
            insertbackground="#FFFFFF", relief="flat", padx=10, pady=10
        )
        txt_scroll = ttk.Scrollbar(txt_frame, orient="vertical", command=txt.yview)
        txt.configure(yscrollcommand=txt_scroll.set)

        txt.pack(side="left", fill="both", expand=True)
        txt_scroll.pack(side="right", fill="y")

        reload_json()

    # ─── Forget Me / Reset Memory ─────────────────────────────────────────────
    def confirm_forget_me(self):
        confirm = messagebox.askyesno(
            "Confirm Reset",
            "Are you sure you want to clear your saved user profile?\n"
            "This will erase your stored name, location, and preferences.",
            parent=self.root
        )
        if confirm:
            reply = process_turn("forget me", self.memory)[0]
            self.add_bubble("system", "Profile data cleared from persistent memory")
            self.add_bubble("bot", reply)
            self.update_sidebar_profile()

    def clear_chat_display(self):
        for widget in self.messages_inner.winfo_children():
            widget.destroy()
        self.message_count = 0
        self.stats_badge.configure(text="0 messages")
        self.add_bubble("system", "Chat view cleared (session memory still preserved)")

    def on_close(self):
        try:
            save_memory(self.memory)
        except Exception:
            pass
        self.root.destroy()

def run_gui():
    root = tk.Tk()
    app = EchoMindGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
