
class HardcodedInMemoryUsersRepository:

    users = {
        "1": "Rafa",
        "2": "Javi"
    }

    def search(self, user_id):
        return self.users[user_id]
