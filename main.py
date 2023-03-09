from fastapi import FastAPI
from config.database import engine, Base

app = FastAPI()
app.title = "Tweetable API"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)