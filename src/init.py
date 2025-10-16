from src.Sender.handler import rt as sender_router
from src.download import rt
from src.handlers import router
from src.config import TOKEN

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


async def main() -> None:
    dp = Dispatcher()

    bot = Bot(token=TOKEN, timeout=180, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    dp.include_routers(sender_router, router, rt)

    await dp.start_polling(bot)
