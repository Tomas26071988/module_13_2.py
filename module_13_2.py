from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7114780577:AAHxOHecAlYkeEFZ3L1BZXr74pGDVkIxuMI"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


