"""
Alfred AI
Code Analyser
Version 2.0
"""

import os
import ast


class CodeAnalyser:


    def __init__(
        self,
        workspace="workspaces"
    ):

        self.workspace = workspace



    # ---------------------------------

    def analyse_project(
        self,
        project
    ):

        path = os.path.join(
            self.workspace,
            project
        )


        if not os.path.exists(path):

            return {

                "success": False,

                "error":
                "Project not found."

            }


        files = self.get_files(
            path
        )


        report = []


        for file in files:

            report.append(
                self.analyse_file(file)
            )


        return {

            "project": project,

            "files": report

        }



    # ---------------------------------

    def get_files(
        self,
        folder
    ):

        files = []


        for root, dirs, names in os.walk(
            folder
        ):

            for name in names:

                files.append(
                    os.path.join(
                        root,
                        name
                    )
                )


        return files



    # ---------------------------------

    def analyse_file(
        self,
        file
    ):

        extension = os.path.splitext(
            file
        )[1]


        if extension == ".py":

            return self.analyse_python(
                file
            )


        return {

            "file": file,

            "type": extension,

            "status":
            "Basic scan complete."

        }



    # ---------------------------------

    def analyse_python(
        self,
        file
    ):

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                code = f.read()



            tree = ast.parse(
                code
            )


            functions = []

            classes = []


            for node in ast.walk(tree):

                if isinstance(
                    node,
                    ast.FunctionDef
                ):

                    functions.append(
                        node.name
                    )


                if isinstance(
                    node,
                    ast.ClassDef
                ):

                    classes.append(
                        node.name
                    )



            return {

                "file": file,

                "language":
                "Python",

                "functions":
                functions,

                "classes":
                classes,

                "status":
                "Analysed"

            }



        except Exception as error:

            return {

                "file": file,

                "status":
                "Failed",

                "error":
                str(error)

            }



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "analyse_project":

            return self.analyse_project(
                **parameters
            )


        return (
            "Unknown analyser action."
        )
