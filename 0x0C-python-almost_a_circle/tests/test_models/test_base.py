#!/usr/bin/python3
"""
import model.base module
"""
from models.base import Base
"""
import unittest module
"""
import unittest
"""
create class for the tests
"""
class test_base(unittest.TestCase):
    """
    define function constructor
    """
    def test_constructor(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
    def test_con_with_str(self):
        b1 = Base("hello")
        self.assertEqual(b1.id, "hello")
    def test_con_inc(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
    def test_incremental(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)
"""
Checks if the test is run as the main program
"""
if __name__ == "__main__":
    unittest.main()