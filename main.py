from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

from config.database import Session

from routers.user import user_router
from routers.tweet import tweet_router
from routers.comment import comment_router

from models.model import UserModel, TweetModel, CommentModel

from datetime import datetime

app = FastAPI()
app.title = "Tweetable API"
app.version = "0.0.1"

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )

app.include_router(user_router)
app.include_router(tweet_router)
app.include_router(comment_router)
Base.metadata.create_all(bind=engine)

# with Session(bind=engine) as session:
#     user1 = UserModel(email="admin@mail.com", name= "admin", username="admin", password= "123456", avatar= "https://res.cloudinary.com/dw4vczbtg/image/upload/v1678321668/app_offix/upqpstv2rhuu5alqafvt.png")
#     user2 = UserModel(email="test@mail.com", name= "test", username="test", password= "123456", avatar= "https://res.cloudinary.com/dw4vczbtg/image/upload/v1678321544/app_offix/hnzbayz32re1zpfbus15.png")
#     user3 = UserModel(email="test1@mail.com", name= "test1", username="test1", password= "123456", avatar= "https://res.cloudinary.com/dw4vczbtg/image/upload/v1678321947/app_offix/we4eaoassbsvl0xrgvgx.png")

#     session.add_all([user1, user2, user3])
#     session.commit()

#     tweet1 = TweetModel(created_time=datetime(2023,3,10, 10, 10, 10), comments_count=3, user_id=user1.id, body="Put here your tweet")
#     tweet2 = TweetModel(created_time=datetime(2023,3,8, 1, 10, 10), comments_count=2, user_id=user1.id, body="Put here your tweet")
#     tweet3 = TweetModel(created_time=datetime(2023,3,8, 10, 1, 10), comments_count=0, user_id=user1.id, body="Put here your tweet")
#     tweet4 = TweetModel(created_time=datetime(2023,3,8, 11, 10, 10), comments_count=0, user_id=user2.id, body="Put here your tweet")
#     tweet5 = TweetModel(created_time=datetime(2023,3,7, 11, 11, 10), comments_count=0, user_id=user2.id, body="Put here your tweet")
#     tweet6 = TweetModel(created_time=datetime(2023,3,10, 12, 10, 10), comments_count=0, user_id=user3.id, body="Put here your tweet")

#     session.add_all([tweet1, tweet2, tweet3, tweet4, tweet5, tweet6])
#     session.commit()

#     comment1 = CommentModel(created_time=datetime(2023,3,10, 10, 10, 10), tweet_id= tweet1.id, user_id=user1.id, body="Put here your comment")
#     comment2 = CommentModel(created_time=datetime(2023,3,10, 2, 10, 10), tweet_id= tweet1.id, user_id=user1.id, body="Put here your comment")
#     comment3 = CommentModel(created_time=datetime(2023,3,10, 3, 10, 10), tweet_id= tweet1.id, user_id=user2.id, body="Put here your comment")
#     comment4 = CommentModel(created_time=datetime(2023,3,10, 4, 10, 10), tweet_id= tweet2.id, user_id=user1.id, body="Put here your comment")
#     comment5 = CommentModel(created_time=datetime(2023,3,10, 5, 10, 10), tweet_id= tweet2.id, user_id=user3.id, body="Put here your comment")

#     session.add_all([comment1, comment2, comment3, comment4, comment5])
#     session.commit()