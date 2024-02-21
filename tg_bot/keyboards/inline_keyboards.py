from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_url_button(url: str) -> InlineKeyboardMarkup:
    url_button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ссылка', url=url)]
    ])
    return url_button