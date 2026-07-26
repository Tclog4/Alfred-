class AIEngine:


    def __init__(self):

        self.connected = False



    def ask(self, prompt):

        if not self.connected:

            return (
                "AI model is not connected yet. "
                "Waiting for local AI setup."
            )


        # Future:
        # Send prompt to local model here

        return "AI response"
