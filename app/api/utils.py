from fastapi import Depends
from typing import Optional
from sqlalchemy.orm import Session, aliased
from app.db.database import get_db
from app.models import manufacturer, category, model, part_category, product


def get_products_queryset(manufacturer_name: Optional[str] = None, category_name: Optional[str] = None,
                          model_number: Optional[str] = None, part_category_name: Optional[str] = None,
                          part_number: Optional[str] = None, db: Session = Depends(get_db)):
    # Build search query for search product api.
    product_tbl = aliased(product.Product)
    query = db.query(product_tbl)
    if part_number:
        print(f"part_number : {part_number}")
        query = query.filter(product_tbl.part_number == part_number)
    if manufacturer_name:
        manufacturer_tbl = aliased(manufacturer.Manufacturer)
        query = query.join(manufacturer_tbl, product_tbl.manufacturer_id == manufacturer_tbl.id).filter(
            manufacturer_tbl.name == manufacturer_name)
    if category_name:
        category_tbl = aliased(category.Category)
        query = query.join(category_tbl, product_tbl.category_id == category_tbl.id).filter(
            category_tbl.name == category_name)
    if model_number:
        model_tbl = aliased(model.Model)
        query = query.join(model_tbl, product_tbl.model_id == model_tbl.id).filter(
            model_tbl.name == model_number)
    if part_category_name:
        part_category_tbl = aliased(part_category.PartCategory)
        query = query.join(part_category_tbl, product_tbl.part_category_id == part_category_tbl.id).filter(
            part_category_tbl.name == part_category_name)
    return query
