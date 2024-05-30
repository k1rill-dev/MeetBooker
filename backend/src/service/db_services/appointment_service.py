from src.adapters.repository import AbstractRepository
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AppointmentService(AbstractService):
    async def add(self, data):
        pass

    async def list(self):
        pass
