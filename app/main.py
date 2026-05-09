from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Hybrid Semantic Search Engine",
    version="1.0"
)

app.include_router(router)