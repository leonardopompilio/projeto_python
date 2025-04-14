from src.domain.entities.product import Product
from fastapi import HTTPException
from src.infra.repository.product_repository import ProductRepository

product_repository = ProductRepository()

class ProductService:
    @staticmethod
    def create_product(product: Product):
        if product_repository.find_by_id(product.id):
            raise HTTPException(status_code=400, detail="Produto ja existente")
        return product_repository.create_product(product)

    @staticmethod
    def list_products():
        return product_repository.find_all()

    @staticmethod
    def delete_product(product_id: int):
        global products_db
        products_db = [p for p in products_db if p.id != product_id]
        return {"message": f"Produto {product_id} deletado com sucesso."}
    
    @staticmethod
    def find_product(product_id: int):
        return product_repository.find_by_id(product_id)