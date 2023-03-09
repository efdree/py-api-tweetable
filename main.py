from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

from routers.user import user_router
from routers.tweet import tweet_router
from routers.comment import comment_router

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
