import unittest

from .solution import maxProbability

class TestCase(unittest.TestCase):

    def test_example_one(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.2]
        start = 0
        end = 2
        self.assertEqual(maxProbability(n, edges, succProb, start, end), 0.25)
        
    def test_example_two(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.3]
        start = 0
        end = 2
        self.assertEqual(maxProbability(n, edges, succProb, start, end), 0.3)
        
    def test_no_path(self):
        n = 3
        edges = [[0,1]]
        succProb = [0.5]
        start = 0
        end = 2
        self.assertEqual(maxProbability(n, edges, succProb, start, end), 0)