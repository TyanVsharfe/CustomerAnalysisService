from aiogram.dispatcher.filters.state import StatesGroup, State

BOT_TOKEN = '6145336505:AAHq7rZAY4s2Igii_zcBZZ8l09feRKuUl64'

HISTORY = "history"
FAVOURITES = "favourites"

terms_of_service = "Пункты пользовательского соглашения\n" \
                   "1. Разрешаю использование публичных данных аккаунта\n" \
                   "2. Пользователь не будет использовать данного бота в коммерческих целях"

help_user = "1.Как начать работу?\n" \
            "Чтобы начать анализ выберите пункт \"начать анализ\", после введите название продукта, выберите еще че нить кароче"


class Form(StatesGroup):
    username = State()
    banned = State()
    started = State()
    change_token = State()
    product = State()
