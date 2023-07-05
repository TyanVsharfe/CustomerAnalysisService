from random import randint

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

import kb

import query_kb
import utils


def register_query_handlers(dp: Dispatcher):
    @dp.callback_query_handler(text="main_menu")
    async def main_menu_callback(call: CallbackQuery):
        await call.message.answer(text="Главное меню", reply_markup=kb.keyboard_main_menu)

    @dp.callback_query_handler(text="manager_pa")
    async def manager_pa_callback(call: CallbackQuery):
        await call.message.answer(text="Личный кабинет менеджера",
                                  reply_markup=kb.keyboard_manager_pa)

    @dp.callback_query_handler(lambda c: c.data.startswith("url="))
    async def history_report(call: CallbackQuery):
        url = call.data[4:]  # Извлекаем часть строки после "url="
        await call.message.answer(f"Открыт URL: {url}")
        await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)

    @dp.callback_query_handler(text="history_up")
    async def history_down_callback(call: CallbackQuery):
        await utils.show_reports(message=call.message, action="up")
        await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)

    @dp.callback_query_handler(text="history_down")
    async def history_down_callback(call: CallbackQuery):
        await utils.show_reports(message=call.message, action="down")
        await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)
