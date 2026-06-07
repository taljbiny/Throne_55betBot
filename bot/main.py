print("BOT STARTING...")

import threading

from fastapi import FastAPI
import uvicorn

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from bot.config import BOT_TOKEN
from bot.db import init_db
from bot.handlers_user import start, button_handler

# إنشاء الجداول
init_db()

# تطبيق التلغرام
telegram_app = Application.builder().token(BOT_TOKEN).build()

telegram_app.add_handler(
    CommandHandler("start", start)
)

telegram_app.add_handler(
    CallbackQueryHandler(button_handler)
)


def run_bot():
    print("BOT IS RUNNING...")
    telegram_app.run_polling(
        drop_pending_updates=True
    )


# تشغيل البوت في Thread منفصل
threading.Thread(
    target=run_bot,
    daemon=True
).start()


# FastAPI لإبقاء Render Web Service شغال
app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "telegram bot"
    }


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=10000
    )
