import os
import importlib



class PluginManager:


    def __init__(self):

        self.plugins = []



    def load_plugins(self):

        folder = "plugins"


        if not os.path.exists(folder):

            return


        for file in os.listdir(folder):

            if (
                file.endswith(".py")
                and file != "plugin_manager.py"
                and file != "plugin_base.py"
            ):

                name = file[:-3]


                try:

                    module = importlib.import_module(
                        f"plugins.{name}"
                    )


                    for item in dir(module):

                        obj = getattr(
                            module,
                            item
                        )


                        if isinstance(
                            obj,
                            type
                        ):

                            plugin = obj()


                            if hasattr(
                                plugin,
                                "run"
                            ):

                                self.plugins.append(
                                    plugin
                                )


                except Exception as e:

                    print(
                        "Plugin error:",
                        e
                    )



    def list_plugins(self):

        if not self.plugins:

            return "No plugins installed."


        result = "Installed Plugins:\n"


        for plugin in self.plugins:

            result += (
                f"- {plugin.name} "
                f"v{plugin.version}\n"
            )


        return result
