import os



class CodeEditor:


    def __init__(self):

        self.last_change = None



    def read(self, path):

        if not os.path.exists(path):

            return "File not found."


        with open(
            path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.read()



    def create(self, path, content=""):

        if os.path.exists(path):

            return "File already exists."


        folder = os.path.dirname(path)


        if folder:

            os.makedirs(
                folder,
                exist_ok=True
            )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)


        self.last_change = path


        return (
            f"Created file: {path}"
        )



    def overwrite(self, path, content):

        if not os.path.exists(path):

            return "File not found."


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)


        self.last_change = path


        return (
            f"Updated file: {path}"
        )



    def append(self, path, content):

        if not os.path.exists(path):

            return "File not found."


        with open(
            path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(content)


        self.last_change = path


        return (
            f"Added content to: {path}"
        )



    def file_exists(self, path):

        return os.path.exists(path)
