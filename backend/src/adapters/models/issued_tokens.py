from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.models import Base
from src.schemas.issued_tokens import IssuedTokensSchema


class IssuedTokens(Base):
    __tablename__ = 'issued_tokens'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    subject: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    revoke: Mapped[bool] = mapped_column(default=False)
    device_id: Mapped[UUID]

    user = relationship("User", foreign_keys=[subject], backref="issued_tokens", lazy="selectin",
                        cascade="all, delete")

    def to_read_model(self) -> IssuedTokensSchema:
        return IssuedTokensSchema(
            id=self.id,
            subject=self.subject,
            revoke=self.revoke,
            device_id=self.device_id
        )
