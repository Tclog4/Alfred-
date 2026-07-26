import json
import os
from datetime import datetime


IMPROVEMENT_FILE = "database/improvements.json"


class SelfImprovement:


    def __init__(self):

        self.setup()



    def setup(self):

        os.makedirs(
            "database",
            exist_ok=True
        )


        if not os.path.exists(
            IMPROVEMENT_FILE
        ):

            with open(
                IMPROVEMENT_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            IMPROVEMENT_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )



    def save(
        self,
        data
    ):

        with open(
            IMPROVEMENT_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def propose(

        self,

        title,

        reason,

        priority="Medium"

    ):

        improvements = self.load()


        improvements.append({

            "title": title,

            "reason": reason,

            "priority": priority,

            "status": "Pending",

            "created": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })


        self.save(
            improvements
        )


        return "Improvement added."



    def approve(
        self,
        index
    ):

        improvements = self.load()


        try:

            improvements[index]["status"] = "Approved"

        except:

            return "Improvement not found."


        self.save(
            improvements
        )


        return "Approved."



    def reject(
        self,
        index
    ):

        improvements = self.load()


        try:

            improvements[index]["status"] = "Rejected"

        except:

            return "Improvement not found."


        self.save(
            improvements
        )


        return "Rejected."



    def list(self):

        improvements = self.load()


        if not improvements:

            return "No improvements."


        result = ""


        for i, item in enumerate(improvements):

            result += (

                f"{i}. "

                f"{item['title']} "

                f"[{item['status']}]\n"

            )


        return result
