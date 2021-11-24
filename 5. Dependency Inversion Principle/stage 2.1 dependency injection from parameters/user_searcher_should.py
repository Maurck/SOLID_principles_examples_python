import unittest

from src.user_searcher import UserSearcher
from src.hardcoded_in_memory_users_repository import HardcodedInMemoryUsersRepository

class UserSearcherShould(unittest.TestCase):

    def find_existing_users(self):
        # Now we're also injecting the constant parameters needed by the HardcodedInMemoryUsersRepository through its constructor.
        # 👍 Win: We can send different parameters depending on the environment.
        # That is, in our production environment we would have actual users,
        # while in our tests cases we will set only the needed ones to run our test cases
        
        rafa_id = 1
        users = {
            rafa_id: "Rafa"
        }

        usersRepository = HardcodedInMemoryUsersRepository(users)
        userSearcher = UserSearcher(usersRepository)

        expected_user_name = "Rafa"

        self.assertEquals(expected_user_name, userSearcher.search(rafa_id))

    def not_find_non_existing_users(self):
        users = {}
        usersRepository = HardcodedInMemoryUsersRepository(users)
        userSearcher = UserSearcher(usersRepository)

        # 👍 Win: Now we don't have to be coupled of the actual HardcodedInMemoryUsersRepository users.
        # We can send a random user ID in order to force an empty result because we've set an empty map as the system users.

        non_existing_userId = "1"
        expected_empty_result = "-1"

        self.assertEquals(expected_empty_result, userSearcher.search(non_existing_userId))
    