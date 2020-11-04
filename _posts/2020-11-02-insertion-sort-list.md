---
title: Insertion sort list
date: 2020-11-02
shortname: insertion_sort_list
leetcode: https://leetcode.com/problems/insertion-sort-list
tags: [linked list, recursion, monthly challenge]
---

## Problem

> Implement insertion sort on a linked list of numbers.

## Some questions to ask
* Return a new list? Or perform sorting in-place?
* Are the numbers integers or floats?
* Can the list be empty?

## Approach
Let our solution be a function parameterised by the input list (`head`)
and an accumulator list (`res`).
We process each element of the list in turn and accumulate the
sorted elements in a new list.

At each iteration, we insert `head.val` into `res` (using the insertion
sort algorithm), and recursively call our solution on the tail of
the input list (`head.next`) with the new `res`. 
The invariant is that `res` is always sorted.

The base case is when `head is None`, where we return the accumulator.

To insert `head.val` into `res`, we traverse the `res` list with two pointers,
`prev` and `curr`, and insert `head.val` where `prev.val <= head.val <= curr.val`,
i.e. create new node and update pointers.

```python
def insertionSortList(head: ListNode, result: ListNode = None) -> ListNode:
    """Sort linked list represented by 'head' using insertion sort,
    and return new sorted linked list."""
    
    if head is None:
        return result
    
    tail = head.next
    node = ListNode(head.val)
    
    prev = None
    curr = result
    while curr is not None and node.val > curr.val:
        prev = curr
        curr = curr.next
    
    if prev is None:
        node.next = curr
        return insertionSortList(tail, node)
    else:
        prev.next = node
        node.next = curr
        return insertionSortList(tail, result)
```

### Complexity
Let n be the length of the linked list.

* O(n^2) time, as the worst-case number of comparions is 1 + 2 + ... + n-1 = n(n-1)/2
* O(n) space, as you keep track of the input and ouput lists
