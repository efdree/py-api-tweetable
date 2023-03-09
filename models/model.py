from config.database import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String)
    username = Column(String, unique = True)
    name = Column(String)
    avatar = Column(String)

    tweets_users = relationship("Tweet", back_populates = "users_tweets")
    comments_users = relationship("Comment", back_populates = "users_comments")

class TweetModel(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key = True, index = True)
    body = Column(String)
    comments_count = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    users_tweets = relationship("User", back_populates = "tweets_users")
    comments_tweets = relationship("Comment", back_populates = "tweets_comments")

class CommentModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key = True, index = True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    tweet_id = Column(Integer, ForeignKey("tweets.id"))

    users_comments = relationship("User", back_populates = "comments_users")
    tweets_comments = relationship("Tweet", back_populates = "comments_tweets")