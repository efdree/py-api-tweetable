from schemas.user import User

from jwt import encode, decode


def create_token(user: User):
    payload = {"email": user.email, "password": user.password}
    token: str = encode(payload=payload, key="my_secret_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data
