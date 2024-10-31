# app/routes/payments.py
from fastapi import APIRouter, HTTPException
from random import randint

router = APIRouter()

# Mock database (em um projeto real, você usaria um banco de dados)
payments_db = []

@router.get("/pago")
def pago ():
    return {
        "mensagem" : "pago"
    }

