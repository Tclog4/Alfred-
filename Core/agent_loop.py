from datetime import datetime



class AgentLoop:


    def __init__(
        self,
        planner,
        memory,
        decision
    ):

        self.planner = planner

        self.memory = memory

        self.decision = decision



    def observe(
        self,
        request
    ):

        return {

            "request": request,

            "time":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }



    def think(
        self,
        observation
    ):

        tools = self.decision.choose_action(
            observation["request"]
        )


        return {

            "goal":
            observation["request"],

            "tools":
            tools

        }



    def plan(
        self,
        thought
    ):

        return self.planner.create_plan(
            thought["goal"]
        )



    def learn(
        self,
        result
    ):

        return (
            "Result stored for learning."
        )



    def run(
        self,
        request
    ):

        observation = self.observe(
            request
        )


        thought = self.think(
            observation
        )


        plan = self.plan(
            thought
        )


        return {

            "observation": observation,

            "thought": thought,

            "plan": plan

        }
