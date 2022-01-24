from app.crud.base import filter_helper
from sqlalchemy.orm import Session, selectinload
from app.models import product


def get_products_with_field_and_label(db: Session, **filter_kwargs) -> list[product.Product]:
    # To get Products with required fields and label if required.
    query = filter_helper(db, product.Product, **filter_kwargs)
    query = query.options(selectinload(product.Product.manufacturer),
                          selectinload(product.Product.category),
                          selectinload(product.Product.model),
                          selectinload(product.Product.part_category))
    return query
