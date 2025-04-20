from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, controllers
from ..lib.db import get_db
from typing import List
from ..lib.auth import get_current_active_user
from .. import models

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return controllers.create_order(db=db, order=order, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return controllers.get_orders(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if controllers.delete_order(db=db, order_id=order_id, user_id=current_user.id):
        return {"message": "Order deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found")
