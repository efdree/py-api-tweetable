from pydantic import BaseModel, Field
from typing import Optional

class Comment(BaseModel):

    id: Optional[int] = None
    body: str = Field(min_length=1, max_length=140)
    user_id: int
    tweet_id: int

    class Config:
        schema_extra = {
            "example": {
                "body": "Put here your comment",
                "user_id": 0,
                "tweet_id": 0
            }
        }