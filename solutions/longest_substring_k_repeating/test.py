import unittest
from .solution import longestSubstring

class TestCase(unittest.TestCase):

    def test_example_one(self):
        s = 'aaabb'
        k = 3
        self.assertEqual(longestSubstring(s, k), 3)

    def test_example_two(self):
        s = 'ababbc'
        k = 2
        self.assertEqual(longestSubstring(s, k), 5)