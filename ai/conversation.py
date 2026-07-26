"""
Alfred AI
Conversation Manager
Version 2.0
"""


from datetime import datetime


class Conversation:


    def __init__(self):

        self.messages = []



    # ---------------------------------

    def add_message(
        self,
        role,
        content
    ):

        message = {

            "role": role,

            "content": content,

            "time": str(
                datetime.now()
            )

        }


        self.messages.append(
            message
        )


        return message



    # ---------------------------------

    def add_user(
        self,
        message
    ):

        return self.add_message(

            "user",

            message

        )



    # ---------------------------------

    def add_alfred(
        self,
        message
    ):

        return self.add_message(

            "alfred",

            message

        )



    # ---------------------------------

    def history(
        self
    ):

        return self.messages



    # ---------------------------------

    def recent(
        self,
        amount=10
    ):

        return self.messages[-amount:]



    # ---------------------------------

    def clear(
        self
    ):

        self.messages = []



    # ---------------------------------

    def build_prompt(
        self,
        user_message
    ):

        prompt = """

You are Alfred, an AI assistant.

Conversation:

"""


        for message in self.recent():

            prompt += (

                message["role"]
                +
                ": "
                +
                message["content"]
                +
                "\n"

            )


        prompt += (

            "\nUser: "
            +
            user_message

        )


        return prompt
