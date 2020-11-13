import unittest
from .solution import MinStack
from ..utils import proxyCall

class TestCase(unittest.TestCase):

    def setUp(self):
        self.stack = MinStack()

    def test_example_one(self):
        commands = ["push","push","push","getMin","pop","top","getMin"]
        args = [[-2],[0],[-3],[],[],[],[]]

        res = [proxyCall(self.stack, command, arg)
                   for command, arg in zip(commands, args)]
        
        self.assertListEqual(res, [None, None, None, -3, None, 0, -2])