from uuid import UUID

from pydantic import BaseModel


class IssuedTokensSchema(BaseModel):
    id: UUID
    subject: UUID
    revoke: bool
    device_id: UUID

    class Config:
        from_attributes = True


class UpdateIssuedTokensSchema(BaseModel):
    revoke: bool
