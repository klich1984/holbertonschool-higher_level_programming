#!/usr/bin/python3
"""Test base.py"""
import pep8
import unittest
from models import base
from models.base import Base


class Test_Base(unittest.TestCase):
    """create class Base for test program"""
    def test_pep8_conformance(self):
        """ Test that pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """ test docstrings """
        #self.assertIsNotNone(models.base.__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_id(self):
        """test main"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1 = Base()
        self.assertEqual(b1.id, 4)

    def test_others_cases(self):
        """other cases"""
        b1 = Base("klich")
        self.assertEqual(b1.id, "klich")
        b1 = Base(-69)
        self.assertEqual(b1.id, -69)
