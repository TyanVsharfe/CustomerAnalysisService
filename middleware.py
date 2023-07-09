from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

import Test
import config
from src.keyboards import query_kb


class BanMiddleware(BaseMiddleware):
    @staticmethod
    async def on_pre_process_message(msg: types.Message, data: dict):
        user = msg.from_user
        if Test.UserTest.status == "banned":
            # Бан пользователя
            await msg.reply("Вы забанены!")
            raise IgnoreException()


class AgreementMiddleware(BaseMiddleware):
    @staticmethod
    async def on_pre_process_message(msg: types.Message, data: dict):
        if (msg.text == "/start") & (not Test.UserTest.agreement):
            await msg.answer("Привет! Перед началом работы вы должны прочитать и принять пользовательское соглашение.",
                             reply_markup=types.ReplyKeyboardRemove())
            await msg.answer(text=config.terms_of_service, reply_markup=query_kb.keyboard_agreement)
            raise IgnoreException()
        elif (not Test.UserTest.agreement) & (Test.UserTest.registration is not None):
            await msg.answer("Для начала работы примите пользовательское соглашение")
            raise IgnoreException()
        else:
            await msg.answer("Для начала работы введи команду /start")
            raise IgnoreException()


class IgnoreException(Exception):
    pass
