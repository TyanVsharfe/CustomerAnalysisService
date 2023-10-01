from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import config
from src.data_fetchers.bookmarks import fetch_all_bookmarks
from src.data_fetchers.histories import delete_all_history, fetch_all_history
from src.data_fetchers.users import fetch_user_tokens
from src.keyboards import query_kb, kb
import utils
import Test
from src.websocket.search import run_search_products


# ГЛАВНОЕ МЕНЮ
async def main_menu(message: types.Message):
    keyboard = kb.keyboard_main_menu
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await main_menu_with_admin_panel(message)
    else:
        await message.answer("Вы вошли в главное меню", reply_markup=keyboard)


# ХЗ ЗАЧЕМ, ВИДИМО УЖЕ НЕ НАДО
async def personal_account_start(message: types.Message):
    # await message.answer(f"Вы вошли в личный кабинет {message.from_user.username}")
    # if Test.UserTest.role == "admin":
    #    await admin_panel_admin(message)
    # elif Test.UserTest.role == "manager":
    #    await admin_panel_manager(message)
    # else:
    await personal_account(message)


# ЛИЧНЫЙ КАБИНЕТ
async def personal_account(message: types.Message):
    keyboard = kb.keyboard_user_pa
    await message.answer(text="Вы вошли в личный кабинет", reply_markup=keyboard)
    await message.answer("Вернуться в главное меню:", reply_markup=query_kb.keyboard_main_menu)


# ГЛАВНОЕ МЕНЮ С АДМИНКОЙ
async def main_menu_with_admin_panel(message: types.Message):
    keyboard = kb.keyboard_main_menu_admin
    await message.answer(text="Вы вошли в главное меню с админ-панелью", reply_markup=keyboard)


# ИСТОРИЯ
async def personal_history(message: types.Message):
    keyboard = kb.keyboard_history
    await fetch_all_history(message.from_user.id)
    await message.answer("Вы вошли в историю запросов", reply_markup=keyboard)
    await utils.show_reports(message, "history", reports=Test.reports)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ОЧИСТИТЬ ИСТОРИЮ
async def personal_history_clear(message: types.Message):
    Test.reports.clear()
    await delete_all_history(message.from_user.id)
    keyboard = kb.keyboard_history
    await message.answer("История очищена", reply_markup=keyboard)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ИЗБРАННОЕ
async def personal_bookmarks(message: types.Message):
    await message.answer("Вы вошли в избранные отчеты")
    await fetch_all_bookmarks(message.from_user.id)
    await utils.show_reports(message, "favourites", reports=Test.favourite_reports) # reports=Test.favourite_reports
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ПОКАЗЫВАЕТ ТЕКУЩИЙ БАЛАНС ТОКЕНОВ
async def personal_balance(message: types.Message):
    tokens = await fetch_user_tokens(message.from_user.id)
    await message.answer(
        text=f"Количество токенов у пользователя {message.from_user.username}: {tokens}",
        reply_markup=query_kb.keyboard_main_menu)


# НАЧАТЬ АНАЛИЗ
async def analyze_start(message: types.Message):
    await config.Form.product.set()
    await message.answer(text=f"Введите наименование продукта", reply_markup=query_kb.keyboard_main_menu)


# НАЧАТЬ АНАЛИЗ (State)
async def analyze_process_product(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=f"Вы ввели продукт: {message.text}", reply_markup=query_kb.keyboard_main_menu)
    result = await run_search_products(message.text, message.from_user.id)
    print(result)
    await utils.show_products(message, owner="product", reports=Test.product)


# ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ
async def personal_agreement(message: types.Message):
    await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_main_menu)


# ПОМОЩЬ
async def personal_help(message: types.Message):
    await message.answer(text=config.help_user, reply_markup=query_kb.keyboard_main_menu)
