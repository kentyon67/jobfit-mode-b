from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app import models
from backend.app.database import engine
from backend.app.routers import jobs


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="JobFit Mode B API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(jobs.router)


@app.get("/")
def root():
    return {"message": "JobFit Mode B API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
