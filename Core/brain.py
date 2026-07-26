from core.ai import AIEngine
from core.planner import Planner
from core.tools import ToolManager
from core.executor import ActionExecutor
from core.permissions import PermissionManager

from core.memory import (
    remember,
    recall,
    remember_event,
    get_history
)

from core.projects import (
    add_project,
    get_projects
)

from core.ideas import (
    add_idea,
    get_ideas
)

from core.tasks import (
    add_task,
    get_tasks,
    complete_task
)

from core.learning import (
    record_problem,
    record_improvement,
    get_learning
)

from plugins.plugin_manager import PluginManager



class AlfredBrain:


    def __init__(self):

        self.name = "Alfred"


        # AI system
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
        # APPROVAL SYSTEM
        # =========================

        if lower.startswith("allow "):

            answer = lower.replace(
                "allow ",
                "",
                1
            )


            result = self.permissions.approve(
                answer,
                self.executor
            )


            remember_event(
                f"Permission response: {answer}"
            )


            return result



        # =========================
        # PLUGINS
        # =========================

        for plugin in self.plugin_manager.plugins:

            if hasattr(plugin, "run"):

                response = plugin.run(
                    lower
                )


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


                result = remember(
                    key.strip(),
                    value.strip()
                )


                remember_event(
                    f"Remembered {key.strip()}"
                )


                return result



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
        # HISTORY
        # =========================

        if lower.startswith(
            "remember event "
        ):

            event = message.replace(
                "remember event ",
                "",
                1
            )


            return remember_event(
                event
            )



        if lower == "history":

            return get_history()



        # =========================
        # PROJECTS
        # =========================

        if lower.startswith(
            "add project "
        ):

            project = message.replace(
                "add project ",
                "",
                1
            )


            remember_event(
                f"Created project: {project}"
            )


            return add_project(
                project
            )



        if lower == "projects":

            return get_projects()



        # =========================
        # IDEAS
        # =========================

        if lower.startswith(
            "save idea "
        ):

            idea = message.replace(
                "save idea ",
                "",
                1
            )


            remember_event(
                f"Saved idea: {idea}"
            )


            return add_idea(
                idea
            )



        if lower == "ideas":

            return get_ideas()



        # =========================
        # TASKS
        # =========================

        if lower.startswith(
            "add task "
        ):

            task = message.replace(
                "add task ",
                "",
                1
            )


            remember_event(
                f"Added task: {task}"
            )


            return add_task(
                task
            )



        if lower == "tasks":

            return get_tasks()



        if lower.startswith(
            "complete task "
        ):

            number = lower.replace(
                "complete task ",
                "",
                1
            )


            try:

                result = complete_task(
                    int(number)
                )


                remember_event(
                    f"Completed task {number}"
                )


                return result


            except:

                return (
                    "Invalid task number."
                )



        # =========================
        # SELF IMPROVEMENT
        # =========================

        if lower.startswith(
            "report problem "
        ):

            problem = message.replace(
                "report problem ",
                "",
                1
            )


            return record_problem(
                problem
            )



        if lower.startswith(
            "suggest improvement "
        ):

            idea = message.replace(
                "suggest improvement ",
                "",
                1
            )


            return record_improvement(
                idea
            )



        if lower == "learning":

            return get_learning()



        # =========================
        # ACTION REQUESTS
        # =========================

        if lower.startswith(
            "read file "
        ):

            path = message.replace(
                "read file ",
                "",
                1
            )


            return self.permissions.request(
                "read_file",
                path
            )



        if lower.startswith(
            "search file "
        ):

            name = message.replace(
                "search file ",
                "",
                1
            )


            return self.permissions.request(
                "search_files",
                name
            )



        if "edit file" in lower:

            return self.permissions.request(
                "edit_file",
                message
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


            output = (
                "Plan created:\n"
            )


            for step in plan:

                output += (
                    f"- {step}\n"
                )


            remember_event(
                "Created a plan"
            )


            return output



        # =========================
        # AI MODEL
        # =========================

        response = self.ai.ask(
            message
        )


        if self.ai.connected:

            remember_event(
                "Used AI model"
            )

            return response



        # =========================
        # BASIC RESPONSES
        # =========================

        if lower in [
            "hi",
            "hello"
        ]:

            return (
                "Hello. Alfred is online."
            )



        if "who are you" in lower:

            return (
                "I am Alfred, "
                "your personal AI assistant."
            )



        return (
            "I understand the request, "
            "but my AI model is not connected yet."
        )
