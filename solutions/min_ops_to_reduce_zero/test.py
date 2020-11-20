import unittest
from .solution import minOperations

class TestCase(unittest.TestCase):

    def test_example_one(self):
        nums = [1,1,4,2,3]
        x = 5
        self.assertEqual(minOperations(nums, x), 2)
    
    def test_example_two(self):
        nums = [5,6,7,8,9]
        x = 4
        self.assertEqual(minOperations(nums, x), -1)

    def test_example_one(self):
        nums = [3,2,20,1,1,3]
        x = 10
        self.assertEqual(minOperations(nums, x), 5)