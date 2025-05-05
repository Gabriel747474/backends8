# ecommerce_lib/microservices/order_service.py

class OrderService:
    def __init__(self):
        self.orders = []

    def place_order(self, user, product, product_service):
        if product_service.check_availability(product):
            self.orders.append((user, product))
            return "Order placed successfully"
        return "Product not available"
