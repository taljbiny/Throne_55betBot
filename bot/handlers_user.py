import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.config import API_URL


async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("إنشاء حساب", callback_data="create")],
        [InlineKeyboardButton("رصيدي", callback_data="balance")]
    ]

    await update.message.reply_text(
        "أهلاً بك 👋",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update, context):
    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    if query.data == "create":
        r = requests.post(
            f"{API_URL}/create-user",
            json={"telegram_id": user_id}
        )

        await query.edit_message_text(
            r.json()["message"]
        )

    elif query.data == "balance":
        await query.edit_message_text(
            "ميزة الرصيد قيد الإعداد"
        )
