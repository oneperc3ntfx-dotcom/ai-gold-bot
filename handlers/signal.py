from aiogram import Router, F
from aiogram.types import Message


from config.settings import (
    SOURCE_GROUP_ID,
    SIGNAL_TOPIC_ID
)


from services.membership import (
    get_active_members
)


from services.scheduler import (
    trading_open
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


    print("\n======================")
    print("=== SIGNAL MASUK ===")
    print("======================")


    print(
        "CHAT ID:",
        message.chat.id
    )


    print(
        "TOPIC:",
        message.message_thread_id
    )


    print(
        "FROM:",
        message.from_user.full_name
        if message.from_user
        else None
    )


    print(
        "IS BOT:",
        message.from_user.is_bot
        if message.from_user
        else None
    )


    print(
        "TEXT:",
        message.text
    )



    # ======================
    # CHECK TOPIC
    # ======================


    if message.message_thread_id != SIGNAL_TOPIC_ID:


        print(
            "BUKAN TOPIC SIGNAL"
        )

        return




    # ======================
    # MARKET TIME
    # ======================


    if not trading_open():


        print(
            "DILUAR JAM TRADING"
        )

        return




    # ======================
    # CHECK TEXT
    # ======================


    if not message.text:


        print(
            "TEXT KOSONG"
        )

        return





    # ======================
    # AMBIL SIGNAL ASLI
    # ======================


    signal_text = message.text





    # ======================
    # MEMBER ACTIVE
    # ======================


    members = get_active_members()



    print(
        "TOTAL MEMBER:",
        len(members)
    )





    # ======================
    # SEND USER
    # ======================


    for member in members:


        telegram_id = member.get(
            "telegram_id"
        )


        if not telegram_id:


            continue



        try:


            await message.bot.send_message(

                chat_id=int(
                    telegram_id
                ),

                text=signal_text

            )



            print(
                "TERKIRIM:",
                telegram_id
            )



        except Exception as e:


            print(
                "GAGAL:",
                telegram_id,
                e
            )
