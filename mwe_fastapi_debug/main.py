"""API server."""
import uvicorn
from fastapi import FastAPI

from .config import settings
from .debug import connect_pydevd

if settings.PYCHARM_DEBUGGER:
    connect_pydevd()

app = FastAPI(
    title="API Service.",
)


@app.get("/")
async def root() -> str:
    """Endpoint."""
    return "Hello debugger!"


def main() -> None:
    """Application entrypoint."""
    server = uvicorn.Server(
        uvicorn.Config(
            "mwe_fastapi_debug.main:app", host=settings.APP_HOST, port=settings.APP_PORT
        ),
    )
    server.run()


if __name__ == "__main__":
    main()
