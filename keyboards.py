import aiogram
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_buttons = [
    [
        InlineKeyboardButton(text='Отправить заявку', callback_data='send'),
        InlineKeyboardButton(text='Помощь', callback_data='help'),
        InlineKeyboardButton(text='О нас', callback_data='about'),
    ]
]
