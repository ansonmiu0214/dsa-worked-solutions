import unittest

from .solution import maximalNetworkRank

class TestCase(unittest.TestCase):

    def test_example_one(self):
        n = 4
        roads = [[0,1],[0,3],[1,2],[1,3]]
        self.assertEqual(maximalNetworkRank(n, roads), 4)

    def test_example_two(self):
        n = 5
        roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        self.assertEqual(maximalNetworkRank(n, roads), 5)
    
    def test_example_three(self):
        n = 8
        roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
        self.assertEqual(maximalNetworkRank(n, roads), 5)