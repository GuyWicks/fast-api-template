from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import items
from .routers import users

from .database.connection import engine
from .database import models

# Build the schema from the model
models.Base.metadata.create_all(bind=engine)

# Init the API
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


# Include routes
app.include_router(
    items.router,
    tags=["items"],
    prefix="/api"
)

app.include_router(
    users.router,
    tags=["users"],
    prefix="/api"
)
