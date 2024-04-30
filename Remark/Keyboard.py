from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Answer = KeyboardButton('/Ответ')
Info = KeyboardButton('/info')

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.row(Answer, Info)
