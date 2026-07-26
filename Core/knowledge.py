import json
import os
from datetime import datetime


KNOWLEDGE_FILE = "database/knowledge.json"



class KnowledgeBase:


    def __init__(self):

        self.setup()



    def setup(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(KNOWLEDGE_FILE):

            with open(
                KNOWLEDGE_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            KNOWLEDGE_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            KNOWLEDGE_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def add(
        self,
        title,
        information
    ):

        knowledge = self.load()


        knowledge.append({

            "title": title,

            "information": information,

            "created":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })


        self.save(
            knowledge
        )


        return (
            "Knowledge saved."
        )



    def search(
        self,
        keyword
    ):

        knowledge = self.load()


        results = []


        for item in knowledge:

            if (
                keyword.lower()
                in item["title"].lower()
                or
                keyword.lower()
                in item["information"].lower()
            ):

                results.append(item)



        if not results:

            return (
                "No knowledge found."
            )


        output = "Knowledge:\n"


        for item in results:

            output += (
                f"\n{item['title']}\n"
                f"{item['information']}\n"
            )


        return output



    def all(self):

        return self.load()
