from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import uuid

from src.utils.states import AddInvites
from src.utils.unitofwork import IUnitOfWork, UnitOfWork
from .security import admin_validate


async def add_invite(message: Message, state: FSMContext, middleware_data):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    await message.answer("Чудово! Давайте розпочнемо створення запрошення.")
    await message.answer("Введіть прізвище")
    await state.set_state(AddInvites.last_name)
    return

async def last_name(message: Message, state: FSMContext, middleware_data):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    await state.update_data(last_name=message.text)
    await message.answer("Введіть ім'я")
    await state.set_state(AddInvites.first_name)
    return

async def first_name(message: Message, state: FSMContext, middleware_data):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    await state.update_data(first_name=message.text)
    await message.answer("Введіть по-батькові")
    await state.set_state(AddInvites.patronymic_name)
    return

async def patronymic_name(message: Message, state: FSMContext, middleware_data):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    await state.update_data(patronymic_name=message.text)
    await message.answer("Введіть id групи")
    await state.set_state(AddInvites.group_id)
    return

async def group_id(
        message: Message, 
        state: FSMContext,
        bot: Bot,
        middleware_data,
        uow: IUnitOfWork = UnitOfWork()
    ):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    try:
        group_id = int(message.text)
    except ValueError:
        await message.answer("Ви ввели невірний id групи")
        return
    async with uow:
        group = await uow.groups.get_one(id=group_id)
        if group is None:
            await message.answer("Групи з таким id не існує")
            return
        await state.update_data(group_id=group_id)
        data = await state.get_data()
        data["code"] = str(uuid.uuid4())
        invites = await uow.invites.add_one(data=data)
        bot_user = await bot.get_me()
        bot_name = bot_user.username
        await uow.commit()
        await message.answer(
            "Запрошення успішно створено!\n\n" \
            f"Прізвище: {invites.last_name}\n" \
            f"Ім'я: {invites.first_name}\n" \
            f"По-батькові: {invites.patronymic_name}\n" \
            f"Посилання для реєстрації: t.me/{bot_name}?start={invites.code}\n\n"
        )
        await state.clear()
        return

async def stop_adding_invite(message: Message, state: FSMContext, middleware_data):
    if not await admin_validate(middleware_data):
        return await message.answer("У вас немає доступу до цієї команди")
    await message.answer("Створення запрошення скасовано")
    await state.clear()
    return

async def not_text_message(message: Message):
    await message.answer("Ви ввели невірний формат даних")
    return