from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import Test
from src.keyboards import query_kb

report_position = 0


async def show_reports(message: types.Message, owner, action="default", reports=None):
    if (reports is None) | len(reports) == 0:
        await message.answer("Отчеты отсутствуют")
        return

    reports_kb = InlineKeyboardMarkup()
    if len(reports) == 0:
        await message.answer("История запросов пуста")
        return
    current_position = 1
    global report_position
    if (action == "down") & (report_position + 10 <= len(reports)):
        report_position += 10
    if (action == "up") & (report_position - 10 >= 0):
        report_position -= 10
    if report_position > 9:
        if owner == "history":
            reports_kb.add(query_kb.keyboard_history_report_button_up)
        else:
            reports_kb.add(query_kb.keyboard_favourite_report_button_up)
    for i in reports[report_position:]:
        reports_kb.add(InlineKeyboardButton(text=f"{i}", callback_data=f"url=test_report_{i}"))
        if current_position >= 10:
            break
        current_position += 1
    if len(reports) > 10:
        if owner == "history":
            reports_kb.add(query_kb.keyboard_history_report_button_down)
        else:
            reports_kb.add(query_kb.keyboard_favourite_report_button_down)
    if (action == "down") | (action == "up"):
        await message.edit_text("Отчеты:", reply_markup=reports_kb)
    else:
        await message.answer("Отчеты", reply_markup=reports_kb)


# СКОРЕЕ ВСЕГО НЕ ПРИГОДИТСЯ
# TODO НАВЕРНОЕ ПРОДУКТЫ НЕ БУДУТ ОТЛИЧАТЬСЯ ПО СТРУКТУРЕ ОТ ОТЧЕТОВ, ТОГДА МОЖНО УБРАТЬ
async def show_products(message: types.Message, owner, action="default", reports=None):
    if (reports is None) | len(reports) == 0:
        await message.answer("Отчеты отсутствуют")
        return

    reports_kb = InlineKeyboardMarkup()
    if len(reports) == 0:
        await message.answer("История запросов пуста")
        return
    current_position = 1
    global report_position
    if (action == "down") & (report_position + 10 <= len(reports)):
        report_position += 10
    if (action == "up") & (report_position - 10 >= 0):
        report_position -= 10
    if report_position > 9:
        if owner == "history":
            reports_kb.add(query_kb.keyboard_history_report_button_up)
        elif owner == "product":
            reports_kb.add(query_kb.products_button_up)
        else:
            reports_kb.add(query_kb.keyboard_favourite_report_button_up)
    for i in reports[report_position:]:
        reports_kb.add(InlineKeyboardButton(text=f"{i}", callback_data=f"url=bebra_report_{i}"))
        if current_position >= 10:
            break
        current_position += 1
    if len(reports) > 10:
        if owner == "history":
            reports_kb.add(query_kb.keyboard_history_report_button_down)
        elif owner == "product":
            reports_kb.add(query_kb.products_button_down)
        else:
            reports_kb.add(query_kb.keyboard_favourite_report_button_down)
    if (action == "down") | (action == "up"):
        await message.edit_text("Отчеты:", reply_markup=reports_kb)
    else:
        await message.answer("Отчеты", reply_markup=reports_kb)


async def check_ban(message: types.Message):
    if Test.UserTest.status == "banned":
        import main
        await main.start(message)
