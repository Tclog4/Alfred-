"""
Alfred AI
Reasoning Engine
Version 2.0
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ReasoningResult:

    intent: str

    confidence: float

    tools: List[str] = field(default_factory=list)

    goal: str = ""

    requires_permission: bool = False


class Reasoning:

    def __init__(self):

        self.tool_map = {

            "website": [
                "website_builder",
                "editor"
            ],

            "app": [
                "app_builder",
                "editor"
            ],

            "code": [
                "editor",
                "scanner"
            ],

            "research": [
                "browser",
                "research"
            ],

            "memory": [
                "memory"
            ],

            "system": [
                "monitor"
            ]

        }

    # ---------------------------------

    def analyse(
        self,
        request,
        context
    ):

        text = request.lower()

        intent = self.detect_intent(
            text
        )

        tools = self.choose_tools(
            intent
        )

        permission = self.requires_permission(
            intent
        )

        return ReasoningResult(

            intent=intent,

            confidence=0.80,

            tools=tools,

            goal=request,

            requires_permission=permission

        )

    # ---------------------------------

    def detect_intent(
        self,
        text
    ):

        if any(
            word in text
            for word in [
                "website",
                "web"
            ]
        ):
            return "website"

        if any(
            word in text
            for word in [
                "app",
                "application"
            ]
        ):
            return "app"

        if any(
            word in text
            for word in [
                "python",
                "code",
                "script",
                "program"
            ]
        ):
            return "code"

        if any(
            word in text
            for word in [
                "search",
                "research",
                "internet"
            ]
        ):
            return "research"

        if any(
            word in text
            for word in [
                "remember",
                "memory"
            ]
        ):
            return "memory"

        return "conversation"

    # ---------------------------------

    def choose_tools(
        self,
        intent
    ):

        return self.tool_map.get(
            intent,
            []
        )

    # ---------------------------------

    def requires_permission(
        self,
        intent
    ):

        dangerous = {

            "code",

            "website",

            "app"

        }

        return intent in dangerous
