from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.product import get_products_with_field_and_label
from app.api.utils import get_products_query_filter
router = APIRouter()


def demo():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Demo Error.")


@router.get("/product_details")
def get_product_details(manufacturer_name: Optional[str] = None, category_name: Optional[str] = None,
                        model_number: Optional[str] = None, part_category_name: Optional[str] = None,
                        part_number: Optional[str] = None, db: Session = Depends(get_db)) -> list:
    filter_kwargs = get_products_query_filter(
        manufacturer_name, category_name, model_number, part_category_name, part_number, db)
    products = get_products_with_field_and_label(db, **filter_kwargs)
    json_compatible_item_data = jsonable_encoder(products)
    return JSONResponse(content=json_compatible_item_data)
