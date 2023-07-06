from aiogram import Dispatcher
from aiogram.types import CallbackQuery

import Test
import kb

import query_kb
import utils


async def main_menu_callback(call: CallbackQuery):
    utils.report_position = 0
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu_admin)
    else:
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu)


async def manager_pa_callback(call: CallbackQuery):
    await call.message.answer(text="Личный кабинет менеджера",
                              reply_markup=kb.keyboard_manager_pa)


# Показываем данные отчета
async def history_report(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Открыт URL: {url}", reply_markup=query_kb.keyboard_watch_report)
    await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


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


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(main_menu_callback, text="main_menu")
    dp.register_callback_query_handler(manager_pa_callback, text="manager_pa")
    dp.register_callback_query_handler(history_report, lambda c: c.data.startswith("url="))
    dp.register_callback_query_handler(history_up_callback, text="history_up")
    dp.register_callback_query_handler(history_down_callback, text="history_down")
    dp.register_callback_query_handler(favourites_up_callback, text="favourite_up")
    dp.register_callback_query_handler(favourites_down_callback, text="favourite_down")
