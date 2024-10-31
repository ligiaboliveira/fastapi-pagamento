# app/main.py
from fastapi import FastAPI
from app.routes import payments

app = FastAPI()

# Incluindo as rotas de pagamento
app.include_router(payments.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Payment API"}
