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
        return {"status": "ok", "message": "المستخدم موجود مسبقاً"}

    cur.execute("INSERT INTO users (telegram_id) VALUES (%s)", (telegram_id,))
    db.commit()

    return {"status": "ok", "message": "تم إنشاء الحساب"}

@app.post("/deposit")
def deposit(data: dict):
    cur.execute(
        "UPDATE users SET balance = balance + %s WHERE telegram_id=%s",
        (data["amount"], data["telegram_id"])
    )
    db.commit()
    return {"status": "ok"}

@app.post("/withdraw")
def withdraw(data: dict):
    cur.execute("SELECT balance FROM users WHERE telegram_id=%s", (data["telegram_id"],))
    user = cur.fetchone()

    if not user or user["balance"] < data["amount"]:
        return {"status": "error", "message": "رصيد غير كافي"}

    cur.execute(
        "UPDATE users SET balance = balance - %s WHERE telegram_id=%s",
        (data["amount"], data["telegram_id"])
    )
    db.commit()

    return {"status": "ok"}
