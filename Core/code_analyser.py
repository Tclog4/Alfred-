import os



class CodeAnalyser:


    def __init__(self):

        self.supported = {

            ".py": "Python",

            ".js": "JavaScript",

            ".html": "HTML",

            ".css": "CSS",

            ".json": "JSON",

            ".java": "Java",

            ".cpp": "C++",

            ".cs": "C#"

        }



    def analyse_file(self, path):


        if not os.path.exists(path):

            return "File not found."


        extension = os.path.splitext(
            path
        )[1]


        language = self.supported.get(
            extension,
            "Unknown"
        )


        with open(
            path,
            "r",
            errors="ignore"
        ) as file:

            content = file.read()



        return {

            "file": path,

            "language": language,

            "lines": len(
                content.splitlines()
            ),

            "characters": len(content),

            "empty_lines": content.count(
                "\n\n"
            )

        }



    def find_code_files(self, folder="."):

        files = []


        for root, folders, names in os.walk(folder):

            for name in names:

                extension = os.path.splitext(
                    name
                )[1]


                if extension in self.supported:

                    files.append(
                        os.path.join(
                            root,
                            name
                        )
                    )


        return files
