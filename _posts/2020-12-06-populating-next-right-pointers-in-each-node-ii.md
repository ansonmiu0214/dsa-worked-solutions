---
title: Populating next right pointers in each node ii
date: 2020-12-06
shortname: populating_next_right_pointers_ii
leetcode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
tags: [tree, monthly challenge]
---

## Problem

> Given a binary tree
> 
> ```
> struct Node {
>   int val;
>   Node *left;
>   Node *right;
>   Node *next;
> }
> ```
> 
> Populate each next pointer to point to its next right node.
> If there is no next right node, the next pointer should be set to `NULL`.
> 
> Initially, all next pointers are set to `NULL`.
> 
> **Follow up:**
> 
> * You may only use constant extra space.
> * Recursive approach is fine,
>   you may assume implicit stack space
>   does not count as extra space for this problem.

## Some questions to 

* Would an empty tree be valid input?
* Is it a complete binary tree?

## Approach

Connect the `next` pointer level by level.

Leverage the fact that the current level has its `next` pointers already connected, and traverse the current level using the `next` pointers to connect the level below.

Keep track of the `nextParent`, which would be the leftmost node in the next level, to know which node to proceed to after the current level has been fully connected.

```python
def connect(root: TreeNodeWithNext) -> TreeNodeWithNext:
    """Populate the 'next' pointer of each node in the tree 
    specified by 'root'."""

    if root is None:
        return root

    currParent = root
    while currParent is not None:
        # Connect the nodes in the level below 'currParent', i.e.
        # the level where the children of 'currParent' resides.

        prevNode = None
        nextParent = None
        while currParent is not None:

            # Iterate through children nodes and connect their
            # right pointers.
            for child in (currParent.left, currParent.right):
                if child is None:
                    continue

                # Connect 'next' pointer of 'prevNode' if possible,
                # and update 'prevNode'.
                if prevNode is not None:
                    prevNode.next = child

                prevNode = child
                if nextParent is None:
                    # Found the leftmost node in the next level.
                    nextParent = child
            
            # Go across to next node in the same level.
            currParent = currParent.next
        
        # Set 'currParent' to be the leftmost node in the next level.
        currParent = nextParent

    return root
```

### Complexity

Let n be the number of nodes in `root`.

* O(n) time complexity, from visiting each node
* O(1) space complexity, from just keeping track of `currParent`, `nextParent` and `prev`

### Other approaches

A simpler approach is to apply BFS to perform level-order traversal and connect the `next` pointer by keeping track of the previous node.

This would no longer be a constant space solution, as the size ofthe queue used for BFS depends on the number of nodes in the tree.
