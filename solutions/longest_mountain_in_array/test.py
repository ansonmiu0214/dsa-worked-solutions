import unittest
from .solution import longestMountain

class TestCase(unittest.TestCase):

    def test_example_one(self):
        arr = [2,1,4,7,3,2,5]
        self.assertEqual(longestMountain(arr), 5)
    
    def test_flat_terrain(self):
        arr = [2,2,2]
        self.assertEqual(longestMountain(arr), 0)

    def test_ascent(self):
        arr = list(range(5))
        self.assertEqual(longestMountain(arr), 0)
    
    def test_descent(self):
        arr = list(reversed(range(5)))
        self.assertEqual(longestMountain(arr), 0)