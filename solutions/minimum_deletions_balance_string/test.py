import unittest
from .solution import minimumDeletions

class TestCase(unittest.TestCase):

    def test_example_one(self):
        s = 'aababbab'
        self.assertEqual(minimumDeletions(s), 2)

    def test_example_two(self):
        s = 'bbaaaabb'
        self.assertEqual(minimumDeletions(s), 2)