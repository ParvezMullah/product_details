from fastapi import APIRouter, HTTPException
from .endpoints import products
router = APIRouter()

router.include_router(
    products.router,
    prefix="")
