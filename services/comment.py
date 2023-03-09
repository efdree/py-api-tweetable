from models.model import CommentModel
from schemas.comment import Comment

class CommentService():

    def __init__(self,db) -> None:
        self.db = db

    def get_comments(self):
        result = self.db.query(CommentModel).all()
        return result
    
    def get_comment(self, id: int):
        result = self.db.query(CommentModel).filter(
            CommentModel.id == id).first()
        return result
    
    def get_comment_by_tweet(self, tweet_id:int):
        result = self.db.query(CommentModel).filter(
            CommentModel.tweet_id == tweet_id).all()
        return result

    def create_comment(self, comment: Comment):
        new_comment = CommentModel(**comment.dict())
        self.db.add(new_comment)
        self.db.commit()
        return
    
    def update_comment(self, id:int, data: Comment):
        comment = self.db.query(CommentModel).filter(
            CommentModel.id == id).first()
        comment.body = data.body
        comment.user_id = data.user_id
        comment.tweet_id = data.tweet_id
        self.db.commit()
        return
    
    def delete_comment(self, id:int):
        self.db.query(CommentModel).filter(
            CommentModel.id == id).delete()
        self.db.commit()
        return