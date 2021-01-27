#!/usr/bin/python3
"""Test base.py"""
import pep8
import unittest
import models.base
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


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
        self.assertIsNotNone(models.base.__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_main(self):
        """test main"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_others_cases(self):
        """other cases"""
        b1 = Base("klich")
        self.assertEqual(b1.id, "klich")
        b1 = Base(-69)
        self.assertEqual(b1.id, -69)
