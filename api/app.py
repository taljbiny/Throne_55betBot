from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

db = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode="require"
)

cur = db.cursor()

# إنشاء الجدول تلقائياً
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
db.commit()

@app.get("/")
def home():
    return {"status": "online"}

@app.post("/create-user")
def create_user(data: dict):
    telegram_id = data["telegram_id"]

    cur.execute(
        "SELECT id FROM users WHERE telegram_id = %s",
        (telegram_id,)
    )

    if cur.fetchone():
        return {"status": "ok", "message": "المستخدم موجود"}

    cur.execute(
        "INSERT INTO users (telegram_id) VALUES (%s)",
        (telegram_id,)
    )

    db.commit()

    return {"status": "ok", "message": "تم إنشاء الحساب"}
