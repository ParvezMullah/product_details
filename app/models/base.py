from sqlalchemy import Boolean, Column, Integer, DateTime
from app.db.database import Base
import datetime


class BaseModelFields(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
    is_active = Column(Boolean, default=True)
