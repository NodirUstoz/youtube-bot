import logging

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from src.Sender.broadcast import BroadcastState
from src.Sender.utils import show_summary
from src.user_manager import UserService
from src.db import Database
from src.config import ADMIN, TOKEN

rt = Router()
db = Database()
bot = Bot(token=TOKEN)
service = UserService(db)


@rt.message(Command("sender"))
async def start_broadcast(message: Message, state: FSMContext):
    if not service.is_admin(message.from_user.id):
        await message.reply("Эта команда доступна только администраторам.")
        return

    await state.set_state(BroadcastState.text)
    await message.reply("Введите текст сообщения для рассылки:")


@rt.message(Command("cancel"))
@rt.message(F.text.casefold() == "отмена")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)

    await state.clear()
    await message.answer("Отмена.")


@rt.message(BroadcastState.text)
async def process_text(message: Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    await state.set_state(BroadcastState.photo)

    await message.answer("Теперь отпавь фото")


@rt.message(BroadcastState.photo)
async def process_photo(message: Message, state: FSMContext) -> None:
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(BroadcastState.link)

    await message.answer("Теперь ссылку")


@rt.message(BroadcastState.link)
async def process_link(message: Message, state: FSMContext) -> None:
    await state.update_data(link=message.text)
    await state.set_state(BroadcastState.confirmation)

    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo', None)
    link = data.get('link', None)

    await show_summary(message, state)


@rt.callback_query(BroadcastState.confirmation, F.data == "Да")
async def process_send_broadcast(callback_query: CallbackQuery, state: FSMContext):
    if service.is_admin(callback_query.from_user.id):  # Проверка на админа
        await callback_query.message.answer("Это комадна доступна только админам")
        return

    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo', None)
    link = data.get('link', None)

    sender_link = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти по ссылке", url=link)]])

    for users_id in db.get_all_users():
        try:
            if photo:
                await bot.send_photo(users_id, photo=photo, caption=text, reply_markup=sender_link)
            else:
                await bot.send_message(users_id, text=text, reply_markup=sender_link)
        except Exception as e:
            logging.error(
                f"Не удалось отправить сообщение пользователю {users_id}: {e}")

    await bot.send_message(ADMIN, f"Сообщение отправлено {len(db.get_all_users())}")
    await state.clear()


@rt.callback_query(BroadcastState.confirmation, F.data == "Нет")
async def process_cancel(callback_query: CallbackQuery, state: FSMContext):
    if service.is_admin(callback_query.from_user.id):
        await callback_query.message.answer("Это комадна доступна только админам")
        return

    await bot.send_message(callback_query.from_user.id, "Отмена...")
    await state.clear()
