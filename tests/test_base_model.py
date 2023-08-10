#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ class Test basemodel options"""

    def __init__(self, *args, **keywor_args):
        """ model initiate"""
        super().__init__(*args, **keywor_args)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ model setup"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except BaseException:
            pass

    def test_default(self):
        """ model test default valus"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_keywor_args(self):
        """ model test word arguments"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_keywor_args_int(self):
        """ model test word arguments 2"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ model test string valus insertion"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ model test valus added to dictionary """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_keywor_args_none(self):
        """ model test no words arguments"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_keywor_args_one(self):
        """ model test multi words arguments """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ model test """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ model test """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ model test """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()

