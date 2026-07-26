import os
import platform


class SystemMonitor:


    def __init__(self):

        self.system = platform.system()



    def get_system_info(self):

        return {

            "system": self.system,

            "machine": platform.machine(),

            "processor": platform.processor()

        }



    def get_storage(self, path="."):

        try:

            usage = os.statvfs(path)

            total = (
                usage.f_frsize *
                usage.f_blocks
            )

            free = (
                usage.f_frsize *
                usage.f_bfree
            )

            used = total - free


            return {

                "total": total,

                "used": used,

                "free": free

            }


        except:

            return (
                "Storage unavailable."
            )



    def get_summary(self):

        info = self.get_system_info()


        return (
            f"System: {info['system']}\n"
            f"Machine: {info['machine']}\n"
            f"CPU: {info['processor']}"
        )
