from src.domain.entities.user import User
from fastapi import HTTPException


class UserService:
    @staticmethod
    def create_user(user: User):
        if any(u.id == user.id for u in users_db):
            raise HTTPException(status_code=400, detail="ID de usuário já existe")
        users_db.append(user)
        return user

    @staticmethod
    def list_users():
        return users_db

    @staticmethod
    def delete_user(user_id: int):
        global users_db
        users_db = [u for u in users_db if u.id != user_id]
        return {"message": f"Usuário {user_id} deletado com sucesso."}