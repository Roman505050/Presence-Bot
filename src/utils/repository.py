from abc import ABC, abstractmethod
from typing import Any, Sequence

from sqlalchemy import insert, select, update, delete, func, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession



class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        return NotImplemented
    
    @abstractmethod
    async def get_one():
        return NotImplemented
    
    @abstractmethod
    async def get_all():
        return NotImplemented
    
    @abstractmethod
    async def update_one():
        return NotImplemented
    
    @abstractmethod
    async def delete_one():
        return NotImplemented
    
    # @abstractmethod
    # async def count():
    #     return NotImplemented

class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(data).returning('*')
        res = await self.session.execute(stmt)
        return res.fetchone()
    
    async def update_one(self, data: dict, **filter_by):
        stmt = update(self.model).filter_by(**filter_by).values(**data).returning('*')
        res = await self.session.execute(stmt)
        return res.fetchone()

    async def get_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalars().first()
        if res is not None:
            return res
        return None
    
    async def get_all(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalars().all()
    
    async def delete_one(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)