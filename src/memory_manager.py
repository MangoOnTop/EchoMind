import json
import os
from datetime import datetime
from src.schema import memory_schema
import time
import copy

MEMORY_FILE = "echomind_memory.json"

def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_memory() -> dict:
    #First-ever run check
    if not os.path.exists(MEMORY_FILE):
        new_memory = copy.deepcopy(memory_schema)
        new_memory["metadata"]["session_start_time"] = get_current_time()
        new_memory["metadata"]["session_count"] = 1
        save_memory(new_memory)
        return new_memory
    try:
        #Reading existing file
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
            memory["metadata"]["session_start_time"] = get_current_time()
            memory["metadata"]["session_count"] += 1
            return memory
    #Crash protection (Corrupted file handling)    
    except (json.JSONDecodeError, KeyError):
        print("WARNING! Memory file is corrupted.")
        time.sleep(1)
        print("Starting with a fresh memory")
        new_memory = copy.deepcopy(memory_schema)
        new_memory["metadata"]["session_start_time"] = get_current_time()
        new_memory["metadata"]["session_count"] = 1
        save_memory(new_memory)
        return new_memory

def save_memory(memory: dict) -> None:
    memory["metadata"]["last_saved"] = get_current_time()
    with open(MEMORY_FILE, "w", encoding = "utf-8") as f:
        json.dump(memory, f, indent=4)

#Runs a quick self-test of load_memory() and save_memory()        
if __name__ == "__main__":
    state = load_memory()
    print("Memory loaded successfully!")
    print(f"Session count: {state["metadata"]["session_count"]}")
    print(f"Session started at: {state["metadata"]["session_start_time"]}")
    save_memory(state)
    print(f"Memory saved to {MEMORY_FILE}")                    