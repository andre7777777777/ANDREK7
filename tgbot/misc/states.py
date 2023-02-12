from aiogram.dispatcher.filters.state import State, StatesGroup


class Mailing(StatesGroup):
    mailing_message = State()

class blockUser(StatesGroup):
    user_id = State()

class UnblockUser(StatesGroup):
    user_id = State()
