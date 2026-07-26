from core.ai import AIEngine
from core.planner import Planner
from core.tools import ToolManager
from core.permissions import PermissionManager
from core.executor import ActionExecutor

from core.memory import remember, recall
from core.projects import add_project, get_projects
from core.ideas import add_idea, get_ideas
from core.tasks import add_task, get_tasks, complete_task

from plugins.plugin_manager import PluginManager


class AlfredBrain:


    def __init__(self):

        self.name = "Alfred"


        # AI engine
        self.ai = AIEngine()


        # Agent systems
        self.planner = Planner()

        self.tools = ToolManager()

        self.executor = ActionExecutor(
            self.tools
        )

        self.permissions = PermissionManager()


        # Plugins
        self.plugin_manager = PluginManager()

        self.plugin_manager.load_plugins()



    def think(self, message):

        message = message.strip()

        lower = message.lower()



        # =========================
        # PERMISSION RESPONSES
        # =========================

        if lower.startswith("allow "):

            answer = lower.replace(
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

                response = plugin.run(lower)

                if response:

                    return response



        # =========================
        # MEMORY
        # =========================

        if lower.startswith("remember "):

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



        if lower.startswith("what is "):

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

        if lower.startswith("add project "):

            project = message.replace(
                "add project ",
                "",
                1
            )

            return add_project(project)



        if lower == "projects":

            return get_projects()



        # =========================
        # IDEAS
        # =========================

        if lower.startswith("save idea "):

            idea = message.replace(
                "save idea ",
                "",
                1
            )

            return add_idea(idea)



        if lower == "ideas":

            return get_ideas()



        # =========================
        # TASKS
        # =========================

        if lower.startswith("add task "):

            task = message.replace(
                "add task ",
                "",
                1
            )

            return add_task(task)



        if lower == "tasks":

            return get_tasks()



        if lower.startswith("complete task "):

            number = lower.replace(
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
        # ACTION REQUESTS
        # =========================

        if "read file" in lower:

            path = message.replace(
                "read file ",
                "",
                1
            )


            return self.permissions.request(
                f"Read file: {path}"
            )



        if "edit file" in lower:

            return self.permissions.request(
                "Edit requested file"
            )



        # =========================
        # PLANNING
        # =========================

        if (
            "plan" in lower
            or "help me" in lower
        ):

            plan = self.planner.create_plan(
                message
            )


            output = "Plan created:\n"


            for item in plan:

                output += (
                    f"- {item}\n"
                )


            return output



        # =========================
        # AI MODEL
        # =========================

        response = self.ai.ask(
            message
        )


        if self.ai.connected:

            return response



        # =========================
        # BASIC
        # =========================

        if lower in ["hi", "hello"]:

            return (
                "Hello. Alfred is online."
            )



        if "who are you" in lower:

            return (
                "I am Alfred, "
                "your personal AI assistant."
            )



        return (
            "I am ready. "
            "My AI model is waiting "
            "to be connected."
        )
