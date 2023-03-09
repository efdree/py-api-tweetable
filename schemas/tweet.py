from pydantic import BaseModel, Field
from typing import Optional

class Tweet(BaseModel):

    id: Optional[int] = None
    body: str = Field(min_length=1, max_length=140)
    comments_count: Optional[int] = 0
    user_id: int

    class Config:
        schema_extra = {
            "example":{
                "body":"Put here your tweet",
                "user_id": 0
            }
        }