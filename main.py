# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, model , schema , database
from database import SessionLocal, engine,get_db

app = FastAPI()

# Tạo bảng trong database
model.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(book: schema.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, title=book.title, description=book.description)

# API Endpoint để lấy danh sách Books
@app.get("/books/")
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

# API Endpoint để lấy thông tin của một Book theo ID
@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
