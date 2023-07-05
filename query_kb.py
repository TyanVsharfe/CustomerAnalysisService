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
keyboard_history_report.add()



