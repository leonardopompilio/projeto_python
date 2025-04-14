from fastapi import APIRouter
from src.domain.entities.user import User   
from typing import List
from src.application.user_service import UserService

router = APIRouter()
user_service = UserService()

class UserController:

    @router.post("/users", response_model=User)
    def create_user(user: User):
        return user_service.create_user(user) 

    @router.get("/users", response_model=List[User])
    def get_users():
        return user_service.get_users()

    @router.delete("/users/{user_id}")
    def delete_user(user_id: int):
        global users_db
        users_db = [u for u in users_db if u.id != user_id]
        return {"message": f"Usuário {user_id} deletado com sucesso."}
    
