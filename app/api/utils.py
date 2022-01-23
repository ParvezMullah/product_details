from fastapi import status, HTTPException, Depends
from typing import Optional
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.base import get_filtered_object
from app.models import manufacturer, category, model, part_category


def get_products_query_filter(manufacturer_name: Optional[str] = None, category_name: Optional[str] = None,
                              model_number: Optional[str] = None, part_category_name: Optional[str] = None,
                              part_number: Optional[str] = None, db: Session = Depends(get_db)) -> dict:
    # This will create dictionary of arguments that we need to add in our query.
    manufacturer_id = category_id = model_id = part_category_id = None
    filter_kwargs = dict()
    if not (manufacturer_name or category_name or model_number or part_category_name or part_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Please provide atleast one of the query params.")
    if manufacturer_name:
        manufacturer_obj = get_filtered_object(
            db, manufacturer.Manufacturer, name=manufacturer_name)
        if not manufacturer_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Manufacturerer: {manufacturer_name} not found.")
        manufacturer_id = manufacturer_obj.id
        filter_kwargs['manufacturer_id'] = manufacturer_id
    if category_name:
        category_obj = get_filtered_object(
            db, category.Category, name=category_name)
        if not category_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Category: {category_name} not found.")
        category_id = category_obj.id
        filter_kwargs['category_id'] = category_id
    if model_number:
        model_obj = get_filtered_object(
            db, model.Model, name=model_number)
        if not model_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Model: {model_number} not found.")
        model_id = model_obj.id
        filter_kwargs['model_id'] = model_id
    if part_category_name:
        part_category_obj = get_filtered_object(
            db, part_category.PartCategory, name=part_category_name)
        if not part_category_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Part Category: {part_category_name} not found.")
        part_category_id = part_category_obj.id
        filter_kwargs['part_category_id'] = part_category_id
    if part_number:
        filter_kwargs['part_number'] = part_number
    return filter_kwargs
