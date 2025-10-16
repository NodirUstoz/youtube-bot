import src.keyboards as kb
from src.user_manager import UserService
from src.db import Database

from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

db = Database()
service = UserService(db)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    username = message.from_user.username
    user_id = message.from_user.id

    if service.add_new_user(user_id, username):
        await message.reply(f"Привет, {html.bold(message.from_user.full_name)}!", reply_markup=kb.main)
        return

    await message.reply(f"Привет, {html.bold(message.from_user.full_name)}!", reply_markup=kb.main)


@router.message(F.text == "Что мне делать?")
async def replyMsg(message: Message):
    await message.reply("Отправь ссылку на видео с ютуба")
