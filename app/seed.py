# app/seeds.py
from sqlalchemy.orm import Session
from app.models import User, Payment

def seed_users(db: Session):
    users = [
        User(name="Alice"),
        User(name="Bob"),
        User(name="Charlie"),
    ]
    db.add_all(users)
    db.commit()

def seed_payments(db: Session):
    payments = [
        Payment(amount=100, user_id=1),  # Assuming user with ID 1 exists
        Payment(amount=200, user_id=2),  # Assuming user with ID 2 exists
    ]
    db.add_all(payments)
    db.commit()

def seed_all(db: Session):
    seed_users(db)
    seed_payments(db)

# To run the seeds
if __name__ == "__main__":
    from app.database import SessionLocal

    db = SessionLocal()
    try:
        seed_all(db)
    finally:
        db.close()
