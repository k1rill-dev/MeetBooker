from .login import auth_router
from .register import register_router

all_routers = [
    register_router,
    auth_router
]