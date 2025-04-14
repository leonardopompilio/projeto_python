from fastapi import FastAPI
from src.interface import user_controller, product_controller


app = FastAPI()
app.include_router(user_controller.router)
app.include_router(product_controller.router)



