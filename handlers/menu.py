from aiogram import Router, F

from aiogram.types import (
    Message,
    CallbackQuery
)


from services.membership import (
    check_member
)


from keyboards.menu import (
    member_menu
)


from keyboards.buttons import (
    renew_button
)



router = Router()





# ==========================
# COMMAND /MENU
# ==========================


@router.message(
    F.text == "/menu"
)

async def menu(
    message: Message
):


    user_id = message.from_user.id



    member = check_member(
        user_id
    )



    if not member["active"]:


        await message.answer(

            """

🔒 <b>MEMBERSHIP TIDAK AKTIF</b>


Saat ini membership Anda
sudah berakhir.


Silakan lakukan perpanjangan
untuk mendapatkan kembali:


📊 Signal XAUUSD

🧠 Smart Money Concept

⚡ Market Update


""",

            reply_markup=renew_button(),

            parse_mode="HTML"

        )


        return






    text = f"""

⚙️ <b>MEMBER MENU</b>


Halo <b>{message.from_user.first_name}</b> 👋


Status Membership:

🟢 <b>ACTIVE</b>


━━━━━━━━━━━━━━


📦 Paket:

<b>{member['package']}</b>


⏳ Aktif Sampai:

<b>{member['expired']}</b>


━━━━━━━━━━━━━━


Silakan pilih menu:


"""



    await message.answer(

        text,

        reply_markup=member_menu(),

        parse_mode="HTML"

    )








# ==========================
# CEK EXPIRED BUTTON
# ==========================


@router.callback_query(

    F.data=="check_expired"

)

async def check_expired(

    callback: CallbackQuery

):


    user_id = callback.from_user.id



    member = check_member(
        user_id
    )



    if member["active"]:


        text = f"""

⏳ <b>MEMBERSHIP STATUS</b>


🟢 Status:

ACTIVE


📦 Paket:

{member['package']}


📅 Expired:

{member['expired']}


━━━━━━━━━━━━━━


Terima kasih telah menjadi
bagian dari:


🤖 <b>XAU AI ASSISTANT</b>


"""


    else:


        text = """

🔒 <b>MEMBERSHIP EXPIRED</b>


Masa aktif Anda telah selesai.


Silakan perpanjang membership
untuk mendapatkan akses kembali.


"""



    await callback.message.answer(

        text,

        parse_mode="HTML"

    )



    await callback.answer()
