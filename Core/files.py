import os
import shutil
from datetime import datetime


BACKUP_FOLDER = "database/backups"



def create_backup_folder():

    if not os.path.exists(BACKUP_FOLDER):

        os.makedirs(BACKUP_FOLDER)



def read_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    except Exception as e:

        return f"Error: {e}"



def write_file(path, content):

    try:

        create_backup(path)

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)


        return "File updated successfully."


    except Exception as e:

        return f"Error: {e}"



def create_file(path, content=""):

    try:

        if os.path.exists(path):

            return "File already exists."


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)


        return "File created."


    except Exception as e:

        return f"Error: {e}"



def create_backup(path):

    if not os.path.exists(path):

        return


    create_backup_folder()


    filename = os.path.basename(path)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    backup = (
        f"{BACKUP_FOLDER}/"
        f"{filename}_{timestamp}.bak"
    )


    shutil.copy(
        path,
        backup
    )



def list_files(path="."):

    try:

        files = os.listdir(path)

        result = "Files:\n"

        for file in files:

            result += f"- {file}\n"


        return result


    except Exception as e:

        return f"Error: {e}"



def search_files(name, start_path="."):

    matches = []


    for root, folders, files in os.walk(start_path):

        for file in files:

            if name.lower() in file.lower():

                matches.append(
                    os.path.join(root,file)
                )


    if not matches:

        return "No files found."


    return "\n".join(matches)
