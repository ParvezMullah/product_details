from pydantic import BaseModel


class Product(BaseModel):
    manufacturer_id : int
    category_id: int
    model_id : int
    part_category_id: int
    part_number : int


class ProductFetch(BaseModel):
    manufacturer : str
    category: str
    model : str
    part_category: str
    part_number : str
