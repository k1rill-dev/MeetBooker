import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, NameEmail, Field


class UserSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    email: NameEmail
    password: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    profile_picture: Optional[str] = None

    class Config:
        from_attributes = True


class AddUserSchema(BaseModel):
    email: NameEmail
    password: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    profile_picture: Optional[str] = None

    class Config:
        from_attributes = True


class LoginUserSchema(BaseModel):
    email: NameEmail
    password: str

    class Config:
        from_attributes = True


class UpdateUserSchema(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_picture: Optional[str] = None

    class Config:
        from_attributes = True
