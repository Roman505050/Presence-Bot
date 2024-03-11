from src.schemas.students import StudentsSchema
from src.database.enums import Role

async def admin_validate(middleware_data: StudentsSchema):
    if middleware_data is not None and middleware_data.role == Role.ADMIN:
        return True
    return False