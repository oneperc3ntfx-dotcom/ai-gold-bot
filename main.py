import asyncio


from aiogram import Bot, Dispatcher


from fastapi import FastAPI
import uvicorn



from config.settings import BOT_TOKEN



from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.signal import router as signal_router
from handlers.admin import router as admin_router



from api.signal_api import router as signal_api_router





# ==========================
# BOT SETUP
# ==========================


bot = Bot(
    token=BOT_TOKEN
)



dp = Dispatcher()





# ==========================
# REGISTER TELEGRAM HANDLER
# ==========================


dp.include_router(
    start_router
)


dp.include_router(
    menu_router
)


dp.include_router(
    signal_router
)


dp.include_router(
    admin_router
)






# ==========================
# FASTAPI SETUP
# ==========================


app = FastAPI(
    title="XAU AI SIGNAL API"
)



app.include_router(
    signal_api_router
)






# ==========================
# RUN FASTAPI
# ==========================


async def run_api():


    config = uvicorn.Config(

        app,

        host="0.0.0.0",

        port=8000,

        log_level="info"

    )


    server = uvicorn.Server(
        config
    )


    await server.serve()






# ==========================
# RUN TELEGRAM BOT
# ==========================


async def run_bot():


    print(
        "🤖 XAU AI SIGNAL BOT RUNNING..."
    )


    await dp.start_polling(
        bot
    )






# ==========================
# MAIN
# ==========================


async def main():


    await asyncio.gather(

        run_bot(),

        run_api()

    )







if __name__ == "__main__":


    asyncio.run(main())
