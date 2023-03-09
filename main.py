from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Tweetable API"
app.version = "0.0.1"

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],)

Base.metadata.create_all(bind=engine)
