from src.utils.unitofwork import IUnitOfWork
from src.schemas.students import StudentsTelegramInfoSchema, StudentsCreateSchema

from src.services.invites import InvitesService

class StudentsService:
    async def add_student(self, uow: IUnitOfWork, telegram_data: StudentsTelegramInfoSchema, code: str) -> bool:
        async with uow:
            data = await uow.invites.get_one(code=code)
            if data is None:
                return False
            await uow.students.add_one(
                StudentsCreateSchema(
                    **telegram_data.model_dump(),
                    first_name = data.first_name,
                    last_name = data.last_name,
                    patronymic_name = data.patronymic_name,
                    group_id = data.group_id
                ).model_dump()
            )
            await uow.invites.delete_one(code=code)
            await uow.commit()
            return True