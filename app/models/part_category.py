from sqlalchemy import Column, String

from app.models.base import BaseModelFields


class PartCategory(BaseModelFields):
    __tablename__ = "part_category"

    name = Column(String, unique=True)
