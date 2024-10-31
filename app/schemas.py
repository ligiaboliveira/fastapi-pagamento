# app/schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Enables compatibility with ORM models

class PaymentCreate(BaseModel):
    amount: int
    user_id: int

class PaymentResponse(BaseModel):
    id: int
    amount: int
    user_id: int

    class Config:
        orm_mode = True
