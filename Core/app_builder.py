import os


class AppBuilder:


    def __init__(self):

        self.templates = {
            "website": [
                "index.html",
                "style.css",
                "script.js",
                "README.md"
            ],

            "python": [
                "main.py",
                "README.md",
                ".gitignore"
            ],

            "node": [
                "package.json",
                "index.js",
                "README.md"
            ]
        }



    def create_project(
        self,
        project_name,
        template="website"
    ):

        if template not in self.templates:

            return "Unknown template."


        os.makedirs(
            project_name,
            exist_ok=True
        )


        for filename in self.templates[template]:

            path = os.path.join(
                project_name,
                filename
            )


            if os.path.exists(path):

                continue


            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.default_content(
                        filename,
                        project_name
                    )
                )


        return (
            f"{project_name} created successfully."
        )



    def default_content(
        self,
        filename,
        project_name
    ):

        defaults = {

            "index.html":
f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{project_name}</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>{project_name}</h1>

<script src="script.js"></script>

</body>
</html>
""",

            "style.css":
"""body{

font-family:Arial;

margin:40px;

}
""",

            "script.js":
"""console.log("Project Loaded");""",

            "README.md":
f"# {project_name}\nCreated by Alfred AI.",

            "main.py":
"""print("Hello from Alfred")""",

            "package.json":
"""{
    "name":"project",
    "version":"1.0.0"
}""",

            ".gitignore":
"""__pycache__/
.env
"""
        }


        return defaults.get(
            filename,
            ""
        )
