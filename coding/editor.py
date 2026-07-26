"""
Alfred AI
Code Editor Tool
Version 2.0
"""

import os
import shutil
from datetime import datetime


class Editor:


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

    def create_file(
        self,
        path,
        content=""
    ):

        full_path = self.get_path(
            path
        )

        folder = os.path.dirname(
            full_path
        )

        if folder:

            os.makedirs(
                folder,
                exist_ok=True
            )


        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                content
            )


        return (
            f"Created file: {path}"
        )


    # ---------------------------------

    def read_file(
        self,
        path
    ):

        full_path = self.get_path(
            path
        )


        if not os.path.exists(
            full_path
        ):

            return (
                "File does not exist."
            )


        with open(
            full_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()



    # ---------------------------------

    def update_file(
        self,
        path,
        content
    ):

        backup = self.backup(
            path
        )


        full_path = self.get_path(
            path
        )


        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                content
            )


        return {

            "updated": path,

            "backup": backup

        }



    # ---------------------------------

    def append_file(
        self,
        path,
        content
    ):

        full_path = self.get_path(
            path
        )


        with open(
            full_path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                content
            )


        return (
            f"Added content to {path}"
        )



    # ---------------------------------

    def delete_file(
        self,
        path
    ):

        full_path = self.get_path(
            path
        )


        if os.path.exists(
            full_path
        ):

            os.remove(
                full_path
            )

            return (
                f"Deleted {path}"
            )


        return (
            "File not found."
        )



    # ---------------------------------

    def backup(
        self,
        path
    ):

        source = self.get_path(
            path
        )


        if not os.path.exists(
            source
        ):

            return None


        backup_path = (
            source
            +
            ".backup."
            +
            datetime.now()
            .strftime("%Y%m%d%H%M%S")
        )


        shutil.copy(
            source,
            backup_path
        )


        return backup_path



    # ---------------------------------

    def get_path(
        self,
        path
    ):

        return os.path.join(
            self.workspace,
            path
        )



    # ---------------------------------

    def list_files(
        self
    ):

        files = []


        for root, dirs, filenames in os.walk(
            self.workspace
        ):

            for filename in filenames:

                files.append(
                    os.path.join(
                        root,
                        filename
                    )
                )


        return files



    # ---------------------------------

    # Executor compatibility

    def execute(
        self,
        action,
        parameters
    ):

        actions = {

            "create_file":
            self.create_file,

            "read_file":
            self.read_file,

            "update_file":
            self.update_file,

            "append_file":
            self.append_file

        }


        function = actions.get(
            action
        )


        if function:

            return function(
                **parameters
            )


        return (
            f"Unknown editor action: {action}"
        )
