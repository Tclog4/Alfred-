"""
Alfred AI
Skill Manager
Version 2.0
"""


class Skill:

    def __init__(
        self,
        name,
        description,
        tools
    ):

        self.name = name

        self.description = description

        self.tools = tools



class SkillManager:


    def __init__(self):

        self.skills = {}



    # ---------------------------------

    def register_skill(
        self,
        name,
        description,
        tools
    ):

        skill = Skill(

            name,

            description,

            tools

        )

        self.skills[name] = skill



    # ---------------------------------

    def get_skill(
        self,
        name
    ):

        return self.skills.get(
            name
        )



    # ---------------------------------

    def remove_skill(
        self,
        name
    ):

        if name in self.skills:

            del self.skills[name]



    # ---------------------------------

    def list_skills(
        self
    ):

        return [

            {

                "name": skill.name,

                "description":
                skill.description,

                "tools":
                skill.tools

            }

            for skill in self.skills.values()

        ]



    # ---------------------------------

    def find_for_tool(
        self,
        tool_name
    ):

        results = []


        for skill in self.skills.values():

            if tool_name in skill.tools:

                results.append(
                    skill.name
                )


        return results
