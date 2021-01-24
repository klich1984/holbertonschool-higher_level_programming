#!/usr/bin/python3
"""Test base.py"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """create class Base for test program"""

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
