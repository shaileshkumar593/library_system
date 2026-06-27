from fastapi import FastAPI

from app.api import books
from app.api import borrow
from app.api import members

from app.core.config import settings
from app.core.exceptions import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

register_exception_handlers(app)

app.include_router(books.router)

app.include_router(members.router)

app.include_router(borrow.router)


@app.get("/")
def root():

    return {
        "message": "Library Management API",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():

    return {
        "status": "UP"
    }