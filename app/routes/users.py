from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from pwdlib import PasswordHash

from app.schemas import(
    UserCreate,
    UserResponse,
    UserReplace,
    UserPatch
)

from app import database

password_hash = PasswordHash.recommended()

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserResponse], status_code=200)
def get_users():
    users = list(database.USERS_DB.values())
    return users

@router.post("/", response_model=UserResponse, status_code=201)
def add_user(user: UserCreate) -> UserResponse:

    for existing_user in database.USERS_DB.values():
        if existing_user['username'] == user.username:
            raise HTTPException(status_code=409, detail="Username already registered")
        if existing_user['email'] == user.email:
            raise HTTPException(status_code=409, detail="Email already registered")
    
    hashed_password = password_hash.hash(
        user.password.get_secret_value()
    )
    new_user = {
        'id': next(database.USERS_ID),
        'username': user.username,
        'email': user.email,
        'password': hashed_password,
        'ruolo': "user",
        'iscritto_il': datetime.now(timezone.utc)
    }
    database.USERS_DB[new_user['id']] = new_user
    return new_user
