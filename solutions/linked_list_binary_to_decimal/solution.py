from ..utils import ListNode

def getDecimalValue(head: ListNode) -> int:
    """Return decimal value of binary number encoded in list."""

    value, _ = getValueAndLength(head)
    return value
        
def getValueAndLength(node: ListNode):
    """Return decimal value of binary number encoded in list,
    along with the length of list."""

    if node is None:
        return 0, 0
    
    tailVal, tailLength = getValueAndLength(node.next)
    if node.val == 0:
        return tailVal, (tailLength + 1)
    return ((node.val << tailLength) + tailVal), (tailLength + 1)