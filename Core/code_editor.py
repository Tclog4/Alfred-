import os
import shutil
from datetime import datetime


BACKUP_FOLDER = "database/code_backups"



def create_backup(path):

    if not os.path.exists(path):
        return


    if not os.path.exists(BACKUP_FOLDER):

        os.makedirs(BACKUP_FOLDER)


    filename = os.path.basename(path)

    time = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    backup_path = (
        f"{BACKUP_FOLDER}/"
        f"{filename}_{time}.bak"
    )


    shutil.copy(
        path,
        backup_path
    )


    return backup_path



def read_code(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    except Exception as e:

        return f"Error: {e}"



def replace_code(path, old, new):

    try:

        create_backup(path)


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()



        if old not in content:

            return "Could not find the code to replace."



        content = content.replace(
            old,
            new
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)



        return "Code updated successfully. Backup created."


    except Exception as e:

        return f"Error: {e}"



def append_code(path, code):

    try:

        create_backup(path)


        with open(
            path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write("\n" + code)



        return "Code added successfully. Backup created."


    except Exception as e:

        return f"Error: {e}"



def file_info(path):

    if not os.path.exists(path):

        return "File does not exist."


    size = os.path.getsize(path)


    return (
        f"File: {path}\n"
        f"Size: {size} bytes"
    )
