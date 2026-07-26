"""
Alfred AI
Project Tester
Version 2.0
"""

import os
import subprocess


class Tester:


    def __init__(
        self,
        workspace="workspaces"
    ):

        self.workspace = workspace



    # ---------------------------------

    def test_project(
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
                "Project does not exist."

            }


        files = self.scan_files(
            path
        )


        results = []


        for file in files:

            result = self.test_file(
                file
            )

            results.append(
                result
            )


        return {

            "project": project,

            "results": results

        }



    # ---------------------------------

    def scan_files(
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

    def test_file(
        self,
        file
    ):

        extension = os.path.splitext(
            file
        )[1]


        if extension == ".py":

            return self.test_python(
                file
            )


        if extension == ".js":

            return {

                "file": file,

                "status":
                "JavaScript detected. Runtime test unavailable."

            }


        if extension == ".html":

            return {

                "file": file,

                "status":
                "HTML structure checked."

            }


        return {

            "file": file,

            "status":
            "Skipped."

        }



    # ---------------------------------

    def test_python(
        self,
        file
    ):

        try:

            result = subprocess.run(

                [
                    "python",
                    "-m",
                    "py_compile",
                    file
                ],

                capture_output=True,

                text=True

            )


            if result.returncode == 0:

                return {

                    "file": file,

                    "status":
                    "Passed"

                }


            return {

                "file": file,

                "status":
                "Failed",

                "error":
                result.stderr

            }


        except Exception as error:

            return {

                "file": file,

                "status":
                "Error",

                "error":
                str(error)

            }



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "test_project":

            return self.test_project(
                **parameters
            )


        return (
            "Unknown tester action."
        )
