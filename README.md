# EchoMind 🧠
<<<<<<< HEAD
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
=======
A lightweight, modern rule-engine chatbot and persistent memory assistant built in Python. **EchoMind** serves as a beginner-friendly exploration into state management, session memory, and intent mapping—foundational concepts used by modern AI agents—now with both a **modern desktop GUI** and a classic terminal CLI!

## What It Is
EchoMind is a rule-based agent with dual interfaces:
1. **Modern Desktop GUI:** A sleek dark-mode desktop window featuring real-time memory inspection, interactive prompt chips, and a scrollable bubble chat feed.
2. **Terminal CLI:** A lightweight command-line interface for fast terminal interaction.

Unlike stateless scripts, EchoMind tracks user profile details, session metadata, and conversation history across restarts using a structured JSON schema (`echomind_memory.json`).

### Key Features

- **🎨 Modern Desktop GUI:** Beautiful dark-themed interface built with zero external dependencies (pure Python Tkinter). Features real-time memory state display, quick action buttons, prompt chips, and an in-app JSON inspector.
- **💾 Persistent Memory:** Remembers your name, location, favorite games, and hobbies across sessions using `echomind_memory.json`.
- **🧠 Context Awareness:** Recalls previous statements (e.g., answering `"what did i say?"` using short-term conversation logs).
- **🔤 Punctuation-Safe Matching:** Built-in normalization handles punctuation, contractions, and varying cases seamlessly (e.g. `"Hello!"`, `"What's my name?"`, `"Where do I live?"`).
- **🛡️ Self-Healing State:** Automatically verifies and heals the memory file against `schema.py` if missing or corrupted.
- **📁 Universal Launchers:** Run anywhere—from project root, from `src/`, or via one-click Windows batch files (`run_gui.bat`, `run_cli.bat`).

---

## Project Structure

```
EchoMind/
├── .gitignore
├── README.md
├── gui.py                  # Main Desktop GUI launcher
├── run.py                  # Universal launcher (GUI by default, --cli for terminal)
├── run_gui.bat             # 1-click Windows launcher for GUI
├── run_cli.bat             # 1-click Windows launcher for CLI
├── echomind_memory.json    # Auto-generated persistent JSON memory
└── src/
    ├── schema.py           # Blueprint for user profile & conversation memory
    ├── memory_manager.py   # Handles reading, writing, and self-healing JSON memory
    ├── rules.py            # Keyword triggers mapped to intent categories
    ├── handler.py          # Functions that process logic for matched intents
    ├── handler_mapping.py  # Dictionary linking intent keys to handler functions
    ├── engine.py           # Central intent matching & conversation engine
    ├── gui.py              # Modern Tkinter desktop application
    └── main.py             # Classic terminal chat loop
```

---

## How to Run

### Prerequisites

- Python 3.8 or higher installed on your system (standard installation includes Tkinter).

### 1. Launching the Modern Desktop GUI (Recommended)

From the project root directory, run:
>>>>>>> 4bedd04adc7f07915fcd65748dfd626673b8eb53

```bash
python gui.py
```
<<<<<<< HEAD

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
=======
*Or simply double-click **`run_gui.bat`** on Windows!*

### 2. Launching via Universal Launcher

```bash
python run.py         # Launches the modern GUI
python run.py --cli   # Launches the Terminal CLI
```

### 3. Launching the Terminal CLI Directly

```bash
python src/main.py
```
*Or double-click **`run_cli.bat`** on Windows.*

Type `bye`, `exit`, or `quit` to end the session.

---

## Example Commands You Can Try

| Category | Example Inputs | EchoMind Action |
|---|---|---|
| **Identity** | `"My name is Mahi"`, `"Call me Sarah"` | Saves name to persistent profile |
| **Recall Identity** | `"Who am I?"`, `"What is my name?"` | Retrieves stored username |
| **Location** | `"I live in Tokyo"`, `"I am from London"` | Saves location to persistent profile |
| **Recall Location** | `"Where do I live?"`, `"Where am I from?"` | Retrieves stored location |
| **Favorites** | `"My favorite game is Cyberpunk"`, `"My hobby is Coding"` | Stores game & hobby |
| **Recall Favorites** | `"What is my favorite game?"`, `"What is my hobby?"` | Retrieves saved favorites |
| **Short-Term Memory** | `"What did I say?"`, `"What did I just say?"` | Recalls previous statement |
| **Memory Status** | `"Show memory"`, `"My profile"` | Displays full session and profile stats |
| **Clear Data** | `"Forget me"`, `"Reset my memory"` | Wipes stored profile data safely |
| **Help & Info** | `"Help"`, `"Who are you"`, `"How are you"` | Explains capabilities and status |
| **Farewell** | `"Bye"`, `"Goodbye"`, `"Exit"` | Greets goodbye by name and ends session |

---

## Limitations

- **Rule & Pattern Matching:** Operates using pattern recognition and substring matching rather than a heavy cloud LLM.
- **Single-Turn Focus:** Focuses on immediate triggers and turn-by-turn memory rather than deep multi-paragraph reasoning.
- **Local JSON Storage:** Memory is stored in a clean local JSON file without encryption, perfect for local desktop privacy and learning.
>>>>>>> 4bedd04adc7f07915fcd65748dfd626673b8eb53
