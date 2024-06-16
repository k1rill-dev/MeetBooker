from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from src.endpoints.dependencies import UnitOfWorkDependency, get_user_from_token, get_specialist_from_token
from src.schemas.specialists import SpecialistSchema, SpecialistRatingSchema, CreateSpecialistSchema, \
    UpdateSpecialistSchema, CreateSpecialistRatingSchema, JoinedResult
from src.schemas.user import UserSchema
from src.service.db_services.specialist_service import SpecialistService, SpecialistRatingService

specialists_router = APIRouter(tags=["specialists"])


@specialists_router.get("/specialist", response_model=Page[JoinedResult])
async def get_all_specialists(uow: UnitOfWorkDependency):
    data = await SpecialistService().joined_list(uow=uow)
    return paginate(data)


@specialists_router.post("/specialist")
async def create_specialist(uow: UnitOfWorkDependency, spec: CreateSpecialistSchema):
    specialist = await SpecialistService().add(uow, spec)
    return specialist


@specialists_router.get("/specialist/{id}")
async def get_specialist(id: UUID, uow: UnitOfWorkDependency):
    data = await SpecialistService().joined_list(uow=uow, specialist_id=id)
    return data[0]


@specialists_router.get("/specialist-by-user-id")
async def get_specialist_by_user_id(uow: UnitOfWorkDependency,
                                    user: UserSchema = Depends(get_specialist_from_token)):
    data = await SpecialistService().joined_list(uow=uow, specialist_id=user.id)
    return data[0]


@specialists_router.patch("/specialist")
async def update_specialist(uow: UnitOfWorkDependency,
                            spec_data: UpdateSpecialistSchema,
                            user: UserSchema = Depends(get_specialist_from_token)):
    specialist = await SpecialistService().update(uow=uow, pk=user.id, data=spec_data)
    return specialist


@specialists_router.post("/specialist-rating")
async def set_specialist_rating(uow: UnitOfWorkDependency, rating_data: CreateSpecialistRatingSchema,
                                user: UserSchema = Depends(get_user_from_token)):
    rating = await SpecialistRatingService().add(uow, rating_data)
    return rating
