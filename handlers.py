import aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import State, StatesGroup


import config
import kb
import query_kb
import utils
import Test


class Form(StatesGroup):
    username = State()
    banned = State()
    started = State()
    change_token = State()
    product = State()


async def main_menu(message: types.Message):
    keyboard = kb.keyboard_main_menu
    if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
        await main_menu_with_admin_panel(message)
    else:
        await message.answer("Вы вошли в главное меню", reply_markup=keyboard)


async def personal_account(message: types.Message):
    # await message.answer(f"Вы вошли в личный кабинет {message.from_user.username}")
    # if Test.UserTest.role == "admin":
    #    await admin_panel_admin(message)
    # elif Test.UserTest.role == "manager":
    #    await admin_panel_manager(message)
    # else:
    await personal_account_user(message)


async def personal_account_user(message: types.Message):
    keyboard = kb.keyboard_user_pa
    await message.answer(text="Вы вошли в личный кабинет обычного пользователя", reply_markup=keyboard)
    await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)


async def main_menu_with_admin_panel(message: types.Message):
    keyboard = kb.keyboard_main_menu_admin
    await message.answer(text="Вы вошли в главное меню с админкой", reply_markup=keyboard)


async def admin_panel(message: types.Message):
    if Test.UserTest.role == "admin":
        await admin_panel_admin(message)
    elif Test.UserTest.role == "manager":
        await admin_panel_manager(message)


async def admin_panel_manager(message: types.Message):
    keyboard = kb.keyboard_manager_pa
    await message.answer("Вы вошли в личный кабинет менеджера", reply_markup=keyboard)
    await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)


async def admin_panel_admin(message: types.Message):
    keyboard = kb.keyboard_admin_pa
    await message.answer("Вы вошли в личный кабинет админа", reply_markup=keyboard)
    await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)


async def personal_history(message: types.Message):
    keyboard = kb.keyboard_history
    await message.answer("Вы вошли в историю запросов", reply_markup=keyboard)
    # TODO СДЕЛАТЬ ЗАПРОС СПИСКА ИЗБРАННОГО
    await utils.show_reports(message, "history", reports=Test.reports)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


async def personal_history_clear(message: types.Message):
    Test.reports.clear()
    keyboard = kb.keyboard_history
    await message.answer("История очищена", reply_markup=keyboard)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


async def select_user(message: types.Message):
    await Form.username.set()
    await message.answer("Введите @username пользователя:", reply_markup=query_kb.keyboard_manager_and_admin_pa)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return
    # Cancel state and inform user about it
    await state.finish()
    await message.reply('Cancelled.')


async def process_name(message: types.Message, state: FSMContext):
    for u in Test.Users:
        if u.username == message.text:
            User = u
            await state.finish()

    if Test.UserTest.role == "admin":
        keyboard = kb.keyboard_select_user_admin
    elif Test.UserTest.role == "manager":
        keyboard = kb.keyboard_select_user_manager
    else:
        await message.answer("У вас нету доступа к данной команде")
        return
    await message.reply(f"Вы выбрали пользователя {User.username}, что хотите сделать?", reply_markup=keyboard)


async def user_information(message: types.Message):
    await message.answer(f"Имя - {Test.UserTest.username}\n"
                         f"Количество токенов - {Test.UserTest.token_count}\n"
                         f"Роль - {Test.UserTest.role}", reply_markup=query_kb.keyboard_main_menu)


async def personal_favourites(message: types.Message):
    # TODO СДЕЛАТЬ КАК В ИСТОРИИ
    await message.answer("Вы вошли в избранные отчеты")
    await utils.show_reports(message, "favourites", reports=Test.favourite_reports)
    await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)


# ПОКАЗЫВАЕТ ТЕКУЩИЙ БАЛАНС ТОКЕНОВ
async def personal_balance(message: types.Message):
    await message.answer(text=f"Количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}", reply_markup=query_kb.keyboard_main_menu)


# ПОМЕНЯТЬ КОЛ-ВО ТОКЕНОВ
async def personal_change_token(message: types.Message):
    await Form.change_token.set()
    await message.answer(text=f"Количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}\n"
                              f"введите новое значение:",
                         reply_markup=query_kb.keyboard_main_menu)


