import unittest
from .solution import mirrorReflection

class TestCase(unittest.TestCase):

    def test_example_one(self):
        p = 2
        q = 1
        self.assertEqual(mirrorReflection(p, q), 2)