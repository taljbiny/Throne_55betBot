from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards import main_menu
from bot.api import login, get_players


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في بوت 55BETS 🚀",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "players":

        # تسجيل الدخول
        login_result = login()

        if not login_result.get("status"):
            await query.edit_message_text("❌ فشل تسجيل الدخول إلى 55BETS")
            return

        # جلب اللاعبين
        players_result = get_players()

        if not players_result.get("status"):
            await query.edit_message_text("❌ تعذر جلب قائمة اللاعبين")
            return

        records = players_result["result"]["records"]

        if len(records) == 0:
            await query.edit_message_text("لا يوجد لاعبين.")
            return

        text = "👥 قائمة اللاعبين\n\n"

        for player in records:
            text += (
                f"👤 {player['username']}\n"
                f"🆔 {player['playerId']}\n"
                f"📧 {player['email']}\n"
                f"📅 {player['registrationDate']}\n"
                f"──────────────\n"
            )

        await query.edit_message_text(text)

    elif query.data == "create_player":

        await query.edit_message_text(
            "🚧 ميزة إنشاء لاعب سنضيفها بالخطوة القادمة."
        )

    elif query.data == "balance":

        await query.edit_message_text(
            "💰 ميزة الرصيد سنضيفها بالخطوة القادمة."
        )
