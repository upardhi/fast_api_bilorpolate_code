from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.health import router as health_router
from app.api.routes.users import router as user_router
from app.db.base import Base
from app.db.session import engine
from app.api.routes.auth import router as auth_router

# import models so SQLAlchemy knows them
from app.models import user  # noqa


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug
    )

    # Create DB tables
    Base.metadata.create_all(bind=engine)

    app.include_router(health_router)
    app.include_router(user_router)
    app.include_router(auth_router)

    return app


app = create_app()
