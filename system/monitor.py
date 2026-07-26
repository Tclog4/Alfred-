"""
Alfred AI
System Monitor
Version 2.0
"""

import os
import platform
import shutil

try:
    import psutil
except ImportError:
    psutil = None



class SystemMonitor:


    def __init__(self):

        self.system = platform.system()

        self.hostname = platform.node()



    # ---------------------------------

    def cpu_usage(
        self
    ):

        if psutil:

            return psutil.cpu_percent(
                interval=1
            )


        return "Unavailable"



    # ---------------------------------

    def memory_usage(
        self
    ):

        if psutil:

            memory = psutil.virtual_memory()

            return {

                "total":
                self.convert_bytes(
                    memory.total
                ),

                "used":
                self.convert_bytes(
                    memory.used
                ),

                "percent":
                memory.percent

            }


        return "Unavailable"



    # ---------------------------------

    def storage(
        self
    ):

        drive = os.getcwd()

        total, used, free = shutil.disk_usage(
            drive
        )


        return {

            "total":
            self.convert_bytes(
                total
            ),

            "used":
            self.convert_bytes(
                used
            ),

            "free":
            self.convert_bytes(
                free
            )

        }



    # ---------------------------------

    def system_info(
        self
    ):

        return {

            "OS":
            self.system,

            "hostname":
            self.hostname,

            "cpu":
            self.cpu_usage(),

            "memory":
            self.memory_usage(),

            "storage":
            self.storage()

        }



    # ---------------------------------

    def get_summary(
        self
    ):

        info = self.system_info()


        return f"""
Alfred System Report

OS:
{info['OS']}

CPU:
{info['cpu']}%

Memory:
{info['memory']}

Storage:
{info['storage']}
"""



    # ---------------------------------

    def convert_bytes(
        self,
        size
    ):

        units = [

            "B",
            "KB",
            "MB",
            "GB",
            "TB"

        ]


        index = 0


        while size >= 1024 and index < len(units)-1:

            size /= 1024

            index += 1


        return f"{round(size,2)} {units[index]}"



    # ---------------------------------

    def execute(
        self,
        action,
        parameters=None
    ):

        if action == "status":

            return self.get_summary()


        if action == "info":

            return self.system_info()


        return (
            "Unknown monitor action."
        )
