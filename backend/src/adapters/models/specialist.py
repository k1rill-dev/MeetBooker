import uuid
from uuid import UUID
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from src.adapters.models import Base


class Specialist(Base):
    __tablename__ = 'specialists'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    speciality: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))


class SpecialistRating(Base):
    __tablename__ = 'specialist_ratings'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id'))
    rating: Mapped[float]
