"""
Alfred AI
Planner
Version 2.0
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Step:

    action: str

    tool: str

    description: str

    requires_permission: bool = False

    parameters: Dict = field(default_factory=dict)


@dataclass
class Plan:

    intent: str

    goal: str

    steps: List[Step] = field(default_factory=list)


class Planner:

    def __init__(self):

        self.templates = {

            "website": self.website_plan,

            "app": self.app_plan,

            "code": self.code_plan,

            "research": self.research_plan,

            "memory": self.memory_plan,

            "conversation": self.chat_plan

        }

    # -----------------------------------------

    def create_plan(
        self,
        reasoning
    ):

        builder = self.templates.get(
            reasoning.intent,
            self.chat_plan
        )

        return builder(reasoning)

    # -----------------------------------------

    def website_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="website",

            goal=reasoning.goal,

            steps=[

                Step(
                    "create_project",
                    "website_builder",
                    "Create website folder",
                    True
                ),

                Step(
                    "create_html",
                    "editor",
                    "Generate index.html",
                    True
                ),

                Step(
                    "create_css",
                    "editor",
                    "Generate style.css",
                    True
                ),

                Step(
                    "create_javascript",
                    "editor",
                    "Generate script.js",
                    True
                ),

                Step(
                    "test_website",
                    "tester",
                    "Run website tests"
                )

            ]

        )

    # -----------------------------------------

    def app_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="app",

            goal=reasoning.goal,

            steps=[

                Step(
                    "create_project",
                    "app_builder",
                    "Create application",
                    True
                ),

                Step(
                    "generate_source",
                    "editor",
                    "Generate source code",
                    True
                ),

                Step(
                    "test_app",
                    "tester",
                    "Run tests"
                )

            ]

        )

    # -----------------------------------------

    def code_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="code",

            goal=reasoning.goal,

            steps=[

                Step(
                    "analyse_code",
                    "scanner",
                    "Analyse project"
                ),

                Step(
                    "edit_code",
                    "editor",
                    "Apply improvements",
                    True
                )

            ]

        )

    # -----------------------------------------

    def research_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="research",

            goal=reasoning.goal,

            steps=[

                Step(
                    "search_web",
                    "browser",
                    "Search the internet"
                ),

                Step(
                    "summarise",
                    "research",
                    "Summarise findings"
                )

            ]

        )

    # -----------------------------------------

    def memory_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="memory",

            goal=reasoning.goal,

            steps=[

                Step(
                    "remember",
                    "memory",
                    "Store memory"
                )

            ]

        )

    # -----------------------------------------

    def chat_plan(
        self,
        reasoning
    ):

        return Plan(

            intent="conversation",

            goal=reasoning.goal,

            steps=[]

        )
