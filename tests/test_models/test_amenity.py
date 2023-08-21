#!/usr/bin/python3

import pep8
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def setUpClass(cls):
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Hot Tub"

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity1), True)

    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity1.name), str)


if __name__ == "__main__":
    unittest.main()
