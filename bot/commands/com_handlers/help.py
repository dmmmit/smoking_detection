from aiogram import Router
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def cmd_help(message):
    await message.answer(
        "Для пользования ботом, пришлите фотографию. Далее бот определит, находится ли на фото курильщик. Всё просто!"
    )


@router.message(Command("about"))
async def cmd_about(message):
    await message.answer("Бот создан для HACK NAME командой TEAM NAME.\n(Ссылки)")
