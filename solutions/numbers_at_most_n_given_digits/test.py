import unittest
from .solution import atMostNGivenDigitSet

class TestCase(unittest.TestCase):

    def test_example_one(self):
        digits = [1,3,5,7]
        n = 100
        self.assertEqual(atMostNGivenDigitSet(digits, n), 20)

    def test_example_twp(self):
        digits = [1,4,9]
        n = 1000000000
        self.assertEqual(atMostNGivenDigitSet(digits, n), 29523)
        
    def test_example_three(self):
        digits = [7]
        n = 8
        self.assertEqual(atMostNGivenDigitSet(digits, n), 1)

    def test_example_one(self):
        digits = [9]
        n = 55
        self.assertEqual(atMostNGivenDigitSet(digits, n), 1)