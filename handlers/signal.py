from aiogram import Router, F
from aiogram.types import Message


from config.settings import (
    SOURCE_GROUP_ID,
    SIGNAL_TOPIC_ID
)


from services.membership import (
    get_active_members
)


from services.signal_parser import (
    format_signal
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
        "TOPIC ID:",
        message.message_thread_id
    )


    print(
        "FROM:",
        message.from_user.full_name if message.from_user else None
    )


    print(
        "IS BOT:",
        message.from_user.is_bot if message.from_user else None
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
            "Bukan topic signal"
        )

        return






    # ======================
    # CHECK TRADING TIME
    # ======================


    if not trading_open():


        print(
            "DILUAR JAM TRADING"
        )

        return






    # ======================
    # CHECK MESSAGE
    # ======================


    if not message.text:


        print(
            "Pesan tidak memiliki text"
        )

        return






    # ======================
    # FORMAT SIGNAL
    # ======================


    signal_text = format_signal(

        message.text

    )


    print(
        "SIGNAL FORMAT:"
    )


    print(
        signal_text
    )








    # ======================
    # GET ACTIVE MEMBERS
    # ======================


    members = get_active_members()


    print(
        "TOTAL MEMBER:",
        len(members)
    )








    # ======================
    # BROADCAST
    # ======================


    for member in members:



        telegram_id = member.get(
            "telegram_id"
        )



        if not telegram_id:


            print(
                "Telegram ID kosong:",
                member
            )

            continue






        try:


            await message.bot.send_message(

                chat_id=int(
                    telegram_id
                ),

                text=signal_text,

                parse_mode="HTML"

            )



            print(

                "TERKIRIM KE:",

                telegram_id

            )







        except Exception as e:



            print(

                "GAGAL KIRIM:",

                telegram_id,

                e

            )
