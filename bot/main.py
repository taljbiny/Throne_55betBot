from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot.config import BOT_TOKEN
from bot.handlers import start, button_handler

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button_handler))

updater.start_polling()
updater.idle()
