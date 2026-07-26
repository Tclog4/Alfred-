import json
import os
from datetime import datetime


LEARNING_FILE = "database/learning.json"



def create_file():

    if not os.path.exists(LEARNING_FILE):

        with open(
            LEARNING_FILE,
            "w"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )



def load_learning():

    create_file()

    with open(
        LEARNING_FILE,
        "r"
    ) as file:

        return json.load(file)



def save_learning(data):

    with open(
        LEARNING_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



def record_problem(problem):

    data = load_learning()


    data.append({

        "type": "problem",

        "message": problem,

        "time": datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })


    save_learning(data)


    return "Problem recorded."



def record_improvement(idea):

    data = load_learning()


    data.append({

        "type": "improvement",

        "message": idea,

        "time": datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })


    save_learning(data)


    return "Improvement saved."



def get_learning():

    data = load_learning()


    if not data:

        return "No learning data yet."


    result = "Alfred Learning:\n"


    for item in data:

        result += (
            f"- {item['type']}: "
            f"{item['message']}\n"
        )


    return result
