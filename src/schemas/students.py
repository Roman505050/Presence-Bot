from pydantic import BaseModel
import datetime

from src.database.enums import Role

class StudentsTelegramInfoSchema(BaseModel):
    username: str | None
    photo_id: str | None
    telegram_id: int

class StudentsCreateSchema(StudentsTelegramInfoSchema):
    first_name: str
    last_name: str
    patronymic_name: str
    group_id: int | None

class StudentsSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    patronymic_name: str
    username: str | None
    photo_id: str | None
    telegram_id: int
    role: Role
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime