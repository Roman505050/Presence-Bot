from pydantic import BaseModel


class StudentsTelegramInfoSchema(BaseModel):
    username: str
    photo_id: str | None
    telegram_id: int

class StudentsCreateSchema(StudentsTelegramInfoSchema):
    first_name: str
    last_name: str
    patronymic_name: str
    group_id: int | None