import json
import os
import sys
from datetime import datetime
import time
import copy

# Ensure project root is in sys.path so imports work from any working directory
if getattr(sys, "frozen", False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
else:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.schema import memory_schema

MEMORY_FILE = os.path.join(PROJECT_ROOT, "echomind_memory.json")

def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def reset_memory() -> dict:
    """Creates and persists a fresh memory structure based on schema.py."""
    new_memory = copy.deepcopy(memory_schema)
    now = get_current_time()
    new_memory["metadata"]["session_start_time"] = now
    new_memory["metadata"]["session_count"] = 1
    new_memory["metadata"]["last_saved"] = now
    new_memory["metadata"]["latest-update-time"] = now
    save_memory(new_memory)
    return new_memory

def load_memory() -> dict:
    # First-ever run check
    if not os.path.exists(MEMORY_FILE):
        return reset_memory()

    try:
        # Reading existing file
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
            
            # Backfill any missing schema keys for backwards compatibility & self-healing
            for key, val in memory_schema.items():
                if key not in memory:
                    memory[key] = copy.deepcopy(val)
            if isinstance(memory.get("user_profile"), dict):
                for k, v in memory_schema["user_profile"].items():
                    if k not in memory["user_profile"]:
                        memory["user_profile"][k] = copy.deepcopy(v)
            if isinstance(memory.get("metadata"), dict):
                for k, v in memory_schema["metadata"].items():
                    if k not in memory["metadata"]:
                        memory["metadata"][k] = copy.deepcopy(v)

            memory["metadata"]["session_start_time"] = get_current_time()
            memory["metadata"]["session_count"] = memory["metadata"].get("session_count", 0) + 1
            return memory

    # Crash protection (Corrupted file handling)    
    except (json.JSONDecodeError, KeyError, Exception) as e:
        print(f"WARNING! Memory file issue detected ({e}).")
        time.sleep(0.5)
        print("Starting with fresh memory.")
        return reset_memory()

def save_memory(memory: dict) -> None:
    now = get_current_time()
    if "metadata" in memory:
        memory["metadata"]["last_saved"] = now
        memory["metadata"]["latest-update-time"] = now
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)

# Runs a quick self-test of load_memory() and save_memory()        
if __name__ == "__main__":
    state = load_memory()
    print("Memory loaded successfully!")
    print(f"Session count: {state['metadata']['session_count']}")
    print(f"Session started at: {state['metadata']['session_start_time']}")
    save_memory(state)
    print(f"Memory saved to {MEMORY_FILE}")
