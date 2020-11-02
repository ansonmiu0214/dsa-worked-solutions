import unittest

from .solution import spiralOrder
from ..utils.list import flatten

class TestCase(unittest.TestCase):

    def test_empty(self):
        self.assertListEqual(spiralOrder([]), [])
        
    def test_single_row(self):
        row = [[1,2,3]]
        self.assertListEqual(spiralOrder(row), flatten(row))

    def test_single_column(self):
        column = [[1],[2],[3]]
        self.assertListEqual(spiralOrder(column), flatten(column))
    
    def test_square(self):
        square = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        self.assertListEqual(spiralOrder(square), [1,2,3,6,9,8,7,4,5])
    
    def test_rectangle(self):
        rectangle = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
        ]
        self.assertListEqual(spiralOrder(rectangle), [1,2,3,4,8,12,11,10,9,5,6,7])