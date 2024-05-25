from src.adapters.models import User
from src.adapters.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = User
