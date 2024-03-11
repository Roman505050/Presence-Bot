from aiogram import Bot, Dispatcher

from src.config import settings
from src.handlers.default import start_bot, stop_bot
from src.handlers.users.router import router as users_router
from src.handlers.admin.router import router as admin_router

from src.middleware.main_middleware import MainMiddleware

async def start():
    bot = Bot(token=settings.TELEGRAM_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.update.middleware.register(MainMiddleware())

    dp.include_router(users_router)
    dp.include_router(admin_router)

    dp.shutdown.register(stop_bot)
    await dp.start_polling(bot)
