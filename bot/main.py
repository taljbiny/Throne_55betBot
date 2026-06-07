print("BOT STARTING...")

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from bot.config import BOT_TOKEN
from bot.db import init_db
from bot.handlers_user import start, button_handler

# إنشاء الجداول عند تشغيل البوت
init_db()

# إنشاء التطبيق
app = Application.builder().token(BOT_TOKEN).build()

# أوامر المستخدم
app.add_handler(CommandHandler("start", start))

# أزرار Inline
app.add_handler(CallbackQueryHandler(button_handler))

print("BOT IS RUNNING...")

# تشغيل البوت
app.run_polling(
    drop_pending_updates=True
)
