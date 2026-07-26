"""
Alfred AI
Knowledge Base
Version 2.0
"""

import json
import os
from datetime import datetime


class KnowledgeBase:


    def __init__(
        self,
        file="database/knowledge.json"
    ):

        self.file = file

        self.entries = []

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
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.entries = json.load(
                        f
                    )

            except:

                self.entries = []

        else:

            self.entries = []



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
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.entries,
                f,
                indent=4
            )



    # ---------------------------------

    def store(
        self,
        topic,
        information
    ):

        entry = {

            "topic": topic,

            "information": information,

            "created":
            str(datetime.now())

        }


        self.entries.append(
            entry
        )


        self.save()


        return entry



    # ---------------------------------

    def search(
        self,
        keyword
    ):

        results = []


        for entry in self.entries:

            if keyword.lower() in (

                entry["topic"].lower()

                +

                entry["information"].lower()

            ):

                results.append(
                    entry
                )


        return results



    # ---------------------------------

    def get_all(
        self
    ):

        return self.entries



    # ---------------------------------

    def delete(
        self,
        topic
    ):

        self.entries = [

            entry

            for entry in self.entries

            if entry["topic"] != topic

        ]


        self.save()


        return True



    # ---------------------------------

    def count(
        self
    ):

        return len(
            self.entries
        )



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "store":

            return self.store(
                **parameters
            )


        if action == "search":

            return self.search(
                **parameters
            )


        return (
            "Unknown knowledge action."
        )
