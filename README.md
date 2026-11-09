# EchoMind 🧠
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

```bash
python gui.py
```
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
