import logging

import aiogram
import middleware
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
import config
from src import handlers
from src.data_fetchers.auth import user_signup
from src.data_fetchers.users import fetch_user

from src.handlers.handlers import main_menu_with_admin_panel
from src.keyboards import query_kb, kb

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(middleware.BanMiddleware())
# dp.middleware.setup(middleware.AgreementMiddleware())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    logging.info(f"ID:{message.from_user.id} Пользователь {message.from_user.username} Начал работу с ботом")
    if not Test.UserTest.agreement:
        await message.reply("Привет! Перед началом работы вы должны прочитать и принять пользовательское соглашение.",
                            reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_agreement)
        # Test.UserTest.agreement = True
    else:
        if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
            await main_menu_with_admin_panel(message)
        else:
            await message.answer("Вы вошли в главное меню", reply_markup=kb.keyboard_main_menu)
    handlers.register_handlers(dp)
    handlers.register_query_handlers(dp)
    dp.message_handlers.register(start_message)
    dp.message_handlers.unregister(start_message)
    dp.register_message_handler(agreement_message)


@dp.message_handler()
async def start_message(message: types.Message):
    await bot.set_my_commands([
        aiogram.types.BotCommand("start", "Начать работу"),
        aiogram.types.BotCommand("mm", "Главное меню"),
        # aiogram.types.BotCommand("help", "it is help command...")
    ])
    await message.answer("Для начала работы введи команду /start")


@dp.message_handler()
async def agreement_message(message: types.Message):
    await message.answer("Для начала работы примите пользовательское соглашение")


@dp.callback_query_handler(text="accept_agreement")
async def accept_agreement(call: CallbackQuery):
    dp.message_handlers.unregister(agreement_message)
    user = call.from_user
    print("start", user.id, user.first_name, user.last_name, user.username)

    if user.last_name:
        await user_signup(return_to="start", user_id=user.id, first_name=user.first_name, last_name=user.last_name,
                          username=user.username, is_accept_terms="true")
    else:
        await user_signup(return_to="start", user_id=user.id, first_name=user.first_name,
                          username=user.username, is_accept_terms="true")

    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await main_menu_with_admin_panel(call.message)
    else:
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
