from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bot_db"
)

cur = db.cursor(dictionary=True)

@app.post("/create-user")
def create_user(data: dict):
    telegram_id = data["telegram_id"]

    cur.execute("SELECT * FROM users WHERE telegram_id=%s", (telegram_id,))
    if cur.fetchone():
        return {"status": "ok", "message": "المستخدم موجود"}

    cur.execute("INSERT INTO users (telegram_id) VALUES (%s)", (telegram_id,))
    db.commit()

    return {"status": "ok", "message": "تم إنشاء الحساب"}
