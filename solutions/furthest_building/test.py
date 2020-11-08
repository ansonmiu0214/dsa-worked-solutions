import unittest

from .solution import furthestBuilding

class TestCase(unittest.TestCase):

    def test_example_one(self):
        heights = [4,2,7,6,9,14,12]
        bricks = 5
        ladders = 1
        self.assertEqual(furthestBuilding(heights, bricks, ladders), 4)
        
    def test_example_two(self):
        heights = [4,12,2,7,3,18,20,3,19]
        bricks = 10
        ladders = 2
        self.assertEqual(furthestBuilding(heights, bricks, ladders), 7)

    def test_example_three(self):
        heights = [14,3,19,3]
        bricks = 17
        ladders = 0
        self.assertEqual(furthestBuilding(heights, bricks, ladders), 3)