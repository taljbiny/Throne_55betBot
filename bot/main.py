print("BOT STARTING...")

from contextlib import asynccontextmanager

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

init_db()

telegram_app = Application.builder().token(BOT_TOKEN).build()

telegram_app.add_handler(
    CommandHandler("start", start)
)

telegram_app.add_handler(
    CallbackQueryHandler(button_handler)
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("STARTING TELEGRAM BOT...")

    await telegram_app.initialize()
    await telegram_app.start()
    await telegram_app.updater.start_polling(
        drop_pending_updates=True
    )

    print("BOT STARTED")

    yield

    await telegram_app.updater.stop()
    await telegram_app.stop()
    await telegram_app.shutdown()


app = FastAPI(lifespan=lifespan)


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
