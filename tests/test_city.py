#!/usr/bin/python3
""" City Model Unit tests """
from tests.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test normal base initiation """

    def __init__(self, *args, **kwargs):
        """ Test normal base initiation """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test model """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """  Test model """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()

