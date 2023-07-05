from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import Test
import query_kb

report_position = 0


# TODO СДЕЛАТЬ ЧТОБЫ ПЕРЕРИСОВЫВАЛОСЬ ТЕКУЩЕЕ СООБЩЕНИЕ
async def show_reports(message: types.Message, action="default"):
    reports_kb = InlineKeyboardMarkup()
    if len(Test.reports) == 0:
        await message.answer("История запросов пуста")
        return
    current_position = 1
    global report_position
    if (action == "down") & (report_position + 10 <= len(Test.reports)):
        report_position += 10
        # TODO Ловим ошибку если зашли за границы (ПЛЮС)
    if (action == "up") & (report_position - 10 >= 0):
        report_position -= 10
        # TODO Ловим ошибку если зашли за границы (МИНУС)
    if report_position > 9:
        reports_kb.add(query_kb.keyboard_history_report_button_up)
    for i in Test.reports[report_position:]:
        reports_kb.add(InlineKeyboardButton(text=f"{i}", callback_data=f"url=bebra_report_{i}"))
        if current_position >= 10:
            break
        current_position += 1
    if len(Test.reports) > 10:
        reports_kb.add(query_kb.keyboard_history_report_button_down)
    await message.answer("История запросов", reply_markup=reports_kb)


async def check_ban(message: types.Message):
    if Test.UserTest.status == "banned":
        import main
        await main.start(message)


