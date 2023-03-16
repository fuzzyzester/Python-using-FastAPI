#create models.py to represent the actual database models
from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'items'

    bookId = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)