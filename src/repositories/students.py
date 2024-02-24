from src.utils.repository import SQLAlchemyRepository
from src.database.models.students import Students
from src.database.models.groups import Groups
from src.database.models.students_groups_association import students_groups_association_table

from sqlalchemy import select, insert

class StudentsRepository(SQLAlchemyRepository):
    model = Students

    async def add_one_student(self, data: dict, group_id: int):
        stmt = (
            insert(self.model)
            .values(data)
            .returning('*')
        )
        res = await self.session.execute(stmt)
        student = res.fetchone()
        stmt = (
            select(Groups)
            .where(Groups.id == group_id)
        )
        res = await self.session.execute(stmt)
        group = res.scalars().first()
        if group is not None:
            await self.session.execute(
                students_groups_association_table.insert().values(
                    students_id = student.id,
                    groups_id = group.id
                )
            )
        return student