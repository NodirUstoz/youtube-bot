from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Что мне делать?")]], resize_keyboard=True)


builder = InlineKeyboardBuilder()

chBtn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📼144p", callback_data="144")],
    [InlineKeyboardButton(text="📼240p", callback_data="240")],
    [InlineKeyboardButton(text="📼360p", callback_data="360")],
    [InlineKeyboardButton(text="📼720p", callback_data="720")],
    [InlineKeyboardButton(text="🎧", callback_data="mp3")],
    [InlineKeyboardButton(text="🖼️Превью", callback_data="jpg")],
])

builder.attach(InlineKeyboardBuilder.from_markup(chBtn))
