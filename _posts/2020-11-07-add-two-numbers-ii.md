---
title: Add two numbers ii
date: 2020-11-07
shortname: add_two_numbers_ii
leetcode: https://leetcode.com/problems/add-two-numbers-ii
tags: [linked list, recursion, monthly challenge]
---

## Problem

> You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and 
> each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
> 
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.
> 
> What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

## Some questions to ask

* Is empty list valid input?

## Approach

Devise a helper function to perform the sum and keep track of the carry.

We can only compute the sum accurately when the digits of both numbers
are aligned. To do so, we also keep track of the number of digits in both numbers
(which would be the length of the linked list), and process as follow:

* If `l1` is longer than `l2` (e.g. `[1,9,2]` + `[4,5]`),
we invoke the helper function on `l1.next` and `l2`, which returns the sum (37) and carry (1) for 92 + 45.
The result is prepending `l1.val + carry` to the sum returned by the recursive call.

* If `l2` is longer than `l1`, we do the same as above but swapping `l2` and `l1`.

* If both lists have the same length, we invoke the helper function on `l1.next` and `l2.next`,
but prepend the sum from the recursive call with `l1.val + l2.val + carry`, since the digits are aligned.

```python
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
```

### Complexity
Let n be the length of the longest linked list.

* O(n) time complexity, from traversing the list
* O(1) space complexity, if ignoring the recursion overhead

### Other approaches

You could traverse both lists to convert them into numbers, i.e.

```python
def linkedListToNum(node: ListNode) -> int:
    num = 0
    while node is not None:
        num *= 10
        num += node.val
        node = node.next
    return num
```

Then perform the addition operation and convert the number back to a list, i.e.

```python
def numToLinkedList(num: int) -> ListNode:
    if num == 0:
        return ListNode(0)

    root = None
    while num > 0:
        num, digit = divmod(num, 10)
        digitNode = ListNode(digit)
        digitNode.next = root
        root = digitNode
    return root
```

This would still take O(n) time, but also O(n) space for the intermediate lists.