import os



class ErrorDetector:


    def __init__(self):

        self.errors = []



    def check_file(self, path):

        self.errors = []


        if not os.path.exists(path):

            return [
                "File does not exist."
            ]



        try:

            with open(
                path,
                "r",
                errors="ignore"
            ) as file:

                content = file.read()



        except Exception as e:

            return [
                str(e)
            ]



        self.check_empty_file(
            content
        )

        self.check_todo(
            content
        )

        self.check_common_mistakes(
            content
        )


        return self.errors



    def check_empty_file(self, content):

        if not content.strip():

            self.errors.append(
                "File is empty."
            )



    def check_todo(self, content):

        if "TODO" in content:

            self.errors.append(
                "Contains unfinished TODO items."
            )



    def check_common_mistakes(self, content):

        patterns = {

            "print(": "Debug print found.",

            "console.log(": "Console logging found.",

            "pass": "Empty code block found."

        }


        for pattern, message in patterns.items():

            if pattern in content:

                self.errors.append(
                    message
                )



    def scan_project(self, folder="."):

        results = {}


        for root, folders, files in os.walk(folder):

            for file in files:

                path = os.path.join(
                    root,
                    file
                )


                problems = self.check_file(
                    path
                )


                if problems:

                    results[path] = problems



        return results
