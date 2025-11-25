import aiohttp
import asyncio, logging, os
from urllib.parse import urlencode
from dotenv import  load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandObject, Command
from services.tg_bot_service.apartment_utils import format_flat, format_flats_list, fetch_and_send_flats
from config import config
load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']
FASTAPI_BASE_URL = os.environ['FASTAPI_BASE_URL']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# TODO разнести по директориям и файлам(подсказка routers)
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    # TODO целые тексты лучше выносить в константы
    await message.answer('Привет! Я бот, который автоматически подбирает квартиры по вашим критериям и отправляет прямые ссылки на объявления')

@dp.message(Command('search'))
async def cmd_search(message: types.Message, command: CommandObject):
    args_str = command.args
    if not args_str:
        await message.answer(
            'Пожалуйста, укажи параметры поиска.\n'
            'Пример: /search city=Москва min_rooms=3'
        )
        return

    params = {}
    for pair in args_str.split():
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
        else:
            await message.answer(f'Некорректный параметр: {pair}. Используй формат key=value.')
            return

    query_string = urlencode(params)
    url = f"{FASTAPI_BASE_URL}apartments/?{query_string}"

    await fetch_and_send_flats(message, url)


@dp.message(Command('get_apartments'))
async def cmd_get_apartments(message: types.Message):
    url = f'{FASTAPI_BASE_URL}apartments'
    await fetch_and_send_flats(message, url)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
