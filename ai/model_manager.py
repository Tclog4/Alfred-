"""
Alfred AI
Model Manager
Version 2.0
"""


class Model:


    def __init__(
        self,
        name,
        model_type,
        handler=None
    ):

        self.name = name

        self.model_type = model_type

        self.handler = handler



    # ---------------------------------

    def generate(
        self,
        prompt
    ):

        if self.handler is None:

            return (
                "No AI model connected."
            )


        return self.handler.generate(
            prompt
        )



class ModelManager:


    def __init__(self):

        self.models = {}

        self.active = None


        self.register_default_models()



    # ---------------------------------

    def register_default_models(
        self
    ):

        self.register(

            "default",

            "General Assistant"

        )


        self.register(

            "coding",

            "Programming Assistant"

        )


        self.register(

            "research",

            "Research Assistant"

        )



    # ---------------------------------

    def register(
        self,
        name,
        model_type,
        handler=None
    ):

        model = Model(

            name,

            model_type,

            handler

        )


        self.models[name] = model


        if self.active is None:

            self.active = name



    # ---------------------------------

    def set_active(
        self,
        name
    ):

        if name in self.models:

            self.active = name

            return True


        return False



    # ---------------------------------

    def get_active(
        self
    ):

        return self.models.get(
            self.active
        )



    # ---------------------------------

    def current_model(
        self
    ):

        if self.active:

            return self.active


        return None



    # ---------------------------------

    def ask(
        self,
        prompt
    ):

        model = self.get_active()


        if model is None:

            return (
                "No model selected."
            )


        return model.generate(
            prompt
        )



    # ---------------------------------

    def list_models(
        self
    ):

        return [

            {

                "name": model.name,

                "type": model.model_type

            }

            for model in self.models.values()

        ]
