from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.product import ProductFetch
from app.crud.base import get_filtered_objects
from app.models import manufacturer, category, product, model, part_category
from app.api.utils import get_products_query_filter
router = APIRouter()


def demo():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Demo Error.")


@router.get("/product_details", response_model=List[ProductFetch])
def get_product_details(manufacturer_name: Optional[str] = None, category_name: Optional[str] = None,
                        model_number: Optional[str] = None, part_category_name: Optional[str] = None,
                        part_number: Optional[str] = None, db: Session = Depends(get_db)) -> list:
    filter_kwargs = get_products_query_filter(
        manufacturer_name, category_name, model_number, part_category_name, part_number, db)
    products = get_filtered_objects(db, product.Product, **filter_kwargs)
    print(filter_kwargs, products)
    return products
    # return [{
    #     "manufacturer": manufacturer_name,
    #     "category": category_name,
    #     "model": model_number,
    #     "part_category": part_category_name,
    #     "part_number": part_number or "",
    # }]
