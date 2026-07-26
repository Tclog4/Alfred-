"""
Alfred AI
Executor
Version 2.0
"""

from dataclasses import asdict


class Executor:

    def __init__(self):

        self.tools = {}

        self.history = []


    # ---------------------------------

    def register_tool(
        self,
        name,
        tool
    ):

        self.tools[name] = tool


    # ---------------------------------

    def execute(
        self,
        plan
    ):

        results = []

        for step in plan.steps:

            result = self.execute_step(
                step
            )

            results.append(result)

            self.history.append({

                "action": step.action,

                "tool": step.tool,

                "result": result

            })


        return self.format_results(
            results
        )


    # ---------------------------------

    def execute_step(
        self,
        step
    ):

        tool = self.tools.get(
            step.tool
        )


        if tool is None:

            return {

                "success": False,

                "error":
                f"Tool '{step.tool}' not found."

            }


        if step.requires_permission:

            approved = self.request_permission(
                step
            )

            if not approved:

                return {

                    "success": False,

                    "error":
                    "Permission denied."

                }


        try:

            result = tool.execute(
                step.action,
                step.parameters
            )


            return {

                "success": True,

                "action": step.action,

                "result": result

            }


        except Exception as error:

            return {

                "success": False,

                "error": str(error)

            }


    # ---------------------------------

    def request_permission(
        self,
        step
    ):

        print()

        print(
            "Alfred wants permission:"
        )

        print(
            step.description
        )

        answer = input(
            "Allow? (y/n): "
        )


        return answer.lower() == "y"


    # ---------------------------------

    def format_results(
        self,
        results
    ):

        output = []

        for result in results:

            if result["success"]:

                output.append(
                    str(result["result"])
                )

            else:

                output.append(
                    "Error: "
                    +
                    result["error"]
                )


        return "\n".join(
            output
        )


    # ---------------------------------

    def get_history(
        self
    ):

        return self.history
