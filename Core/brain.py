from core.memory import remember, recall, forget
from core.config import get_info
from plugins.plugin_manager import PluginManager


class AlfredBrain:

    def __init__(self):
        self.name = "Alfred"

        # Start plugin system
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()


    def think(self, message):

        message = message.lower().strip()


        # Check plugins first
        for plugin in self.plugin_manager.plugins:

            if hasattr(plugin, "run"):

                response = plugin.run(message)

                if response:
                    return response


        # Alfred identity
        if "who are you" in message or "what are you" in message:

            info = get_info()

            return (
                f"I am {info['name']} "
                f"version {info['version']}."
            )


        # Show Alfred information
        if "system info" in message:

            info = get_info()

            return (
                f"Name: {info['name']}\n"
                f"Version: {info['version']}\n"
                f"Status: {info['status']}\n"
                f"Creator: {info['creator']}"
            )


        # Remember something
        if message.startswith("remember "):

            data = message.replace("remember ", "", 1)

            if " is " in data:

                key, value = data.split(" is ", 1)

                return remember(
                    key.strip(),
                    value.strip()
                )

            return "Tell me what you want me to remember."


        # Recall memory
        if message.startswith("what is "):

            key = message.replace("what is ", "", 1)

            return recall(key.strip())


        # Forget memory
        if message.startswith("forget "):

            key = message.replace("forget ", "", 1)

            return forget(key.strip())


        # List plugins
        if "list plugins" in message:

            return self.plugin_manager.list_plugins()


        # Greetings
        if "hello" in message or "hi" in message:

            return "Hello. How can I assist you?"


        if "good morning" in message:

            return "Good morning. Alfred is ready."


        if "good night" in message:

            return "Good night. Systems standing by."


        # Default response
        return (
            "I am still learning. "
            "This function has not been added yet."
        )
