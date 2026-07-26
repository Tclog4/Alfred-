class PermissionManager:


    def __init__(self):

        self.pending_action = None



    def request(self, action, data=None):

        self.pending_action = {

            "action": action,

            "data": data

        }


        return (
            "Permission required:\n\n"
            f"Action: {action}\n"
            f"Data: {data}\n\n"
            "Approve? yes/no"
        )



    def approve(self, answer, executor):

        answer = answer.lower().strip()


        if answer == "yes":

            if not self.pending_action:

                return "No pending action."


            action = self.pending_action["action"]

            data = self.pending_action["data"]


            self.pending_action = None


            return executor.execute(
                action,
                data
            )



        if answer == "no":

            self.pending_action = None

            return "Action cancelled."


        return "Please answer yes or no."
