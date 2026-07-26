class DecisionEngine:


    def __init__(self):

        self.tools = {}



    def register_tool(
        self,
        name,
        tool
    ):

        self.tools[name] = tool



    def choose_action(
        self,
        request
    ):

        request = request.lower()


        if "code" in request or "website" in request:

            return [
                "project_scanner",
                "code_analyser",
                "error_detector"
            ]



        if (
            "search" in request
            or "find" in request
        ):

            return [
                "web_browser",
                "research_agent"
            ]



        if (
            "remember" in request
            or "learn" in request
        ):

            return [
                "memory",
                "knowledge_base"
            ]



        return [
            "ai_reasoning"
        ]
