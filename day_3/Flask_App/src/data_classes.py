from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# This is the base class for all the data classes.
# What that means is that all the classes you create will inherit from this class.
# The reason for this is that it allows you to create the tables in the database using the create_all() method.
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    # Primary key means that this is the unique identifier for the row
    # Unique means that the value in this column must be unique
    # Index means that the value in this column will be indexed for faster searching
    name = Column(String(50))
    username = Column(String(50), unique=True)
    email = Column(String(50))
    password = Column(String(50))