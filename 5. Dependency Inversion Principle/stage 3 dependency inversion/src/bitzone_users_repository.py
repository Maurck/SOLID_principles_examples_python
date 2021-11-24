from .users_repository import UsersRepository

class BitzoneUsersRepository(UsersRepository):
    bitzone_users = {
        "1": "Mauricio",
        "2": "Sebastian"
    }

    def search(self, user_id):
        try:
            return self.bitzone_users[user_id]
        except Exception:
            return None