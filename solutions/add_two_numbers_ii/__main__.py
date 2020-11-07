from typing import List

from .solution import addTwoNumbers
from ..utils import ListNode

def numToList(num: int) -> List[int]:
    if num == 0:
        return []

    head, tail = divmod(num, 10)
    return [*numToList(head), tail]

def linkedListToNum(node: ListNode, acc: int = 0) -> int:
    if node is None:
        return acc
    return linkedListToNum(node.next, acc * 10 + node.val)

print('Enter two (space-separated) numbers:', end=' ')
first, second, *_ = list(map(int, input().strip().split(' ')))

l1, l2 = numToList(first), numToList(second)
sumNode = addTwoNumbers(ListNode.fromList(l1), ListNode.fromList(l2))

print(f'Sum = {linkedListToNum(sumNode)}')

