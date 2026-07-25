import json
import os

MEMORY_FILE = "database/memory.json"


def create_memory_file():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as file:
            json.dump({}, file, indent=4)


def load_memory():
    create_memory_file()

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):
    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return f"I will remember that {key} is {value}."


def recall(key):
    memory = load_memory()

    if key in memory:
        return memory[key]

    return "I don't remember that yet."


def forget(key):
    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)
        return f"I forgot {key}."

    return "I couldn't find that memory."
