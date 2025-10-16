from src.db import Database
from src.config import ADMIN


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def is_admin(self, user_id):
        print(user_id)
        print(ADMIN)
        print(f"user_id: {user_id} ({type(user_id)})")
        print(f"ADMIN: {ADMIN} ({type(ADMIN)})")
        return user_id == ADMIN

    def if_user_exist(self, user_id):
        return self.db.get_user(user_id) is not None

    def add_new_user(self, user_id, username):
        if not self.if_user_exist(user_id):
            self.db.add_user(user_id, username)
            return True

        return False
