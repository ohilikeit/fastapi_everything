import uvicorn
from fastapi import FastAPI
from logging_setup import LoggerSetup
import logging

# setup root logger
logger_setup = LoggerSetup()

# get logger for module
LOGGER = logging.getLogger(__name__)


def init_app():
    app = FastAPI(title="jihwan code", description="Fast API", version="1.0.0")

    async def startup():
        LOGGER.info("--- Start up App ---")

    async def shutdown():
        LOGGER.info("--- Shutdown App ---")

    # Using new way to handle startup and shutdown events
    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)

    @app.get("/")
    def home():
        return "welcome home!"

    from controllers import home

    app.include_router(home.router)

    return app


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
