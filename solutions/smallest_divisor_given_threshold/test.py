import unittest

from .solution import smallestDivisor
from ..utils.list import flatten

class TestCase(unittest.TestCase):

    def test_example_one(self):
        nums = [1,2,5,9]
        threshold = 6
        self.assertEqual(smallestDivisor(nums, threshold), 5)
        
    def test_example_two(self):
        nums = [2,3,5,7,11]
        threshold = 11
        self.assertEqual(smallestDivisor(nums, threshold), 3)

    def test_example_three(self):
        nums = [19]
        threshold = 5
        self.assertEqual(smallestDivisor(nums, threshold), 4)