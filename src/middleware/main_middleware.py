from aiogram import BaseMiddleware, Bot, exceptions
from aiogram.types import TelegramObject
from typing import Any, Awaitable, Callable, Dict

from src.services.students import StudentsService
from src.utils.unitofwork import UnitOfWork, IUnitOfWork

import logging

class MainMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
            event: TelegramObject,
            data: Dict[str, Any],
            ) -> Any:
        if event.message is not None:
            uow: IUnitOfWork = UnitOfWork()
            student = await StudentsService().get_student_for_middlewares(uow, event.message.from_user.id)
            data['middleware_data'] = student
            return await handler(event, data)
        if event.callback_query is not None:
            uow: IUnitOfWork = UnitOfWork()
            student = await StudentsService().get_student_for_middlewares(uow, event.callback_query.from_user.id)
            data['middleware_data'] = student
            return await handler(event, data)
        return logging.error('Unknown event type')