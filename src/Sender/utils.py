from aiogram import html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def show_summary(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo', None)
    link = data.get('link', None)

    summary = f"<b>Подтверждение рассылки:</b>\n\n"
    summary += f"<b>Текст сообщения:</b>\n{text}\n\n"

    if link:
        summary += f"<b>Ссылка:</b> {link}\n\n"
    else:
        summary += "<b>Ссылка:</b> не добавлена\n\n"

    if photo:
        summary += "<b>Изображение:</b> присутствует\n"
    else:
        summary += "<b>Изображение:</b> не добавлено\n"

    if photo:
        await message.answer_photo(photo, caption=summary, parse_mode=ParseMode.HTML)
    else:
        await message.answer(summary, parse_mode=ParseMode.HTML)

    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отправить", callback_data="Да")],
        [InlineKeyboardButton(text="Отмена", callback_data="Нет")]
    ])

    await message.answer("Вы уверены, что хотите отправить это сообщение?", reply_markup=inline_kb)
