import unittest

from .solution import getDecimalValue
from ..utils import ListNode

class TestCase(unittest.TestCase):

    def test_zero(self):
        binary = ListNode.fromList([0])
        self.assertEqual(getDecimalValue(binary), 0)
        
    def test_one(self):
        binary = ListNode.fromList([1])
        self.assertEqual(getDecimalValue(binary), 1)

    def test_simple(self):
        binary = ListNode.fromList([1,0,1])
        self.assertEqual(getDecimalValue(binary), 5)
    
    def test_large_input(self):
        binary = ListNode.fromList([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
        self.assertEqual(getDecimalValue(binary), 18880)