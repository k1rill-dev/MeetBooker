import uuid
from uuid import UUID
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.adapters.models import Base
from src.schemas.specialists import SpecialistSchema, SpecialistRatingSchema


class Specialist(Base):
    __tablename__ = 'specialists'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    speciality: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), unique=True)

    user = relationship("User", foreign_keys=[user_id], backref="specialists", lazy="joined",
                        cascade="all, delete")

    def __str__(self):
        return self.speciality

    def to_read_model(self) -> SpecialistSchema:
        return SpecialistSchema(
            id=self.id,
            speciality=self.speciality,
            bio=self.bio,
            user_id=self.user_id
        )


class SpecialistRating(Base):
    __tablename__ = 'specialist_ratings'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id'))
    rating: Mapped[float]

    user = relationship("User", foreign_keys=[user_id], backref="specialist_ratings", lazy="selectin")
    specialist = relationship("Specialist", foreign_keys=[specialist_id], backref="specialist_ratings", lazy="selectin")

    def to_read_model(self) -> SpecialistRatingSchema:
        return SpecialistRatingSchema(
            id=self.id,
            user_id=self.user_id,
            specialist_id=self.specialist_id,
            rating=self.rating
        )
