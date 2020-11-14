---
title: Even odd tree
date: 2020-11-14
shortname: even_odd_treee
leetcode: https://leetcode.com/problems/even-odd-tree
tags: [binary tree, BFS]
---

## Problem

> A binary tree is named __Even-Odd__ if it meets the following conditions:
> 
> * The root of the binary tree is at level index `0`, its children are at level index `1`, their children are at level index `2`, etc.
> * For every __even-indexed__ level, all nodes at the level have __odd__ integer values in __strictly increasing__ order (from left to right).
> * For every __odd-indexed__ level, all nodes at the level have __even__ integer values in __strictly decreasing__ order (from left to right).
> 
> Given the `root` of a binary tree, return `true` if the binary tree is __Even-Odd__, otherwise return `false`.

## Some questions to ask

* What to return for empty node?

## Approach

Apply breadth-first search to process nodes in order of level,
keeping track of the parity of the level.

Also keep track of the previous node in order to compare values
to check whether it is strictly increasing/decreasing.

As parity is either 0 or 1, the solution below stores the validation
functions in a list, which can be accessed using the level parity.

```python
def isEvenOddTree(root: TreeNode) -> bool:
    """Return true iff tree rooted at 'root' is even-odd tree."""

    if root is None:
        return True
    
    checkNodeForParity = [
        lambda x: x % 2 != 0,   # Even-index nodes must be odd.
        lambda x: x % 2 == 0,   # Odd-index nodes must be even.
    ]

    checkPrevForParity = [
        lambda prev, curr: prev < curr, # Even-index lvl increases (->)
        lambda prev, curr: curr < prev, # Odd-index lvl decreases (<-)
    ]

    prev = None
    prevParity = None

    # Check for conditions using BFS, keeping track of level parity.
    queue = deque([(root, 0)])
    while queue:
        currNode, parity = queue.popleft()
        curr = currNode.val

        if not checkNodeForParity[parity](curr):
            return False

        if prevParity == parity:
            if not checkPrevForParity[parity](prev, curr):
                return False
    
        prev = curr
        prevParity = parity

        if currNode.left is not None:
            queue.append((currNode.left, 1 - parity))
    
        if currNode.right is not None:
            queue.append((currNode.right, 1 - parity))
    
    return True
```

### Complexity
Let n be the number of nodes in the tree.

* O(n) time complexity, from traversing the whole tree
* O(n) space complexity, as queue can grow to hold at most ceil(n/2 ) nodes
