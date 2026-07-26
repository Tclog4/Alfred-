"""
Alfred AI
Version Manager
Version 2.0
"""

import os
import shutil
from datetime import datetime


class GitManager:


    def __init__(
        self,
        project_folder=".",
        backup_folder="backups"
    ):

        self.project_folder = project_folder

        self.backup_folder = backup_folder

        os.makedirs(
            backup_folder,
            exist_ok=True
        )


    # ---------------------------------

    def create_backup(
        self
    ):

        name = (
            "backup_"
            +
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )


        destination = os.path.join(
            self.backup_folder,
            name
        )


        shutil.copytree(

            self.project_folder,

            destination,

            dirs_exist_ok=True

        )


        return {

            "success": True,

            "backup": destination

        }



    # ---------------------------------

    def list_backups(
        self
    ):

        return os.listdir(
            self.backup_folder
        )



    # ---------------------------------

    def restore_backup(
        self,
        backup_name
    ):

        source = os.path.join(

            self.backup_folder,

            backup_name

        )


        if not os.path.exists(
            source
        ):

            return "Backup not found."


        shutil.copytree(

            source,

            self.project_folder,

            dirs_exist_ok=True

        )


        return {

            "restored": True,

            "backup": backup_name

        }



    # ---------------------------------

    def create_checkpoint(
        self,
        message
    ):

        return {

            "checkpoint": message,

            "time":
            str(datetime.now())

        }



    # ---------------------------------

    def execute(
        self,
        action,
        parameters=None
    ):


        if action == "backup":

            return self.create_backup()


        if action == "list":

            return self.list_backups()


        if action == "restore":

            return self.restore_backup(
                **parameters
            )


        return (
            "Unknown version action."
        )
