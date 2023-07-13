"""Remote debugger helper."""

from .config import settings


def connect_pydevd() -> None:
    """Connect to PyCharm Python Debug Server.

    Debug Server must be already started.
    """
    try:
        import sys

        sys.path.append(settings.PYCHARM_DEBUGGER_PATH)
        import pydevd_pycharm

        pydevd_pycharm.settrace(
            host=settings.DEBUGGER_HOST,
            port=settings.DEBUGGER_PORT,
            stdoutToServer=True,
            stderrToServer=True,
            suspend=False,
        )
    except Exception as exc:
        print(f"Connection to PyCharm Python Debug Server failed. {exc}")
