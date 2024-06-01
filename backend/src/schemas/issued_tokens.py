from uuid import UUID

from pydantic import BaseModel


class IssuedTokensSchema(BaseModel):
    jti: UUID
    subject: UUID
    revoked: bool
    device_id: UUID

    class Config:
        from_attributes = True
