"""
Alfred AI
Self Improvement System
Version 2.0
"""

import json
import os
from datetime import datetime


class Improvement:


    def __init__(
        self,
        title,
        reason,
        priority
    ):

        self.title = title

        self.reason = reason

        self.priority = priority

        self.created = str(
            datetime.now()
        )



    def data(
        self
    ):

        return {

            "title":
            self.title,

            "reason":
            self.reason,

            "priority":
            self.priority,

            "created":
            self.created

        }



class SelfImprovement:


    def __init__(
        self,
        file="database/improvements.json"
    ):

        self.file = file

        self.improvements = []

        self.load()



    # ---------------------------------

    def load(
        self
    ):

        if os.path.exists(
            self.file
        ):

            try:

                with open(
                    self.file,
                    "r"
                ) as f:

                    self.improvements = json.load(f)

            except:

                self.improvements = []



    # ---------------------------------

    def save(
        self
    ):

        folder = os.path.dirname(
            self.file
        )

        if folder:

            os.makedirs(
                folder,
                exist_ok=True
            )


        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                self.improvements,
                f,
                indent=4
            )



    # ---------------------------------

    def propose(
        self,
        title,
        reason,
        priority="Medium"
    ):

        improvement = Improvement(

            title,

            reason,

            priority

        )


        self.improvements.append(

            improvement.data()

        )


        self.save()


        return improvement.data()



    # ---------------------------------

    def list(
        self
    ):

        return self.improvements



    # ---------------------------------

    def find_priority(
        self,
        priority
    ):

        return [

            item

            for item in self.improvements

            if item["priority"] == priority

        ]



    # ---------------------------------

    def clear(
        self
    ):

        self.improvements = []

        self.save()



    # ---------------------------------

    def execute(
        self,
        action,
        parameters=None
    ):

        if action == "propose":

            return self.propose(
                **parameters
            )


        if action == "list":

            return self.list()


        return (
            "Unknown improvement action."
        )
