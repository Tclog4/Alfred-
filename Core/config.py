# Alfred Configuration

ALFRED_NAME = "Alfred"
ALFRED_VERSION = "0.1.0"
ALFRED_STATUS = "Online"

CREATOR = "Founder"

SETTINGS = {
    "theme": "dark",
    "memory": True,
    "voice": False,
    "plugins": True
}


def get_info():
    return {
        "name": ALFRED_NAME,
        "version": ALFRED_VERSION,
        "status": ALFRED_STATUS,
        "creator": CREATOR
    }
