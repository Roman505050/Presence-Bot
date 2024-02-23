from src.utils.unitofwork import IUnitOfWork


class InvitesService:
    async def is_valid_code(self, uow: IUnitOfWork, code: str):
        async with uow:
            invite = await uow.invites.get_one(code=code)
            if invite is not None:
                return True
            return False
    
    async def delete_invite(self, uow: IUnitOfWork, code: str):
        async with uow:
            await uow.invites.delete_one(code=code)
    
    async def create_invite(self, uow: IUnitOfWork, data: dict):
        async with uow:
            ...