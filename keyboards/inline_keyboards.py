from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_url_button(url: str) -> InlineKeyboardMarkup:
    url_button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ссылка', url=url)]
    ])
    return url_button


menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать фильтры', callback_data='choise_filters')],
    [InlineKeyboardButton(text='Остановить парсер', callback_data='stop')],
    [InlineKeyboardButton(text='Запустить парсер', callback_data='start')]
])

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Меню', callback_data='menu')]
])