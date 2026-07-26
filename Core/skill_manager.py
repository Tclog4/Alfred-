class SkillManager:


    def __init__(self):

        self.skills = {}



    def register_skill(
        self,
        name,
        description,
        tools
    ):

        self.skills[name] = {

            "description": description,

            "tools": tools

        }



    def get_skill(
        self,
        name
    ):

        return self.skills.get(
            name
        )



    def list_skills(self):

        if not self.skills:

            return "No skills installed."


        result = "Alfred Skills:\n"


        for name, skill in self.skills.items():

            result += (
                f"- {name}: "
                f"{skill['description']}\n"
            )


        return result



    def find_skill(
        self,
        keyword
    ):

        matches = []


        for name in self.skills:

            if keyword.lower() in name.lower():

                matches.append(name)


        return matches
