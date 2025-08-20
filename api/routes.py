from fastapi import APIRouter, Request
from profiler.core import analyze_payload

router = APIRouter()

@router.get("/ping")
def ping():
    return {"status": "alive"}

@router.post("/analyze")
async def analyze(request: Request):
    payload = await request.json()
    result = analyze_payload(payload)
    return result
