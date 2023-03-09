from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):

    id: Optional[int] = None
    email: str = Field(min_length=5, regex="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    password: str = Field(min_length=6)
    username: str = Field(min_length=1)
    name: str = Field(min_length=1)
    avatar: str

    class Config:
        schema_extra = {
            "example": {
                "email":"example@mail.com",
                "password":"******",
                "username":"pepito",
                "name":"pepito",
                "avatar":"Upload your avatar",
            }
        }