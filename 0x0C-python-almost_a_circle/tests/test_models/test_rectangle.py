#!/usr/bin/python3
""" test rectangle.py """


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ class test_rectangle task 1 """
    def test_main(self):
        """ test main """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_other_case(self):
        """ other cases """
        r1 = Rectangle(210, 22, 10, 30)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 210)
        self.assertEqual(r1.height, 22)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 30)
        r2 = Rectangle(210, 22, 10, 30, 34)
        self.assertEqual(r2.id, 34)
        self.assertEqual(r2.width, 210)
        self.assertEqual(r2.height, 22)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 30)

    def test_task_3(self):
        """ test task 3 """
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, "2")
        self.assertEqual(str(ar.exception), "height must be an integer")

        with self.assertRaises(ValueError) as ar:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(ar.exception), "width must be > 0")

        with self.assertRaises(TypeError) as ar:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(ar.exception), "x must be an integer")

        with self.assertRaises(ValueError) as ar:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(ar.exception), "y must be > 0")

    def test_task_4(self):
        """ test task 4 """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)