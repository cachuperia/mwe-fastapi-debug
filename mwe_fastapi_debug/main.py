"""API server."""
import uvicorn

from fastapi import FastAPI


app = FastAPI(
    title="MWE API",
)


@app.get("/")
async def root() -> str:
    """Endpoint."""
    return "Hello debugger!"


def main() -> None:
    """Application entrypoint."""
    server = uvicorn.Server(
        uvicorn.Config(
            "mwe_fastapi_debug.main:app",
            host="0.0.0.0",
        ),
    )
    server.run()


if __name__ == "__main__":
    main()
