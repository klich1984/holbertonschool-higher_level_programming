#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_main_one(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_main_two(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_number_negative(self):
        self.assertEqual(max_integer([-1, -3, -4, -2, -5]), -1)

    def test_one_number(self):
        self.assertEqual(max_integer([5]), 5)

    def test_one_number_negative(self):
        self.assertEqual(max_integer([-198]), -198)

    def test_number_negative_and_positive(self):
        self.assertEqual(max_integer([11, -334, 69, 2, -5]), 69)

    def test_self_number(self):
        self.assertEqual(max_integer([11, 11, 11]), 11)
        self.assertEqual(max_integer([-11, -11, -11]), -11)
