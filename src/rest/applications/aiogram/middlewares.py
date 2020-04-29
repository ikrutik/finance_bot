from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from src.base.exception import NotAuthorizedUserException
from src.rest.settings import settings


class AuthMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_pre_process_update(self, update: types.Update, data: dict):

        if not self.__check_authorize(user_id=self.__get_user_id(update)):
            await update.bot.send_message(self.__get_chat_id(update), "Вы не авторизованы !")
            raise NotAuthorizedUserException()

        return True

    @classmethod
    def __get_user_id(cls, update: types.Update) -> str:
        """
        Get user`s id
        :param update:
        """
        if update.message:
            return update.message.from_user.id
        elif update.callback_query:
            return update.callback_query.from_user.id

        raise ValueError("Chat not found")

    @classmethod
    def __get_chat_id(cls, update: types.Update) -> str:
        """
        Get chat`s id
        :param update:
        """
        if update.message:
            return update.message.chat.id
        elif update.callback_query:
            return update.callback_query.message.chat.id

        raise ValueError("Chat not found")

    @classmethod
    def __check_authorize(cls, user_id: str) -> bool:
        return str(settings.TELEGRAM_USER_ID) == str(user_id)
