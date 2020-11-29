import unittest
from .solution import canReach

class TestCase(unittest.TestCase):

    def test_example_one(self):
        arr = [4,2,3,0,3,1,2]
        start = 5
        self.assertTrue(canReach(arr, start))

    def test_example_two(self):
        arr = [4,2,3,0,3,1,2]
        start = 0
        self.assertTrue(canReach(arr, start))

    def test_example_three(self):
        arr = [3,0,2,1,2]
        start = 2
        self.assertFalse(canReach(arr, start))