from aiogram import Router
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message):
    await message.answer(
        "Сводка комманд:\n  /help - помощь в пользовании\n  /about - информация о боте"
    )
