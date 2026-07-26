class ModelManager:


    def __init__(self):

        self.models = {}

        self.active = None



    def register_model(
        self,
        name,
        description,
        model
    ):

        self.models[name] = {

            "description": description,

            "model": model

        }



    def choose_model(
        self,
        task
    ):

        task = task.lower()


        if "code" in task:

            return self.models.get(
                "coding"
            )


        if (
            "search" in task
            or "research" in task
        ):

            return self.models.get(
                "research"
            )


        return self.models.get(
            "default"
        )



    def list_models(self):

        if not self.models:

            return "No AI models connected."


        result = "AI Models:\n"


        for name, info in self.models.items():

            result += (
                f"- {name}: "
                f"{info['description']}\n"
            )


        return result



    def set_active(
        self,
        name
    ):

        if name in self.models:

            self.active = name

            return (
                f"{name} activated."
            )


        return (
            "Model not found."
        )
