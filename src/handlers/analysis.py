from aiogram.types import CallbackQuery

from src.keyboards import query_kb

# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ


# АНАЛИЗ 1
async def analysis_type_1(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Анализ 1", reply_markup=query_kb.keyboard_aa)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# АНАЛИЗ 2
async def analysis_type_2(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Анализ 2", reply_markup=query_kb.keyboard_aa)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# АНАЛИЗ 3
async def analysis_type_3(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Анализ 3", reply_markup=query_kb.keyboard_aa)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# АНАЛИЗ 4
async def analysis_type_4(call: CallbackQuery):
    url = call.data[4:]  # Извлекаем часть строки после "url="
    await call.message.answer(f"Анализ 4", reply_markup=query_kb.keyboard_aa)
    # await call.message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)
