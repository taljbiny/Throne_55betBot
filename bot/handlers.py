from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "أهلاً بك في بوت 55BETS 🚀",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "players":

        await query.edit_message_text(
            "📋 سيتم جلب اللاعبين..."
        )

    elif query.data == "create_player":

        await query.edit_message_text(
            "➕ سيتم إنشاء لاعب..."
        )

    elif query.data == "balance":

        await query.edit_message_text(
            "💰 سيتم جلب الرصيد..."
        )
