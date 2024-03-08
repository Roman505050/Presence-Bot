from aiogram import Router

from .start.router import router as start_router
from .schedule.router import router as schedule_router


router = Router()
router.include_router(start_router)
router.include_router(schedule_router)