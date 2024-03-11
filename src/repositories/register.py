from src.database.models import Register, Schedule
from src.utils.repository import SQLAlchemyRepository

import datetime
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class RegisterRepository(SQLAlchemyRepository):
    model = Register

    async def get(self, couple: int, student_id: int, date: datetime.date) -> Register | None:
        stmt = (
            select(self.model)
            .options(joinedload(self.model.schedule))
            .join(Schedule)
            .where(
                Schedule.id == self.model.schedule_id,
            )
            .where(
                Schedule.couple == couple,
                self.model.student_id == student_id,
                self.model.date == date
            )
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()