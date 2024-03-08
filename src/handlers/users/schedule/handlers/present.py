from aiogram.types import CallbackQuery

import pytz
import datetime

from src.database.models import Register
from src.utils.unitofwork import UnitOfWork, IUnitOfWork
from src.schemas.students import StudentsSchema

from src.config import settings

async def present(
        call: CallbackQuery,
        middleware_data: StudentsSchema,
        uow: IUnitOfWork = UnitOfWork(),
    ):
    if middleware_data is None:
        return await call.answer('Forbidden', show_alert=True)
    register_id = int(call.data.split(':')[-1])
    async with uow:
        register: Register = await uow.registers.get_one(id=register_id)
        if register is None:
            return await call.answer('Щось пішло не так', show_alert=True)
        if register.student_id != middleware_data.id:
            return await call.answer('Forbidden', show_alert=True)
        if register.presence:
            return await call.answer(f'Ви вже відмітилися. Status: {register.presence}', show_alert=True)
        UTC_NOW = datetime.datetime.utcnow()
        KIEV_NOW = UTC_NOW.astimezone(pytz.timezone(settings.TIMEZONE))
        if KIEV_NOW - register.created_at > datetime.timedelta(hours=2):
            return await call.answer('Час відмітки вийшов', show_alert=True)
        register.presence = True
        await uow.commit()
        return await call.answer('Ви відмітилися', show_alert=True)