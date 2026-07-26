"""
Alfred AI
Web Browser Tool
Version 2.0
"""

import requests


class WebBrowser:


    def __init__(self):

        self.enabled = False

        self.history = []



    # ---------------------------------

    def enable(
        self
    ):

        self.enabled = True

        return "Internet enabled."



    # ---------------------------------

    def disable(
        self
    ):

        self.enabled = False

        return "Internet disabled."



    # ---------------------------------

    def open(
        self,
        url
    ):

        if not self.enabled:

            return {

                "success": False,

                "error":
                "Internet access disabled."

            }


        try:

            response = requests.get(
                url,
                timeout=10
            )


            self.history.append(
                url
            )


            return {

                "success": True,

                "status":
                response.status_code,

                "content":
                response.text[:1000]

            }


        except Exception as error:

            return {

                "success": False,

                "error":
                str(error)

            }



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

        if action == "open":

            return self.open(
                **parameters
            )


        if action == "enable":

            return self.enable()


        if action == "disable":

            return self.disable()


        return (
            "Unknown browser action."
        )
