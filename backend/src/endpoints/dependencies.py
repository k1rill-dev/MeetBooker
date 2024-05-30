from typing import Annotated

from fastapi import Depends

from src.service.unit_of_work.unit_of_work import IUnitOfWork, UnitOfWork

UnitOfWorkDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]
