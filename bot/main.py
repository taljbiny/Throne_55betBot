print("BOT STARTING...")

import asyncio
import threading
import traceback

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

print("BOT_TOKEN FOUND:", bool(BOT_TOKEN))

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
    try:
        print("BOT IS RUNNING...")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        telegram_app.run_polling(
            drop_pending_updates=True
        )

    except Exception as e:
        print("BOT ERROR:", repr(e))
        traceback.print_exc()


# تشغيل البوت بخيط منفصل
bot_thread = threading.Thread(
    target=run_bot,
    daemon=True
)
bot_thread.start()


# FastAPI
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
