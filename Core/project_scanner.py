import os


class ProjectScanner:


    def scan(self, path="."):

        result = {

            "name": os.path.basename(
                os.path.abspath(path)
            ),

            "files": 0,

            "languages": [],

            "folders": []

        }


        languages = set()


        for root, folders, files in os.walk(path):

            for folder in folders:

                if folder not in result["folders"]:

                    result["folders"].append(
                        folder
                    )


            for file in files:

                result["files"] += 1


                extension = os.path.splitext(
                    file
                )[1]


                if extension:

                    language = self.detect_language(
                        extension
                    )


                    if language:

                        languages.add(
                            language
                        )


        result["languages"] = list(
            languages
        )


        return result



    def detect_language(self, extension):

        languages = {

            ".py": "Python",

            ".js": "JavaScript",

            ".html": "HTML",

            ".css": "CSS",

            ".java": "Java",

            ".cpp": "C++",

            ".cs": "C#",

            ".json": "JSON",

            ".md": "Markdown"

        }


        return languages.get(
            extension
        )
