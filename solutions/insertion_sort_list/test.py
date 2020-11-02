import unittest

from .solution import insertionSortList
from ..utils import ListNode

class TestCase(unittest.TestCase):

    def test_empty(self):
        sortedList = insertionSortList(ListNode.fromList([]))
        self.assertIsNone(sortedList)
        
    def test_singleton(self):
        singleton = [1]
        sortedList = insertionSortList(ListNode.fromList(singleton))
        self.assertEqual(sortedList.toList(), singleton)

    def test_already_sorted(self):
        alreadySorted = [1,2,3,4,5]
        sortedList = insertionSortList(ListNode.fromList(alreadySorted))
        self.assertEqual(sortedList.toList(), alreadySorted)
    
    def test_reverse_sorted(self):
        reverseSorted = [5,4,3,2,1]
        sortedList = insertionSortList(ListNode.fromList(reverseSorted))
        self.assertEqual(sortedList.toList(), list(reversed(reverseSorted)))
    
    def test_unsorted(self):
        unsorted = [5,3,4,2,6,1]
        sortedList = insertionSortList(ListNode.fromList(unsorted))
        self.assertEqual(sortedList.toList(), list(sorted(unsorted)))