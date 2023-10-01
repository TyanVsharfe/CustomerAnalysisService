import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
from config import Form
from src.data_fetchers.admins import fetch_all_user_activity, fetch_new_users_stats, change_user_role
from src.data_fetchers.users import fetch_user, fetch_user_by_username
from src.keyboards import query_kb, kb

selected_user = []


# АДМИН ПАНЕЛЬ
async def admin_panel(message: types.Message):
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await message.answer("Вы вошли в админ-панель", reply_markup=query_kb.keyboard_admin_panel)
        await message.answer("Вернуться в главное меню:", reply_markup=query_kb.keyboard_main_menu)


# ПРОСМОТР АКТИВНОСТИ
async def select_users_activity(call: CallbackQuery):
    global formatted_string
    activity = await fetch_all_user_activity(call.from_user.id)
    print(len(activity))
    formatted_strings = []

    # Проходим по каждому элементу JSON-массива
    for item in activity:
        print(item)
        # Создаем строку в желаемом формате и добавляем ее в массив
        formatted_string = (f'Действие: {item["action"]}\n'
                            f'user_to: {item["user_to"]}\n'
                            f'user_from: {item["user_from"]}\n'
                            f'id: {item["id"]}\n'
                            f'Дата: {item["date"]}')
        formatted_strings.append(formatted_string)

    print(formatted_strings)
    await call.message.answer(f"Статистика активности пользователей\n", reply_markup=query_kb.keyboard_main_menu)
    for i in range(len(formatted_strings) - 1, len(formatted_strings) - 6, -1):
        await call.message.answer(formatted_strings[i])
    # await call.message.answer(f"\n{json.dumps(activity[0], indent=2, ensure_ascii=False)}")


# ПРОСМОТР АКТИВНОСТИ
async def select_new_users(call: CallbackQuery):
    new_users = await fetch_new_users_stats(call.from_user.id)
    formatted_users = []

    for item in new_users:
        print(item)
        # Создаем строку в желаемом формате и добавляем ее в массив
        formatted_user = (f'Количество новых пользователей: {item["user_count"]}\n'
                          f'Дата регистрации: {item["registration_date"]}')
        formatted_users.append(formatted_user)

    await call.message.answer(f"Статистика новых пользователей\n", reply_markup=query_kb.keyboard_main_menu)
    if len(new_users) > 1:
        for i in range(len(formatted_users) - 1, len(formatted_users) - 5, -1):
            await call.message.answer(formatted_users[i])
    else:
        await call.message.answer(formatted_users[0])


# ВЫБРАТЬ ПОЛЬЗОВАТЕЛЯ
async def select_user(call: CallbackQuery):
    await Form.username.set()
    await call.message.answer("Введите @username пользователя:", reply_markup=query_kb.keyboard_main_menu)


# ВЫБРАТЬ ПОЛЬЗОВАТЕЛЯ (State)
async def process_name(message: types.Message, state: FSMContext, user=None):
    # for u in Test.Users:
    #     if u.username == message.text:
    #         user = u
    #         await state.finish()
    user_info = await fetch_user_by_username(user_id=message.from_user.id, username=message.text)
    print(user_info[1])
    if user_info is not None:
        if user_info[1] == 'admin':
            keyboard = kb.keyboard_select_user_admin
        elif user_info[1] == 'manager':
            keyboard = kb.keyboard_select_user_manager
        else:
            await message.answer("У вас нету доступа к данной команде")
            await state.finish()
            return
        await state.finish()
        global selected_user
        selected_user = user_info
        await message.reply(f"Вы выбрали пользователя {user_info[0]}, что хотите сделать?", reply_markup=keyboard)


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
    print(message.from_user.id, selected_user)
    user_info = await fetch_user_by_username(user_id=message.from_user.id, username=selected_user[0])
    print(user_info)
    await message.answer(f"Имя - {user_info[0]}\n"  # Test.UserTest.username
                         f"Количество токенов - {user_info[2]}\n"  # Test.UserTest.token_count
                         f"Роль - {user_info[1]}", reply_markup=query_kb.keyboard_main_menu)  # Test.UserTest.role


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
    await message.answer(text=f"Пользователь: {selected_user[0]} \n Роль: {selected_user[1]}",
                         reply_markup=query_kb.keyboard_change_role) # Test.UserTest.username Test.UserTest.role


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
    print(call.from_user.id, selected_user)
    user_info = await fetch_user_by_username(user_id=call.from_user.id, username=selected_user[0])
    print(f"personal_change_role_user -> {user_info} перед ифчиком")

    if user_info[1] == "user":
        await call.message.answer(text="У пользователя уже имеется такая роль")
    else:
        await change_user_role(user_id=user_info[3], header_id=call.from_user.id, role="user")
        await call.message.answer(text=f"Пользователю {user_info[0]} \n Выдана роль: user",
                                  reply_markup=query_kb.keyboard_main_menu)
