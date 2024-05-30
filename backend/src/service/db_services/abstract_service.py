from abc import ABC, abstractmethod
from pydantic import BaseModel

from src.adapters.repository import AbstractRepository
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AbstractService(ABC):
    @abstractmethod
    async def add(self, uow: IUnitOfWork, data: BaseModel):
        raise NotImplementedError

    @abstractmethod
    async def list(self, uow: IUnitOfWork, **filter_by: dict):
        raise NotImplementedError
