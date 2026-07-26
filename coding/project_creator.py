"""
Alfred AI
Project Creator
Version 2.0
"""

import os


class ProjectCreator:


    def __init__(
        self,
        workspace="workspaces"
    ):

        self.workspace = workspace

        os.makedirs(
            workspace,
            exist_ok=True
        )


    # ---------------------------------

    def create_project(
        self,
        name,
        project_type="generic"
    ):

        project_path = os.path.join(
            self.workspace,
            name
        )


        if os.path.exists(
            project_path
        ):

            return (
                f"Project {name} already exists."
            )


        os.makedirs(
            project_path
        )


        structure = self.get_structure(
            project_type
        )


        for item in structure:

            path = os.path.join(
                project_path,
                item
            )


            if "." in item:

                with open(
                    path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        ""
                    )

            else:

                os.makedirs(
                    path
                )


        return {

            "created": True,

            "project": name,

            "location": project_path,

            "files": structure

        }


    # ---------------------------------

    def get_structure(
        self,
        project_type
    ):

        projects = {


            "website":

            [

                "index.html",

                "style.css",

                "script.js",

                "assets",

                "assets/images",

                "assets/icons",

                "README.md"

            ],



            "python":

            [

                "main.py",

                "requirements.txt",

                "README.md"

            ],



            "app":

            [

                "src",

                "assets",

                "README.md"

            ]

        }


        return projects.get(

            project_type,

            [

                "README.md"

            ]

        )



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "create_project":

            return self.create_project(
                **parameters
            )


        return (
            "Unknown project action."
        )
