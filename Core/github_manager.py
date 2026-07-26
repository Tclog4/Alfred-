import os



class GitHubManager:


    def __init__(self):

        self.connected = False



    def connect(self):

        self.connected = True

        return "GitHub connected."



    def scan_repository(self, path="."):

        if not os.path.exists(path):

            return "Repository not found."


        files = []


        for root, folders, filenames in os.walk(path):

            for file in filenames:

                files.append(
                    os.path.join(
                        root,
                        file
                    )
                )


        return {
            "files": len(files),
            "repository": path
        }



    def get_status(self):

        if self.connected:

            return (
                "GitHub connection active."
            )


        return (
            "GitHub is not connected yet."
        )
