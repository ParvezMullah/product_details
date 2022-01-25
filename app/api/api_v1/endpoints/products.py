from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import Optional
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.api.utils import get_products_queryset
from app.schemas import product
router = APIRouter()


@router.get("/product_details", response_model=Page[product.Product])
def get_product_details(manufacturer_name: Optional[str] = None, category_name: Optional[str] = None,
                        model_number: Optional[str] = None, part_category_name: Optional[str] = None,
                        part_number: Optional[str] = None, db: Session = Depends(get_db)) -> list:
    products_queryset = get_products_queryset(
        manufacturer_name, category_name, model_number, part_category_name, part_number, db)
    return paginate(products_queryset)


add_pagination(router)
