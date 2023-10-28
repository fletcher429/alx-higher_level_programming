import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
         res = calc.add(10, 55)
         self.assertEqual(res, 65)
if __name__ == '__main__':
    unittest.main()