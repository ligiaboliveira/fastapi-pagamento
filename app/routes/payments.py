# app/routes/payments.py
from fastapi import APIRouter, HTTPException
from app.schemas import PaymentRequest, PaymentResponse
from random import randint

router = APIRouter()

# Mock database (em um projeto real, você usaria um banco de dados)
payments_db = []

@router.get("/pago")
def pago ():
    return {
        "mensagem" : "pago"
    }

