from pydantic import BaseModel


class Product(BaseModel):
    manufacturer_id : int
    category_id: int
    model_id : int
    part_category_id: int
    part_number : int
