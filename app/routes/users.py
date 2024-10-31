from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserResponse
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

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(name=user.name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"Error creating user: {e}")  # Log the error
        raise HTTPException(status_code=400, detail="Error creating user")

@router.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        users = db.query(User).offset(skip).limit(limit).all()
        return users
    except Exception as e:
        print(f"Error reading users: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Error retrieving users")

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        print(f"Error reading user with ID {user_id}: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Error retrieving user")
