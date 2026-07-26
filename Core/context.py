import json
import os
from datetime import datetime


CONTEXT_FILE = "database/context.json"



class ContextManager:


    def __init__(self):

        self.create_storage()



    def create_storage(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(CONTEXT_FILE):

            with open(
                CONTEXT_FILE,
                "w"
            ) as file:

                json.dump(
                    {
                        "workspace": None,
                        "file": None,
                        "goal": None,
                        "history": []
                    },
                    file,
                    indent=4
                )



    def load(self):

        with open(
            CONTEXT_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            CONTEXT_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def set_context(
        self,
        workspace=None,
        file=None,
        goal=None
    ):

        data = self.load()


        if workspace:

            data["workspace"] = workspace


        if file:

            data["file"] = file


        if goal:

            data["goal"] = goal



        data["history"].append({

            "time": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "workspace": workspace,

            "file": file,

            "goal": goal

        })


        self.save(data)


        return "Context updated."



    def get_context(self):

        data = self.load()


        return (
            f"Workspace: {data['workspace']}\n"
            f"File: {data['file']}\n"
            f"Goal: {data['goal']}"
        )
