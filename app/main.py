import uuid

from fastapi import FastAPI
from app.routes.todos import router



app = FastAPI(title="Todo API", version="1.0.0")
app.include_router(router)

