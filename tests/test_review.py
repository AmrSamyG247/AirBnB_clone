#!/usr/bin/python3
""" Test Models for review units """
from tests.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test basemodel initiate """

    def __init__(self, *args, **kwargs):
        """ Test 1"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test 2"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test 3"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test 4"""
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()

