from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.user import UserService
from schemas.user import User

user_router = APIRouter()

@user_router.get('/users', tags=['user'], response_model=List[User], status_code=200)
def get_users() -> List[User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/user/{id}', tags=['user'], response_model=User, status_code=200)
def get_user(id: int = Path(ge=1)) -> User:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post('/user', tags=['user'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message":"User Created"})

@user_router.patch('/user/{id}', tags=['user'], response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message":"User Updated"})