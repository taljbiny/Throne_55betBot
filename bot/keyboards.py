from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "👥 اللاعبين",
                callback_data="players"
            )
        ],
        [
            InlineKeyboardButton(
                "➕ إنشاء لاعب",
                callback_data="create_player"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 الرصيد",
                callback_data="balance"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
