from abc import ABC, abstractmethod
from typing import Type

from src.database.core import async_session_maker
from src.repositories.invites import InvitesRepository
from src.repositories.students import StudentsRepository
from src.repositories.schedule import ScheduleRepository
from src.repositories.register import RegisterRepository
from src.repositories.group import GroupsRepository

class IUnitOfWork(ABC):
    invites: Type[InvitesRepository]
    students: Type[StudentsRepository]
    schedules: Type[ScheduleRepository]
    registers: Type[RegisterRepository]
    groups: Type[GroupsRepository]

    @abstractmethod
    async def __init__(self):
        ...
    
    @abstractmethod
    async def __aenter__(self):
        ...
    
    @abstractmethod
    async def __aexit__(self, *args):
        ...
    
    @abstractmethod
    async def commit(self):
        ...
    
    @abstractmethod
    async def rollback(self):
        ...

class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker
    
    async def __aenter__(self):
        self.session = self.session_factory()

        self.invites = InvitesRepository(self.session)
        self.students = StudentsRepository(self.session)
        self.schedules = ScheduleRepository(self.session)
        self.registers = RegisterRepository(self.session)
        self.groups = GroupsRepository(self.session)
    
    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()
    
    async def commit(self):
        await self.session.commit()
    
    async def rollback(self):
        await self.session.rollback()