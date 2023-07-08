from aiogram import types

# Главное меню
keyboard_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mm_button_1 = types.KeyboardButton(text="Личный кабинет")
mm_button_2 = types.KeyboardButton(text="Начать анализ")
mm_button_3 = types.KeyboardButton(text="Избранное")
mm_button_4 = types.KeyboardButton(text="История")
keyboard_main_menu.add(mm_button_1, mm_button_2)
keyboard_main_menu.add(mm_button_3, mm_button_4)

# Главное меню админа и менеджера
keyboard_main_menu_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
mm_admin_button_1 = types.KeyboardButton(text="Личный кабинет")
mm_admin_button_2 = types.KeyboardButton(text="Начать анализ")
mm_admin_button_3 = types.KeyboardButton(text="Избранное")
mm_admin_button_4 = types.KeyboardButton(text="История")
mm_admin_button_5 = types.KeyboardButton(text="Администрирование")
keyboard_main_menu_admin.add(mm_admin_button_1, mm_admin_button_2)
keyboard_main_menu_admin.add(mm_admin_button_4, mm_admin_button_3)
keyboard_main_menu_admin.add(mm_admin_button_5)

# Личный кабинет пользователя
keyboard_user_pa = types.ReplyKeyboardMarkup(resize_keyboard=True)
pa_user_button_1 = types.KeyboardButton(text="Баланс токенов")
pa_user_button_2 = types.KeyboardButton(text="Пользовательское соглашение")
# pa_user_button_3 = types.KeyboardButton(text="Назад")
pa_user_button_4 = types.KeyboardButton(text="Помощь")
keyboard_user_pa.add(pa_user_button_1, pa_user_button_2)
keyboard_user_pa.add(pa_user_button_4)

# Админ-панель
keyboard_admin_panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel_button_1 = types.KeyboardButton(text="Просмотр новых пользователей")
admin_panel_button_2 = types.KeyboardButton(text="Просмотр активности")
# pa_manager_button_3 = types.KeyboardButton(text="Назад")
admin_panel_button_4 = types.KeyboardButton(text="Выбрать пользователя")
keyboard_admin_panel.add(admin_panel_button_1, admin_panel_button_2)
keyboard_admin_panel.add(admin_panel_button_4)

# Выбрать пользователя менеджер
keyboard_select_user_manager = types.ReplyKeyboardMarkup(resize_keyboard=True)
favourites_button_1 = types.KeyboardButton(text="Изменить количество токенов")
favourites_button_2 = types.KeyboardButton(text="Информация о пользователе")
favourites_button_3 = types.KeyboardButton(text="Забанить/Разбанить")
keyboard_select_user_manager.add(favourites_button_1, favourites_button_2)
keyboard_select_user_manager.add(favourites_button_3)

# Выбрать пользователя Админ
keyboard_select_user_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
select_user_admin_button_1 = types.KeyboardButton(text="Изменить количество токенов")
select_user_admin_button_2 = types.KeyboardButton(text="Информация о пользователе")
select_user_admin_button_3 = types.KeyboardButton(text="Забанить")
select_user_admin_button_4 = types.KeyboardButton(text="Поменять роль")
keyboard_select_user_admin.add(select_user_admin_button_1, select_user_admin_button_2)
keyboard_select_user_admin.add(select_user_admin_button_3, select_user_admin_button_4)

# История
keyboard_history = types.ReplyKeyboardMarkup(resize_keyboard=True)
# history_button_1 = types.KeyboardButton(text="Вверх")
# history_button_2 = types.KeyboardButton(text="Вниз")
# history_button_3 = types.KeyboardButton(text="Выбрать отчет")
# history_button_4 = types.KeyboardButton(text="Назад")
history_button_5 = types.KeyboardButton(text="Очистить историю")
# keyboard_history.add(history_button_1, history_button_2)
keyboard_history.add(history_button_5)

# Избранное
# keyboard_favourites = types.ReplyKeyboardMarkup(resize_keyboard=True)
# favourites_button_1 = types.KeyboardButton(text="Вверх")
# favourites_button_2 = types.KeyboardButton(text="Вниз")
# favourites_button_3 = types.KeyboardButton(text="Выбрать отчет")
# keyboard_favourites.add(favourites_button_1, favourites_button_2)
# keyboard_favourites.add(favourites_button_3)

# Выбрать отчет
keyboard_watch_report = types.ReplyKeyboardMarkup(resize_keyboard=True)
watch_report_button_1 = types.KeyboardButton(text="Добавить в избранное")
watch_report_button_2 = types.KeyboardButton(text="Удалить")
watch_report_button_3 = types.KeyboardButton(text="Просмотр")
keyboard_watch_report.add(watch_report_button_1)
keyboard_watch_report.add(watch_report_button_2, watch_report_button_3)

# Пользовательское соглашение
keyboard_agreement = types.ReplyKeyboardMarkup(resize_keyboard=True)
agreement_button = types.KeyboardButton(text="Принять пользовательское соглашение")
keyboard_agreement.add(agreement_button)

# Отмена
keyboard_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_button = types.KeyboardButton(text="Отмена")
keyboard_cancel.add(cancel_button)

# Поменять роль
keyboard_change_role = types.ReplyKeyboardMarkup(resize_keyboard=True)
change_role_button_1 = types.KeyboardButton(text="Сделать пользователем")
change_role_button_2 = types.KeyboardButton(text="Сделать менеджером")
keyboard_change_role.add(change_role_button_1, change_role_button_2)

# Начать анализ
keyboard_start_analyze = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_analyze_button_1 = types.KeyboardButton(text="Выбрать из списка категорий")
start_analyze_button_2 = types.KeyboardButton(text="Выбрать из списка товаров")
keyboard_start_analyze.add(change_role_button_1, change_role_button_2)
