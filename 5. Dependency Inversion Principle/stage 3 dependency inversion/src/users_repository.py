import abc

class UsersRepository(abc.ABC):
    @abc.abstractmethod
    def search(self, user_id):
        raise NotImplementedError