from sqlalchemy import Column, String

from app.models.base import BaseModelFields


class Model(BaseModelFields):
    __tablename__ = "model"

    external_id = Column(String)
