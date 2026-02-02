# openTech Backend

FastAPI backend برای سایت openTech

## نصب

1. نصب dependencies:
```bash
pip install -r requirements.txt
```

2. اجرای سرور:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

یا:
```bash
bash run.sh
```

## API Endpoints

### Books
- `GET /api/books` - لیست کتاب‌ها
- `GET /api/books/{id}` - جزئیات کتاب
- `POST /api/books` - ایجاد کتاب
- `PUT /api/books/{id}` - ویرایش کتاب
- `DELETE /api/books/{id}` - حذف کتاب

### News
- `GET /api/news` - لیست اخبار
- `GET /api/news/{id}` - جزئیات خبر
- `POST /api/news` - ایجاد خبر
- `PUT /api/news/{id}` - ویرایش خبر
- `DELETE /api/news/{id}` - حذف خبر

### Projects
- `GET /api/projects` - لیست پروژه‌ها
- `GET /api/projects/{id}` - جزئیات پروژه
- `POST /api/projects` - ایجاد پروژه
- `PUT /api/projects/{id}` - ویرایش پروژه
- `DELETE /api/projects/{id}` - حذف پروژه

### Tutorials
- `GET /api/tutorials` - لیست آموزش‌ها
- `GET /api/tutorials/{id}` - جزئیات آموزش
- `POST /api/tutorials` - ایجاد آموزش
- `PUT /api/tutorials/{id}` - ویرایش آموزش
- `DELETE /api/tutorials/{id}` - حذف آموزش

## Swagger Docs
http://localhost:8000/docs

## ReDoc
http://localhost:8000/redoc
