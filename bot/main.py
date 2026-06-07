print("BOT STARTING...")

import asyncio
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)

from bot.config import BOT_TOKEN
from bot.handlers_user import start, button_handler


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
