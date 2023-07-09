from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import config
from src.keyboards import query_kb, kb
import utils
import Test


class Form(StatesGroup):
    username = State()
    banned = State()
    started = State()
    change_token = State()
    product = State()


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


# АДМИН-ПАНЕЛЬ
async def admin_panel(message: types.Message):
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await message.answer("Вы вошли в админ-панель", reply_markup=query_kb.keyboard_admin_panel)
        await message.answer("Вернуться в главное меню:", reply_markup=query_kb.keyboard_main_menu)


# ИСТОРИЯ
async def personal_history(message: types.Message):
    keyboard = kb.keyboard_history
    await message.answer("Вы вошли в историю запросов", reply_markup=keyboard)
    await utils.show_reports(message, "history", reports=Test.reports)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ОЧИСТИТЬ ИСТОРИЮ
async def personal_history_clear(message: types.Message):
    Test.reports.clear()
    keyboard = kb.keyboard_history
    await message.answer("История очищена", reply_markup=keyboard)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ВЫБРАТЬ ПОЛЬЗОВАТЕЛЯ
async def select_user(message: types.Message):
    await Form.username.set()
    await message.answer("Введите @username пользователя:", reply_markup=query_kb.keyboard_admin_panel)


# ВЫБРАТЬ ПОЛЬЗОВАТЕЛЯ (State)
async def process_name(message: types.Message, state: FSMContext, User=None):
    for u in Test.Users:
        if u.username == message.text:
            User = u
            await state.finish()
    if User is not None:
        if Test.UserTest.role == "admin":
            keyboard = kb.keyboard_select_user_admin
        elif Test.UserTest.role == "manager":
            keyboard = kb.keyboard_select_user_manager
        else:
            await message.answer("У вас нету доступа к данной команде")
            return
        await message.reply(f"Вы выбрали пользователя {User.username}, что хотите сделать?", reply_markup=keyboard)


# ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ
async def user_information(message: types.Message):
    await message.answer(f"Имя - {Test.UserTest.username}\n"
                         f"Количество токенов - {Test.UserTest.token_count}\n"
                         f"Роль - {Test.UserTest.role}", reply_markup=query_kb.keyboard_main_menu)


# ИЗБРАННОЕ
async def personal_favourites(message: types.Message):
    await message.answer("Вы вошли в избранные отчеты")
    await utils.show_reports(message, "favourites", reports=Test.favourite_reports)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ПОКАЗЫВАЕТ ТЕКУЩИЙ БАЛАНС ТОКЕНОВ
async def personal_balance(message: types.Message):
    await message.answer(
        text=f"Количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}",
        reply_markup=query_kb.keyboard_main_menu)


# ПОМЕНЯТЬ КОЛ-ВО ТОКЕНОВ
async def personal_change_token(message: types.Message):
    await Form.change_token.set()
    await message.answer(
        text=f"Количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}\n"
             f"введите новое значение:",
        reply_markup=query_kb.keyboard_cancel_change_role)


# ПОМЕНЯТЬ КОЛ-ВО ТОКЕНОВ (State)
async def process_change_token(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.finish()
        Test.UserTest.token_count = message.text
        await message.answer(
            text=f"Новое количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}",
            reply_markup=query_kb.keyboard_main_menu)
    else:
        await message.answer(text="Введено некорректное число, попробуйте снова")


# ПОМЕНЯТЬ РОЛЬ
async def personal_change_role(message: types.Message):
    await message.answer(text=f"Пользователь: {Test.UserTest.username} \n Роль: {Test.UserTest.role}",
                         reply_markup=query_kb.keyboard_change_role)


# БАН/РАЗБАН
async def personal_am_ban(message: types.Message):
    # TODO ДОДЕЛАТЬ КОГДА СКИНУТ (ПЕРЕДЕЛАТЬ В QUERY HANDLER | БАН/РАЗБАН)
    if Test.UserTest.status == "banned":
        Test.UserTest.status = "active"
        await message.answer(text=f"Пользователь {Test.UserTest.username} разбанен",
                             reply_markup=query_kb.keyboard_main_menu)
    else:
        Test.UserTest.status = "banned"
        await message.answer(text=f"Пользователь {Test.UserTest.username} забанен",
                             reply_markup=query_kb.keyboard_main_menu)


# НАЧАТЬ АНАЛИЗ
async def analyze_start(message: types.Message):
    await Form.product.set()
    await message.answer(text=f"Введите наименование продукта", reply_markup=query_kb.keyboard_main_menu)


# НАЧАТЬ АНАЛИЗ (State)
async def analyze_process_product(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=f"Вы ввели продукт: {message.text}", reply_markup=query_kb.keyboard_main_menu)
    await utils.show_products(message, owner="product", reports=Test.product)


# ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ
async def personal_agreement(message: types.Message):
    await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_main_menu)


# ПОМОЩЬ
async def personal_help(message: types.Message):
    await message.answer(text=config.help_user, reply_markup=query_kb.keyboard_main_menu)
