from src.memory_manager import load_memory, save_memory
from src.rules import rules
from src.rules import rules
from src.handler_mapping import handlers

memory = load_memory()
save_memory(memory)

if memory["user_profile"]["username"]:
    print(f"EchoMind: Welcome back, {memory["user_profile"]["username"]}")
else:
    print("EchoMind: Hi, I am EchoMind. What's your name?") 

def get_response(user_input, memory):
    text = user_input.lower()
    words = text.split()
    for category, handler in handlers.items():
        trigger_list = rules[category]
        if any((x in text if " " in x else x in words) for x in trigger_list):
            return handler(user_input, memory)
    return "Sorry I didn't understand that."  

while True:
    user_input = input("You: ")
    words = user_input.lower().split()
    reply = get_response(user_input, memory)
    if any(word in rules["farewell"] for word in words):
            print(f"EchoMind: {reply}\n")
            memory["conversation_history"].append({"speaker" : "user", "text" : user_input})
            memory["conversation_history"].append({"speaker" : "bot", "text" : reply})
            save_memory(memory)
            break
    else:
        print(f"EchoMind: {reply}")
        memory["conversation_history"].append({"speaker" : "user", "text" : user_input})
        memory["conversation_history"].append({"speaker" : "bot", "text" : reply})                                        
        save_memory(memory)