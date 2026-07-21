from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():

    keyboard = ReplyKeyboardMarkup(

        keyboard=[

            [
                KeyboardButton(
                    text="🚀 START"
                ),
                KeyboardButton(
                    text="⚙️ MENU"
                )
            ]

        ],

        resize_keyboard=True

    )


    return keyboard
