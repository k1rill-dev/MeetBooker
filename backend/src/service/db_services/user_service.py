from src.adapters.models import User
from src.adapters.repository import AbstractRepository
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class UserService(AbstractService):
    def __init__(self, uow: IUnitOfWork, repo: AbstractRepository):
        super().__init__(uow, repo)

    async def add(self, data: User):
        pass

    async def list(self):
        pass
