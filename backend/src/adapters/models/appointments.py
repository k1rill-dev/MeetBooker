from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.models import Base


class Appointment(Base):
    __tablename__ = 'appointments'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    specialist_id: Mapped[UUID] = mapped_column(ForeignKey('specialists.id'))
    slot_id: Mapped[UUID] = mapped_column(ForeignKey('schedule_slots.id'))
    is_confirmed: Mapped[bool]
