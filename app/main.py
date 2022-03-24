from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import resource

app = FastAPI(
    title="title",
    description="""
Description of the API
""",
    version="version",
    swagger_ui_parameters={
        "docExpansion": "full"
    }
)

app.include_router(
    resource.router,
    prefix="/api"
)
