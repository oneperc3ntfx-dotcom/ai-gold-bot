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

🔒 <b>MEMBERSHIP EXPIRED</b>


Halo <b>{message.from_user.first_name}</b> 👋


<blockquote>
"Masa aktif membership Anda
telah berakhir."
</blockquote>


━━━━━━━━━━━━━━


Saat ini Anda tidak mendapatkan:


📊 XAUUSD Premium Signal

🧠 Smart Money Concept Analysis

⚡ Market Update Gold


━━━━━━━━━━━━━━


Silakan lakukan perpanjangan
membership untuk mendapatkan
akses kembali.


🤖 <b>XAU AI ASSISTANT</b>


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
    # IMAGE 1
    # WELCOME
    # ==========================


    await message.answer_photo(

        photo=FSInputFile(

            "assets/welcome.jpg"

        ),


        caption=f"""

🤖 <b>XAU AI ASSISTANT PREMIUM</b>


Halo <b>{message.from_user.first_name}</b> 👋


Selamat datang di sistem
AI Trading Assistant Anda.


<blockquote>
"Smart Money Concept Analysis
untuk membantu membaca
pergerakan XAUUSD lebih terstruktur."
</blockquote>


""",

        parse_mode="HTML"

    )







    # ==========================
    # IMAGE 2
    # LOT SIZE
    # ==========================


    await message.answer_photo(

        photo=FSInputFile(

            "assets/lot_size.jpg"

        ),


        caption="""

📚 <b>MONEY MANAGEMENT GUIDE</b>


Sebelum mengikuti signal,
pastikan penggunaan lot sesuai
dengan modal dan risk management.


<blockquote>
"Protect your capital first,
profit will follow."
</blockquote>


⚠️ Jangan menggunakan lot besar
tanpa perhitungan risiko.


""",

        parse_mode="HTML"

    )







    # ==========================
    # WELCOME TEXT
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


🕒 Waktu:
Menit 00


📈 Analisa:

• Smart Money Concept

• Liquidity Analysis

• Market Structure


━━━━━━━━━━━━━━


⚠️ <b>TRADING RULE</b>


Gunakan money management yang baik.


Ikuti signal dengan disiplin agar
hasil portofolio dapat maksimal.


━━━━━━━━━━━━━━


📈 <b>TEAM PORTFOLIO</b>


Anda dapat melihat perkembangan
portofolio team kami:


https://docs.google.com/spreadsheets/d/1p1jiuCcU6tUxxPEmodkwaQBmCB8u-BLOGa5J7LpETKE/edit


━━━━━━━━━━━━━━


Ketik:

<b>/menu</b>


untuk melihat layanan Anda.


🤖 <b>XAU AI ASSISTANT</b>


"""



    await message.answer(

        text,

        reply_markup=member_menu(),

        parse_mode="HTML"

    )
