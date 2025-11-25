import aiohttp
from typing import List, Dict, Any
from aiogram import types

def format_flat(flat: Dict[str, Any]) -> str:
    """Форматирует информацию о квартире в строку"""
    return (
        f"Город: {flat.get('city', 'Не указан')}\n"
        f"Комнат: {flat.get('rooms', 'Не указано')}\n"
        f"Цена: {flat.get('price', 'Не указана')}\n"
        f"Площадь: {flat.get('area', 'Не указана')} м²\n"
        f"---------------------------------\n"
    )


def format_flats_list(flat_list: List[Dict[str, Any]]) -> str:
    """Формирует текстовое представление списка квартир"""
    if not flat_list:
        return 'Квартиры не найдены.'

    result_text = ''
    for flat in flat_list:
        result_text += format_flat(flat)
    return result_text


async def fetch_and_send_flats(message: 'types.Message', url: str):
    """Выполняет запрос к API и отправляет результат пользователю"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    json_data = await response.json()
                    if isinstance(json_data, list):
                        result_text = format_flats_list(json_data)
                        await message.answer(result_text)
                    else:
                        await message.answer('Ответ от сервиса не является списком.')
                else:
                    await message.answer(f'Ошибка при получении данных: {response.status}')
        except Exception as e:
            await message.answer(f'Произошла ошибка: {e}')