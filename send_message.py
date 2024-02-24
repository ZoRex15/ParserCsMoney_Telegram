import asyncio
from aiogram import Bot
from aiogram.types import URLInputFile
from config import load_config, Config
import aio_pika

from keyboards.inline_keyboards import create_url_button


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)

    connect = await aio_pika.connect_robust(host='localhost')
    queue_name = 'spam'

    async with connect:
        channel = await connect.channel()
        await channel.set_qos(prefetch_count=10)
        queue = await channel.declare_queue(queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    d_message = message.body.decode().split('\n\n')
                    parametrs = {
                        'photo_url': '',
                        'name': '',
                        'price': '',
                        'url': '',
                        'proffit': ''
                    }
                    for i in d_message:
                        i = i.split(': ')
                        parametrs[i[0]] = i[1] 

                    image_from_url = URLInputFile(url=parametrs['photo_url'])
                     
                    await bot.send_photo(
                        photo=image_from_url,
                        caption=f'Название: {parametrs["name"]}\nЦена: {parametrs["price"]}$\nПрофит: {parametrs["proffit"]}',
                        chat_id=config.group_id,
                        reply_markup=create_url_button(url=parametrs['url'])
                    )
                    await asyncio.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())



