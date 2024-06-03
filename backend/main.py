import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView
from starlette.staticfiles import StaticFiles

from src.adapters.models import User
from src.db.db import engine
from src.endpoints.auth import auth_router
from src.endpoints.specialists import specialists_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000"
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


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.first_name, User.last_name, User.email]


admin.add_view(UserAdmin)


@app.get("/api")
async def root():
    return {"message": "Hello World"}


app.include_router(auth_router, prefix="/api")
app.include_router(specialists_router, prefix="/api")
app.include_router(specialists_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
