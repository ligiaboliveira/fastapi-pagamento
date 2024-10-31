from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Payment
from app.schemas import PaymentCreate, PaymentResponse
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Error occurred while using the database: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Database connection error")
    finally:
        db.close()

@router.post("/payments/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    try:
        db_payment = Payment(amount=payment.amount, user_id=payment.user_id)
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except Exception as e:
        print(f"Error creating payment: {e}")  # Log the error
        raise HTTPException(status_code=400, detail="Error creating payment")

@router.get("/payments/", response_model=list[PaymentResponse])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        payments = db.query(Payment).offset(skip).limit(limit).all()
        return payments
    except Exception as e:
        print(f"Error reading payments: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Error retrieving payments")

@router.get("/payments/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        return payment
    except Exception as e:
        print(f"Error reading payment with ID {payment_id}: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Error retrieving payment")
