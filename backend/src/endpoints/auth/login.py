import pathlib

from fastapi import APIRouter, Depends, UploadFile, Request, Form
from pydantic import NameEmail
from starlette.responses import Response
from fastapi.params import Cookie, File

from config import settings
from src.endpoints.dependencies import UnitOfWorkDependency, get_user_from_token
from src.schemas.user import LoginUserSchema, UserSchema, AddUserSchema, UpdateUserSchema
from src.service.auth_service.auth_service import AuthService
from src.service.auth_service.types import RefreshToken
import aiofiles

from src.service.db_services.user_service import UserService

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/login")
async def login(user: LoginUserSchema, uow: UnitOfWorkDependency, response: Response) -> UserSchema:
    user = await AuthService().login(uow=uow, credentials=user, response=response)
    return user


@auth_router.get("/logout")
async def logout(uow: UnitOfWorkDependency, response: Response,
                 user=Depends(get_user_from_token)) -> dict:
    await AuthService().logout(uow=uow, response=response, user=user)
    return {
        "status": "success"
    }


@auth_router.post("/register")
async def register_user(user: AddUserSchema, uow: UnitOfWorkDependency):
    res = await AuthService().register(user, uow)
    return {"res": res}


@auth_router.get('/')
async def get_user(user: UserSchema = Depends(get_user_from_token)):
    return user


@auth_router.post('/rotate')
async def rotate_token(response: Response, uow: UnitOfWorkDependency,
                       refresh_token: RefreshToken = Cookie(...)):
    await AuthService().rotate_tokens(refresh_token=refresh_token, response=response, uow=uow)
    return {"status": "success"}


async def _update_user_data(request: Request, uow: UnitOfWorkDependency,
                            file: UploadFile,
                            user: UserSchema,
                            email: NameEmail,
                            first_name: str, last_name: str):
    if file is None:
        profile_picture = None
    else:
        path_to_save = f"{str(user.id)}/{file.filename}"
        if not pathlib.Path(settings.path_to_media.joinpath(f"{str(user.id)}")).exists():
            pathlib.Path(settings.path_to_media.joinpath(f"{str(user.id)}")).mkdir(parents=True)
        async with aiofiles.open(settings.path_to_media.joinpath(f"{str(user.id)}/" + file.filename), "wb") as f:
            while contents := file.file.read(1024 * 1024):
                await f.write(contents)
                await f.flush()
        profile_picture = str(request.url_for('media', path=path_to_save))
    updated_data = UpdateUserSchema(
        email=email.email,
        first_name=first_name,
        last_name=last_name,
        profile_picture=profile_picture,
    )
    data = updated_data.dict(exclude_none=True)
    user = await UserService().edit(pk=user.id, data=data, uow=uow)
    return user


@auth_router.patch('/update_user')
async def update_user(request: Request, uow: UnitOfWorkDependency,
                      file: UploadFile = File(None),
                      user=Depends(get_user_from_token),
                      email: NameEmail = Form(None),
                      first_name: str = Form(None), last_name: str = Form(None)):
    user = await _update_user_data(request, uow, file, user, email, first_name, last_name)
    return user
