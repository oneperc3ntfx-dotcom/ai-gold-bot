from aiogram import Router

from aiogram.filters import CommandStart

from aiogram.types import (
    Message,
    FSInputFile
)


from services.membership import check_member


from keyboards.menu import member_menu


from keyboards.buttons import renew_button


import os



router = Router()





# ==========================
# START COMMAND
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





    # ==========================
    # EXPIRED MEMBER
    # ==========================


    if not member["active"]:


        text = f"""

🔒 <b>MEMBERSHIP SUDAH BERAKHIR</b>


Halo <b>{message.from_user.first_name}</b> 👋


<blockquote>
"Masa aktif membership Anda
telah selesai."
</blockquote>


━━━━━━━━━━━━━━


Saat ini akses Anda telah berhenti:


📊 XAUUSD Premium Signal

🧠 Smart Money Concept Analysis

⚡ Gold Market Update


━━━━━━━━━━━━━━


Anda masih dapat melanjutkan
akses premium dengan melakukan
perpanjangan membership.


Silakan hubungi:


🤖 <b>@Intradayxauusd_bot</b>


━━━━━━━━━━━━━━


Terima kasih telah menjadi bagian
dari:


<b>🤖 XAU AI ASSISTANT</b>


"""


        await message.answer(

            text,

            reply_markup=renew_button(),

            parse_mode="HTML"

        )


        return







    # ==========================
    # ACTIVE MEMBER
    # ==========================



    # ==========================
    # IMAGE WELCOME
    # ==========================


    welcome_image = (
        "assets/welcome.jpg"
    )


    if os.path.exists(
        welcome_image
    ):


        await message.answer_photo(

            photo=FSInputFile(
                welcome_image
            ),


            caption=f"""

🤖 <b>XAU AI ASSISTANT PREMIUM</b>


Halo <b>{message.from_user.first_name}</b> 👋


Selamat datang di AI Trading
Assistant pribadi Anda.


<blockquote>
"Sistem analisa Smart Money Concept
untuk membantu membaca pergerakan
XAUUSD secara lebih terstruktur."
</blockquote>


""",

            parse_mode="HTML"

        )







    # ==========================
    # IMAGE LOT SIZE
    # ==========================


    lot_image = (
        "assets/lot_size.jpg"
    )


    if os.path.exists(
        lot_image
    ):


        await message.answer_photo(

            photo=FSInputFile(
                lot_image
            ),


            caption="""

📚 <b>MONEY MANAGEMENT GUIDE</b>


Sebelum mengikuti signal,
selalu gunakan lot sesuai modal
dan batas risiko Anda.


<blockquote>
"Protect your capital first,
profit will follow."
</blockquote>


⚠️ Hindari over lot dan tetap
ikuti aturan money management.


""",

            parse_mode="HTML"

        )







    # ==========================
    # MAIN WELCOME MESSAGE
    # ==========================


    text = f"""

🤖 <b>XAU AI ASSISTANT</b>


Halo <b>{message.from_user.first_name}</b> 👋


<blockquote>
"Saya adalah AI Assistant pribadi Anda.

Saya akan memberikan Signal XAUUSD
setiap 1 jam sekali pada menit 00
dengan analisa Smart Money Concept."
</blockquote>


━━━━━━━━━━━━━━


📊 <b>SYSTEM SIGNAL</b>


⏰ Update:
Setiap 1 jam sekali


🕒 Eksekusi:
Menit 00


📈 Metode Analisa:

• Smart Money Concept

• Liquidity Analysis

• Market Structure


━━━━━━━━━━━━━━


⚠️ <b>TRADING RULE</b>


Gunakan manajemen risiko yang baik.


Ikuti signal dengan disiplin agar
hasil trading lebih terkontrol.


━━━━━━━━━━━━━━


📈 <b>TEAM PORTFOLIO</b>


Lihat perkembangan portofolio team:


https://docs.google.com/spreadsheets/d/1p1jiuCcU6tUxxPEmodkwaQBmCB8u-BLOGa5J7LpETKE/edit


━━━━━━━━━━━━━━


Gunakan perintah:


<b>/menu</b>


untuk melihat layanan Anda.


🤖 <b>XAU AI ASSISTANT</b>


"""


    await message.answer(

        text,

        reply_markup=member_menu(),

        parse_mode="HTML"

    )
