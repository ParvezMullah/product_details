from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Product(BaseModel):
    id: int
    manufacturer_id : int
    category_id: int
    model_id : int
    part_category_id: int
    part_number : str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
