import asyncio
from aiogram import Bot, Dispatcher
from bot import config, db
from bot.handlers import user

async def main():
    await db.init_db()
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
