# ecommerce_lib/microservices/user_service.py

class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
