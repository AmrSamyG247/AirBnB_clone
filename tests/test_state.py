#!/usr/bin/python3
""" Test Model state"""
from tests.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test basemodel intializing """

    def __init__(self, *args, **keyargs):
        """ Test 1 """
        super().__init__(*args, **keyargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test 2 """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()

