# EchoMind 🧠
> **A Desktop AI Assistant & Persistent Memory Engine for Windows**

**EchoMind** is an intelligent desktop companion built with Python. Unlike typical stateless chatbots, EchoMind features a **persistent memory engine** that retains your identity, location, interests, and conversation context across sessions. It features a modern dark-themed graphical user interface (GUI) with a real-time memory inspector, interactive prompt chips, and an in-app JSON memory viewer—with **zero external library dependencies** required!

---

## 🖥️ Desktop Interface

EchoMind is designed around a dual-pane desktop workspace:

```
┌───────────────────────────────┬────────────────────────────────────────────────────────┐
│  🧠 EchoMind                  │  💬 EchoMind Assistant                   [4 messages]  │
│  ● Online • State Synced      │  Persistent memory loaded from echomind_memory.json    │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│  PERSISTENT MEMORY            │                                                        │
│  👤 Name:      Mahi           │   🤖 EchoMind                              [10:30 AM]  │
│  📍 Location:  Tokyo          │   Welcome back, Mahi! How can I help you today?        │
│  🎮 Fav Game:  Cyberpunk 2077 │                                                        │
│  🎨 Hobby:     Coding         │                                    👤 You  [10:31 AM]  │
│  🔢 Session:   #2             │                              What is my favorite game? │
│  ⏱️ Last Saved: 10:30:15      │                                                        │
├───────────────────────────────┤   🤖 EchoMind                              [10:31 AM]  │
│  QUICK ACTIONS                │   Your favorite game is Cyberpunk 2077!                │
│  [👤 Who Am I?]               │                                                        │
│  [📍 Where Do I Live?]        │                                                        │
│  [🎮 What's My Game?]         │                                                        │
│  [🧠 What Did I Say?]         │                                                        │
│  [❓ Help & Commands]         ├────────────────────────────────────────────────────────┤
├───────────────────────────────┤  [👋 Hello!] [🏷️ Set Name] [📍 Set Location] [❓ Help] │
│  MEMORY TOOLS                 ├────────────────────────────────────────────────────────┤
│  [📄 View JSON Memory]        │  Type a message... (Press Enter to send)   [ Send ➔ ]  │
│  [🗑️ Forget Me (Reset)]       │                                                        │
└───────────────────────────────┴────────────────────────────────────────────────────────┘
```

### ✨ Key Highlights

- **🎨 Modern Dark GUI:** Native high-DPI desktop window with smooth bubble messaging, speaker badges, and timestamps.
- **🔍 Live Memory Inspector:** Watch your persistent profile update in real time on the left sidebar as you chat.
- **💾 Persistent JSON Engine:** Stores profile attributes and session metrics across restarts in `echomind_memory.json`.
- **⚡ Quick Action Chips & Buttons:** One-click shortcuts for testing identity, location, recall, and help commands.
- **📄 In-App JSON Viewer:** Inspect and reload the raw `echomind_memory.json` state right inside the app.
- **🛡️ Self-Healing State:** Automatically repairs missing schema keys or recovers corrupted state using `schema.py`.
- **🔤 Punctuation-Safe NLP:** Normalizes contractions and punctuation so inputs like `"Hello!"`, `"What's my name?"`, or `"Where do I live?"` work effortlessly.
- **📦 Standalone Executable Ready:** Can be compiled into a standalone Windows binary: **`EchoMind.exe`**.

---

## 🚀 Running EchoMind

### Prerequisites

- **Python 3.8+** (Tkinter is included with standard Python on Windows).

### 1. Launch the Desktop App (Recommended)

Simply double-click **`EchoMind.bat`**, or run from your terminal:

```bash
python gui.py
```

### 2. Universal Launcher

```bash
python run.py         # Launches the modern Desktop GUI
python run.py --cli   # Launches in Terminal Debug mode
```

---

## 📦 Building `EchoMind.exe` (Standalone Windows Executable)

You can package EchoMind into a single standalone `.exe` so anyone on Windows can run it without needing Python installed.

The official executable name is **`EchoMind.exe`**.

### 1-Click Build:
Double-click **`build_exe.bat`**, or run:

```bash
python build_exe.py
```

This runs PyInstaller with `--noconsole --onefile` and generates:
```
dist/
└── EchoMind.exe
```

Once built, double-clicking **`EchoMind.bat`** will automatically launch your compiled `dist/EchoMind.exe` directly!

---

## 💬 Things You Can Say to EchoMind

| Category | Example Phrases | Bot Action |
|---|---|---|
| **Identity** | `"My name is Alex"`, `"Call me Mahi"` | Remembers your name in `user_profile` |
| **Recall Name** | `"Who am I?"`, `"What is my name?"` | Retrieves stored username |
| **Location** | `"I live in Tokyo"`, `"I am from London"` | Remembers your city/location |
| **Recall Location** | `"Where do I live?"`, `"Where am I from?"` | Retrieves stored location |
| **Favorites** | `"My favorite game is Elden Ring"`, `"My hobby is Photography"` | Saves game & hobby to memory |
| **Recall Favorites** | `"What is my favorite game?"`, `"What is my hobby?"` | Recalls saved preferences |
| **Short-Term Recall** | `"What did I say?"`, `"What did I just say?"` | Recalls previous statement from chat history |
| **Memory Status** | `"Show memory"`, `"My profile"` | Displays full profile summary in chat |
| **Clear Profile** | `"Forget me"`, `"Reset my memory"` | Wipes personal profile safely |
| **Status & Chat** | `"How are you"`, `"I am good"`, `"Thanks"` | Conversational check-ins and mood responses |
| **Help** | `"Help"`, `"What can you do"` | Lists available capabilities and commands |
| **Farewell** | `"Bye"`, `"Goodbye"`, `"Exit"` | Warm goodbye addressing you by name |

---

## 📂 Project Architecture

```
EchoMind/
├── EchoMind.bat            # 1-click launcher (launches EchoMind.exe or gui.py)
├── gui.py                  # Desktop application entry point
├── run.py                  # Universal launcher (GUI by default, --cli flag)
├── build_exe.py            # Automated builder for EchoMind.exe
├── build_exe.bat           # 1-click batch builder for EchoMind.exe
├── echomind_memory.json    # Persistent JSON storage file
├── README.md               # Documentation
├── .gitignore              # Git ignore rules
└── src/
    ├── gui.py              # Tkinter GUI implementation & styling
    ├── engine.py           # Core text normalization & intent matching
    ├── memory_manager.py   # JSON read/write & self-healing state
    ├── schema.py           # Blueprint for persistent memory
    ├── rules.py            # Keyword trigger rules
    ├── handler.py          # Action handlers for intents
    ├── handler_mapping.py  # Connects categories to handlers
    └── main.py             # Optional CLI terminal loop
```

---

## 🧠 Memory Schema (`schema.py`)

Persistent data is stored in standard JSON structured as:

```json
{
    "metadata": {
        "version": "1.0",
        "create-time": "2026-08-25",
        "latest-update-time": "2026-11-11 22:50:00",
        "session_count": 3,
        "last_saved": "2026-11-11 22:50:00",
        "session_start_time": "2026-11-11 22:45:00"
    },
    "user_profile": {
        "username": "Mahi",
        "location": "Tokyo",
        "living": null,
        "fav_hobby": "Coding",
        "fav_game": "Cyberpunk 2077",
        "important_fact": []
    },
    "conversation_history": [
        {"speaker": "user", "text": "Who am I?"},
        {"speaker": "bot", "text": "Your name is Mahi!"}
    ]
}
```

---

## 📜 License
Open-source under the MIT License. Feel free to fork, customize, and build upon EchoMind!
