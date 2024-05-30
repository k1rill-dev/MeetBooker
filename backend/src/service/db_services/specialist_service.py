from src.adapters.repository import AbstractRepository
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class SpecialistService(AbstractService):

    async def add(self, uow: IUnitOfWork, data):
        pass

    async def list(self, uow: IUnitOfWork, **filter_by):
        pass


class SpecialistRatingService(AbstractService):

    async def add(self, uow: IUnitOfWork, data):
        pass

    async def list(self, uow: IUnitOfWork, **filter_by):
        pass
