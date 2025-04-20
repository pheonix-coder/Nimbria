from fastapi import APIRouter
from .user_router import router as user_router
from .product_router import router as product_router
from .order_router import router as order_router
from .receiver_router import router as receiver_router

router = APIRouter()
router.include_router(user_router)
router.include_router(product_router)
router.include_router(order_router)
router.include_router(receiver_router)
