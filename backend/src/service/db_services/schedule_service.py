from typing import Any
from uuid import UUID

from src.schemas.schedule import ScheduleSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class ScheduleService(AbstractService):
    async def add(self, uow: IUnitOfWork, data):
        async with uow:
            res = await uow.schedule_slots.add_one(data=data)
            await uow.commit()
            return res

    async def list(self, uow: IUnitOfWork, **filter_by: Any):
        async with uow:
            res = await uow.schedule_slots.find_all(**filter_by)
            await uow.commit()
            return res

    async def edit(self, uow: IUnitOfWork, pk: UUID, data: ScheduleSchema):
        async with uow:
            res = await uow.schedule_slots.edit_one(pk=pk, data=data)
            await uow.commit()
            return res
