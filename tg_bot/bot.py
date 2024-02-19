import asyncio
from aiogram import Bot
from config import load_config, Config
import aio_pika

async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)

    connect = await aio_pika.connect_robust(host='localhost')
    queue_name = 'spam'

    async with connect:
        channel = await connect.channel()
        await channel.set_qos

if __name__ == '__main__':
    asyncio.run(main())



