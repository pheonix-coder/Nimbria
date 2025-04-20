from sqlalchemy.orm import Session
from .. import models, schemas

def create_receiver(db: Session, receiver: schemas.ReceiverCreate, user_id: int):
    db_receiver = models.Receiver(**receiver.dict(), user_id=user_id)
    db.add(db_receiver)
    db.commit()
    db.refresh(db_receiver)
    return db_receiver

def get_receivers(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Receiver).filter(models.Receiver.user_id == user_id).offset(skip).limit(limit).all()

def delete_receiver(db: Session, receiver_id: int, user_id: int):
    db_receiver = db.query(models.Receiver).filter(models.Receiver.id == receiver_id, models.Receiver.user_id == user_id).first()
    if db_receiver:
        db.delete(db_receiver)
        db.commit()
        return True
    return False
