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


def register_handlers(dp: Dispatcher):
    @dp.message_handler(Command("mm"))
    async def main_menu(message: types.Message):
        keyboard = kb.keyboard_main_menu
        if (Test.UserTest.role == "admin") | (Test.UserTest.role == "manager"):
            await personal_account_user_with_admin_panel(message)
        else:
            await message.answer("Вы вошли в главное меню", reply_markup=keyboard)

    @dp.message_handler(Text("Личный кабинет"))
    async def personal_account(message: types.Message):
        await message.answer(f"Вы вошли в личный кабинет {message.from_user.username}")
        if Test.UserTest.role == "admin":
            await personal_account_admin(message)
        elif Test.UserTest.role == "manager":
            await personal_account_manager(message)
        else:
            await personal_account_user(message)

    @dp.message_handler(Command("pau"))
    async def personal_account_user(message: types.Message):
        keyboard = kb.keyboard_user_pa
        await message.answer(text="Вы вошли в личный кабинет обычного пользователя", reply_markup=keyboard)
        await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Command("puma"))
    async def personal_account_user_with_admin_panel(message: types.Message):
        keyboard = kb.keyboard_main_menu_admin
        await message.answer(text="Вы вошли в главное меню с админкой", reply_markup=keyboard)

    @dp.message_handler(Command("pam"))
    async def personal_account_manager(message: types.Message):
        keyboard = kb.keyboard_manager_pa
        await message.answer("Вы вошли в личный кабинет менеджера", reply_markup=keyboard)
        await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Command("paa"))
    async def personal_account_admin(message: types.Message):
        keyboard = kb.keyboard_admin_pa
        await message.answer("Вы вошли в личный кабинет админа", reply_markup=keyboard)
        await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Command("su"))
    async def select_user(message: types.Message):
        await Form.username.set()
        await message.answer("Введите @username пользователя:", reply_markup=query_kb.keyboard_manager_and_admin_pa)

    @dp.message_handler(state='*', commands=['cancel'])
    async def cancel_handler(message: types.Message, state: FSMContext):
        current_state = await state.get_state()
        if current_state is None:
            # User is not in any state, ignoring
            return
        # Cancel state and inform user about it
        await state.finish()
        await message.reply('Cancelled.')

    @dp.message_handler(state=Form.username)
    async def process_name(message: types.Message, state: FSMContext):
        await state.finish()
        if Test.UserTest.role == "admin":
            keyboard = kb.keyboard_select_user_manager
        elif Test.UserTest.role == "manager":
            keyboard = kb.keyboard_select_user_manager
        else:
            await message.answer("У вас нету доступа к данной команде")
            return
        await message.reply(f"Вы выбрали пользователя {message.text}, что хотите сделать?", reply_markup=keyboard)

    @dp.message_handler(Text("Информация о пользователе"))
    async def user_information(message: types.Message):
        await message.answer(f"Имя - {Test.UserTest.username}\n"
                             f"Количество токенов - {Test.UserTest.token_count}\n"
                             f"Роль - {Test.UserTest.role}", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("История"))
    async def personal_history(message: types.Message):
        keyboard = kb.keyboard_history
        await message.answer("Вы вошли в историю запросов", reply_markup=keyboard)
        await utils.show_reports(message)
        await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Очистить историю"))
    async def personal_history(message: types.Message):
        Test.reports.clear()
        keyboard = kb.keyboard_history
        await message.answer("История очищена", reply_markup=keyboard)
        await message.answer("Вернуться:", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Избранное"))
    async def personal_favourites(message: types.Message):
        # keyboard = kb.keyboard_favourites
        # TODO СДЕЛАТЬ КАК В ИСТОРИИ
        await message.answer("Вы вошли в избранные отчеты")
        await message.answer("*Текст*", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Баланс токенов"))
    async def personal_balance(message: types.Message):
        await message.answer(text=f"Количество токенов у пользователя {Test.UserTest.username}: {Test.UserTest.token_count}",
                             reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Пользовательское соглашение"))
    async def personal_agreement(message: types.Message):
        await message.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Помощь"))
    async def personal_help(message: types.Message):
        await message.answer(text=config.help_user, reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Поменять роль"))
    async def personal_change_role(message: types.Message):
        await message.answer(text=f"Пользователь: {Test.UserTest.username} \n Роль: {Test.UserTest.role}",
                             reply_markup=kb.keyboard_change_role)

    @dp.message_handler(Text("Сделать пользователем"))
    async def personal_change_role_user(message: types.Message):
        # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
        if Test.UserTest.role == Test.role[0]:
            await message.answer(text="У пользователя уже имеется такая роль")
        else:
            await message.answer(text=f"Пользователю {Test.UserTest.username} \n Выдана роль: {Test.UserTest.role}")
        await select_user(message)

    @dp.message_handler(Text("Сделать менеджером"))
    async def personal_change_role_manager(message: types.Message):
        # TODO СДЕЛАТЬ ФУНКЦИОНАЛ
        await message.answer(text=f"Пользователь: {Test.UserTest.username} \nРоль: {Test.UserTest.role}",
                             reply_markup=kb.keyboard_change_role)

    @dp.message_handler(Text("Забанить"))
    async def personal_am_ban(message: types.Message):
        # TODO ДОДЕЛАТЬ КОГДА СКИНУТЬ
        Test.UserTest.status = "banned"
        await message.answer(text=f"Пользователь {Test.UserTest.username} забанен", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Начать анализ"))
    async def analyze_start(message: types.Message):
        await message.answer(text=f"Введите наименование продукта", reply_markup=query_kb.keyboard_main_menu)

    @dp.message_handler(Text("Отмена"))
    async def analyze_cansel(message: types.Message):
        await main_menu(message)
