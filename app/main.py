from fastapi import FastAPI
from app.api.routes import research

app = FastAPI()

app.include_router(research.router)