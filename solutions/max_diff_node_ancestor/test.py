import unittest
from .solution import maxAncestorDiff
from ..utils import TreeNode

class TestCase(unittest.TestCase):
    
    def test_example_one(self):
        nodes = [8,3,10,1,6,None,14,None,None,4,7,13]
        root = TreeNode.fromList(nodes)
        self.assertEqual(maxAncestorDiff(root), 7)
    
    def test_example_two(self):
        nodes = [1,None,2,None,0,3,None]
        root = TreeNode.fromList(nodes)
        self.assertEqual(maxAncestorDiff(root), 3)