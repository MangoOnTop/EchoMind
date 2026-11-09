rules = {
    # Identity Queries
    "ask_name": ["what is my name", "whats my name", "who am i", "do you know my name", "tell me my name"],
    "name": ["my name is", "call me", "i am called"],

    # Location Information
    "ask_location": ["where do i live", "where am i from", "what is my location", "do you know where i live", "what is my address"],
    "location": ["i live in", "i am from"],

    # Hobbies & Interests (Schema fields: fav_game, fav_hobby)
    "ask_game": ["what is my favorite game", "whats my favorite game", "what is my fav game", "whats my fav game", "what game do i like"],
    "game": ["my favorite game is", "my favourite game is", "my fav game is"],
    "ask_hobby": ["what is my hobby", "whats my hobby", "what is my favorite hobby", "whats my favorite hobby", "what's my hobby"],
    "hobby": ["my favorite hobby is", "my favourite hobby is", "my fav hobby is", "my hobby is"],

    # Context & Recall
    "recall": ["what did i said just now", "what did i tell you", "what did i say", "what was my last message", "repeat what i said", "what did i just say"],

    # Bot Status & Humor
    "status_check": ["how are you", "how are you doing", "how r u", "how do you do", "hows it going"],
    "farewell_check": ["how are you"],  # Original key retained for backward compatibility
    "user_mood": ["i am good", "i am doing good", "i'm good", "i am fine", "i'm fine", "doing well", "doing great", "not good", "feeling sad", "feeling happy", "feeling great"],

    # Greetings & Farewells
    "greeting": ["hi", "hello", "hey", "wazzap", "yo", "whats up", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "quit", "exit", "goodbye", "see you", "cya", "farewell"],

    # Politeness & Utility
    "thanks": ["thank you", "thanks", "thx", "appreciate it", "thank you so much"],
    "help": ["help", "what can you do", "commands", "options", "features", "what are your commands"],
    "identity": ["who are you", "what are you", "tell me about yourself", "what is echomind"],
    "forget_me": ["forget me", "reset my memory", "clear my data", "reset memory", "clear memory", "wipe memory", "erase memory"],
    "memory_status": ["show memory", "memory status", "my profile", "session info", "what do you remember", "what do you know about me"],
}
