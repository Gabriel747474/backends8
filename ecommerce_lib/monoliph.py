# ecommerce_lib/monolith.py

class EcommerceSystem:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, user, product):
        if product in self.products:
            self.orders.append((user, product))
            return "Order placed successfully"
        return "Product not available"
