from aiogram.fsm.state import StatesGroup, State

class AddInvites(StatesGroup):
    last_name = State()
    first_name = State()
    patronymic_name = State()
    group_id = State()