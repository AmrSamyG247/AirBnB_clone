#!/usr/bin/python3
""" Test Model for Place """
from tests.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test normal base initiazation """

    def __init__(self, *args, **keyargs):
        """ Test 1 """
        super().__init__(*args, **keyargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test 2 """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test 3 """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test 4 """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test 5 """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test 6 """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test 7 """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test 8 """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test 9 """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test 10 """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test 11 """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test 12 """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()

