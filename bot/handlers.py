from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from services.auth import login


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
        "👋 أهلاً بك\n\nاختر أحد الخيارات:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update, context):

    query = update.callback_query
    await query.answer()

    if query.data == "players":

        result = login()

        await query.edit_message_text(
            f"{result}"
        )

    elif query.data == "create_player":

        await query.edit_message_text(
            "🚧 سيتم إضافة إنشاء اللاعب لاحقاً."
        )

    elif query.data == "balance":

        await query.edit_message_text(
            "🚧 سوسو لاحقاً."
        )

    elif query.data == "statistics":

        await query.edit_message_text(
            "🚧 سيتم إضافة الإحصائيات لاحقاً."
        )
