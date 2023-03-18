from fastapi import APIRouter
from fastapi import Path,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.comment import CommentService
from schemas.comment import Comment

from middlewares.jwt_bearer import JWTBearer

from services.tweet import TweetService

comment_router = APIRouter()

@comment_router.get('/comments', tags=['comment'], response_model=List[Comment], status_code=200)
def get_comments() -> List[Comment]:
    db = Session()
    result = CommentService(db).get_comments()
    if not result:
        return JSONResponse(status_code=404, content={"message": "There is not comments"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@comment_router.get('/comment/{id}', tags=['comment'], response_model=Comment, status_code=200, dependencies=[Depends(JWTBearer())])
def get_comment(id:int = Path(ge=1)) -> Comment:
    db = Session()
    result = CommentService(db).get_comment(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})        
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@comment_router.post('/comment', tags=['comment'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_comment(comment: Comment) -> dict:
    db = Session()
    CommentService(db).create_comment(comment)
    tweet = TweetService(db).get_tweet(comment.tweet_id)
    tweet.comments_count += 1
    TweetService(db).update_tweet(tweet.id, tweet)
    return JSONResponse(status_code=201, content={"message": "Comment Created"})        

@comment_router.patch('/comment/{id}', tags=['comment'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_comment(id: int, comment: Comment) -> dict:
    db = Session()
    result = CommentService(db).get_comment(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CommentService(db).update_comment(id, comment)
    return JSONResponse(status_code=200, content={"message": "Updated"})


@comment_router.delete('/comment/{id}', tags=['comment'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_comment(id: int) -> dict:
    db = Session()
    result = CommentService(db).get_comment(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CommentService(db).delete_comment(id)
    tweet = TweetService(db).get_tweet(result.tweet_id)
    tweet.comments_count -= 1
    TweetService(db).update_tweet(tweet.id, tweet)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
