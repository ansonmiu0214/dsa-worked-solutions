import unittest
from .solution import increasingBST
from ..utils import TreeNode

class TestCase(unittest.TestCase):

    def test_example_one(self):
        tree = [5,3,6,2,4,None,8,1,None,None,None,7,9]
        root = TreeNode.fromList(tree)
        actual = increasingBST(root).toList()
        expected = [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9]
        self.assertListEqual(actual, expected)

    def test_example_two(self):
        tree = [5,1,7]
        root = TreeNode.fromList(tree)
        actual = increasingBST(root).toList()
        expected = [1,None,5,None,7]
        self.assertListEqual(actual, expected)