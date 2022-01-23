from fastapi import APIRouter
from typing import Optional, List
from sqlalchemy.orm import Session
from app.db.database import engine, SessionLocal
from app.schemas.product import ProductFetch
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/product_details", response_model=List[ProductFetch])
def get_product_details(manufacturer: str, category: str,
                        model: str, part_category: Optional[str],
                        part_number: Optional[str]) -> list:

    return [{
        "manufacturer": manufacturer,
        "category": category,
        "model": model,
        "part_category": part_category,
        "part_number": part_number,
    }]
