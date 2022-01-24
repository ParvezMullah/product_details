from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.schemas import manufacturer, category, model, part_category


class Product(BaseModel):
    id: int
    manufacturer_id : int
    manufacturer: manufacturer.Manufacturer
    category_id: int
    category: category.Category
    model_id : int
    model: model.Model
    part_category_id: int
    part_category: part_category.PartCategory
    part_number : str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
