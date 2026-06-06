import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.config import API_URL

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("إنشاء حساب", callback_data="create")],
        [InlineKeyboardButton("شحن رصيد", callback_data="deposit")],
        [InlineKeyboardButton("سحب رصيد", callback_data="withdraw")],
        [InlineKeyboardButton("رصيدي", callback_data="balance")]
    ])

async def start(update, context):
    await update.message.reply_text("أهلاً بك 👋", reply_markup=main_menu())

async def handle_buttons(update, context):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "create":
        r = requests.post(f"{API_URL}/create-user", json={"telegram_id": user_id})
        await query.edit_message_text(r.json()["message"])

    elif query.data == "deposit":
        await query.edit_message_text("أرسل المبلغ للشحن")

    elif query.data == "withdraw":
        await query.edit_message_text("أرسل المبلغ للسحب")

    elif query.data == "balance":
        await query.edit_message_text("جاري جلب الرصيد...")
