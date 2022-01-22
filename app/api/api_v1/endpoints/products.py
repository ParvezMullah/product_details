from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/product_details")
def get_product_details():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]
