import re
import os
import sys

# Ensure root in sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.rules import rules
from src.handler_mapping import handlers
from src.memory_manager import save_memory

def normalize_text(text: str) -> str:
    """Normalize text by expanding contractions, removing punctuation, and collapsing whitespace."""
    if not text:
        return ""
    t = text.lower()
    t = t.replace("what's", "whats").replace("i'm", "i am").replace("how's", "hows")
    # Replace punctuation with spaces
    t_clean = re.sub(r"[^\w\s]", " ", t)
    return " ".join(t_clean.split())

def match_intent(user_input: str):
    """Matches the input against rules and returns (category, handler) or (None, None)."""
    norm = normalize_text(user_input)
    words = norm.split()
    if not words:
        return None, None

    for category, handler in handlers.items():
        trigger_list = rules.get(category, [])
        # If trigger contains spaces, search normalized substring; otherwise check exact word list
        if any((t in norm if " " in t else t in words) for t in trigger_list):
            return category, handler

    return None, None

def get_response(user_input: str, memory: dict) -> str:
    """Generate a response for a user input using the rule engine."""
    clean_input = user_input.strip() if user_input else ""
    if not clean_input:
        return "I'm listening! Feel free to say something or type 'help'."

    category, handler = match_intent(clean_input)
    if handler:
        return handler(clean_input, memory)

    return "Sorry, I didn't understand that. Type 'help' to see what I can do!"

def is_farewell_input(user_input: str) -> bool:
    """Check if input signals a farewell/exit."""
    norm = normalize_text(user_input)
    words = norm.split()
    farewell_triggers = rules.get("farewell", [])
    return any((t in norm if " " in t else t in words) for t in farewell_triggers)

def process_turn(user_input: str, memory: dict) -> tuple:
    """
    Processes one conversational turn:
    1. Computes bot reply
    2. Logs user and bot messages to conversation history
    3. Persists memory to disk
    4. Returns (reply, is_farewell)
    """
    reply = get_response(user_input, memory)
    farewell = is_farewell_input(user_input)

    # Short-term working memory
    memory.setdefault("conversation_history", []).append({"speaker": "user", "text": user_input})
    memory["conversation_history"].append({"speaker": "bot", "text": reply})
    save_memory(memory)

    return reply, farewell
