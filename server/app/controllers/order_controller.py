from sqlalchemy.orm import Session
from .. import models, schemas

def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(**order.dict(), user_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Order).filter(models.Order.user_id == user_id).offset(skip).limit(limit).all()

def delete_order(db: Session, order_id: int, user_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id, models.Order.user_id == user_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return True
    return False
