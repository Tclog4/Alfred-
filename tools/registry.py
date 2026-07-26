"""
Alfred AI
Tool Registry
Version 2.0
"""


class Tool:

    def __init__(
        self,
        name,
        description,
        handler
    ):

        self.name = name

        self.description = description

        self.handler = handler


    def execute(
        self,
        action,
        parameters=None
    ):

        if parameters is None:

            parameters = {}

        method = getattr(
            self.handler,
            action,
            None
        )


        if method is None:

            return (
                f"Action '{action}' "
                "not supported."
            )


        return method(
            **parameters
        )



class ToolRegistry:


    def __init__(self):

        self.tools = {}



    # ---------------------------------

    def register(
        self,
        name,
        description,
        handler
    ):

        tool = Tool(

            name,

            description,

            handler

        )

        self.tools[name] = tool



    # ---------------------------------

    def get(
        self,
        name
    ):

        return self.tools.get(
            name
        )



    # ---------------------------------

    def remove(
        self,
        name
    ):

        if name in self.tools:

            del self.tools[name]



    # ---------------------------------

    def list_tools(
        self
    ):

        return [

            {

                "name": tool.name,

                "description":
                tool.description

            }

            for tool in self.tools.values()

        ]



    # ---------------------------------

    def has_tool(
        self,
        name
    ):

        return name in self.tools
