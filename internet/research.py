"""
Alfred AI
Research Agent
Version 2.0
"""


from datetime import datetime


class ResearchAgent:


    def __init__(
        self,
        browser=None,
        knowledge=None
    ):

        self.browser = browser

        self.knowledge = knowledge

        self.history = []



    # ---------------------------------

    def research(
        self,
        topic
    ):

        if self.browser is None:

            return {

                "success": False,

                "error":
                "Browser unavailable."

            }


        result = self.browser.open(
            topic
        )


        report = {

            "topic": topic,

            "source": result,

            "time":
            str(datetime.now())

        }


        self.history.append(
            report
        )


        if self.knowledge:

            self.knowledge.store(

                topic,

                str(report)

            )


        return report



    # ---------------------------------

    def summarise(
        self,
        information
    ):

        text = str(
            information
        )


        if len(text) > 500:

            return (
                text[:500]
                +
                "..."
            )


        return text



    # ---------------------------------

    def get_history(
        self
    ):

        return self.history



    # ---------------------------------

    def execute(
        self,
        action,
        parameters
    ):

        if action == "research":

            return self.research(
                **parameters
            )


        if action == "summarise":

            return self.summarise(
                **parameters
            )


        return (
            "Unknown research action."
        )
