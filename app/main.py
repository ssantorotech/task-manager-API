import uuid

from fastapi import FastAPI
from app.routes import (todos, users)


app = FastAPI(title="Todo API", version="1.0.0")
app.include_router(todos.router)
app.include_router(users.router)

