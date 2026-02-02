from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import News
from app.schemas.schemas import News as NewsSchema, NewsCreate, NewsUpdate

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/", response_model=list[NewsSchema])
def get_news(skip: int = 0, limit: int = 10, category: str = None, db: Session = Depends(get_db)):
    query = db.query(News)
    if category:
        query = query.filter(News.category == category)
    news = query.offset(skip).limit(limit).all()
    return news

@router.get("/{news_id}", response_model=NewsSchema)
def get_news_detail(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="خبری یافت نشد")
    return news

@router.post("/", response_model=NewsSchema)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    db_news = News(**news.model_dump())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

@router.put("/{news_id}", response_model=NewsSchema)
def update_news(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    db_news = db.query(News).filter(News.id == news_id).first()
    if not db_news:
        raise HTTPException(status_code=404, detail="خبری یافت نشد")
    
    update_data = news.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_news, key, value)
    
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

@router.delete("/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    db_news = db.query(News).filter(News.id == news_id).first()
    if not db_news:
        raise HTTPException(status_code=404, detail="خبری یافت نشد")
    
    db.delete(db_news)
    db.commit()
    return {"message": "خبر حذف شد"}
