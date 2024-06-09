from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.routers.router import router

app = FastAPI(
    title="Show Video Service",
    description="Shows video service",
    version="1.0",
)

app.include_router(router)

origins = ["localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

