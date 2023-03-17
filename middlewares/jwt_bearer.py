from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from util.jwt_manager import validate_token
from services.user import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        db = Session()
        result = UserService(db).get_users()
        list_emails = []
        for dato in result:
            list_emails.append(dato.email)

        if not data['email'] in list_emails:
            raise HTTPException(status_code=403, detail="Invalid Credentials")
