
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, SecretStr
from enum import Enum


class Priorita(str, Enum):
    BASSA = "bassa"
    MEDIA = "media"
    ALTA = "alta"


class Ruolo(str, Enum):
    ADMIN = "admin"
    USER = "user"

# SCHEMAS TASK
class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    priorita: Priorita = Priorita.MEDIA


class TodoReplace(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    completed: bool = False
    priorita: Priorita = Priorita.MEDIA

class TodoPatch(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, min_length=1)
    completed: Optional[bool] = None
    priorita: Optional[Priorita] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    priorita: Priorita



# SCHEMAS UTENTE

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: SecretStr = Field(min_length=8, max_length=16)



class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    ruolo: Ruolo
    iscritto_il: datetime

class UserReplace(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr
    ruolo: Ruolo
    

class UserPatch(BaseModel):
    username: Optional[str] = Field(default = None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    ruolo: Optional[Ruolo] = None
