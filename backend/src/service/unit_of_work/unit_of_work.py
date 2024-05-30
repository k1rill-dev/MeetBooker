from abc import ABC, abstractmethod
from typing import Type

from src.db.db import async_session_maker
from src.repositories import UsersRepository, AppointmentRepository, ScheduleSlotsRepository, SpecialistRepository, \
    SpecialistRatingRepository


class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    appointments: Type[AppointmentRepository]
    schedule_slots: Type[ScheduleSlotsRepository]
    specialist: Type[SpecialistRepository]
    specialist_ratings: Type[SpecialistRatingRepository]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self._session = self.session_factory()
        self.users = UsersRepository(self._session)
        self.appointments = AppointmentRepository(self._session)
        self.schedule_slots = ScheduleSlotsRepository(self._session)
        self.specialist = SpecialistRepository(self._session)
        self.specialist_ratings = SpecialistRatingRepository(self._session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self._session.close()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
