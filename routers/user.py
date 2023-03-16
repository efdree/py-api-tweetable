from fastapi import APIRouter
from fastapi import Path,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Dict

from util.jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer

from config.database import Session
from services.user import UserService
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@mail.com" and user.password == "123456":
        print("*"*20)
        print(user)
        print("*"*20)
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)


@user_router.get('/users', tags=['user'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
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


@user_router.post('/user', tags=['user'], response_model=Dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_user(user: User) -> Dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message":"User Created"})

@user_router.patch('/user/{id}', tags=['user'], response_model=Dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_user(id: int, user: User) -> Dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message":"User Updated"})