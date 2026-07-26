"""
Alfred AI
Memory System
Version 2.0
"""

import json
import os
from datetime import datetime


class Memory:


    def __init__(
        self,
        file="database/memory.json"
    ):

        self.file = file

        self.memories = []

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

                    self.memories = json.load(f)

            except:

                self.memories = []

        else:

            self.memories = []



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
                self.memories,
                f,
                indent=4
            )



    # ---------------------------------

    def add(
        self,
        category,
        content
    ):

        memory = {

            "category": category,

            "content": content,

            "time": str(
                datetime.now()
            )

        }


        self.memories.append(
            memory
        )


        self.save()


        return memory



    # ---------------------------------

    def add_user_message(
        self,
        message
    ):

        return self.add(
            "user",
            message
        )



    # ---------------------------------

    def add_assistant_message(
        self,
        message
    ):

        return self.add(
            "alfred",
            message
        )



    # ---------------------------------

    def search(
        self,
        keyword
    ):

        results = []


        for memory in self.memories:

            if keyword.lower() in memory["content"].lower():

                results.append(
                    memory
                )


        return results



    # ---------------------------------

    def recent(
        self,
        amount=10
    ):

        return self.memories[-amount:]



    # ---------------------------------

    def total_memories(
        self
    ):

        return len(
            self.memories
        )



    # ---------------------------------

    def clear(
        self
    ):

        self.memories = []

        self.save()
