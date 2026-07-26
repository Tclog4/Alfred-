from core.planner import Planner
from core.tools import ToolManager
from core.memory import remember, recall


class AlfredBrain:


    def __init__(self):

        self.planner = Planner()

        self.tools = ToolManager()



    def think(self, message):

        message = message.strip()


        # Create a plan

        plan = self.planner.create_plan(
            message
        )


        response = (
            "I have analysed your request.\n\n"
            "Plan:\n"
        )


        for step in plan:

            response += (
                f"- {step}\n"
            )


        response += (
            "\nAvailable tools: "
        )


        response += ", ".join(
            self.tools.available_tools()
        )


        return response
