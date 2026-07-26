class ToolRegistry:


    def __init__(self):

        self.tools = {}



    def register(
        self,
        name,
        description,
        tool
    ):

        self.tools[name] = {

            "description": description,

            "tool": tool

        }



    def get_tool(
        self,
        name
    ):

        if name in self.tools:

            return self.tools[name]["tool"]


        return None



    def list_tools(self):

        if not self.tools:

            return "No tools available."


        result = "Alfred Tools:\n"


        for name, info in self.tools.items():

            result += (
                f"- {name}: "
                f"{info['description']}\n"
            )


        return result



    def has_tool(
        self,
        name
    ):

        return name in self.tools
