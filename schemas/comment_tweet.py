from typing import List
from schemas.tweet import Tweet
from schemas.comment import Comment
from schemas.user import User
class TweetSchema(Tweet):
    comments: List[Comment ]