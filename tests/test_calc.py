import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calc.plus(2,7), 10)
    def test_minus(self):
        self.assertEqual(calc.minus(10,3), 7)
