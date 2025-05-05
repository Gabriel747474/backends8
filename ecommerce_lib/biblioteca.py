from monoliph import EcommerceSystem 
from microsservices.users_sevices import UserService 
from microsservices.product_services import ProductService 
from microsservices.order_service import OrderService 

# Monolítico
system = EcommerceSystem()
system.add_user("Alice")
system.add_product("Laptop")
print(system.place_order("Alice", "Laptop"))

# Microsserviços
user_service = UserService()
product_service = ProductService()
order_service = OrderService()

user_service.add_user("Bob")
product_service.add_product("Smartphone")
print(order_service.place_order("Bob", "Smartphone", product_service))
