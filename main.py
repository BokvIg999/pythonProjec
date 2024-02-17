from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
import json
from app import keyboards as kb
from config import *
from app import database



async def startup(_):
    await database.db_start()
    print("Database")


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['adminca'])
async def adminca(message: types.Message):
    if message.from_user.id == (1976130204):
        await message.answer(f'Добро пожаловать мой хозяин, {message.from_user.first_name}', reply_markup=kb.admin_keyboard)
    else:
        await message.answer('Иди ка ты на хуй')

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловть в магазин техники для авиа симуляторов "Ходули от бабули"', reply_markup=kb.keyboard)

@dp.message_handler(commands=["id"])
async def main(message: types.Message):
    await message.reply( f"id = {message.from_user.id}")

@dp.message_handler(text=['Каталог'])
async def catalog(message: types.Message):
    await message.reply(f'wot', reply_markup=kb.video_list)

@dp.message_handler(text=['ID'])
async def catalog(message: types.Message):
    if message.from_user.id == (1976130204):
        await message.answer(f'Ваш ID: {message.from_user.id}')
    else:
        await message.answer('0')

@dp.message_handler(text=['Добавить видео'])
async def news_video(message: types.Message):
    if message.from_user.id == (1976130204):
        await message.answer('Напишите ссылку на видео')
        with open("news.json", "w") as file:
            json.dump(text, file, indent=4, ensure_ascii=False)
    else:
        await message.answer('0')

@dp.message_handler(text=['Ссылки'])
async def cslki(message: types.Message):
    with open('news.json') as file:
        video_list = json.load(file)
        await message.answer(video_list)







if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_sartup)
