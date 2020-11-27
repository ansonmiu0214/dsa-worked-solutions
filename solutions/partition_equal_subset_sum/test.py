import unittest
from .solution import canPartition

class TestCase(unittest.TestCase):

    def test_example_one(self):
        nums = [1,5,11,5]
        self.assertTrue(canPartition(nums))

    def test_example_two(self):
        nums = [1,2,3,5]
        self.assertFalse(canPartition(nums))