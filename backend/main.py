import uvicorn
from fastapi import FastAPI

from src.endpoints.auth import all_routers

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World"}


[app.include_router(router, prefix="/api") for router in all_routers]

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
