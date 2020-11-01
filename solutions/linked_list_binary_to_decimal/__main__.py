from .solution import getDecimalValue
from ..utils import ListNode

binaryNumber = list(map(int, input().strip().split(',')))
linkedList = ListNode.fromList(binaryNumber)
decimalValue = getDecimalValue(linkedList)
print(f'{binaryNumber} = {decimalValue}')