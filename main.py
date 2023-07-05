import logging

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
import config
import handlers
import kb
import query_handlers
import query_kb

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if Test.UserTest.status == "banned":
        await handlers.Form.banned.set()
        await message.answer("Вы заблокированы")
    else:
        await message.reply("Привет! Перед началом работы ты должен прочитать и принять пользовательское соглашение.")
        await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_agreement)
        handlers.register_handlers(dp)
        query_handlers.register_query_handlers(dp)
        dp.message_handlers.unregister(start_message)


@dp.message_handler()
async def start_message(message: types.Message):
    await bot.set_my_commands([
        aiogram.types.BotCommand("start", "it is start command..."),
        aiogram.types.BotCommand("help", "it is help command...")
    ])
    await message.answer("Для начала работы введи команду /start")


@dp.message_handler()
async def agreement_message(message: types.Message):
    await message.answer("Для начала работы примите пользовательское соглашение")


@dp.message_handler(state=handlers.Form.banned)
async def handle_banned_commands(message: types.Message, state: FSMContext):
    await message.answer("Вы заблокированы")


@dp.callback_query_handler(text="accept_agreement")
async def accept_agreement(call: CallbackQuery):
    await delete_agreement_message()
    #TODO ПРИ ПЕРВОМ ЗАХОДЕ ЗАХОДИТ КАК ДЕФОЛТ ПОЛЬЗОВАТЕЛЬ, ИСПРАВИТЬ, ПРОБЛЕМА В handlers.py, нельзя подсосать методы
    await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu)


async def delete_agreement_message():
    dp.message_handlers.unregister(agreement_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
