from app.crud.base import filter_helper, defer_fields
from sqlalchemy.orm import Session, selectinload
from app.models import manufacturer, category, product, model, part_category


def get_products_with_field_and_label(db: Session, **filter_kwargs):
    # To get Products with required fields and label if required.
    query = filter_helper(db, product.Product, **filter_kwargs)
    query = query.options(selectinload(product.Product.manufacturer),
                          selectinload(product.Product.category),
                          selectinload(product.Product.model),
                          selectinload(product.Product.part_category))
    results = query.all()
    return results
