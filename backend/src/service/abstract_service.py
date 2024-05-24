from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.adapters.repository import AbstractRepository


class AbstractService(ABC):
    def __init__(self, repo: AbstractRepository):
        self._repo: AbstractRepository = repo()

    @abstractmethod
    async def add(self, data: BaseModel):
        raise NotImplementedError

    @abstractmethod
    async def list(self, **filter_by: dict):
        raise NotImplementedError
