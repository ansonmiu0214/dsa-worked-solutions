import unittest
from .solution import lcaDeepestLeaves
from ..utils import TreeNode

class TestCase(unittest.TestCase):

    def test_example_one(self):
        tree = [3,5,1,6,2,0,8,None,None,7,4]
        root = TreeNode.fromList(tree)
        self.assertEqual(lcaDeepestLeaves(root), TreeNode.fromList([2,7,4]))

    def test_example_two(self):
        tree = [1]
        root = TreeNode.fromList(tree)
        self.assertEqual(lcaDeepestLeaves(root), root)

    def test_example_three(self):
        tree = [0,1,3,None,2]
        root = TreeNode.fromList(tree)
        self.assertEqual(lcaDeepestLeaves(root), TreeNode.fromList([2]))