import unittest
from .solution import canPlaceFlowers

class TestCase(unittest.TestCase):

    def test_example_one(self):
        flowerBed = [1,0,0,0,1]
        n = 1
        self.assertTrue(canPlaceFlowers(flowerBed, n))

    def test_example_two(self):
        flowerBed = [1,0,0,0,1]
        n = 2
        self.assertFalse(canPlaceFlowers(flowerBed, n))