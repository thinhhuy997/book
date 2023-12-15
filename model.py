# # model.py

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Book(Base):
#     __tablename__ = 'books'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String)


# model.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    author2 = Column(Integer, ForeignKey('author.id'))

    
    author = relationship('Author', back_populates='books')



class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    
Author.books = relationship('Book', back_populates='author')
