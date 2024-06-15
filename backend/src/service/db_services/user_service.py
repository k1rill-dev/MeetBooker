import uuid
from typing import Any, Optional
from uuid import UUID
from fastapi import HTTPException
from pydantic import NameEmail
from sqlalchemy.exc import IntegrityError
from src.endpoints.auth.utils import Hasher
from src.schemas.user import AddUserSchema, UserSchema, UpdateUserSchema
from src.service.db_services.abstract_service import AbstractService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class UserService(AbstractService):
    async def add(self, uow: IUnitOfWork, data: UserSchema) -> UUID | None:
        data.password = Hasher.hash_password(data.password).decode('utf-8')
        data.email = data.email.email
        user = data.model_dump()
        async with uow:
            try:
                user_id = await uow.users.add_one(data=user)
                await uow.commit()
                return user_id
            except IntegrityError:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='User already exists')

    async def list(self, uow: IUnitOfWork, **filter_by):
        async with uow:
            users = await uow.users.find_all(**filter_by)
            return users

    async def get_by_email(self, uow: IUnitOfWork, email: NameEmail) -> Optional[UserSchema]:
        async with uow:
            try:
                user = await uow.users.find_one(email=email.email)
                return user
            except IntegrityError:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='User does not exist')

    async def get(self, uow: IUnitOfWork, **filter_by) -> Optional[UserSchema]:
        async with uow:
            try:
                user = await uow.users.find_one(**filter_by)
                return user
            except IntegrityError:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='User does not exist')

    async def edit(self, uow: IUnitOfWork, data: dict, pk: UUID) -> UserSchema:
        async with uow:
            user = await uow.users.edit_one(pk=pk, data=data)
            await uow.commit()
            print(user)
            return user
