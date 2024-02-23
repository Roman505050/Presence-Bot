from aiogram import Router

from src.handlers.users.start.router import router as start_router


router = Router()
router.include_router(start_router)