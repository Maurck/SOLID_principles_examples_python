from .users_repository import UsersRepository

class EmptyUsersRepository(UsersRepository):
    users = {}

    def search(self, user_id):
        try:
            return self.users[user_id]
        except Exception:
            return None