from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ===== Books =====
class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    rating: Optional[float] = 0

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    rating: Optional[float] = None

class Book(BookBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# ===== News =====
class NewsBase(BaseModel):
    title: str
    content: str
    author: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None

class News(NewsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ===== Projects =====
class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: Optional[str] = None
    technologies: Optional[str] = None
    link: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    technologies: Optional[str] = None
    link: Optional[str] = None

class Project(ProjectBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# ===== Tutorials =====
class TutorialBase(BaseModel):
    title: str
    content: str
    author: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None
    difficulty: Optional[str] = "beginner"

class TutorialCreate(TutorialBase):
    pass

class TutorialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None
    difficulty: Optional[str] = None

class Tutorial(TutorialBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
