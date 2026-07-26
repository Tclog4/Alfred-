"""
Alfred AI
Task Scheduler
Version 2.0
"""

import time
import threading
from datetime import datetime


class Task:


    def __init__(
        self,
        name,
        action,
        interval
    ):

        self.name = name

        self.action = action

        self.interval = interval

        self.last_run = None



class Scheduler:


    def __init__(self):

        self.tasks = {}

        self.running = False



    # ---------------------------------

    def add_task(
        self,
        name,
        action,
        interval
    ):

        task = Task(

            name,

            action,

            interval

        )


        self.tasks[name] = task


        return {

            "created": True,

            "task": name

        }



    # ---------------------------------

    def remove_task(
        self,
        name
    ):

        if name in self.tasks:

            del self.tasks[name]

            return True


        return False



    # ---------------------------------

    def run_task(
        self,
        name
    ):

        task = self.tasks.get(
            name
        )


        if not task:

            return "Task not found."


        try:

            result = task.action()


            task.last_run = str(
                datetime.now()
            )


            return result


        except Exception as error:

            return str(error)



    # ---------------------------------

    def start(
        self
    ):

        if self.running:

            return


        self.running = True


        thread = threading.Thread(

            target=self.loop,

            daemon=True

        )


        thread.start()



    # ---------------------------------

    def stop(
        self
    ):

        self.running = False



    # ---------------------------------

    def loop(
        self
    ):

        while self.running:

            for name, task in self.tasks.items():

                if task.last_run is None:

                    self.run_task(
                        name
                    )


            time.sleep(
                60
            )



    # ---------------------------------

    def list_tasks(
        self
    ):

        return [

            {

                "name":
                task.name,

                "interval":
                task.interval,

                "last_run":
                task.last_run

            }

            for task in self.tasks.values()

        ]



    # ---------------------------------

    def execute(
        self,
        action,
        parameters=None
    ):

        if action == "add":

            return self.add_task(
                **parameters
            )


        if action == "list":

            return self.list_tasks()


        if action == "remove":

            return self.remove_task(
                **parameters
            )


        return (
            "Unknown scheduler action."
        )
