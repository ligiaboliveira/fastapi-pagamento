from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative class definitions
Base = declarative_base()

def init_db():
    """
    Initialize the database by creating all tables.
    Ensure that the models are imported before calling this function.
    """
    import app.models  # Ensure models are imported to create tables
    Base.metadata.create_all(bind=engine)
