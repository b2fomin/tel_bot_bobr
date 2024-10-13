from aiogram import Bot
import os
import getpass
from buttons import dp
import asyncio

os.environ['TELEGRAM_BOT_API_KEY'] = getpass.getpass("Введите API ключ: ")

bot = Bot(token=os.environ.get('TELEGRAM_BOT_API_KEY'))

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())