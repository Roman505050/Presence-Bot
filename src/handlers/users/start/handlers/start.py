from aiogram import Bot
from aiogram.types import Message

from src.utils.unitofwork import IUnitOfWork, UnitOfWork
from src.services.students import StudentsService
from src.services.invites import InvitesService
from src.schemas.students import StudentsSchema, StudentsTelegramInfoSchema


async def start(
        message: Message,
        bot: Bot,
        middleware_data: StudentsSchema,
        uow: IUnitOfWork = UnitOfWork()
        ):
    if len(message.text) == 6:
        return await message.answer('Данний бот призначений для закритого кола користувачів. Якщо ви отримали запрошення, введіть code-запрошення в форматі /start [code-запрошення]')
    message_code = message.text.split(' ')[1]
    if middleware_data:
        return await message.answer(
            'Ай-ай-ай, і тобі не стидно? Ти вже зареєстрований в системі!\n'
        )
    if not await InvitesService().is_valid_code(uow=uow, code=message_code):
        return await message.answer('Ви ввели невірний code-запрошення')
    profile_photos = await bot.get_user_profile_photos(user_id=message.from_user.id)
    if not profile_photos.photos:
        photo_id = None
    else:
        photo_id = profile_photos.photos[0][-1].file_id
    student = await StudentsService().add_student(
        uow=uow, 
        telegram_data=StudentsTelegramInfoSchema(
            username=message.from_user.username,
            photo_id=photo_id,
            telegram_id=message.from_user.id
        ), 
        code=message_code
    )
    return await message.answer(
        f'{student.first_name},\n' \
        'Ви успішно зареєструвались в системі!\n' \
        'Використовуйте команду /profile (скажу чесно, команда не працює.. Я перевіряв) для перегляду профілю'
    )