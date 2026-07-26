"""
Alfred AI

Entry Point

Version: 1.0
"""

import traceback

from brain import Alfred


VERSION = "1.0"


def startup():

    print("=" * 50)
    print("        Alfred AI")
    print(f"        Version {VERSION}")
    print("=" * 50)
    print()

    try:

        alfred = Alfred()

        report = alfred.startup_check()

        print("Startup Complete")
        print()

        print(f"Version : {report['version']}")
        print(f"Tools   : {report['tools']}")
        print(f"Skills  : {report['skills']}")
        print(f"Models  : {report['models']}")
        print()

        return alfred

    except Exception:

        print("Alfred failed to start.")
        print()

        traceback.print_exc()

        return None


def shutdown(alfred):

    print()
    print("Saving Alfred...")

    try:

        if hasattr(alfred, "memory"):

            try:
                alfred.memory.save()
            except Exception:
                pass

        if hasattr(alfred, "knowledge"):

            try:
                data = alfred.knowledge.all()

                print(
                    f"Knowledge entries: {len(data)}"
                )

            except Exception:
                pass

        print("Shutdown complete.")

    except Exception:

        traceback.print_exc()


def main():

    alfred = startup()

    if alfred is None:

        return

    try:

        alfred.run()

    except KeyboardInterrupt:

        print()

        print("Interrupted.")

    except Exception:

        print()

        print("Unexpected error:")

        traceback.print_exc()

    finally:

        shutdown(
            alfred
        )


if __name__ == "__main__":

    main()
