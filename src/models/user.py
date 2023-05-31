from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, alias, password):
        self.id = id
        self.alias = alias
        self.password = password

    @staticmethod
    def get(user_id):
        return users.get(int(user_id))

users = {
    1: User(1, 'admin', 'password'),
    2: User(2, 'alexanyernas', 'password')
}