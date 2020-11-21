import unittest
from .solution import getSmallestString

class TestCase(unittest.TestCase):

    def test_example_one(self):
        n = 3
        k = 27
        self.assertEqual(getSmallestString(n, k), 'aay')

    def test_example_two(self):
        n = 5
        k = 73
        self.assertEqual(getSmallestString(n, k), 'aaszz')