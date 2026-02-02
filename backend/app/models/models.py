from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from app.database.db import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False)
    description = Column(Text)
    image_url = Column(String(500))
    rating = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class News(Base):
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author = Column(String(255))
    image_url = Column(String(500))
    category = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    image_url = Column(String(500))
    technologies = Column(String(500))
    link = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)


class Tutorial(Base):
    __tablename__ = "tutorials"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author = Column(String(255))
    image_url = Column(String(500))
    category = Column(String(100))
    difficulty = Column(String(50), default="beginner")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
