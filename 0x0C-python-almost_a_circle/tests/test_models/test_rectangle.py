#!/usr/bin/python3
""" test rectangle.py """
import unittest
import pep8
"""import os
from io import StringIO
from unittest.mock import patch"""
from models import rectangle
from models import base
Rectangle = rectangle.Rectangle
Base = base.Base



class Test_Rectangle(unittest.TestCase):
    """ class test_rectangle task 1 """
    def test_pep8_conformance(self):
        """ Test that pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """ test docstrings """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.check_height_with.__doc__)
        self.assertIsNotNone(Rectangle.check_x_y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_main(self):
        """ test main task 2 """
        Base._Base__nb_objects = 0
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
        r4 = Rectangle(210, 22, 10, 30)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.width, 210)
        self.assertEqual(r4.height, 22)
        self.assertEqual(r4.x, 10)
        self.assertEqual(r4.y, 30)
        r5 = Rectangle(210, 22, 10, 30, 34)
        self.assertEqual(r5.id, 34)
        self.assertEqual(r5.width, 210)
        self.assertEqual(r5.height, 22)
        self.assertEqual(r5.x, 10)
        self.assertEqual(r5.y, 30)

    def test_task_3(self):
        """ test task 3 main """
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, "2")
        the_exception = ar.exception
        self.assertEqual(str(the_exception), "height must be an integer")

        with self.assertRaises(ValueError) as ar:
            r1 = Rectangle(10, 2)
            r1.width = -10
        the_exception = ar.exception
        self.assertEqual(str(the_exception), "width must be > 0")

        with self.assertRaises(TypeError) as ar:
            r1 = Rectangle(10, 2)
            r1.x = {}
        the_exception = ar.exception
        self.assertEqual(str(the_exception), "x must be an integer")

        with self.assertRaises(ValueError) as ar:
            Rectangle(10, 2, 3, -1)
        the_exception = ar.exception
        self.assertEqual(str(the_exception), "y must be > 0")

    def test_task_4(self):
        """ test task 4 main """
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    """def test_task_5(self):"""
    """ test task 5 main """
    """ Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6)
        out = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), out)
        r1 = Rectangle(2, 2)
        out = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), out)"""

    def test_task_6(self):
        """ test task 6 main """
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    """def test_task_7(self):"""
    """ test task 7 main """
    """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        out = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), out)
        r2 = Rectangle(3, 2, 1, 0)
        out = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), out)"""

    def test_task_8(self):
        """ test task 8 main """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_task_9(self):
        """ test task 9 main """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_task_13(self):
        """ class test_square task 13 """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                         'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

    def test_task_13(self):
        """ class test_square task 13 """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1,
                                      'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1,\
 "height": 7, "width": 10}]')
        self.assertEqual(type(json_dictionary), str)
