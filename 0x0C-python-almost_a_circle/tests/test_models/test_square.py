#!/usr/bin/python3
""" test square.py """
import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    """ class test_square task 10 """
    def test_task_10(self):
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        out = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), out)
        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        out = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), out)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        out = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(), out)

    def test_task_11(self):
        """ class test_square task 11 """
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError) as ar:
            s1.size = "9"
        the_exception = ar.exception
        self.assertEqual(str(the_exception), "width must be an integer")

    def test_task_12(self):
        """ class test_square task 12 """
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        # special case
        s1.update(1, 2, 3, 4, x=8, y=9)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_task_14(self):
        """ class test_square task 14 """
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        self.assertEqual(s2.__str__(), "[Square] (2) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(s2.__str__(), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)
