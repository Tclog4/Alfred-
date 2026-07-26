import json
import os
from datetime import datetime


NOTIFICATION_FILE = "database/notifications.json"



class NotificationManager:


    def __init__(self):

        self.setup()



    def setup(self):

        if not os.path.exists("database"):

            os.makedirs("database")


        if not os.path.exists(
            NOTIFICATION_FILE
        ):

            with open(
                NOTIFICATION_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )



    def load(self):

        with open(
            NOTIFICATION_FILE,
            "r"
        ) as file:

            return json.load(file)



    def save(self, data):

        with open(
            NOTIFICATION_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def send(
        self,
        message,
        category="general"
    ):

        notifications = self.load()


        notifications.append({

            "message": message,

            "category": category,

            "time": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "read": False

        })


        self.save(
            notifications
        )


        return (
            "Notification created."
        )



    def get_notifications(self):

        notifications = self.load()


        if not notifications:

            return "No notifications."



        result = "Notifications:\n"


        for item in notifications:

            status = "Unread"


            if item["read"]:

                status = "Read"


            result += (
                f"- [{item['category']}] "
                f"{item['message']} "
                f"({status})\n"
            )


        return result



    def clear(self):

        self.save([])


        return (
            "Notifications cleared."
        )
