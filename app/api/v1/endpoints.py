from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
def healthcheck() -> Dict[str, str]:
    return {"status": "ok"}
