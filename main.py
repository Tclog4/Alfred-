from core.brain import AlfredBrain
from core.config import ALFRED_NAME


def start():
    print(f"🤖 {ALFRED_NAME} is online.")
    print("Type 'exit' to shut down.\n")

    alfred = AlfredBrain()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("🤖 Alfred shutting down.")
            break

        response = alfred.think(user_input)

        print(f"Alfred: {response}")


if __name__ == "__main__":
    start()
