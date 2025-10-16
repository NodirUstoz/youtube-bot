from aiogram.fsm.state import State, StatesGroup


class BroadcastState(StatesGroup):
    text = State()
    photo = State()
    link = State()
    confirmation = State()
