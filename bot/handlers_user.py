from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from bot.db import (
    create_user,
    get_user,
    get_wallet_balance,
)


async def start(update, context):
    user = update.effective_user

    create_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 حسابي",
                callback_data="account"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 محفظتي",
                callback_data="wallet"
            )
        ],
        [
            InlineKeyboardButton(
                "➕ إيداع",
                callback_data="deposit"
            ),
            InlineKeyboardButton(
                "➖ سحب",
                callback_data="withdraw"
            )
        ],
        [
            InlineKeyboardButton(
                "📜 سجل العمليات",
                callback_data="history"
            )
        ],
        [
            InlineKeyboardButton(
                "☎️ الدعم",
                callback_data="support"
            )
        ]
    ]

    await update.message.reply_text(
        f"أهلاً بك {user.first_name} 👋\n\n"
        "مرحباً بك في منصة الخدمات.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update, context):
    query = update.callback_query

    await query.answer()

    telegram_id = query.from_user.id

    user = get_user(telegram_id)

    if not user:
        await query.edit_message_text(
            "حدث خطأ، أرسل /start مجدداً."
        )
        return

    if query.data == "wallet":
        balance = get_wallet_balance(user["id"])

        await query.edit_message_text(
            f"💰 رصيد محفظتك:\n\n{balance}"
        )

    elif query.data == "account":
        await query.edit_message_text(
            "🎮 قسم الحسابات\n\n"
            "سيتم تفعيل إنشاء الحسابات في الخطوة القادمة."
        )

    elif query.data == "deposit":
        await query.edit_message_text(
            "➕ قسم الإيداع\n\n"
            "سيتم تفعيله في الخطوة القادمة."
        )

    elif query.data == "withdraw":
        await query.edit_message_text(
            "➖ قسم السحب\n\n"
            "سيتم تفعيله في الخطوة القادمة."
        )

    elif query.data == "history":
        await query.edit_message_text(
            "📜 سجل العمليات\n\n"
            "لا توجد عمليات حالياً."
        )

    elif query.data == "support":
        await query.edit_message_text(
            "☎️ الدعم الفني\n\n"
            "سيتم إضافة بيانات التواصل لاحقاً."
        )
