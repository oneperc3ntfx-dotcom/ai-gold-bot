from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():

    keyboard = ReplyKeyboardMarkup(

        keyboard=[

            [

                KeyboardButton(
                    text="🚀 Start"
                ),

                KeyboardButton(
                    text="📋 Menu"
                )

            ]

        ],

        resize_keyboard=True

    )


    return keyboard
