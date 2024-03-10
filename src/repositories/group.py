from src.utils.repository import SQLAlchemyRepository
from src.database.models import Groups

from sqlalchemy import select
from sqlalchemy.orm import joinedload

class GroupsRepository(SQLAlchemyRepository):
    model = Groups

    async def get_one(self, **filter_by):
        stmt = (
            select(self.model)
            .options(
                joinedload(Groups.students)
            )
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        return res.scalars().first()