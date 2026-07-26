import os
import shutil
from datetime import datetime



class BackupManager:


    def __init__(self):

        self.backup_folder = "backups"


        if not os.path.exists(
            self.backup_folder
        ):

            os.makedirs(
                self.backup_folder
            )



    def create_backup(self, file_path):


        if not os.path.exists(file_path):

            return "File does not exist."


        filename = os.path.basename(
            file_path
        )


        time = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )


        backup_name = (
            f"{filename}_{time}"
        )


        destination = os.path.join(
            self.backup_folder,
            backup_name
        )


        shutil.copy2(
            file_path,
            destination
        )


        return (
            f"Backup created: {destination}"
        )



    def list_backups(self):


        files = os.listdir(
            self.backup_folder
        )


        if not files:

            return "No backups found."


        result = "Backups:\n"


        for file in files:

            result += (
                f"- {file}\n"
            )


        return result
