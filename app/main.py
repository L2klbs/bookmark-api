from fastapi import FastAPI
from .api import router as api_router
# from .telemetry import setup_telemetry

def create_app() -> FastAPI:
    app = FastAPI(
        title="Bookmark API",
        version="0.1.0",
        description="Bookmarking your spot in media content."
    )

    # setup_telemetry(app) # Initialize OpenTelemetry

    app.include_router(api_router)

    return app

app = create_app()