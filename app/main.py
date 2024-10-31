from fastapi import FastAPI
from app.routes import users, payments
from app.database import init_db  # Import the init_db function

app = FastAPI()

# Initialize the database
init_db()

# Include the routers with prefixes and tags
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(payments.router, prefix="/api", tags=["payments"])
