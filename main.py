
from fastapi import FastAPI, HTTPException, Depends
from typing import List
#import random
import models
import schemas 
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session



Base.metadata.create_all(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

# welcome message at home page
@app.get("/")
def root():
    return {" Message": " Welcome to Rianna's Book Corner!"}

#get the list of all books
@app.get("/list-books")
def list_books(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return {"books": items}
   
#get book by index
@app.get("/book-by-index/{bookId}")
def get_book(bookId:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(bookId)
    return item

    
# create new book record
@app.post("/")
def add_book(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(title = item.title, author = item.author)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.put("/{bookId}")
def update_book(bookId: int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(bookId)
    itemObject.title = item.title
    itemObject.author = item.author
    session.commit()
    session.refresh(itemObject)
    return itemObject

#delete a book
@app.delete("/{BookId}")
def delete_book(bookId:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(bookId)
    session.delete(itemObject)
    session.commit()
    session.close()
    return  'The book is now deleted!'



