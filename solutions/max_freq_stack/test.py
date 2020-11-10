import unittest
from .solution import FreqStack
from ..utils import proxyCall

class TestCase(unittest.TestCase):

    def setUp(self):
        self.stack = FreqStack()

    def test_example_one(self):
        allCmds = ["push","push","push","push","push","push","pop","pop","pop","pop"]
        allArgs = [[5],[7],[5],[7],[4],[5],[],[],[],[]]
        output = [proxyCall(self.stack, cmd, args)
                  for cmd, args in zip(allCmds, allArgs)]
        self.assertListEqual(output, [None,None,None,None,None,None,5,7,5,4])

