from .hardcoded_in_memory_users_repository import HardcodedInMemoryUsersRepository

class UserSearcher:
    users_repository = None

    def __init__(self, users_repository: HardcodedInMemoryUsersRepository):
        self.users_repository = users_repository

    def search(self, user_id):
        try:
            return self.users_repository.search(user_id)
        except Exception:
            return "-1"