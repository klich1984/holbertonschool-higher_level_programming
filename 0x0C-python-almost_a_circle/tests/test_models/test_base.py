#!/usr/bin/python3
"""[summary]
"""

import unittest
from models import base
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class testBase(unittest.TestCase):

    def test_doc_class(self):

        self.assertTrue(len(Base.__doc__) > 0)

    def test_doc_file(self):

        self.assertTrue(len(base.__doc__) > 0)

    def test_doc_init(self):

        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_doc_to_json_string(self):

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def test_doc_save_to_file(self):

        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_doc_from_json_string(self):

        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_doc_create(self):

        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_doc_load_from_file(self):

        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_id(self):
        test = Base()
        self.assertEqual(test.id, 1)
        test = Base()
        self.assertEqual(test.id, 2)
        test = Base(12)
        self.assertEqual(test.id, 12)