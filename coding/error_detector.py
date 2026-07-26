"""
Alfred AI
Error Detector
Version 2.0
"""

import os
import ast


class ErrorDetector:


    def __init__(
        self,
        workspace="workspaces"
    ):

        self.workspace = workspace



    # ---------------------------------

    def scan_project(
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


        errors = []


        for root, dirs, files in os.walk(path):

            for file in files:

                full_path = os.path.join(
                    root,
                    file
                )


                if file.endswith(".py"):

                    result = self.check_python(
                        full_path
                    )


                    if result:

                        errors.append(
                            result
                        )


        return {

            "project": project,

            "errors": errors,

            "count": len(errors)

        }



    # ---------------------------------

    def check_python(
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



            ast.parse(
                code
            )


            return None



        except SyntaxError as error:

            return {

                "file": file,

                "type":
                "Syntax Error",

                "line":
                error.lineno,

                "message":
                error.msg

            }



        except Exception as error:

            return {

                "file": file,

                "type":
                "Error",

                "message":
                str(error)

            }



    # ---------------------------------

    def check_common_issues(
        self,
        code
    ):

        warnings = []


        if "TODO" in code:

            warnings.append(
                "Contains unfinished TODO sections."
            )


        if "print(" in code:

            warnings.append(
                "Debug print statements found."
            )


        if "except:" in code:

            warnings.append(
                "Broad exception handling detected."
            )


        return warnings



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "scan_project":

            return self.scan_project(
                **parameters
            )


        return (
            "Unknown error action."
        )
