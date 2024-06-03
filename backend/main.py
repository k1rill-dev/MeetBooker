import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.endpoints.auth import all_routers

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


@app.get("/api")
async def root():
    return {"message": "Hello World"}


[app.include_router(router, prefix="/api") for router in all_routers]

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
