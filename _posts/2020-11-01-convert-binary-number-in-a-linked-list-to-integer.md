---
title: Convert binary number in a linked list to integer
date: 2020-11-01
shortname: linked_list_binary_to_decimal
leetcode: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
tags: [linked list, recursion, monthly challenge]
---

## Problem

> Given `head` which is a reference node to a singly-linked list. 
> The value of each node in the linked list is either 0 or 1. 
> The linked list holds the binary representation of a number.
> 
> Return the _decimal value_ of the number in the linked list.

## Some questions to ask
* Can the list be empty?
* What is the binary representation? Signed/unsigned integers? Floating point?
* Can I use extra space?

## Approach

We can take a recursive approach, as a linked list is a recursive data structure.

Using `[1,0,1]` as an example, we destructure the list into its head `1` and tail `[0,1]`. 

1. The decimal value for the tail is 1.
2. Assume we also know that the length of the tail is 2.
3. The result would be left-shifting the current binary digit by the tail length (`1 << 2 = 4`) plus the decimal value for the tail, i.e. `4 + 1 = 5`.

```python
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
```

### Complexity
Let n be the length of the linked list.

* O(n) time, as you iterate over the entire list
* O(n) space, as the recursive function goes n levels deep

## Other approaches

Another would be to process each binary digit in turn and build up to the decimal value by left-shifting on every iteration.

```python
def getDecimalValue(node: ListNode):
    decimalValue = 0
    while node is not None:
        decimalValue <<= 1
        decimalValue += node.val
        node = node.next
    return decimalValue
```

This yields O(n) time complexity and O(1) space complexity.