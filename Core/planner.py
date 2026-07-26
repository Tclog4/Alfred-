class Planner:


    def create_plan(self, goal):

        goal = goal.lower()


        plan = []


        if "website" in goal:

            plan.append(
                "Analyse website files"
            )

            plan.append(
                "Check design and structure"
            )

            plan.append(
                "Suggest improvements"
            )


        elif "code" in goal:

            plan.append(
                "Inspect code"
            )

            plan.append(
                "Find possible improvements"
            )

            plan.append(
                "Create changes"
            )


        else:

            plan.append(
                "Understand user goal"
            )

            plan.append(
                "Find required tools"
            )


        return plan
