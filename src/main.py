import os
import sys

# Ensure project root in sys.path
if getattr(sys, "frozen", False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
else:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.memory_manager import load_memory, save_memory
from src.engine import get_response, process_turn

def run_cli():
    memory = load_memory()
    save_memory(memory)

    username = memory.get("user_profile", {}).get("username")
    if username:
        print(f"EchoMind: Welcome back, {username}!")
    else:
        print("EchoMind: Hi, I am EchoMind. What's your name? (Type 'help' for options)")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEchoMind: Goodbye!")
            break

        if not user_input:
            continue

        reply, is_farewell = process_turn(user_input, memory)
        print(f"EchoMind: {reply}")

        if is_farewell:
            break

if __name__ == "__main__":
    run_cli()
