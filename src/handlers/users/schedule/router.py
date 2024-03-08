from aiogram import Router, F

from .handlers.present import present

router = Router()

router.callback_query.register(present, F.data.startswith('present:'))