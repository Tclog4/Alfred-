"""
Alfred AI
Application Builder
Version 2.0
"""


class AppBuilder:


    def __init__(
        self,
        project_creator,
        editor
    ):

        self.project_creator = project_creator

        self.editor = editor



    # ---------------------------------

    def create_app(
        self,
        name,
        app_type="python"
    ):

        project = self.project_creator.create_project(
            name,
            "app"
        )


        if project.get("created") is False:

            return project



        files = {}


        if app_type == "python":

            files = {

                "main.py":
                self.python_template(),

                "requirements.txt":
                "",

                "README.md":
                f"# {name}\n\nCreated by Alfred AI."

            }


        elif app_type == "web":

            files = {

                "src/app.js":
                self.javascript_template(),

                "README.md":
                f"# {name}\n\nCreated by Alfred AI."

            }



        for file, content in files.items():

            self.editor.update_file(

                f"{name}/{file}",

                content

            )


        return {

            "success": True,

            "project": name,

            "type": app_type,

            "files": list(files.keys())

        }



    # ---------------------------------

    def python_template(
        self
    ):

        return """

def main():

    print(
        "Application running."
    )


if __name__ == "__main__":

    main()

"""



    # ---------------------------------

    def javascript_template(
        self
    ):

        return """

console.log(
    "Application started."
);

"""



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "create_app":

            return self.create_app(
                **parameters
            )


        return (
            "Unknown app action."
        )
