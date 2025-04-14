from fastapi import APIRouter
from src.application.product_service import ProductService
from src.domain.entities.product import Product 
from typing import List

router = APIRouter()
product_service = ProductService()

class ProductController:

    @router.post("/products", response_model=Product)
    def create_product(product: Product):
        return product_service.create_product(Product)

    @router.get("/products", response_model=List[Product])
    def get_products():
        return product_service.list_products()

    @router.delete("/products/{product_id}")
    def delete_product(product_id: int):
        return product_service.delete_product(product_id)