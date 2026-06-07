print("BOT STARTING...")

import threading

from fastapi import FastAPI
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

# إنشاء تطبيق التلغرام
telegram_app = Application.builder().token(BOT_TOKEN).build()

telegram_app.add_handler(
    CommandHandler("start", start)
)

telegram_app.add_handler(
    CallbackQueryHandler(button
