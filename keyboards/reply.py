from aiogram import Router, F
from aiogram.types import Message

from handlers.start import start


router = Router()



@router.message(
    F.text=="🚀 START"
)
async def start_button(
    message: Message
):

    await start(message)





@router.message(
    F.text=="⚙️ MENU"
)
async def menu_button(
    message: Message
):

    await message.answer(
        "/menu"
    )
