from src.utils.repository import SQLAlchemyRepository
from src.database.models.invites import Invites

class InvitesRepository(SQLAlchemyRepository):
    model = Invites