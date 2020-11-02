from .solution import insertionSortList
from ..utils import ListNode

unsortedList = list(map(int, input().strip().split(',')))
sortedList = insertionSortList(ListNode.fromList(unsortedList))
print(f'Unsorted: {unsortedList}')
print(f'Sorted: {sortedList.toList()}')