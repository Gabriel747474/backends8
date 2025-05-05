# ecommerce_lib/microservices/product_service.py

class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_availability(self, product):
        return product in self.products
