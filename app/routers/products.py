from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def get_product_details():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]