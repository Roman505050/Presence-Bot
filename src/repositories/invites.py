from src.utils.repository import SQLAlchemyRepository
from src.database.models import Invites

class InvitesRepository(SQLAlchemyRepository):
    model = Invites