from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# НАЗАД В ГЛАВНОЕ МЕНЮ
keyboard_main_menu = InlineKeyboardMarkup()
keyboard_main_menu.add(InlineKeyboardButton(text="Назад", callback_data="main_menu"),)

keyboard_admin_panel = InlineKeyboardMarkup()
keyboard_admin_panel.add(InlineKeyboardButton(text="Назад", callback_data="admin_panel"),)

keyboard_agreement = InlineKeyboardMarkup()
keyboard_agreement.add(InlineKeyboardButton(text="Принять пользовательское соглашение",
                                            callback_data="accept_agreement"))

# ДЛЯ ПРОСМОТРА СПИСКА ОТЧЕТОВ ИЗБРАННОЕ (НЕ КЛАВИАТУРА, ИСПОЛЬЗУЮТСЯ ТОЛЬКО КНОПКИ)
keyboard_history_report = InlineKeyboardMarkup()
keyboard_history_report_button_up = InlineKeyboardButton(text="Вверх", callback_data="history_up")
keyboard_history_report_button_down = InlineKeyboardButton(text="Вниз", callback_data="history_down")

# ДЛЯ ПРОСМОТРА СПИСКА ОТЧЕТОВ ИСТОРИЯ (НЕ КЛАВИАТУРА, ИСПОЛЬЗУЮТСЯ ТОЛЬКО КНОПКИ)
keyboard_favourite_report = InlineKeyboardMarkup()
keyboard_favourite_report_button_up = InlineKeyboardButton(text="Вверх", callback_data="favourite_up")
keyboard_favourite_report_button_down = InlineKeyboardButton(text="Вниз", callback_data="favourite_down")

# ДЛЯ ПРОСМОТРА СПИСКА ПРОДУКТОВ (НЕ КЛАВИАТУРА, ИСПОЛЬЗУЮТСЯ ТОЛЬКО КНОПКИ)
keyboard_products = InlineKeyboardMarkup()
products_button_up = InlineKeyboardButton(text="Вверх", callback_data="product_up")
products_button_down = InlineKeyboardButton(text="Вниз", callback_data="product_down")

# Просмотр отчета
# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
keyboard_watch_report = InlineKeyboardMarkup()
watch_report_button_1 = InlineKeyboardButton(text="Добавить в избранное", callback_data="add_favourite")
watch_report_button_2 = InlineKeyboardButton(text="Удалить", callback_data="delete_history_favourite")
watch_report_button_3 = InlineKeyboardButton(text="Просмотр", callback_data="watch")
keyboard_watch_report.add(watch_report_button_1)
keyboard_watch_report.add(watch_report_button_2, watch_report_button_3)

# Поменять роль
keyboard_change_role = InlineKeyboardMarkup()
change_role_button_1 = InlineKeyboardButton(text="Сделать пользователем", callback_data="make_user")
change_role_button_2 = InlineKeyboardButton(text="Сделать менеджером", callback_data="make_manager")
keyboard_change_role.add(change_role_button_1, change_role_button_2)

# Поменять роль
keyboard_cancel_change_role = InlineKeyboardMarkup()
cancel_role_button_1 = InlineKeyboardButton(text="Отмена", callback_data="cancel_change_token")
keyboard_cancel_change_role.add(cancel_role_button_1)

# Поменять роль
keyboard_cancel_product = InlineKeyboardMarkup()
cancel_product_button_1 = InlineKeyboardButton(text="Отмена", callback_data="cancel_product")
keyboard_cancel_product.add(cancel_product_button_1)

# Выбрать тип анализа
# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
keyboard_analysis_type = InlineKeyboardMarkup()
analysis_type_button_1 = InlineKeyboardButton(text="Анализ 1", callback_data="analysis_type_1")
analysis_type_button_2 = InlineKeyboardButton(text="Анализ 2", callback_data="analysis_type_2")
analysis_type_button_3 = InlineKeyboardButton(text="Анализ 3", callback_data="analysis_type_3")
analysis_type_button_4 = InlineKeyboardButton(text="Анализ 4", callback_data="analysis_type_4")
keyboard_analysis_type.add(analysis_type_button_1, analysis_type_button_2)
keyboard_analysis_type.add(analysis_type_button_3, analysis_type_button_4)

# Интерактив с анализом
# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
keyboard_aa = InlineKeyboardMarkup()
aa_button_1 = InlineKeyboardButton(text="Открыть на сайте", callback_data="open_site")
aa_button_2 = InlineKeyboardButton(text="Добавить в избранное", callback_data="add_fvrt")
aa_button_3 = InlineKeyboardButton(text="Назад", callback_data="back_analysis")
keyboard_aa.add(aa_button_1)
keyboard_aa.add(aa_button_2)
keyboard_aa.add(aa_button_3)

# АДМИН-ПАНЕЛЬ
keyboard_admin_panel = InlineKeyboardMarkup()
admin_panel_button_1 = InlineKeyboardButton(text="Просмотр новых пользователей", callback_data="33")
admin_panel_button_2 = InlineKeyboardButton(text="Просмотр активности", callback_data="22")
admin_panel_button_4 = InlineKeyboardButton(text="Выбрать пользователя", callback_data="12")
keyboard_admin_panel.add(admin_panel_button_1, admin_panel_button_2)
keyboard_admin_panel.add(admin_panel_button_4)


