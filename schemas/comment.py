from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Comment(BaseModel):

    id: Optional[int] = None
    body: str = Field(min_length=1, max_length=140)
    created_time: date
    user_id: int
    tweet_id: int

    class Config:
        schema_extra = {
            "example": {
                "body": "Put here your comment",
                "created_time":"2023-03-10 10:10:10",
                "user_id": 0,
                "tweet_id": 0
            }
        }