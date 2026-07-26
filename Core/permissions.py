class PermissionManager:


    def __init__(self):

        self.pending_action = None



    def request(self, action):

        self.pending_action = action

        return (
            "Permission required:\n"
            f"{action}\n\n"
            "Approve? (yes/no)"
        )



    def approve(self, answer):

        answer = answer.lower().strip()


        if answer == "yes":

            action = self.pending_action

            self.pending_action = None

            return (
                "Approved.\n"
                f"Executing: {action}"
            )


        if answer == "no":

            self.pending_action = None

            return "Action cancelled."


        return "Please answer yes or no."
