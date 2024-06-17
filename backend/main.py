import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from sqladmin import Admin
from starlette.staticfiles import StaticFiles

from src.admin.appointment import AppointmentAdmin
from src.admin.schedule_slot import ScheduleSlotAdmin
from src.admin.specialists import SpecialistAdmin, SpecialistRatingAdmin
from src.admin.user import UserAdmin
from src.db.db import engine
from src.endpoints.auth import auth_router
from src.endpoints.social_auth.yandex_auth import social_auth_router
from src.endpoints.specialists import specialists_router
from src.endpoints.schedule import schedule_routes

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/media", StaticFiles(directory="media"), name="media")

admin = Admin(app, engine)

admin.add_view(AppointmentAdmin)
admin.add_view(ScheduleSlotAdmin)
admin.add_view(SpecialistAdmin)
admin.add_view(SpecialistRatingAdmin)
admin.add_view(UserAdmin)

add_pagination(app)


@app.get("/api")
async def root():
    return {"message": "Hello World"}


app.include_router(auth_router, prefix="/api")
app.include_router(specialists_router, prefix="/api")
app.include_router(schedule_routes, prefix="/api")
app.include_router(social_auth_router, prefix="/api")
# app.include_router(vk_router, prefix="/api") АВТОРИЗАЦИЯ ВК НЕ РАБОТАЕТ, ТАК КАК НУЖЕН ПРОТОКОЛ HTTPS, NGROK ДЛЯ СЛАБЫХ ДУХОМ

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
