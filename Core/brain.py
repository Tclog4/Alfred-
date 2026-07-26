"""
Alfred AI
brain.py

Main Controller
Version 2.0
"""

from ai.reasoning import Reasoning
from ai.planner import Planner
from ai.executor import Executor
from ai.conversation import Conversation
from ai.model_manager import ModelManager

from memory.memory import Memory
from memory.context import Context


class Alfred:

    def __init__(self):

        print("Starting Alfred...")

        self.reasoning = Reasoning()
        self.planner = Planner()
        self.executor = Executor()

        self.memory = Memory()
        self.context = Context()

        self.conversation = Conversation()
        self.models = ModelManager()

        self.running = True

        print("Alfred Ready.")

    # ------------------------

    def process(self, request):

        self.memory.add_user_message(request)

        self.context.update(request)

        reasoning = self.reasoning.analyse(
            request,
            self.context
        )

        plan = self.planner.create_plan(
            reasoning
        )

        result = self.executor.execute(
            plan
        )

        self.memory.add_assistant_message(
            result
        )

        return result

    # ------------------------

    def chat(self, request):

        return self.process(request)

    # ------------------------

    def status(self):

        return {

            "running": self.running,

            "model": self.models.current_model(),

            "memory": self.memory.total_memories(),

            "context": self.context.current()

        }

    # ------------------------

    def stop(self):

        self.running = False

    # ------------------------

    def run(self):

        print()

        print("===================")
        print(" Alfred AI Ready ")
        print("===================")
        print()

        while self.running:

            try:

                request = input("You > ")

            except KeyboardInterrupt:

                break

            if not request:

                continue

            if request.lower() in [
                "exit",
                "quit"
            ]:

                break

            if request.lower() == "status":

                print(self.status())

                continue

            response = self.chat(request)

            print()

            print("Alfred >")

            print(response)

            print()

        print("Goodbye.")
