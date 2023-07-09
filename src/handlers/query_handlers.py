from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import Test
from src.handlers.admin_panel import admin_panel
from src.keyboards import query_kb, kb

import utils


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
    # TODO
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Открыт URL: {url}", reply_markup=query_kb.keyboard_watch_report)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


async def history_up_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="history", action="up", reports=Test.reports)


async def history_down_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="history", action="down", reports=Test.reports)


async def favourites_up_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="favourites", action="up", reports=Test.favourite_reports)


async def favourites_down_callback(call: CallbackQuery):
    await utils.show_reports(message=call.message, owner="favourites", action="down", reports=Test.favourite_reports)


async def product_up_callback(call: CallbackQuery):
    await utils.show_products(message=call.message, owner="product", action="up", reports=Test.product)


async def product_down_callback(call: CallbackQuery):
    await utils.show_products(message=call.message, owner="product", action="down", reports=Test.product)


# ДОБАВИТЬ В ИЗБРАННОЕ
async def add_favourite_callback(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    await call.message.answer("Отчет добавлен в избранное")


# УДАЛИТЬ ОТЧЕТ ИЗ ИЗБРАННОГО ИЛИ ИСТОРИИ
async def delete_favourite_history_callback(call: CallbackQuery):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ (1 или 2 метода хз)
    await call.message.answer("Отчет удален")


# КНОПКА ОТМЕНЫ АНАЛИЗА
async def cancel_product(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await admin_panel(call.message)

