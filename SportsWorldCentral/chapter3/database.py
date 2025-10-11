"""Database configuration"""
# Database.py file sets up the SQLAlchemy configuration to connect to the SQLite database.
# Tasks:
    # 1. creating a database connection that points to the SQLite database with correct settings.
    # 2. creating a parent class to use to define the Python table classes. 

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Get a session which is a SQLAlchemy object that manages the conversation with the database.

SQLALCHEMY_DATABASE_URL = "sqlite:///./fantasy_data.db" # Database URL which tells SQLAlchemy where to find the database.

# Create an engine object with one configuration setting that allows multiple connections to the database without an error being thrown.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Use engine object to creaye a session named SessionLocal which is used to manage the database conversation.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # This is a base class for the Python table classes.
