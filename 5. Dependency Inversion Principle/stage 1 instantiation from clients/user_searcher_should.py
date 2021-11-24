import unittest

from src.user_searcher import UserSearcher

class UserSearcherShould(unittest.TestCase):

    def find_existing_users(self):
        userSearcher = UserSearcher()

        existing_user_id = "1"
        expected_user_name = "Rafa"

        self.assertEquals(expected_user_name, userSearcher.search(existing_user_id))
    

    def not_find_non_existing_users(self, userSearcher):
        user_searcher = UserSearcher()

        # We would be coupled to the actual HardcodedInMemoryUsersRepository implementation.
        # We don't have the option to set test users as we would have to do if we had a real database repository.
        non_existing_user_id = "5"
        expected_error_flag = "-1"

        self.assertEquals(expected_error_flag, user_searcher.search(non_existing_user_id))
    