from sqlalchemy import Column, String

from app.models.base import BaseModelFields


class Manufacturer(BaseModelFields):
    __tablename__ = "manufacturer"

    name = Column(String)
