import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import Redis, RedisStorage
from config import load_config, Config
from handlers import user_handlers
from database.requests import Database


async def main():
    Database.create_tables()
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))
    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)
    dp = Dispatcher(storage=storage)
    dp.include_router(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



