from typing import List
from schemas.tweet import Tweet
from schemas.comment import Comment

class TweetSchema(Tweet):
    comments: List[Comment]