import aiogram
from aiogram import Bot, types, Dispatcher, F
from aiogram.enums import ParseMode
from config import *
from keyboards import *

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    member = message.from_user
    await bot.send_message(message.from_user.id, f'Привет, {member.first_name}!' +
                           + '\n Добро пожаловать в бота.')