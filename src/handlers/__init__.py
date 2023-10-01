from aiogram import Dispatcher

from config import Form
from src.handlers import handlers, query_handlers, analysis, admin_panel


def register_handlers(dp: Dispatcher):
    # dp.register_message_handler(start_message, content_types=types.ContentType.TEXT, regexp='.*')
    # dp.register_message_handler(agreement_message, content_types=types.ContentType.TEXT, regexp='.*')
    # dp.register_message_handler(process_name, state=Form.banned)
    # dp.register_message_handler(accept_agreement, text="accept_agreement")

    dp.register_message_handler(handlers.main_menu, commands=['mm'])
    dp.register_message_handler(handlers.main_menu_with_admin_panel, commands=['puma'])
    dp.register_message_handler(handlers.personal_account_start, text='Личный кабинет')
    dp.register_message_handler(handlers.personal_account, commands=['pau'])
    dp.register_message_handler(handlers.personal_history, text="История")
    dp.register_message_handler(handlers.personal_history_clear, text="Очистить историю")
    dp.register_message_handler(handlers.personal_bookmarks, text="Избранное")
    dp.register_message_handler(handlers.personal_balance, text="Баланс токенов")
    dp.register_message_handler(handlers.personal_agreement, text="Пользовательское соглашение")
    dp.register_message_handler(handlers.personal_help, text="Помощь")
    # dp.register_message_handler(personal_change_role_user, text="Сделать пользователем")
    # dp.register_message_handler(personal_change_role_manager, text="Сделать менеджером")
    dp.register_message_handler(handlers.analyze_start, text="Начать анализ")
    dp.register_message_handler(handlers.analyze_process_product, state=Form.product)

    dp.register_message_handler(admin_panel.admin_panel, text='Администрирование')

    dp.register_message_handler(admin_panel.process_name, state=Form.username)
    dp.register_message_handler(admin_panel.user_information, text="Информация о пользователе")

    dp.register_message_handler(admin_panel.personal_change_token, text="Изменить количество токенов")
    dp.register_message_handler(admin_panel.process_change_token, state=Form.change_token)
    dp.register_message_handler(admin_panel.personal_change_role, text="Поменять роль")
    dp.register_message_handler(admin_panel.personal_am_ban, text="Забанить")


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(query_handlers.main_menu_callback, text="main_menu")
    dp.register_callback_query_handler(query_handlers.admin_panel_callback, text="admin_panel")
    dp.register_callback_query_handler(query_handlers.history_report, lambda c: c.data.startswith("url="))

    dp.register_callback_query_handler(admin_panel.select_new_users, text="select_new_users")
    dp.register_callback_query_handler(admin_panel.select_users_activity, text="select_users_activity")
    dp.register_callback_query_handler(admin_panel.select_user, text="select_user")

    dp.register_callback_query_handler(query_handlers.history_up_callback, text="history_up")
    dp.register_callback_query_handler(query_handlers.history_down_callback, text="history_down")
    dp.register_callback_query_handler(query_handlers.favourites_up_callback, text="favourite_up")
    dp.register_callback_query_handler(query_handlers.favourites_down_callback, text="favourite_down")
    dp.register_callback_query_handler(query_handlers.product_up_callback, text="product_up")
    dp.register_callback_query_handler(query_handlers.product_down_callback, text="product_down")
    dp.register_callback_query_handler(query_handlers.cancel_product, state=Form.product)

    dp.register_callback_query_handler(admin_panel.personal_change_role_user, text="make_user")
    dp.register_callback_query_handler(admin_panel.personal_change_role_manager, text="make_manager")
    dp.register_callback_query_handler(admin_panel.cancel_change_token, state=Form.change_token)

    dp.register_callback_query_handler(query_handlers.add_favourite_callback, text="add_favourite")
    dp.register_callback_query_handler(query_handlers.delete_favourite_history_callback, text="delete_history_favourite")
    dp.register_callback_query_handler(query_handlers.report_analysis_type, text="watch")

    dp.register_callback_query_handler(analysis.analysis_type_1, text="analysis_type_1")
    dp.register_callback_query_handler(analysis.analysis_type_2, text="analysis_type_2")
    dp.register_callback_query_handler(analysis.analysis_type_3, text="analysis_type_3")
    dp.register_callback_query_handler(analysis.analysis_type_4, text="analysis_type_4")
