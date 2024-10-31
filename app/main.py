from fastapi import FastAPI
from app.routes import users, payments
from app.database import init_db 

app = FastAPI()

init_db()

app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(payments.router, prefix="/api", tags=["payments"])
