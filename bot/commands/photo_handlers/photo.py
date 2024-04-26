from aiogram import Router, Bot
from yolomodule import someone_smoking as ss
from aiogram.types import Message


router = Router()


@router.message()
async def photo_handler(message:Message, bot: Bot):
    await bot.download(message.photo[-1],destination=f"C:/Users/dimau/Desktop/bot/images/raw/{message.photo[-1].file_id}.jpg")
    await message.answer("Обработка, подождите...")
    filename = f"C:/Users/dimau/Desktop/bot/images/raw/{message.photo[-1].file_id}.jpg"
    res = ss(filename)
    if (res[0]):
        await bot.edit_message_text(f"Кто-то курит с вероятностью {res[1]}%", message.chat.id, message.message_id + 1) #Для удобства пользователя
    else:
        await bot.edit_message_text(f"Курящих не видно", message.chat.id, message.message_id + 1)
