from fastapi import FastAPI, APIRouter
from routes.portik import portik_router

app = FastAPI()
app.include_router(portik_router)



