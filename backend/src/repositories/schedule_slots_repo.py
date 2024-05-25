from src.adapters.models import ScheduleSlot
from src.adapters.repository import SQLAlchemyRepository


class ScheduleSlotsRepository(SQLAlchemyRepository):
    model = ScheduleSlot
