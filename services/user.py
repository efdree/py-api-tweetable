from models.model import UserModel
from schemas.user import User

class UserService():

    def __init__(self, db) -> None:
        self.db = db
    
    ###Optional
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id: int):
        result = self.db.query(UserModel).filter(
            UserModel.id == id).first()
        return result
    
    def create_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self, id: int, data: User):
        user = self.db.query(UserModel).filter(
            UserModel.id == id).first()
        user.email = data.email
        user.password = data.password
        user.username = data.username
        user.name = data.name
        user.avatar = data.avatar
        self.db.commit()
        return
