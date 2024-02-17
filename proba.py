from aiogram import Bot, Dispatcher, executor, types
from config import *


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(text=['Добавить видео'])
async def news_video(message: types.Message):
    if message.from_user.id == (1976130204):
        await message.answer('Напишите ссылку на видео')


        with open("news.json", "w") as file:
            json.dump(ID, file, indent=4, ensure_ascii=False)
    else:
        await message.answer('Ты не админ')






if __name__ == '__main__':
    executor.start_polling(dp)
