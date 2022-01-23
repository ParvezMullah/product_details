from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1 import api as v1_api
from app.db.database import engine
from app.models.category import Category
from app.models.manufacturer import Manufacturer
from app.models.part_category import PartCategory
from app.models.model import Model
from app.models.source_site import SourceSite
from app.models.product import Product


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


def create_database():
    Category.metadata.create_all(bind=engine)
    Manufacturer.metadata.create_all(bind=engine)
    PartCategory.metadata.create_all(bind=engine)
    Model.metadata.create_all(bind=engine)
    SourceSite.metadata.create_all(bind=engine)
    Product.metadata.create_all(bind=engine)


create_database()
app = get_application()

app.include_router(
    v1_api.router,
    prefix="/v1",
    tags=["V1 Product Api"])
