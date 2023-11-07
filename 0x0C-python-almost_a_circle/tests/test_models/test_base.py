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
"""
Checks if the test is run as the main program
"""
if __name__ == "__main__":
    unittest.main()