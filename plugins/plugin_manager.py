import os
import importlib


PLUGIN_FOLDER = "plugins"


class PluginManager:

    def __init__(self):
        self.plugins = []


    def load_plugins(self):

        for file in os.listdir(PLUGIN_FOLDER):

            if file.endswith(".py") and file != "__init__.py" and file != "plugin_manager.py":

                name = file[:-3]

                module = importlib.import_module(
                    f"{PLUGIN_FOLDER}.{name}"
                )

                self.plugins.append(module)


        return self.plugins


    def list_plugins(self):

        if not self.plugins:
            return "No plugins installed."

        return ", ".join(
            plugin.name for plugin in self.plugins
            if hasattr(plugin, "name")
        )
