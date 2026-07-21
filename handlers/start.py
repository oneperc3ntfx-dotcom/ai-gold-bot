from aiogram import Router

from aiogram.filters import CommandStart

from aiogram.types import (
    Message,
    FSInputFile
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
# START
# ==========================


@router.message(
    CommandStart()
)

async def start(
    message: Message
):


    user_id = message.from_user.id



    member = check_member(
        user_id
    )





    # =====================
    # EXPIRED
    # =====================


    if not member["active"]:


        text = f"""

🔒 <b>MEMBERSHIP BERAKHIR</b>


Halo <b>{message.from_user.first_name}</b> 👋


<blockquote>
"Masa aktif membership Anda
telah selesai."
</blockquote>


━━━━━━━━━━━━━━


Anda sudah tidak menerima:


📊 Signal XAUUSD Premium

🧠 Smart Money Concept Analysis

⚡ Market Update


Silakan perpanjang membership
untuk mendapatkan akses kembali.


🤖 <b>XAU AI ASSISTANT</b>


"""


        await message.answer(

            text,

            reply_markup=renew_button(),

            parse_mode="HTML"

        )


        return






    # =====================
    # ACTIVE
    # =====================



    photo = FSInputFile(

        "assets/lot_size.jpg"

    )




    text = f"""

🤖 <b>XAU AI ASSISTANT</b>


Halo <b>{message.from_user.first_name}</b> 👋


<blockquote>
"Saya adalah AI Assistant pribadi Anda.

Saya akan memberikan Signal XAUUSD
setiap 1 jam sekali dengan analisa
Smart Money Concept."
</blockquote>


━━━━━━━━━━━━━━


📊 <b>SYSTEM SIGNAL</b>


⏰ Update setiap jam

🕒 Entry menit 00

📈 Smart Money Concept

💎 Liquidity Analysis


━━━━━━━━━━━━━━


⚠️ <b>RULE TRADING</b>


Gunakan money management yang baik.

Ikuti aturan trading agar hasil
portofolio dapat maksimal.


━━━━━━━━━━━━━━


📈 <b>PORTOFOLIO TEAM</b>


Lihat perkembangan team:


https://docs.google.com/spreadsheets/d/1p1jiuCcU6tUxxPEmodkwaQBmCB8u-BLOGa5J7LpETKE/edit


━━━━━━━━━━━━━━


Ketik:


/menu


untuk melihat layanan Anda.


"""


    await message.answer_photo(

        photo=photo,

        caption=text,

        reply_markup=member_menu(),

        parse_mode="HTML"

    )
