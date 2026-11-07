import uuid
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class Priorita(str, Enum):
    BASSA = "bassa"
    MEDIA = "media"
    ALTA = "alta"

class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    priorita: Priorita = Priorita.MEDIA


class TodoReplace(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: bool = False
    priorita: Priorita = Priorita.MEDIA

class TodoPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priorita: Optional[Priorita] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    priorita: Priorita
