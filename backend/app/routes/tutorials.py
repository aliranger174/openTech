from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import Tutorial
from app.schemas.schemas import Tutorial as TutorialSchema, TutorialCreate, TutorialUpdate

router = APIRouter(prefix="/api/tutorials", tags=["tutorials"])

@router.get("/", response_model=list[TutorialSchema])
def get_tutorials(skip: int = 0, limit: int = 10, category: str = None, difficulty: str = None, db: Session = Depends(get_db)):
    query = db.query(Tutorial)
    if category:
        query = query.filter(Tutorial.category == category)
    if difficulty:
        query = query.filter(Tutorial.difficulty == difficulty)
    tutorials = query.offset(skip).limit(limit).all()
    return tutorials

@router.get("/{tutorial_id}", response_model=TutorialSchema)
def get_tutorial(tutorial_id: int, db: Session = Depends(get_db)):
    tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
    if not tutorial:
        raise HTTPException(status_code=404, detail="آموزش یافت نشد")
    return tutorial

@router.post("/", response_model=TutorialSchema)
def create_tutorial(tutorial: TutorialCreate, db: Session = Depends(get_db)):
    db_tutorial = Tutorial(**tutorial.model_dump())
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

@router.put("/{tutorial_id}", response_model=TutorialSchema)
def update_tutorial(tutorial_id: int, tutorial: TutorialUpdate, db: Session = Depends(get_db)):
    db_tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
    if not db_tutorial:
        raise HTTPException(status_code=404, detail="آموزش یافت نشد")
    
    update_data = tutorial.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_tutorial, key, value)
    
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

@router.delete("/{tutorial_id}")
def delete_tutorial(tutorial_id: int, db: Session = Depends(get_db)):
    db_tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
    if not db_tutorial:
        raise HTTPException(status_code=404, detail="آموزش یافت نشد")
    
    db.delete(db_tutorial)
    db.commit()
    return {"message": "آموزش حذف شد"}
