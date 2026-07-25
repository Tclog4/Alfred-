import json
import os


PROJECT_FILE = "database/projects.json"



def create_file():

    if not os.path.exists(PROJECT_FILE):

        with open(PROJECT_FILE, "w") as file:

            json.dump([], file, indent=4)



def load_projects():

    create_file()

    with open(PROJECT_FILE, "r") as file:

        return json.load(file)



def save_projects(projects):

    with open(PROJECT_FILE, "w") as file:

        json.dump(projects, file, indent=4)



def add_project(name, status="Idea"):

    projects = load_projects()

    project = {
        "name": name,
        "status": status
    }

    projects.append(project)

    save_projects(projects)

    return f"Added project: {name}"



def get_projects():

    projects = load_projects()


    if not projects:

        return "No projects yet."


    result = "Projects:\n"


    for project in projects:

        result += (
            f"• {project['name']} "
            f"- {project['status']}\n"
        )


    return result
