"""
Alfred AI
Tool Executor
Version 2.0
"""


class Executor:


    def __init__(
        self
    ):

        self.tools = {}



    # ---------------------------------

    def register(
        self,
        name,
        tool
    ):

        self.tools[name] = tool


        return True



    # ---------------------------------

    def execute(
        self,
        tool_name,
        action,
        parameters=None
    ):

        tool = self.tools.get(
            tool_name
        )


        if tool is None:

            return {

                "success": False,

                "error":
                f"Tool {tool_name} not found."

            }



        try:

            result = tool.execute(

                action,

                parameters or {}

            )


            return {

                "success": True,

                "tool":
                tool_name,

                "result":
                result

            }



        except Exception as error:

            return {

                "success": False,

                "tool":
                tool_name,

                "error":
                str(error)

            }



    # ---------------------------------

    def list_tools(
        self
    ):

        return list(
            self.tools.keys()
        )
