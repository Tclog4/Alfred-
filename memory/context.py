"""
Alfred AI
Context Manager
Version 2.0
"""

from datetime import datetime


class Context:


    def __init__(self):

        self.data = {

            "current_task": None,

            "goal": None,

            "topic": None,

            "active_project": None,

            "last_request": None,

            "started": str(
                datetime.now()
            )

        }



    # ---------------------------------

    def update(
        self,
        request
    ):

        self.data["last_request"] = request

        self.data["current_task"] = request


        return self.data



    # ---------------------------------

    def set_goal(
        self,
        goal
    ):

        self.data["goal"] = goal



    # ---------------------------------

    def set_project(
        self,
        project
    ):

        self.data["active_project"] = project



    # ---------------------------------

    def set_topic(
        self,
        topic
    ):

        self.data["topic"] = topic



    # ---------------------------------

    def get(
        self,
        key
    ):

        return self.data.get(
            key
        )



    # ---------------------------------

    def current(
        self
    ):

        return self.data



    # ---------------------------------

    def clear(
        self
    ):

        self.data = {

            "current_task": None,

            "goal": None,

            "topic": None,

            "active_project": None,

            "last_request": None

        }
