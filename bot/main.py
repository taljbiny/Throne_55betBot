from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)

from bot.config import BOT_TOKEN
from bot.handlers import start, button_handler


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
