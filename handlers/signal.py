from aiogram import Router, F

from aiogram.types import Message


from config.settings import (
    SOURCE_GROUP_ID,
    SIGNAL_TOPIC_ID
)


from services.scheduler import (
    trading_open
)


from services.membership import (
    get_active_members
)


from services.signal_parser import (
    format_signal
)



router = Router()





# ==========================
# RECEIVE SIGNAL FROM GROUP
# ==========================


@router.message(

    F.chat.id == SOURCE_GROUP_ID

)

async def receive_signal(

    message: Message

):


    # ======================
    # CHECK TOPIC
    # ======================


    if message.message_thread_id != SIGNAL_TOPIC_ID:


        return




    # ======================
    # CHECK TRADING TIME
    # ======================


    if not trading_open():


        return





    if not message.text:


        return





    # ======================
    # FORMAT SIGNAL
    # ======================


    signal_text = format_signal(

        message.text

    )





    # ======================
    # GET ACTIVE MEMBERS
    # ======================


    members = get_active_members()





    # ======================
    # BROADCAST
    # ======================


    for member in members:


        try:


            await message.bot.send_message(

                chat_id=

                int(member["Telegram ID"]),


                text=signal_text,


                parse_mode="HTML"

            )


        except Exception as e:


            print(

                "FAILED SEND:",

                member["Telegram ID"],

                e

            )
