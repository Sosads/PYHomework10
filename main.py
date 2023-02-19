from handlers import dp
# Важно импортировать dp из handlers, чтобы "отлавливать" сообщения пользователя
from aiogram import executor






async def on_start(_):
    print('Бот онлайн!')


async def on_shutdown(_):
    print('Бот офлайн!')


executor.start_polling(dp, on_startup=on_start, on_shutdown=on_shutdown)