from core.memory import remember, recall
from core.config import get_info
from core.projects import add_project, get_projects
from core.ideas import add_idea, get_ideas
from plugins.plugin_manager import PluginManager


class AlfredBrain:


    def __init__(self):

        self.name = "Alfred"

        # Load plugins
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
        # ALFRED IDENTITY
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
        # MEMORY SYSTEM
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

            return add_project(
                project
            )



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

            return add_idea(
                idea
            )



        if (
            message == "ideas"
            or "show ideas" in message
        ):

            return get_ideas()



        # =========================
        # PLUGIN COMMANDS
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

            return (
                "You're welcome."
            )



        # =========================
        # UNKNOWN COMMAND
        # =========================

        return (
            "I am still learning. "
            "This command has not been added yet."
        )
