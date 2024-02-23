from src.utils.repository import SQLAlchemyRepository
from src.database.models import Students

class StudentsRepository(SQLAlchemyRepository):
    model = Students