from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
from src import handlers
from src.keyboards import query_kb, kb

import utils
from src.handlers.handlers import admin_panel


# Переход в главное меню
async def main_menu_callback(call: CallbackQuery):
    utils.report_position = 0
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu_admin)
    else:
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu)


# Переход в админ-панель
async def admin_panel_callback(call: CallbackQuery):
    await call.message.answer(text="Админ-панель",
                              reply_markup=kb.keyboard_admin_panel)


# ПОСМОТРЕТЬ ОТЧЕТ
async def watch_report(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Открыт URL: {url}", reply_markup=query_kb.keyboard_watch_report)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ВЫБРАТЬ ТИП АНАЛИЗА У ОТЧЕТА
async def report_analysis_type(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Выберите тип анализа", reply_markup=query_kb.keyboard_analysis_type)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# Показываем данные отчета
async def history_report(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Открыт URL: {url}", reply_markup=query_kb.keyboard_watch_report)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


async def history_up_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="history", action="up", reports=Test.reports)


async def history_down_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="history", action="down", reports=Test.reports)


async def favourites_up_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="favourites", action="up", reports=Test.favourite_reports)
    await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


async def favourites_down_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="favourites", action="down", reports=Test.favourite_reports)
    await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# МЕНЯЕТСЯ РОЛЬ НА ПОЛЬЗОВАТЕЛЯ
async def personal_change_role_user(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    if Test.UserTest.role == Test.role[0]:
        await call.message.answer(text="У пользователя уже имеется такая роль")
    else:
        await call.message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                                  reply_markup=query_kb.keyboard_main_menu)


# МЕНЯЕТСЯ РОЛЬ НА МЕНЕДЖЕРА
async def personal_change_role_manager(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    if Test.UserTest.role == Test.role[1]:
        await call.message.answer(text="У пользователя уже имеется такая роль")
    else:
        await call.message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                                  reply_markup=query_kb.keyboard_main_menu)


async def cancel_change_token(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await admin_panel(call.message)


async def cancel_product(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await admin_panel(call.message)
