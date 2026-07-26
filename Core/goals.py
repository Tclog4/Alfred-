import json
import os
from datetime import datetime


GOAL_FILE = "database/goals.json"



class GoalManager:


    def __init__(self):

        self.setup()



    def setup(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(GOAL_FILE):

            with open(
                GOAL_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            GOAL_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            GOAL_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def create_goal(
        self,
        name
    ):

        goals = self.load()


        goals.append({

            "name": name,

            "progress": 0,

            "tasks": [],

            "created": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })


        self.save(goals)


        return (
            f"Goal created: {name}"
        )



    def add_goal_task(
        self,
        goal,
        task
    ):

        goals = self.load()


        for item in goals:

            if item["name"] == goal:

                item["tasks"].append({

                    "task": task,

                    "complete": False

                })


        self.save(goals)


        return (
            "Task added to goal."
        )



    def complete_goal_task(
        self,
        goal,
        number
    ):

        goals = self.load()


        for item in goals:

            if item["name"] == goal:

                try:

                    item["tasks"][number]["complete"] = True

                except:

                    return "Task not found."



                total = len(
                    item["tasks"]
                )


                done = len(
                    [
                        x for x in item["tasks"]
                        if x["complete"]
                    ]
                )


                if total:

                    item["progress"] = int(
                        (done / total) * 100
                    )



        self.save(goals)


        return (
            "Goal updated."
        )



    def list_goals(self):

        goals = self.load()


        if not goals:

            return "No goals yet."


        result = "Goals:\n"


        for goal in goals:

            result += (
                f"- {goal['name']} "
                f"({goal['progress']}%)\n"
            )


        return result
