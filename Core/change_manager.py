class ChangeManager:


    def __init__(self):

        self.pending = None



    def create_change(
        self,
        file,
        old,
        new
    ):

        self.pending = {

            "file": file,

            "old": old,

            "new": new

        }


        return (
            f"Change ready for: {file}"
        )



    def get_pending(self):

        if not self.pending:

            return "No pending changes."


        return self.pending
