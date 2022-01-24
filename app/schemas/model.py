from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Model(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
