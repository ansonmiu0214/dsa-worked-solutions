import unittest
from .solution import connect, TreeNodeWithNext

class TestCase(unittest.TestCase):

    def test_example_one(self):
        tree = [1,2,3,4,5,None,7]
        root = TreeNodeWithNext.fromList(tree)
        connected = connect(root)
        self.assertListEqual(connected.toList(), [1,'#',2,3,'#',4,5,7,'#'])