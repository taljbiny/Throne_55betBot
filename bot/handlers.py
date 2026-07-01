from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from services.auth import login
from services.players import get_players


async def start(update, context):

    keyboard = [
        [
            InlineKeyboardButton(
                "👤 إنشاء لاعب",
                callback_data="create_player"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 اللاعبون",
                callback_data="players"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 الرصيد",
                callback_data="balance"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="statistics"
            )
        ],
    ]

    await update.message.reply_text(
        "👋 أهلاً بك في لوحة التحكم\n\nاختر أحد الخيارات:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update, context):

    query = update.callback_query
    await query.answer()

    # --------------------------
    # اللاعبين
    # --------------------------

    if query.data == "players":

        if not login():

            await query.edit_message_text(
                "❌ فشل تسجيل الدخول إلى 55BETS"
            )
            return

        data = get_players()

        if not data:

            await query.edit_message_text(
                "❌ لم يتم استلام أي بيانات."
            )
            return

        if not data.get("status"):

            await query.edit_message_text(
                "❌ فشل جلب اللاعبين."
            )
            return

        players = data["result"]["records"]

        if len(players) == 0:

            await query.edit_message_text(
                "لا يوجد لاعبين."
            )
            return

        text = "👥 آخر اللاعبين\n\n"

        for player in players:

            text += (
                f"👤 {player['username']}\n"
                f"🆔 {player['playerId']}\n"
                f"📅 {player['registrationDate']}\n\n"
            )

        await query.edit_message_text(text)

    # --------------------------
    # إنشاء لاعب
    # --------------------------

    elif query.data == "create_player":

        await query.edit_message_text(
            "🚧 ميزة إنشاء اللاعب سنقوم بإضافتها في الخطوة القادمة."
        )

    # --------------------------
    # الرصيد
    # --------------------------

    elif query.data == "balance":

        await query.edit_message_text(
            "🚧 ميزة الرصيد سنقوم بإضافتها في الخطوة القادمة."
        )

    # --------------------------
    # الإحصائيات
    # --------------------------

    elif query.data == "statistics":

        await query.edit_message_text(
            "🚧 ميزة الإحصائيات سنقوم بإضافتها في الخطوة القادمة."
        )
