import unittest
from .solution import maxSlidingWindow

class TestCase(unittest.TestCase):

    def test_example_one(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        maxWindow = [3,3,5,5,6,7]
        self.assertListEqual(maxSlidingWindow(nums, k), maxWindow)

    def test_example_two(self):
        nums = [1,-1]
        k = 1
        maxWindow = [1,-1]
        self.assertListEqual(maxSlidingWindow(nums, k), maxWindow)

    def test_example_three(self):
        nums = [1]
        k = 1
        maxWindow = [1]
        self.assertListEqual(maxSlidingWindow(nums, k), maxWindow)

    def test_example_four(self):
        nums = [9,11]
        k = 2
        maxWindow = [11]
        self.assertListEqual(maxSlidingWindow(nums, k), maxWindow)

    def test_example_five(self):
        nums = [4,-2]
        k = 2
        maxWindow = [4]
        self.assertListEqual(maxSlidingWindow(nums, k), maxWindow)