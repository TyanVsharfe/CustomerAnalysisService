# АДМИН-ПАНЕЛЬ
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
from config import Form
from src.keyboards import query_kb, kb


# АДМИН ПАНЕЛЬ
async def admin_panel(message: types.Message):
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await message.answer("Вы вошли в админ-панель", reply_markup=query_kb.keyboard_admin_panel)
        await message.answer("Вернуться в главное меню:", reply_markup=query_kb.keyboard_main_menu)


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


# КНОПКА ОТМЕНЫ СМЕНЫ ТОКЕНА
async def cancel_change_token(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await admin_panel(call.message)


# ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ
async def user_information(message: types.Message):
    await message.answer(f"Имя - {Test.UserTest.username}\n"
                         f"Количество токенов - {Test.UserTest.token_count}\n"
                         f"Роль - {Test.UserTest.role}", reply_markup=query_kb.keyboard_main_menu)


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


# ПОМЕНЯТЬ РОЛЬ
async def personal_change_role(message: types.Message):
    await message.answer(text=f"Пользователь: {Test.UserTest.username} \n Роль: {Test.UserTest.role}",
                         reply_markup=query_kb.keyboard_change_role)


# МЕНЯЕТСЯ РОЛЬ НА МЕНЕДЖЕРА
async def personal_change_role_manager(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    if Test.UserTest.role == Test.role[1]:
        await call.message.answer(text="У пользователя уже имеется такая роль")
    else:
        await call.message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                                  reply_markup=query_kb.keyboard_main_menu)


# МЕНЯЕТСЯ РОЛЬ НА ПОЛЬЗОВАТЕЛЯ
async def personal_change_role_user(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    if Test.UserTest.role == Test.role[0]:
        await call.message.answer(text="У пользователя уже имеется такая роль")
    else:
        await call.message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                                  reply_markup=query_kb.keyboard_main_menu)