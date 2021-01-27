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

    @classmethod
    def setUpClass(self): 
        ''' Setting the context for the test'''
        self.test = Base()


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

 

    def test_base_id(self):
        '''' Checks instantiation of Base Class'''

        self.assertEqual(self.test.id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(50).id, 50)

