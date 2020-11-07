import unittest

from .solution import addTwoNumbers
from ..utils import ListNode

class TestCase(unittest.TestCase):

    def test_single_digit_no_carry(self):
        num1 = ListNode.fromList([1])
        num2 = ListNode.fromList([2])
        sumNode = addTwoNumbers(num1, num2)
        self.assertListEqual(sumNode.toList(), [3])
        
    def test_single_digit_with_carry(self):
        num1 = ListNode.fromList([8])
        num2 = ListNode.fromList([7])
        sumNode = addTwoNumbers(num1, num2)
        self.assertListEqual(sumNode.toList(), [1,5])

    def test_num1_more_digits_than_num2(self):
        num1 = ListNode.fromList([1,8])
        num2 = ListNode.fromList([7])
        sumNode = addTwoNumbers(num1, num2)
        self.assertListEqual(sumNode.toList(), [2,5])
    
    def test_num1_more_digits_than_num2_with_carry(self):
        num1 = ListNode.fromList([9,8])
        num2 = ListNode.fromList([9])
        sumNode = addTwoNumbers(num1, num2)
        self.assertListEqual(sumNode.toList(), [1,0,7])
    
    def test_commutativity(self):
        num1 = ListNode.fromList([1,8])
        num2 = ListNode.fromList([7])
        self.assertListEqual(addTwoNumbers(num1, num2).toList(), addTwoNumbers(num2, num1).toList())