from .solution import getDecimalValue
from ..utils import io, ListNode

print(f'Enter space-separated digits of binary number:', end=' ')
binaryNumber = io.get_list(int)
linkedList = ListNode.fromList(binaryNumber)
decimalValue = getDecimalValue(linkedList)
print(f'{binaryNumber} = {decimalValue}')