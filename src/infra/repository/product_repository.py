from src.domain.entities.product import Product
from src.infra.config.db_fake import products_db

class ProductRepository:
    @staticmethod
    def create_product (product: Product):
        products_db.append(product)
        return product
    
    @staticmethod
    def delete_by_id (product_id: int):
        global products_db
        products_db = [u for u in products_db if u.id != product_id]

    @staticmethod
    def find_all ():
        return products_db



        
        