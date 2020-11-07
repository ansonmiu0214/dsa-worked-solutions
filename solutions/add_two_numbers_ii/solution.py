from ..utils import ListNode
from typing import Optional, Tuple

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Adds two numbers encoded in lists `l1` and `l2`.
    Returns the sum as a ListNode."""

    def length(node: Optional[ListNode]) -> int:
        """Returns length of linked list."""

        return 0 if node is None else 1 + length(node.next)

    def sumAndCarry(first: ListNode,
                    numDigitsFirst: int,
                    second: ListNode,
                    numDigitsSecond: int) -> Tuple[ListNode, int]:
        """Adds two numbers encoded in `first` and `second`.
        Returns a tuple of the sum (as a ListNode) and any carry-over."""

        if numDigitsFirst == 0 or numDigitsSecond == 0:
            return None, 0

        if numDigitsFirst > numDigitsSecond:
            # `first` is longer -- sum the tail of `first` with `second`
            # to align the digits.
            tail, carry = sumAndCarry(first.next, numDigitsFirst - 1, second, numDigitsSecond)
            newCarry, sumVal = divmod(first.val + carry, 10)
        elif numDigitsSecond > numDigitsFirst:
            # `second` is longer -- sum the tail of `second` with `first`
            # to align the digits.
            tail, carry = sumAndCarry(first, numDigitsFirst, second.next, numDigitsSecond - 1)
            newCarry, sumVal = divmod(second.val + carry, 10)
        else:
            # Digits aligned -- sum both tails and append it
            # after the sum of the heads.
            tail, carry = sumAndCarry(first.next, numDigitsFirst - 1, second.next, numDigitsSecond - 1)
            newCarry, sumVal = divmod(first.val + second.val + carry, 10)
        
        sumNode = ListNode(sumVal, next=tail)
        return sumNode, newCarry

    tail, carry = sumAndCarry(l1, length(l1), l2, length(l2))
    sumNode = ListNode(carry, next=tail) if carry > 0 else tail
    return sumNode