from sqlalchemy import Column, String

from app.models.base import BaseModelFields


class SourceSite(BaseModelFields):
    __tablename__ = "source_site"

    url = Column(String)
