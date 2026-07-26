class Plugin:


    name = "Unknown Plugin"

    version = "1.0"



    def start(self):

        pass



    def run(self, message):

        return None



    def info(self):

        return {
            "name": self.name,
            "version": self.version
        }
