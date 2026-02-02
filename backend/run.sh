#!/usr/bin/env bash
# نصب dependencies
pip install -r requirements.txt

# اجرای سرور
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
