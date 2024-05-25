from abc import ABC, abstractmethod
from pydantic import BaseModel

from src.adapters.repository import AbstractRepository
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AbstractService(ABC):
    def __init__(self, uow: IUnitOfWork, repo: AbstractRepository):
        self._repo: AbstractRepository = repo()
        self._uow = uow

    @abstractmethod
    async def add(self, data: BaseModel):
        raise NotImplementedError

    @abstractmethod
    async def list(self, **filter_by: dict):
        raise NotImplementedError
