from core.files import (
    read_file,
    list_files,
    search_files
)


class ToolManager:


    def __init__(self):

        self.tools = {

            "read_file": read_file,

            "list_files": list_files,

            "search_files": search_files

        }



    def use(self, tool, *args):

        if tool in self.tools:

            return self.tools[tool](*args)


        return "Tool not available."



    def available_tools(self):

        return list(
            self.tools.keys()
        )
