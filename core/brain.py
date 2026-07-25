from core.memory import remember, recall, forget
from core.config import get_info


class AlfredBrain:

    def __init__(self):
        self.name = "Alfred"


    def think(self, message):

        message = message.lower()


        # Alfred information
        if "who are you" in message or "what are you" in message:
            info = get_info()

            return (
                f"I am {info['name']} "
                f"version {info['version']}."
            )


        # Remember command
        if message.startswith("remember "):

            data = message.replace("remember ", "")

            if " is " in data:
                key, value = data.split(" is ", 1)

                return remember(
                    key.strip(),
                    value.strip()
                )


        # Recall command
        if message.startswith("what is "):

            key = message.replace("what is ", "")

            return recall(key.strip())


        # Forget command
        if message.startswith("forget "):

            key = message.replace("forget ", "")

            return forget(key.strip())


        # Basic responses
        if "hello" in message or "hi" in message:
            return "Hello. How can I assist you?"


        return (
            "I am still learning. "
            "This feature has not been added yet."
        )
