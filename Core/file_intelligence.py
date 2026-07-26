import os
import json
from datetime import datetime


INDEX_FILE = "database/file_index.json"



class FileIntelligence:


    def __init__(self):

        self.setup()



    def setup(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(INDEX_FILE):

            with open(
                INDEX_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            INDEX_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            INDEX_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def scan(self, folder="."):

        files = []


        for root, folders, names in os.walk(folder):

            for name in names:

                path = os.path.join(
                    root,
                    name
                )


                files.append({

                    "name": name,

                    "path": path,

                    "extension":
                    os.path.splitext(name)[1],

                    "modified":
                    datetime.fromtimestamp(
                        os.path.getmtime(path)
                    ).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                })


        self.save(files)


        return (
            f"Indexed {len(files)} files."
        )



    def search(self, keyword):

        files = self.load()


        results = []


        for file in files:

            if keyword.lower() in file["name"].lower():

                results.append(file)



        if not results:

            return "No files found."



        output = "Matches:\n"


        for file in results:

            output += (
                f"- {file['path']}\n"
            )


        return output
