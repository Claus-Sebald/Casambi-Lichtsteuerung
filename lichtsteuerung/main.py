"""FastAPI-Anwendung (App-Factory)."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import __version__
from .api import health
from .config import Settings, load_settings

WEB_DIR = Path(__file__).parent / "web"


def create_app(settings: Settings = None) -> FastAPI:
    settings = settings or load_settings()

    app = FastAPI(title="Lichtsteuerung", version=__version__)
    app.state.settings = settings

    app.include_router(health.router, prefix="/api")
    app.mount("/static", StaticFiles(directory=WEB_DIR / "static"), name="static")

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse(WEB_DIR / "index.html")

    return app


app = create_app()
