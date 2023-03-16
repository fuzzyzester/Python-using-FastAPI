#create database models from pydantic
from pydantic import BaseModel

class Item(BaseModel):
    title: str
    author: str