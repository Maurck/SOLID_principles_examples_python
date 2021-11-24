
class HardcodedInMemoryUsersRepository:

    users = {}

    def __init__(self, users):
        self.users = users

    def search(self, user_id):
        return self.users[user_id]
