import unittest

from .solution import findMinHeightTrees

class TestCase(unittest.TestCase):

    def test_example_one(self):
        n = 4
        edges = [[1,0],[1,2],[1,3]]
        self.assertListEqual(findMinHeightTrees(n, edges), [1])
        
    def test_example_two(self):
        n = 6
        edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        self.assertListEqual(findMinHeightTrees(n, edges), [3,4])
        
    def test_no_arcs(self):
        n = 1
        edges = []
        self.assertListEqual(findMinHeightTrees(n, edges), [0])

    def test_example_four(self):
        n = 2
        edges = [[0,1]]
        self.assertListEqual(findMinHeightTrees(n, edges), [0,1])