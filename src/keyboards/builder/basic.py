from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


def prenest_ignore():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='✅ Присутній',
        callback_data='ignore'
    )
    return builder.as_markup()

def absent_ignore():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='❌ Відсутній',
        callback_data='ignore'
    )
    return builder.as_markup()