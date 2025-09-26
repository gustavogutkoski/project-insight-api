from fastapi import FastAPI

from app.api.v1.endpoints import router as api_router

app = FastAPI(title="Project Insight API - MVP")

app.include_router(api_router, prefix="/api/v1")
