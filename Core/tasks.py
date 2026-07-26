import json
import os


TASK_FILE = "database/tasks.json"



def create_file():

    if not os.path.exists(TASK_FILE):

        with open(TASK_FILE, "w") as file:

            json.dump([], file, indent=4)



def load_tasks():

    create_file()

    with open(TASK_FILE, "r") as file:

        return json.load(file)



def save_tasks(tasks):

    with open(TASK_FILE, "w") as file:

        json.dump(tasks, file, indent=4)



def add_task(task):

    tasks = load_tasks()

    tasks.append({
        "task": task,
        "status": "Pending"
    })


    save_tasks(tasks)


    return f"Task added: {task}"



def get_tasks():

    tasks = load_tasks()


    if not tasks:

        return "No tasks."



    result = "Tasks:\n"


    for number, item in enumerate(tasks, 1):

        result += (
            f"{number}. "
            f"{item['task']} "
            f"- {item['status']}\n"
        )


    return result



def complete_task(number):

    tasks = load_tasks()


    try:

        tasks[number - 1]["status"] = "Completed"

        save_tasks(tasks)

        return "Task completed."

    except:

        return "Task not found."
