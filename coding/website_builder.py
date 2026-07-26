"""
Alfred AI
Website Builder
Version 2.0
"""

import os


class WebsiteBuilder:


    def __init__(
        self,
        project_creator,
        editor
    ):

        self.project_creator = project_creator

        self.editor = editor



    # ---------------------------------

    def create_website(
        self,
        name
    ):

        project = self.project_creator.create_project(
            name,
            "website"
        )


        if project.get("created") is False:

            return project



        files = {

            "index.html": self.html_template(name),

            "style.css": self.css_template(),

            "script.js": self.js_template(),

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

            "files": list(files.keys())

        }



    # ---------------------------------

    def html_template(
        self,
        name
    ):

        return f"""
<!DOCTYPE html>

<html>

<head>

<title>{name}</title>

<link rel="stylesheet" href="style.css">

</head>


<body>


<h1>
{name}
</h1>


<p>
Website created by Alfred AI.
</p>


<script src="script.js"></script>

</body>

</html>
"""



    # ---------------------------------

    def css_template(
        self
    ):

        return """

body {

    font-family: Arial, sans-serif;

    text-align: center;

    margin-top: 50px;

}


h1 {

    font-size: 40px;

}

"""



    # ---------------------------------

    def js_template(
        self
    ):

        return """

console.log(
    "Website running!"
);

"""



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "create_website":

            return self.create_website(
                **parameters
            )


        return (
            "Unknown website action."
        )
