import re
import copy
from src.schema import memory_schema
from src.memory_manager import save_memory

def clean_value(raw: str) -> str:
    """Strip leading/trailing punctuation and whitespace, preserving proper case."""
    val = raw.strip().strip(".!?,:;\"'")
    if val.islower():
        return val.title()
    return val

def handle_name(user_input, memory):
    # Match patterns like "my name is Alex", "call me Alex"
    m = re.search(r'\b(?:my name is|call me|i am called)\s+([a-zA-Z0-9_\-\s\']+)', user_input, re.IGNORECASE)
    if m:
        name = clean_value(m.group(1))
        if name:
            memory["user_profile"]["username"] = name
            save_memory(memory)
            return f"Nice to meet you, {name}! I'll remember that."
    return "I didn't catch your name. Please say 'My name is [your name]'!"

def handle_ask_name(user_input, memory):
    username = memory["user_profile"].get("username")
    if username:
        return f"Your name is {username}!"
    return "I don't know your name yet — tell me with 'My name is [name]'!"

def handle_greeting(user_input, memory):
    username = memory["user_profile"].get("username")
    if username:
        return f"Hello {username}! Great to see you again. How can I help you today?"
    return "Yo! I'm EchoMind. What's your name? (You can say 'My name is ...')"

def handle_status_check(user_input, memory):
    return "I'm doing great, running smoothly on Python! How are you doing today?"

def handle_farewell_check(user_input, memory):
    # Retained original witty response as an option / fallback
    return "Running smoothly! Rule-based, persistent, and ready to assist. What about you?"

def handle_user_mood(user_input, memory):
    text = user_input.lower()
    if any(w in text for w in ["good", "great", "fine", "well", "happy"]):
        return "Glad to hear that! How can I assist you today?"
    elif any(w in text for w in ["sad", "not good", "bad", "tired", "down"]):
        return "Hang in there! I'm just code, but I'm here to chat or help whenever you need."
    return "Noted! Always here if you want to chat or test my memory."

def handle_location(user_input, memory):
    m = re.search(r'\b(?:i live in|i am from|i\'m from)\s+([a-zA-Z0-9_\-\s,]+)', user_input, re.IGNORECASE)
    if m:
        location = clean_value(m.group(1))
        if location:
            memory["user_profile"]["location"] = location
            save_memory(memory)
            return f"Got it, {location} — noted in my memory!"
    return "Where do you live? Tell me with 'I live in [city]'!"

def handle_ask_location(user_input, memory):
    location = memory["user_profile"].get("location")
    if location:
        return f"You live in {location}!"
    return "I don't know where you live yet — tell me with 'I live in [city]'!"

def handle_game(user_input, memory):
    m = re.search(r'\b(?:my favorite game is|my favourite game is|my fav game is)\s+([a-zA-Z0-9_\-\s\':]+)', user_input, re.IGNORECASE)
    if m:
        game = clean_value(m.group(1))
        if game:
            memory["user_profile"]["fav_game"] = game
            save_memory(memory)
            return f"Awesome choice! I've saved that your favorite game is {game}."
    return "What's your favorite game? Say 'My favorite game is [game]'!"

def handle_ask_game(user_input, memory):
    game = memory["user_profile"].get("fav_game")
    if game:
        return f"Your favorite game is {game}!"
    return "I don't know your favorite game yet — tell me with 'My favorite game is [game]'!"

def handle_hobby(user_input, memory):
    m = re.search(r'\b(?:my favorite hobby is|my favourite hobby is|my fav hobby is|my hobby is)\s+([a-zA-Z0-9_\-\s\':]+)', user_input, re.IGNORECASE)
    if m:
        hobby = clean_value(m.group(1))
        if hobby:
            memory["user_profile"]["fav_hobby"] = hobby
            save_memory(memory)
            return f"Sounds wonderful! I've saved that your hobby is {hobby}."
    return "What's your hobby? Say 'My hobby is [hobby]'!"

def handle_ask_hobby(user_input, memory):
    hobby = memory["user_profile"].get("fav_hobby")
    if hobby:
        return f"Your favorite hobby is {hobby}!"
    return "I don't know your hobby yet — tell me with 'My hobby is [hobby]'!"

def handle_recall(user_input, memory):
    history = memory.get("conversation_history", [])
    # Find the most recent message from the user before the current one
    user_msgs = [entry["text"] for entry in history if entry.get("speaker") == "user"]
    if user_msgs:
        return f'You said: "{user_msgs[-1]}"'
    return "We haven't talked long enough for me to recall that yet!"

def handle_identity(user_input, memory):
    return "I'm EchoMind — a lightweight rule-based chatbot with persistent session memory."

def handle_thanks(user_input, memory):
    return "You're very welcome!"

def handle_help(user_input, memory):
    return (
        "Here's what I can do:\n"
        " • Name: 'My name is [name]', 'Who am I?'\n"
        " • Location: 'I live in [city]', 'Where do I live?'\n"
        " • Favorites: 'My favorite game is [game]', 'My hobby is [hobby]'\n"
        " • Recall: 'What did I say?'\n"
        " • Memory: 'Show memory', 'Forget me'\n"
        " • Controls: 'Help', 'How are you', 'Bye'"
    )

def handle_farewell(user_input, memory):
    username = memory["user_profile"].get("username")
    if username:
        return f"See you later, {username}! Have a great day!"
    return "See you later! Have a great day!"

def handle_forget_me(user_input, memory):
    memory["user_profile"] = copy.deepcopy(memory_schema["user_profile"])
    save_memory(memory)
    return "Okay, I've cleared your personal profile from my memory."

def handle_memory_status(user_input, memory):
    prof = memory.get("user_profile", {})
    meta = memory.get("metadata", {})
    return (
        f"Memory Status:\n"
        f" • Username: {prof.get('username') or '(not set)'}\n"
        f" • Location: {prof.get('location') or '(not set)'}\n"
        f" • Fav Game: {prof.get('fav_game') or '(not set)'}\n"
        f" • Fav Hobby: {prof.get('fav_hobby') or '(not set)'}\n"
        f" • Session: #{meta.get('session_count', 1)} (Saved: {meta.get('last_saved', 'N/A')})"
    )
