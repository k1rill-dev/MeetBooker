from .login import login_router
from .register import register_router

all_routers = [
    register_router,
    login_router
]