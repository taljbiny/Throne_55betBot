from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from bot.config import BOT_TOKEN
from bot.handlers_user import start, handle_buttons
from bot.handlers_admin import admin_users, admin_wallet

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))

app.add_handler(CommandHandler("users", admin_users))
app.add_handler(CommandHandler("wallet", admin_wallet))

app.run_polling()
