import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from routers.fastfood import router as fastfood_router

load_dotenv()
TOKEN = os.getenv("bottoken")

defaults = DefaultBotProperties(parse_mode=ParseMode.HTML)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, default=defaults)
    dp = Dispatcher()
    dp.include_router(fastfood_router)
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())