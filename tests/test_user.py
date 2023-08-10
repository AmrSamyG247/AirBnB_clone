#!/usr/bin/python3
""" Test Model user """
from tests.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test basemodel initialize"""

    def __init__(self, *args, **kwargs):
        """ Test 1 """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test 2 """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test 3 """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test 4 """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test 5"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()

