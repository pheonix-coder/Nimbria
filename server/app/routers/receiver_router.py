from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, controllers
from ..lib.db import get_db
from typing import List
from ..lib.auth import get_current_active_user
from .. import models

router = APIRouter(
    prefix="/receivers",
    tags=["receivers"],
)

@router.post("/", response_model=schemas.Receiver)
def create_receiver(receiver: schemas.ReceiverCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return controllers.create_receiver(db=db, receiver=receiver, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Receiver])
def read_receivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return controllers.get_receivers(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.delete("/{receiver_id}")
def delete_receiver(receiver_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if controllers.delete_receiver(db=db, receiver_id=receiver_id, user_id=current_user.id):
        return {"message": "Receiver deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Receiver not found")
