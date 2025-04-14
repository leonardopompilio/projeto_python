from typing import List
from src.domain.entities.user import User
from src.infra.config.db_fake import users_db

class UserRepository:
    @staticmethod
    def save(user: User):
        users_db.append(user)
        return user

    @staticmethod
    def find_all() -> List[User]:
        return users_db

    @staticmethod
    def delete_by_id(user_id: int):
        global users_db
        users_db = [u for u in users_db if u.id != user_id]