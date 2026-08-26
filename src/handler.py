from src.memory_manager import save_memory

def handle_name(user_input, memory):
    name = user_input.lower().split("my name is ")[-1].strip()
    memory["user_profile"]["username"] = name
    save_memory(memory)
    return f"Nice to meet you, {name}!"

def handle_greeting(user_input, memory):
    return "Yo"

def handle_farewell_check(user_input, memory):
    return "Nothing but a if-else python code done by a depressed soul :(. What about you?"

def handle_recall(user_input, memory):
    history = memory["conversation_history"]
    if len(history) < 2:
        return "We haven't talked long enough for me to recall that yet!"
    else:
        previous_message = history[-2]["text"]
        return f"You said, {previous_message}"

def handle_ask_name(user_input, memory):
    username = memory["user_profile"]["username"]
    if username:
        return f"Your name is {username}!"
    else:
        return "I don't know your name yet — tell me!"

def handle_farewell(user_input, memory):
    return f"See you later, {memory['user_profile']['username']}"

def handle_thanks(user_input, memory):
    return "You're welcome!"

def handle_help(user_input, memory):
    return ("Here's what I can do: tell me your name, ask 'who am i', "
            "ask 'how are you', ask 'what did i say', tell me where you live, "
            "or say 'forget me' to wipe your saved info.")

def handle_identity(user_input, memory):
    return "I'm EchoMind — a simple rule-based chatbot with a memory file."

def handle_location(user_input, memory):
    text = user_input.lower()
    if "i live in" in text:
        location = text.split("i live in")[-1].strip()
    else:
        location = text.split("i am from")[-1].strip()
    memory["user_profile"]["location"] = location
    save_memory(memory)
    return f"Got it, {location} — noted!"

def handle_forget_me(user_input, memory):
    memory["user_profile"] = {
        "username": None, "location": None, "living": None,
        "fav_hobby": None, "fav_game": None, "important_fact": [],
    }
    save_memory(memory)
    return "Okay, I've forgotten everything about you."