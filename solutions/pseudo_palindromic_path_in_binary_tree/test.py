import unittest

from .solution import pseudoPalindromicPaths
from ..utils import TreeNode

class TestCase(unittest.TestCase):

    def test_example_one(self):
        root = TreeNode.fromList([2,3,1,3,1,None,1])
        self.assertEqual(pseudoPalindromicPaths(root), 2)
        
    def test_example_two(self):
        root = TreeNode.fromList([2,1,1,1,3,None,None,None,None,None,1])
        self.assertEqual(pseudoPalindromicPaths(root), 1)
        
    def test_no_path(self):
        root = TreeNode.fromList([9])
        self.assertEqual(pseudoPalindromicPaths(root), 1)