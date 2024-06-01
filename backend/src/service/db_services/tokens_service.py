from http import HTTPStatus
from typing import List
from uuid import UUID

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from src.schemas.issued_tokens import IssuedTokensSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class TokenService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: IssuedTokensSchema):
        insert_data = data.model_dump()
        async with uow:
            pk = await uow.issued_tokens.add_one(data=insert_data)
            return pk

    async def list(self, uow: IUnitOfWork, **filter_by) -> List[IssuedTokensSchema]:
        async with uow:
            data = await uow.issued_tokens.find_all(**filter_by)
            return data

    async def get(self, uow: IUnitOfWork, **filter_by) -> IssuedTokensSchema:
        async with uow:
            try:
                data = await uow.issued_tokens.find_one(**filter_by)
                return data
            except IntegrityError as e:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='Tokens doesn\'t exist')

    async def edit(self, uow: IUnitOfWork, id: UUID, data: IssuedTokensSchema) -> UUID:
        async with uow:
            pk = await uow.issued_tokens.edit_one(id=id, data=data.model_dump())
            return pk

    async def check_revoked(self, jti: UUID, uow: IUnitOfWork) -> bool:
        async with uow:
            res = await uow.issued_tokens.find_all(jti=jti)
            if res:
                return True
            return False

    async def edit_multiple(self, uow: IUnitOfWork, data: IssuedTokensSchema):
        async with uow:
            res = await uow.issued_tokens.edit_multiply(updated_data=data.model_dump(), subject=data.subject)
            return res
