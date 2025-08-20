from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Resonance Profiler")
app.include_router(router)
