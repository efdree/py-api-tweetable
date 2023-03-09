from models.model import TweetModel
from schemas.tweet import Tweet

class TweetService():

    def __init__(self, db) -> None:
        self.db = db

    def get_tweets(self):
        result = self.db.query(TweetModel).all()
        return result
    
    def get_tweet(self, id: int):
        result = self.db.query(TweetModel).filter(
            TweetModel.id == id).first()
        return result
    
    def get_tweet_by_user(self, user_id: int):
        result = self.db.query(TweetModel).filter(
            TweetModel.user_id == user_id).all()
        return result
    
    def create_tweet(self, tweet: Tweet):
        new_tweet = TweetModel(**tweet.dict())
        self.db.add(new_tweet)
        self.db.commit()
        return
    
    def update_tweet(self, id: int, data: Tweet):
        tweet = self.db.query(TweetModel).filter(
            TweetModel.id == id).first()
        tweet.body = data.body
        tweet.user_id = data.user_id
        self.db.commit()
        return
    
    def delete_tweet(self, id: int):
        self.db.query(TweetModel).filter(
            TweetModel.id == id).delete()
        self.db.commit()
        return