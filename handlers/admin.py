from aiogram import Router, F

from aiogram.types import Message


from config.settings import ADMIN_USERNAME


from services.membership import (
    get_active_members
)



router = Router()





# ==========================
# CHECK ADMIN
# ==========================


def is_admin(
    username
):

    if not username:

        return False


    return (

        username.lower()

        ==

        ADMIN_USERNAME.replace("@","").lower()

    )





# ==========================
# ADMIN STATUS
# ==========================


@router.message(
    F.text == "/admin"
)

async def admin_panel(

    message: Message

):


    if not is_admin(
        message.from_user.username
    ):


        return




    members = get_active_members()



    await message.answer(

        f"""

🛠 <b>ADMIN PANEL</b>


━━━━━━━━━━━━━━


🟢 Member Aktif:

<b>{len(members)}</b>


━━━━━━━━━━━━━━


Bot Signal XAU AI Assistant


""",

        parse_mode="HTML"

    )








# ==========================
# TEST SIGNAL
# ==========================


@router.message(

    F.text.startswith("/testsignal")

)

async def test_signal(

    message: Message

):


    if not is_admin(

        message.from_user.username

    ):


        return





    text = message.text.replace(

        "/testsignal",

        ""

    )



    if not text:


        await message.answer(

            "Masukkan text signal"

        )

        return





    members = get_active_members()





    total = 0



    for member in members:


        try:


            await message.bot.send_message(

                chat_id=int(

                    member["Telegram ID"]

                ),

                text=text,

                parse_mode="HTML"

            )


            total += 1



        except:


            pass





    await message.answer(

        f"""

✅ <b>TEST SIGNAL TERKIRIM</b>


Jumlah member:

{total}


""",

        parse_mode="HTML"

    )
