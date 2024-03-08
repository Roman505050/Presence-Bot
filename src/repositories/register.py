from src.database.models import Register
from src.utils.repository import SQLAlchemyRepository

class RegisterRepository(SQLAlchemyRepository):
    model = Register

    async def get_one(self, **filter_by) -> Register | None:
        return await super().get_one(**filter_by)