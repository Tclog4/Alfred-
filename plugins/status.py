name = "Status Plugin"


def run(command):

    if "status" in command.lower():
        return "All systems are running."

    return None
