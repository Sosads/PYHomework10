from aiogram import Dispatcher,Bot
from config import TELEGRAM_TOKEN_API,Game

bot = Bot(TELEGRAM_TOKEN_API)
dp = Dispatcher(bot)
game = Game()