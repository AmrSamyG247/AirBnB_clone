#!/usr/bin/python3
""" Amenity Model Unit tests """
from tests.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **keyargs):
        """ Test normal base initiazition """
        super().__init__(*args, **keyargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()

