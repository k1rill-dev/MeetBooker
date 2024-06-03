from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.models import Base
from src.schemas.issued_tokens import IssuedTokensSchema


class IssuedTokens(Base):
    __tablename__ = 'issued_tokens'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    subject: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    revoke: Mapped[bool] = mapped_column(default=False)
    device_id: Mapped[UUID]

    def to_read_model(self) -> IssuedTokensSchema:
        return IssuedTokensSchema(
            id=self.id,
            subject=self.subject,
            revoke=self.revoke,
            device_id=self.device_id
        )
