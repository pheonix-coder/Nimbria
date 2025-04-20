from pydantic import BaseModel

class ReceiverBase(BaseModel):
    name: str
    mobile: str
    address: str

class ReceiverCreate(ReceiverBase):
    pass

class Receiver(ReceiverBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
