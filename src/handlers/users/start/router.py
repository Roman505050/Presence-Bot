from aiogram import Router, F 

from src.handlers.users.start.handlers.start import start

router = Router()


router.message.register(start, F.text.startswith('/start'))