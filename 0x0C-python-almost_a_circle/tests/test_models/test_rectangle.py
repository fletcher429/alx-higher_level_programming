#!/usr/bin/python3
"""
import the rectangle module
"""
from models.rectangle import Rectangle
"""
imports the unittest module
"""
import unittest

"""
define a class to run the test
"""
class TestRectangle(unittest.TestCase):
    """
    define the test constructor of the
    """
    def test_constructor(self):
        # Test the constructor
        rect = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)
    def test_instantation(self):
        rec = Rectangle(1, 2)
        self.assertIsInstance(rec, Rectangle)

        rec2 = Rectangle(1, 2, 3)
        self.assertIsInstance(rec2, Rectangle)


        rec3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(rec3, Rectangle)
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
