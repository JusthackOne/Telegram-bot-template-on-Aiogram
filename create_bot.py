import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=YOUR_TOKEN)
dp = Dispatcher(bot, storage=storage)