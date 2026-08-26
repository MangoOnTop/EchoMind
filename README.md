# EchoMind 
A lightweight, terminal-based rule-engine chatbot built in Python. **EchoMind** serves as a beginner-friendly exploration into state management, session memory, and intent mapping—foundational concepts used by modern AI agents.

## What It Is
EchoMind is a rule-based chatbot running directly in the command line. Unlike stateless scripts, it tracks user profile details, session metadata, and conversation history across restarts using a structured JSON schema.

### Key Features

- **Persistent Memory:** Remembers your name and location across terminal sessions using `echomind_memory.json`.
- **Context Awareness:** Recalls previous inputs (e.g., answering `"what did i say?"` using short-term conversation logs).
- **Modular Architecture:** Cleanly separates memory schema, intent triggers, execution handlers, and file operations.
- **Self-Healing State:** Automatically generates a new memory file from `schema.py` if missing or corrupted.

## Project Structure
Plaintext

```
EchoMind/
├── .gitignore
├── README.md
└── src/
    ├── schema.py           # Blueprint for user profile & conversation memory
    ├── memory_manager.py   # Handles reading, writing, and resetting JSON memory
    ├── rules.py            # Keyword triggers mapped to intent categories
    ├── handler.py          # Functions that process logic for matched intents
    ├── handler_mapping.py  # Dictionary linking intent keys to handler functions
    └── main.py             # Main terminal chat loop
```

## How to Make It Work

### Prerequisites

- Python 3.8 or higher installed on your system.

### Running the Chatbot

1. Open your terminal in the project root directory.
2. Run `src/main.py` directly :
Bash

```
python src/main.py
```

1. Type your messages in the prompt. Type `bye`, `exit`, or `quit` to end the session.

### Example Commands You Can Try

- **Set Name:** `"my name is mahi"`
- **Recall Identity:** `"who am i?"` or `"what is my name?"`
- **Recall Last Message:** `"what did i say?"`
- **Set Location:** `"i live in Tokyo"` or `"i am from London"`
- **Clear Data:** `"forget me"`
- **Get Help:** `"help"`

## Limitations

- **Exact Keyword Matching:** Relies on predefined keyword lists and sub-string matching rather than Natural Language Processing (NLP) or LLMs. Phrasing outside defined triggers will result in fallback responses.
- **Sequential Processing:** Matches the first keyword intent found; it cannot handle complex multi-intent statements in a single turn.
- **Simple Recall Window:** Short-term recall is basic and only looks back to immediate preceding messages rather than semantic search across long history logs.
- **Local JSON Storage:** Memory is stored in a plain local JSON file without encryption, designed strictly for learning purposes rather than production storage.
