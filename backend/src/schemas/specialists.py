import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BaseSpecialistSchema(BaseModel):
    speciality: str
    bio: str
    user_id: UUID

    class Config:
        from_attributes = True


class JoinedResult(BaseModel):
    spec_id: UUID = Field(alias='id', serialization_alias='spec_id')
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    bio: str
    speciality: str
    profile_picture: Optional[str] = None
    sum_rating: float


class SpecialistSchema(BaseSpecialistSchema):
    id: UUID = Field(default_factory=uuid.uuid4)


class CreateSpecialistSchema(BaseSpecialistSchema):
    pass


class UpdateSpecialistSchema(BaseSpecialistSchema):
    speciality: Optional[str] = None
    bio: Optional[str] = None
    user_id: UUID = None


class BaseSpecialistRatingSchema(BaseModel):
    user_id: UUID
    specialist_id: UUID
    rating: float

    class Config:
        from_attributes = True


class SpecialistRatingSchema(BaseSpecialistRatingSchema):
    id: UUID


class CreateSpecialistRatingSchema(BaseSpecialistRatingSchema):
    pass
