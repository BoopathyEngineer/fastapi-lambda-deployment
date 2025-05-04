from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# For local testing with SQLite, you can use a file-based database.
# In production, you'll use the RDS PostgreSQL connection string.

# Example for PostgreSQL:
# DATABASE_URL = "postgresql://username:password@hostname/dbname"

# Example for SQLite:
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Set the DB URL in your environment or use SQLite for local testing.

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

# Create a configured "Session" class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for the declarative model
Base = declarative_base()

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