async def process_change_token(message: types.Message, state: FSMContext):
    # TODO ПРОВЕРКА НА INT ЕСЛИ НЕТ ОШИБКА
    await state.finish()
    Test.UserTest.token_count = message.text
    await message.answer(text=f"Новое количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}",
                         reply_markup=query_kb.keyboard_main_menu)


# ПОМЕНЯТЬ РОЛЬ
async def personal_change_role(message: types.Message):
    await message.answer(text=f"Пользователь: {Test.UserTest.username} \n Роль: {Test.UserTest.role}", reply_markup=kb.keyboard_change_role)


# МЕНЯЕТСЯ РОЛЬ НА ПОЛЬЗОВАТЕЛЯ
async def personal_change_role_user(message: types.Message):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    if Test.UserTest.role == Test.role[0]:
        await message.answer(text="У пользователя уже имеется такая роль")
    else:
        await message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                             reply_markup=query_kb.keyboard_main_menu)


# МЕНЯЕТСЯ РОЛЬ НА МЕНЕДЖЕРА
async def personal_change_role_manager(message: types.Message):
    # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
    await message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}",
                         reply_markup=query_kb.keyboard_main_menu)


async def personal_am_ban(message: types.Message):
    # TODO ДОДЕЛАТЬ КОГДА СКИНУТ
    Test.UserTest.status = "banned"
    await Form.banned.set()
    await message.answer(text=f"Пользователь {Test.UserTest.username} забанен", reply_markup=query_kb.keyboard_main_menu)


async def analyze_start(message: types.Message):
    await Form.product.set()
    await message.answer(text=f"Введите наименование продукта", reply_markup=query_kb.keyboard_main_menu)


async def analyze_process_product(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=f"Вы ввели продукт: {message.text}", reply_markup=query_kb.keyboard_main_menu)


async def analyze_cansel(message: types.Message):
    await main_menu(message)


async def personal_agreement(message: types.Message):
    await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_main_menu)


async def personal_help(message: types.Message):
    await message.answer(text=config.help_user, reply_markup=query_kb.keyboard_main_menu)


def register_handlers(dp: Dispatcher):
    # dp.register_message_handler(start_message, content_types=types.ContentType.TEXT, regexp='.*')
    # dp.register_message_handler(agreement_message, content_types=types.ContentType.TEXT, regexp='.*')
    # dp.register_message_handler(process_name, state=Form.banned)
    # dp.register_message_handler(accept_agreement, text="accept_agreement")

    dp.register_message_handler(main_menu, commands=['mm'])
    dp.register_message_handler(main_menu_with_admin_panel, commands=['puma'])
    dp.register_message_handler(personal_account, text='Личный кабинет')
    dp.register_message_handler(admin_panel, text='Администрирование')
    dp.register_message_handler(personal_account_user, commands=['pau'])
    dp.register_message_handler(admin_panel_manager, commands=['pam'])
    dp.register_message_handler(admin_panel_admin, commands=['paa'])
    dp.register_message_handler(select_user, text="Выбрать пользователя")
    dp.register_message_handler(cancel_handler, commands=['cancel'])
    dp.register_message_handler(process_name, state=Form.username)
    dp.register_message_handler(user_information, text="Информация о пользователе")
    dp.register_message_handler(personal_history, text="История")
    dp.register_message_handler(personal_history_clear, text="Очистить историю")
    dp.register_message_handler(personal_favourites, text="Избранное")
    dp.register_message_handler(personal_balance, text="Баланс токенов")
    dp.register_message_handler(personal_agreement, text="Пользовательское соглашение")
    dp.register_message_handler(personal_help, text="Помощь")
    dp.register_message_handler(personal_change_token, text="Изменить количество токенов")
    dp.register_message_handler(process_change_token, state=Form.change_token)
    dp.register_message_handler(personal_change_role, text="Поменять роль")
    dp.register_message_handler(personal_change_role_user, text="Сделать пользователем")
    dp.register_message_handler(personal_change_role_manager, text="Сделать менеджером")
    dp.register_message_handler(personal_am_ban, text="Забанить")
    dp.register_message_handler(analyze_start, text="Начать анализ")
    dp.register_message_handler(analyze_process_product, state=Form.product)
    dp.register_message_handler(analyze_cansel, text="Отмена")

