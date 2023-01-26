import asyncio
from aiogram import Bot, Dispatcher
from config import conf

bot = Bot(token = conf.token)
dp = Dispatcher(bot=bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await dp.bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('error')

