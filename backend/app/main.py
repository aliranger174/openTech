from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import Base, engine
from app.routes import books, news, projects, tutorials

# ایجاد جداول در دیتابیس
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="openTech API",
    description="API برای سایت openTech",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# راوترها
app.include_router(books.router)
app.include_router(news.router)
app.include_router(projects.router)
app.include_router(tutorials.router)

@app.get("/")
def read_root():
    return {
        "message": "خوش آمدید به openTech API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
