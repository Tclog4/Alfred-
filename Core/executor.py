class ActionExecutor:


    def __init__(self, tools):

        self.tools = tools



    def execute(self, action, data=None):


        if action == "read_file":

            return self.tools.use(
                "read_file",
                data
            )



        if action == "list_files":

            return self.tools.use(
                "list_files"
            )



        if action == "search_files":

            return self.tools.use(
                "search_files",
                data
            )



        return (
            "I don't know how to perform "
            "that action yet."
        )
