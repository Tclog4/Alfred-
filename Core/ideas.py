import json
import os


IDEA_FILE = "database/ideas.json"



def create_file():

    if not os.path.exists(IDEA_FILE):

        with open(IDEA_FILE, "w") as file:

            json.dump([], file, indent=4)



def load_ideas():

    create_file()

    with open(IDEA_FILE, "r") as file:

        return json.load(file)



def save_ideas(ideas):

    with open(IDEA_FILE, "w") as file:

        json.dump(
            ideas,
            file,
            indent=4
        )



def add_idea(idea):

    ideas = load_ideas()

    ideas.append({
        "idea": idea,
        "status": "New"
    })


    save_ideas(ideas)


    return f"Idea saved: {idea}"



def get_ideas():

    ideas = load_ideas()


    if not ideas:

        return "No ideas saved yet."


    result = "Idea Vault:\n"


    for number, item in enumerate(ideas, 1):

        result += (
            f"{number}. "
            f"{item['idea']} "
            f"- {item['status']}\n"
        )


    return result
