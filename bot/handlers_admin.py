from bot.config import ADMIN_IDS
from bot.db import get_db

def is_admin(user_id):
    return user_id in ADMIN_IDS

async def admin_users(update, context):
    if update.message.from_user.id not in ADMIN_IDS:
        return await update.message.reply_text("ليس لديك صلاحية")

    db = get_db()
    cur = db.cursor(dictionary=True)

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    text = "👥 المستخدمين:\n"
    for u in users:
        text += f"{u['telegram_id']} - {u['balance']}\n"

    await update.message.reply_text(text)


async def admin_wallet(update, context):
    if update.message.from_user.id not in ADMIN_IDS:
        return

    db = get_db()
    cur = db.cursor(dictionary=True)

    cur.execute("SELECT balance FROM bot_wallet LIMIT 1")
    wallet = cur.fetchone()

    await update.message.reply_text(f"💰 محفظة البوت: {wallet['balance']}")
