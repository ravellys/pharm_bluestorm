from fastapi import FastAPI
from core.config import settings
from apis.base import api_router
from db.base import Base
from db.session import engine
import uvicorn


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, varion=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# TODO:
# 1. README
# 2. Testes
# 3. filtros
# 4. docker
# 5. CICD e Deploy