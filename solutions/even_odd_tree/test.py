import unittest
from .solution import isEvenOddTree
from ..utils import TreeNode

class TestCase(unittest.TestCase):

    def test_example_one(self):
        nodes = [1,10,4,3,None,7,9,12,8,6,None,None,2]
        root = TreeNode.fromList(nodes)
        self.assertTrue(isEvenOddTree(root))

    def test_example_two(self):
        nodes = [5,4,2,3,3,7]
        root = TreeNode.fromList(nodes)
        self.assertFalse(isEvenOddTree(root))
    
    def test_example_three(self):
        nodes = [5,9,1,3,5,7]
        root = TreeNode.fromList(nodes)
        self.assertFalse(isEvenOddTree(root))

    def test_example_four(self):
        nodes = [1]
        root = TreeNode.fromList(nodes)
        self.assertTrue(isEvenOddTree(root))

    def test_example_five(self):
        nodes = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
        root = TreeNode.fromList(nodes)
        self.assertTrue(isEvenOddTree(root))