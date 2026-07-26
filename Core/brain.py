from core.ai import AIEngine
from core.planner import Planner
from core.tools import ToolManager
from core.permissions import PermissionManager

from core.memory import remember, recall
from core.projects import add_project, get_projects
from core.ideas import add_idea, get_ideas
from core.tasks import add_task, get_tasks, complete_task

from plugins.plugin_manager import PluginManager



class AlfredBrain:


    def __init__(self):

        self.name = "Alfred"


        # AI system (connect later)
        self.ai = AIEngine()


        # Agent systems
        self.planner = Planner()
        self.tools = ToolManager()
        self.permissions = PermissionManager()


        # Plugins
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()



    def think(self, message):

        message = message.strip()



        # =========================
        # CHECK PERMISSIONS
        # =========================

        if message.lower().startswith("allow "):

            answer = message.replace(
                "allow ",
                "",
                1
            )

            return self.permissions.approve(answer)



        # =========================
        # PLUGINS
        # =========================

        for plugin in self.plugin_manager.plugins:

            if hasattr(plugin, "run"):

                result = plugin.run(message.lower())

                if result:

                    return result



        # =========================
        # MEMORY
        # =========================

        if message.lower().startswith("remember "):

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



        if message.lower().startswith("what is "):

            key = message.replace(
                "what is ",
                "",
                1
            )

            return recall(
                key.strip()
            )



        # =========================
        # PROJECTS
        # =========================

        if message.lower().startswith("add project "):

            project = message.replace(
                "add project ",
                "",
                1
            )

            return add_project(project)



        if message.lower() == "projects":

            return get_projects()



        # =========================
        # IDEAS
        # =========================

        if message.lower().startswith("save idea "):

            idea = message.replace(
                "save idea ",
                "",
                1
            )

            return add_idea(idea)



        if message.lower() == "ideas":

            return get_ideas()



        # =========================
        # TASKS
        # =========================

        if message.lower().startswith("add task "):

            task = message.replace(
                "add task ",
                "",
                1
            )

            return add_task(task)



        if message.lower() == "tasks":

            return get_tasks()



        if message.lower().startswith("complete task "):

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

                return "Invalid task number."



        # =========================
        # REQUEST ACTIONS
        # =========================

        if (
            "edit file" in message.lower()
            or "change file" in message.lower()
        ):

            return self.permissions.request(
                "Modify requested file"
            )



        # =========================
        # PLANNING
        # =========================

        if (
            "plan" in message.lower()
            or "help me" in message.lower()
        ):

            plan = self.planner.create_plan(
                message
            )


            response = "I created a plan:\n"


            for step in plan:

                response += (
                    f"- {step}\n"
                )


            return response



        # =========================
        # AI MODEL
        # =========================

        ai_response = self.ai.ask(
            message
        )


        if self.ai.connected:

            return ai_response



        # =========================
        # BASIC RESPONSES
        # =========================

        if message.lower() in [
            "hello",
            "hi"
        ]:

            return (
                "Hello. Alfred is online."
            )



        if "who are you" in message.lower():

            return (
                "I am Alfred, "
                "your personal AI assistant."
            )



        return (
            "I am ready, but my AI model "
            "is not connected yet."
        )
