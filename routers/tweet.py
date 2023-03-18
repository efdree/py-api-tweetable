from fastapi import APIRouter
from fastapi import Path,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Dict

from config.database import Session
from services.tweet import TweetService
from schemas.tweet import Tweet
from services.comment import CommentService

from middlewares.jwt_bearer import JWTBearer

from schemas.comment_tweet import TweetSchema

tweet_router = APIRouter()

@tweet_router.get('/tweets', tags=['tweet'], response_model=List[TweetSchema], status_code=200)
def get_tweets() -> List[TweetSchema]:
    db = Session()
    result = TweetService(db).get_tweets()
    if not result:
        return JSONResponse(status_code=404, content={"message": "There is not tweet"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@tweet_router.get('/tweet/{id}', tags=['tweet'], response_model=TweetSchema, status_code=200)
def get_tweet(id: int = Path(ge=1)) -> TweetSchema:
    db = Session()
    result_tweet = TweetService(db).get_tweet(id)
    if not result_tweet:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder([result_tweet]))

@tweet_router.post('/tweet', tags=['tweet'], response_model=Dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_tweet(tweet: Tweet) -> Dict:
    db = Session()
    TweetService(db).create_tweet(tweet)
    return JSONResponse(status_code=201, content={"message": "Tweet Created"})

@tweet_router.patch('/tweet/{id}', tags=['tweet'], response_model=Dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_tweet(id: int, tweet: Tweet) -> Dict:
    db = Session()
    result = TweetService(db).get_tweet(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    TweetService(db).update_tweet(id, tweet)
    return JSONResponse(status_code=200, content={"message": "Tweet Updated"})

@tweet_router.delete('/tweet/{id}', tags=['tweet'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_tweet(id: int) -> dict:
    db = Session()
    result = TweetService(db).get_tweet(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_comments = CommentService(db).get_comment_by_tweet(result.id)
    print("*"*20)
    print(result_comments)
    print("*"*20)
    for comment in result_comments:
        CommentService(db).delete_comment(comment.id)
    TweetService(db).delete_tweet(id)
    return JSONResponse(status_code=200, content={"message": "Tweet Deleted"})