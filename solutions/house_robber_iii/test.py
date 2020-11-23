import unittest
from .solution import rob
from ..utils import TreeNode

class TestCase(unittest.TestCase):

    def test_example_one(self):
        tree = [3,2,3,None,3,None,1]
        root = TreeNode.fromList(tree)
        self.assertEqual(rob(root), 7)
    
    def test_example_two(self):
        tree = [3,4,5,1,3,None,1]
        root = TreeNode.fromList(tree)
        self.assertEqual(rob(root), 9)