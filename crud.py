# crud.py

from sqlalchemy.orm import Session
import model

def create_book(db: Session, title: str, description: str):
    db_book = model.Book(title=title, description=description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(model.Book).filter(model.Book.id == book_id).first()

def function_1():
    pass