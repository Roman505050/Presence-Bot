from aiogram import Router, F

from src.utils.states import AddInvites
from .handlers.add_invite import (
    add_invite, 
    last_name, 
    first_name, 
    patronymic_name, 
    group_id,
    stop_adding_invite,
    not_text_message
)

router = Router()

# Start adding invite
router.message.register(add_invite, F.text == '/add_invite') 

# Adding invite - states
router.message.register(last_name, AddInvites.last_name, F.text)
router.message.register(first_name, AddInvites.first_name, F.text)
router.message.register(patronymic_name, AddInvites.patronymic_name, F.text)
router.message.register(group_id, AddInvites.group_id, F.text)

# Stop adding invite
router.message.register(stop_adding_invite, F.text == '/stop_add_invite') 

# Processing non-text messages
router.message.register(not_text_message, ~F.text) 