from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_main_menu = InlineKeyboardMarkup()
keyboard_main_menu.add(InlineKeyboardButton(text="Назад", callback_data="main_menu"),)

keyboard_manager_and_admin_pa = InlineKeyboardMarkup()
keyboard_manager_and_admin_pa.add(InlineKeyboardButton(text="Назад", callback_data="manager_pa"),)

keyboard_agreement = InlineKeyboardMarkup()
keyboard_agreement.add(InlineKeyboardButton(text="Принять пользовательское соглашение", callback_data="accept_agreement"),)

keyboard_history_report = InlineKeyboardMarkup()
keyboard_history_report_button_up = InlineKeyboardButton(text="Вверх", callback_data="history_up")
keyboard_history_report_button_down = InlineKeyboardButton(text="Вниз", callback_data="history_down")

# Просмотр отчета
keyboard_watch_report = InlineKeyboardMarkup()
watch_report_button_1 = InlineKeyboardButton(text="Добавить в избранное", callback_data="add_favourite")
watch_report_button_2 = InlineKeyboardButton(text="Удалить", callback_data="delete_history_favourite")
watch_report_button_3 = InlineKeyboardButton(text="Просмотр", callback_data="watch")
keyboard_watch_report.add(watch_report_button_1)
keyboard_watch_report.add(watch_report_button_2, watch_report_button_3)

keyboard_favourite_report = InlineKeyboardMarkup()
keyboard_favourite_report_button_up = InlineKeyboardButton(text="Вверх", callback_data="favourite_up")
keyboard_favourite_report_button_down = InlineKeyboardButton(text="Вниз", callback_data="favourite_down")




