"""
Alfred AI
Main Brain

Version: 1.0
"""

import os
import json
from datetime import datetime

# ==========================
# Core Modules
# ==========================

from core.memory import Memory
from core.planner import Planner
from core.learning import Learning
from core.workspace import WorkspaceManager
from core.context import ContextManager
from core.goals import GoalManager

from core.notifications import NotificationManager
from core.scheduler import Scheduler

from core.code_editor import CodeEditor
from core.error_detector import ErrorDetector
from core.project_scanner import ProjectScanner
from core.file_intelligence import FileIntelligence

from core.app_builder import AppBuilder

from core.web_browser import WebBrowser
from core.research_agent import ResearchAgent

from core.system_monitor import SystemMonitor

from core.tool_registry import ToolRegistry
from core.skill_manager import SkillManager
from core.model_manager import ModelManager

from core.self_improvement import SelfImprovement

from core.agent_loop import AgentLoop
from core.decision_engine import DecisionEngine

from core.knowledge import KnowledgeBase

# ==========================
# Alfred Brain
# ==========================


class Alfred:

    def __init__(self):

        print("\nStarting Alfred...\n")

        self.version = "1.0"

        self.started = datetime.now()

        # ----------------------
        # Intelligence
        # ----------------------

        self.memory = Memory()

        self.learning = Learning()

        self.planner = Planner()

        self.knowledge = KnowledgeBase()

        self.context = ContextManager()

        self.goals = GoalManager()

        # ----------------------
        # Project Management
        # ----------------------

        self.workspace = WorkspaceManager()

        self.files = FileIntelligence()

        self.scanner = ProjectScanner()

        # ----------------------
        # Coding
        # ----------------------

        self.editor = CodeEditor()

        self.errors = ErrorDetector()

        self.builder = AppBuilder()

        # ----------------------
        # Internet
        # ----------------------

        self.web = WebBrowser()

        self.research = ResearchAgent(
            self.web,
            self.knowledge
        )

        # ----------------------
        # System
        # ----------------------

        self.monitor = SystemMonitor()

        self.notifications = NotificationManager()

        self.scheduler = Scheduler()

        # ----------------------
        # AI Systems
        # ----------------------

        self.decision = DecisionEngine()

        self.models = ModelManager()

        self.skills = SkillManager()

        self.registry = ToolRegistry()

        self.improvements = SelfImprovement()

        self.agent = AgentLoop(
            self.planner,
            self.memory,
            self.decision
        )

        # ----------------------
        # Register Everything
        # ----------------------

        self.register_tools()

        self.register_skills()

        self.register_models()

        print("Alfred Ready.\n")

    # =====================================================
    # TOOL REGISTRATION
    # =====================================================

    def register_tools(self):

        self.registry.register(
            "code_editor",
            "Create and edit files",
            self.editor
        )

        self.registry.register(
            "project_scanner",
            "Scan projects",
            self.scanner
        )

        self.registry.register(
            "error_detector",
            "Find coding problems",
            self.errors
        )

        self.registry.register(
            "website_builder",
            "Create websites",
            self.builder
        )

        self.registry.register(
            "web_browser",
            "Internet access",
            self.web
        )

        self.registry.register(
            "research",
            "Research information",
            self.research
        )

        self.registry.register(
            "memory",
            "Store memories",
            self.memory
        )

        self.registry.register(
            "knowledge",
            "Knowledge base",
            self.knowledge
        )

        self.registry.register(
            "workspace",
            "Manage projects",
            self.workspace
        )

        self.registry.register(
            "monitor",
            "System monitoring",
            self.monitor
        )

    # =====================================================
    # SKILLS
    # =====================================================

    def register_skills(self):

        self.skills.register_skill(

            "coding",

            "Programming assistant",

            [
                "code_editor",
                "project_scanner",
                "error_detector"
            ]

        )

        self.skills.register_skill(

            "website",

            "Website builder",

            [
                "website_builder",
                "code_editor",
                "research"
            ]

        )

        self.skills.register_skill(

            "research",

            "Internet research",

            [
                "web_browser",
                "research",
                "knowledge"
            ]

        )

        self.skills.register_skill(

            "system",

            "Computer management",

            [
                "monitor"
            ]

        )

    # =====================================================
    # AI MODELS
    # =====================================================

    def register_models(self):

        self.models.register_model(

            "default",

            "Default AI",

            None

        )

        self.models.register_model(

            "coding",

            "Coding AI",

            None

        )

        self.models.register_model(

            "research",

            "Research AI",

            None

# =====================================================
# REQUEST PROCESSING
# =====================================================

    def process(self, request):

        request = str(request).strip()

        if not request:
            return "Please enter a request."

        print(f"\nUser: {request}")

        # ----------------------
        # Update Context
        # ----------------------

        self.context.set_context(
            goal=request
        )

        # ----------------------
        # Store Conversation
        # ----------------------

        try:
            self.memory.add(
                "user",
                request
            )
        except:
            pass

        # ----------------------
        # Observe
        # ----------------------

        observation = self.agent.observe(
            request
        )

        # ----------------------
        # Think
        # ----------------------

        thought = self.agent.think(
            observation
        )

        # ----------------------
        # Plan
        # ----------------------

        plan = self.agent.plan(
            thought
        )

        # ----------------------
        # Decide Action
        # ----------------------

        response = self.route_request(
            request,
            thought,
            plan
        )

        # ----------------------
        # Save Response
        # ----------------------

        try:
            self.memory.add(
                "alfred",
                response
            )
        except:
            pass

        return response


# =====================================================
# MAIN ROUTER
# =====================================================

    def route_request(
        self,
        request,
        thought,
        plan
    ):

        request_lower = request.lower()

        # ------------------
        # Website Creation
        # ------------------

        if "website" in request_lower:

            return self.handle_website(
                request
            )

        # ------------------
        # App Creation
        # ------------------

        if "app" in request_lower:

            return self.handle_app(
                request
            )

        # ------------------
        # Coding
        # ------------------

        if (
            "python" in request_lower
            or
            "code" in request_lower
            or
            "program" in request_lower
        ):

            return self.handle_code(
                request
            )

        # ------------------
        # Project Scan
        # ------------------

        if (
            "scan" in request_lower
            or
            "project" in request_lower
        ):

            return self.handle_scan()

        # ------------------
        # Errors
        # ------------------

        if "error" in request_lower:

            return self.handle_errors()

        # ------------------
        # Internet
        # ------------------

        if (
            "search" in request_lower
            or
            "research" in request_lower
        ):

            return self.handle_research(
                request
            )

        # ------------------
        # Goals
        # ------------------

        if "goal" in request_lower:

            return self.goals.list_goals()

        # ------------------
        # Workspaces
        # ------------------

        if "workspace" in request_lower:

            return self.workspace.list_workspaces()

        # ------------------
        # Notifications
        # ------------------

        if "notification" in request_lower:

            return self.notifications.get_notifications()

        # ------------------
        # System
        # ------------------

        if (
            "system" in request_lower
            or
            "computer" in request_lower
            or
            "status" in request_lower
        ):

            return self.monitor.get_summary()

        # ------------------
        # Knowledge
        # ------------------

        if "knowledge" in request_lower:

            keyword = request.replace(
                "knowledge",
                ""
            ).strip()

            return self.knowledge.search(
                keyword
            )

        # ------------------
        # Fallback
        # ------------------

        return self.general_ai(
            request,
            thought,
            plan
        )


# =====================================================
# GENERAL AI
# =====================================================

    def general_ai(
        self,
        request,
        thought,
        plan
    ):

        return f"""
Request:
{request}

Goal:
{thought['goal']}

Suggested Tools:
{", ".join(thought['tools'])}

Plan:
{plan}

No dedicated action exists yet.

This request should be passed to the connected AI model.
"""


# =====================================================
# WEBSITE HANDLER
# =====================================================

    def handle_website(
        self,
        request
    ):

        return (
            "Website request detected.\n"
            "Website Builder skill selected."
        )


# =====================================================
# APP HANDLER
# =====================================================

    def handle_app(
        self,
        request
    ):

        return (
            "Application request detected.\n"
            "App Builder skill selected."
        )


# =====================================================
# CODE HANDLER
# =====================================================

    def handle_code(
        self,
        request
    ):

        return (
            "Coding request detected.\n"
            "Coding skill selected."
        )


# =====================================================
# PROJECT SCAN
# =====================================================

    def handle_scan(self):

        return self.scanner.scan_project(".")


# =====================================================
# ERROR SCAN
# =====================================================

    def handle_errors(self):

        return self.errors.scan_project(".")


# =====================================================
# RESEARCH
# =====================================================

    def handle_research(
        self,
        request
    ):

        return self.research.research(
            request
       # =====================================================
# WEBSITE CREATION
# =====================================================

    def create_website(
        self,
        project_name
    ):

        print(
            f"Creating website: {project_name}"
        )

        result = self.builder.create_project(
            project_name,
            "website"
        )

        self.notifications.send(
            f"Website '{project_name}' created.",
            "builder"
        )

        return result


# =====================================================
# APPLICATION CREATION
# =====================================================

    def create_app(
        self,
        project_name,
        template="python"
    ):

        print(
            f"Creating app: {project_name}"
        )

        result = self.builder.create_project(
            project_name,
            template
        )

        self.notifications.send(
            f"Application '{project_name}' created.",
            "builder"
        )

        return result


# =====================================================
# FILE READING
# =====================================================

    def read_file(
        self,
        path
    ):

        return self.editor.read(path)


# =====================================================
# FILE CREATION
# =====================================================

    def create_file(
        self,
        path,
        content=""
    ):

        return self.editor.create(
            path,
            content
        )


# =====================================================
# FILE UPDATE
# =====================================================

    def update_file(
        self,
        path,
        content
    ):

        return self.editor.overwrite(
            path,
            content
        )


# =====================================================
# APPEND FILE
# =====================================================

    def append_file(
        self,
        path,
        content
    ):

        return self.editor.append(
            path,
            content
        )


# =====================================================
# PROJECT ANALYSIS
# =====================================================

    def analyse_project(
        self,
        folder="."
    ):

        report = {}

        report["scan"] = self.scanner.scan_project(
            folder
        )

        report["errors"] = self.errors.scan_project(
            folder
        )

        report["files"] = self.files.scan(
            folder
        )

        return report


# =====================================================
# BACKUP BEFORE EDIT
# =====================================================

    def backup_before_edit(
        self,
        path
    ):

        if hasattr(
            self,
            "backup"
        ):

            return self.backup.create_backup(
                path
            )

        return "Backup system unavailable."


# =====================================================
# CHANGE PREVIEW
# =====================================================

    def preview_change(
        self,
        old_content,
        new_content
    ):

        if hasattr(
            self,
            "preview"
        ):

            return self.preview.compare(
                old_content,
                new_content
            )

        return "Preview unavailable."


# =====================================================
# SAFE EDIT
# =====================================================

    def safe_edit(
        self,
        file,
        new_content
    ):

        old = self.read_file(file)

        preview = self.preview_change(
            old,
            new_content
        )

        return {

            "status": "awaiting approval",

            "file": file,

            "preview": preview,

            "new_content": new_content

        }


# =====================================================
# APPLY APPROVED CHANGE
# =====================================================

    def apply_change(
        self,
        file,
        content
    ):

        self.backup_before_edit(
            file
        )

        result = self.update_file(
            file,
            content
        )

        self.notifications.send(

            f"{file} updated.",

            "editor"

        )

        return result


# =====================================================
# SELF IMPROVEMENT
# =====================================================

    def analyse_self(self):

        self.improvements.propose(

            "Improve code generation",

            "Generated projects could be cleaner.",

            "High"

        )

        self.improvements.propose(

            "Improve planning",

            "Large projects should be split better.",

            "Medium"

        )

        self.improvements.propose(

            "Improve learning",

            "Remember more successful edits.",

            "Medium"

        )

        return self.improvements.list()


# =====================================================
# KNOWLEDGE
# =====================================================

    def remember_solution(

        self,

        title,

        information

    ):

        return self.knowledge.add(

            title,

            information

        )


# =====================================================
# RESEARCH + SAVE
# =====================================================

    def research_and_save(

        self,

        topic

    ):

        report = self.research.research(

            topic

        )

        self.knowledge.add(

            topic,

            str(report)

        )

        return report


# =====================================================
# GOAL CREATION
# =====================================================

    def create_goal(

        self,

        name

    ):

        return self.goals.create_goal(

            name

        )


# =====================================================
# WORKSPACE
# =====================================================

    def open_workspace(

        self,

        name

    ):

        return self.workspace.open_workspace(

            name

        )


# =====================================================
# SYSTEM REPORT
# =====================================================

    def system_report(self):

        return self.monitor.get_summary()

# =====================================================
# AI MODEL
# =====================================================

    def connect_model(
        self,
        model
    ):

        self.ai_model = model

        print("AI model connected.")

        return True


# =====================================================
# AI RESPONSE
# =====================================================

    def ask_ai(
        self,
        prompt
    ):

        if not hasattr(
            self,
            "ai_model"
        ):

            return (
                "No AI model connected."
            )


        try:

            return self.ai_model.generate(
                prompt
            )


        except Exception as error:

            return (
                f"AI Error: {error}"
            )


# =====================================================
# STARTUP CHECK
# =====================================================

    def startup_check(self):

        report = {}

        report["version"] = self.version

        report["started"] = str(
            self.started
        )

        report["tools"] = len(
            self.registry.tools
        )

        report["skills"] = len(
            self.skills.skills
        )

        report["models"] = len(
            self.models.models
        )

        return report


# =====================================================
# HEALTH REPORT
# =====================================================

    def health(self):

        return {

            "memory": True,

            "planner": True,

            "workspace": True,

            "editor": True,

            "internet": True,

            "monitor": True,

            "agent": True

        }


# =====================================================
# STATUS
# =====================================================

    def status(self):

        return {

            "version": self.version,

            "running": True,

            "started": str(
                self.started
            ),

            "workspace":

            self.context.get_context()

        }


# =====================================================
# HELP
# =====================================================

    def help(self):

        return """

Alfred Commands

status

health

scan project

search

research

create website

create app

goal

workspace

knowledge

system

"""


# =====================================================
# MAIN LOOP
# =====================================================

    def run(self):

        print()

        print("======================")

        print(" Alfred AI Ready ")

        print("======================")

        print()

        while True:

            try:

                request = input(
                    "You > "
                )

            except KeyboardInterrupt:

                print()

                print("Stopping Alfred...")

                break


            if not request:

                continue


            command = request.lower()


            if command == "exit":

                break


            if command == "quit":

                break


            if command == "status":

                print(

                    self.status()

                )

                continue


            if command == "health":

                print(

                    self.health()

                )

                continue


            if command == "help":

                print(

                    self.help()

                )

                continue


            response = self.process(

                request

            )

            print()

            print("Alfred >")

            print(response)

            print()

        print()

        print("Goodbye.")
