from src.adapters.models import User
from src.adapters.repository import AbstractRepository
from src.service.abstract_service import AbstractService


class UserService(AbstractService):
    def __init__(self, repo: AbstractRepository):
        super().__init__(repo)

    async def add(self, data: User):
        pass

    async def list(self):
        pass
