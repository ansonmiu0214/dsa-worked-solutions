from math import sqrt
import unittest
from .solution import validSquare

class TestCase(unittest.TestCase):

    def test_same_point(self):
        p1 = [0,0]
        p2 = [0,0]
        p3 = [0,0]
        p4 = [0,0]

        self.assertFalse(validSquare(p1, p2, p3, p4))

    def test_valid_square(self):
        p1 = [0,0]
        p2 = [1,1]
        p3 = [1,0]
        p4 = [0,1]

        self.assertTrue(validSquare(p1, p2, p3, p4))
    
    def test_rectangle(self):
        p1 = [0,0]
        p2 = [2,1]
        p3 = [2,0]
        p4 = [0,1]

        self.assertFalse(validSquare(p1, p2, p3, p4))

    def test_rotated_square(self):
        p1 = [3 - sqrt(6), 3 + sqrt(2)]
        p2 = [3 + sqrt(2), 3 + sqrt(6)]
        p3 = [3 - sqrt(2), 3 - sqrt(6)]
        p4 = [3 + sqrt(6), 3 - sqrt(2)]

        self.assertTrue(validSquare(p1, p2, p3, p4))