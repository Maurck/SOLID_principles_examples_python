import unittest

from src.user_searcher import UserSearcher
from src.hardcoded_in_memory_users_repository import HardcodedInMemoryUsersRepository

class UserSearcherShould(unittest.TestCase):


    def find_existing_users(self):
        # Now we're injecting the HardcodedInMemoryUsersRepository instance through the UserSearcher constructor.
        # 👍 Win: We've moved away from the UserSearcher the instantiation logic of the HardcodedInMemoryUsersRepository class allowing us to centralize it.
        # 👍 Win: We're exposing the couplings of the UserSearcher class.
        
        users_repository = HardcodedInMemoryUsersRepository()
        user_searcher = UserSearcher(users_repository)

        existing_user_Id = "1"
        expected_user_name = "Rafa"

        self.assertEquals(expected_user_name, user_searcher.search(existing_user_Id))


    def not_find_non_existing_users(self):
        users_repository = HardcodedInMemoryUsersRepository()
        user_searcher = UserSearcher(users_repository)

        non_existing_user_id = "5"
        expected_error_flag = "-1"

        self.assertEquals(expected_error_flag, user_searcher.search(non_existing_user_id))
    

    