from core.memory import remember, recall
from core.config import get_info
from core.projects import add_project, get_projects
from core.ideas import add_idea, get_ideas
from core.tasks import add_task, get_tasks, complete_task
from core.files import (
    read_file,
    create_file,
    list_files,
    search_files
)
from plugins.plugin_manager import PluginManager


class AlfredBrain:


    def __init__(self):

        self.name = "Alfred"

        # Plugin system
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()



    def think(self, message):

        message = message.lower().strip()



        # =========================
        # PLUGINS
        # =========================

        for plugin in self.plugin_manager.plugins:

            if hasattr(plugin, "run"):

                response = plugin.run(message)

                if response:
                    return response



        # =========================
        # IDENTITY
        # =========================

        if (
            "who are you" in message
            or "what are you" in message
        ):

            info = get_info()

            return (
                f"I am {info['name']} "
                f"version {info['version']}."
            )



        if "system info" in message:

            info = get_info()

            return (
                f"Name: {info['name']}\n"
                f"Version: {info['version']}\n"
                f"Creator: {info['creator']}\n"
                f"Status: {info['status']}"
            )



        # =========================
        # MEMORY
        # =========================

        if message.startswith("remember "):

            data = message.replace(
                "remember ",
                "",
                1
            )


            if " is " in data:

                key, value = data.split(
                    " is ",
                    1
                )


                return remember(
                    key.strip(),
                    value.strip()
                )


            return "Tell me what you want me to remember."



        if message.startswith("what is "):

            key = message.replace(
                "what is ",
                "",
                1
            )

            return recall(
                key.strip()
            )



        # =========================
        # PROJECT MANAGER
        # =========================

        if message.startswith("add project "):

            project = message.replace(
                "add project ",
                "",
                1
            )

            return add_project(project)



        if (
            message == "projects"
            or "show projects" in message
        ):

            return get_projects()



        # =========================
        # IDEA VAULT
        # =========================

        if message.startswith("save idea "):

            idea = message.replace(
                "save idea ",
                "",
                1
            )

            return add_idea(idea)



        if (
            message == "ideas"
            or "show ideas" in message
        ):

            return get_ideas()



        # =========================
        # TASK MANAGER
        # =========================

        if message.startswith("add task "):

            task = message.replace(
                "add task ",
                "",
                1
            )

            return add_task(task)



        if (
            message == "tasks"
            or "show tasks" in message
        ):

            return get_tasks()



        if message.startswith("complete task "):

            number = message.replace(
                "complete task ",
                "",
                1
            )

            try:

                return complete_task(
                    int(number)
                )

            except:

                return "Please enter a valid task number."



        # =========================
        # FILE SYSTEM
        # =========================

        if message == "list files":

            return list_files()



        if message.startswith("read file "):

            path = message.replace(
                "read file ",
                "",
                1
            )

            return read_file(path)



        if message.startswith("create file "):

            path = message.replace(
                "create file ",
                "",
                1
            )

            return create_file(path)



        if message.startswith("search file "):

            name = message.replace(
                "search file ",
                "",
                1
            )

            return search_files(name)



        # =========================
        # PLUGINS
        # =========================

        if "list plugins" in message:

            return self.plugin_manager.list_plugins()



        # =========================
        # BASIC CHAT
        # =========================

        if (
            "hello" in message
            or "hi" in message
        ):

            return (
                "Hello. Alfred is online "
                "and ready."
            )



        if "how are you" in message:

            return (
                "All systems are operating normally."
            )



        if "thank you" in message:

            return "You're welcome."



        # =========================
        # UNKNOWN COMMAND
        # =========================

        return (
            "I am still learning. "
            "This command has not been added yet."
        )
