from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('Каталог').add('Корзина').add('Ссылки')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add('Добавить видео').add('Удалить видео').add('ID')


video_list = InlineKeyboardMarkup(row_width = 2)
video_list.add(InlineKeyboardButton(text='Видео с самолетиками', url='https://www.youtube.com/watch?v=oPqsq0s5lM4'),
               InlineKeyboardButton(text='Видео с машинами', url='https://www.youtube.com/watch?v=3IHb-nFCU9k'))