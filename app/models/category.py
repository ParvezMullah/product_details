from sqlalchemy import Column, String

from app.models.base import BaseModelFields


class Category(BaseModelFields):
    __tablename__ = "category"

    name = Column(String, unique=True)
