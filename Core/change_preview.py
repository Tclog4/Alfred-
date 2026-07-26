import difflib



class ChangePreview:


    def __init__(self):

        self.changes = []



    def compare(self, old, new):

        difference = difflib.unified_diff(
            old.splitlines(),
            new.splitlines(),
            fromfile="Before",
            tofile="After",
            lineterm=""
        )


        result = "\n".join(
            difference
        )


        self.changes.append(
            result
        )


        return result



    def latest(self):

        if not self.changes:

            return "No changes available."


        return self.changes[-1]
