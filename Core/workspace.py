import json
import os
from datetime import datetime


WORKSPACE_FILE = "database/workspaces.json"



class WorkspaceManager:


    def __init__(self):

        self.create_storage()



    def create_storage(self):

        folder = "database"


        if not os.path.exists(folder):

            os.makedirs(folder)


        if not os.path.exists(WORKSPACE_FILE):

            with open(
                WORKSPACE_FILE,
                "w"
            ) as file:

                json.dump(
                    {},
                    file,
                    indent=4
                )



    def load(self):

        with open(
            WORKSPACE_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            WORKSPACE_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def create_workspace(
        self,
        name,
        path
    ):

        data = self.load()


        data[name] = {

            "path": path,

            "created": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "notes": [],

            "active": False

        }


        self.save(data)


        return (
            f"Workspace created: {name}"
        )



    def open_workspace(self, name):

        data = self.load()


        if name not in data:

            return (
                "Workspace not found."
            )


        for item in data:

            data[item]["active"] = False



        data[name]["active"] = True


        self.save(data)


        return (
            f"Opened workspace: {name}"
        )



    def list_workspaces(self):

        data = self.load()


        if not data:

            return "No workspaces."



        result = "Workspaces:\n"


        for name, info in data.items():

            status = ""

            if info["active"]:

                status = " (Active)"


            result += (
                f"- {name}{status}\n"
            )


        return result
