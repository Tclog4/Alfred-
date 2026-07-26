import datetime


class ResearchAgent:


    def __init__(
        self,
        browser,
        knowledge
    ):

        self.browser = browser

        self.knowledge = knowledge



    def research(
        self,
        topic
    ):

        result = self.browser.search(
            topic
        )


        report = {

            "topic": topic,

            "search": result,

            "time": datetime.datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }


        return report



    def save_research(
        self,
        title,
        information
    ):

        return self.knowledge.add(
            title,
            information
        )
