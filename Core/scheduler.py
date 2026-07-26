import json
import os
from datetime import datetime


SCHEDULE_FILE = "database/schedules.json"



class Scheduler:


    def __init__(self):

        self.setup()



    def setup(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(SCHEDULE_FILE):

            with open(
                SCHEDULE_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            SCHEDULE_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            SCHEDULE_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def create_schedule(
        self,
        task,
        time
    ):

        schedules = self.load()


        schedules.append({

            "task": task,

            "time": time,

            "completed": False,

            "created": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })


        self.save(
            schedules
        )


        return (
            f"Scheduled: {task}"
        )



    def list_schedules(self):

        schedules = self.load()


        if not schedules:

            return "No schedules."



        result = "Schedules:\n"


        for item in schedules:

            result += (
                f"- {item['task']} "
                f"at {item['time']}\n"
            )


        return result



    def remove_schedule(
        self,
        number
    ):

        schedules = self.load()


        try:

            schedules.pop(number)


        except:

            return "Schedule not found."


        self.save(
            schedules
        )


        return "Schedule removed."
