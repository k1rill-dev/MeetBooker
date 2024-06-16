from typing import Any
from uuid import UUID

from src.schemas.schedule import ScheduleSchema, CreateScheduleSchema, UpdateScheduleSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class ScheduleService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: ScheduleSchema):
        async with uow:
            res = await uow.schedule_slots.add_one(data=data.model_dump())
            await uow.commit()
            return res

    async def list(self, uow: IUnitOfWork, **filter_by: Any):
        async with uow:
            res = await uow.schedule_slots.find_all(**filter_by)
            await uow.commit()
            return res

    async def edit(self, uow: IUnitOfWork, pk: UUID, data: UpdateScheduleSchema):
        async with uow:
            res = await uow.schedule_slots.edit_one(pk=pk, data=data.dict(exclude_none=True))
            await uow.commit()
            return res

    async def delete_one(self, uow: IUnitOfWork, pk: UUID):
        async with uow:
            res = await uow.schedule_slots.delete_one(pk=pk)
            await uow.commit()
            return res
