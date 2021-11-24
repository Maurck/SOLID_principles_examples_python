from .users_repository import UsersRepository

class UserSearcher:
    users_repository = None

    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def search(self, user_id):
        return self.users_repository.search(user_id)