from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    profile_picture: str

    class Config:
        from_attributes = True

