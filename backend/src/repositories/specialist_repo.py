from src.adapters.models import Specialist, SpecialistRating
from src.adapters.repository import SQLAlchemyRepository


class SpecialistRepository(SQLAlchemyRepository):
    model = Specialist


class SpecialistRatingRepository(SQLAlchemyRepository):
    model = SpecialistRating
