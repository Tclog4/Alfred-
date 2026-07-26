import json
import os
from datetime import datetime


MEMORY_FILE = "database/memory.json"



def create_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "w"
        ) as file:

            json.dump(
                {
                    "facts": {},
                    "history": []
                },
                file,
                indent=4
            )



def load_memory():

    create_memory()

    with open(
        MEMORY_FILE,
        "r"
    ) as file:

        return json.load(file)



def save_memory(data):

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



# Remember information

def remember(key, value):

    memory = load_memory()


    memory["facts"][key] = value


    save_memory(memory)


    return (
        f"I will remember that "
        f"{key} is {value}."
    )



# Recall information

def recall(key):

    memory = load_memory()


    if key in memory["facts"]:

        return (
            f"{key} is "
            f"{memory['facts'][key]}"
        )


    return (
        "I don't remember that yet."
    )



# Store events

def remember_event(event):

    memory = load_memory()


    memory["history"].append({

        "event": event,

        "time": datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })


    save_memory(memory)


    return "Event saved."



# View history

def get_history():

    memory = load_memory()


    if not memory["history"]:

        return "No history yet."


    result = "Alfred History:\n"


    for item in memory["history"]:

        result += (
            f"- {item['time']}: "
            f"{item['event']}\n"
        )


    return result
