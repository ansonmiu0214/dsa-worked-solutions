---
title: Increasing order search tree
date: 2020-12-03
shortname: increasing_order_search_tree
leetcode: https://leetcode.com/problems/increasing-order-search-tree
tags: [tree, recursion, monthly challenge]
---

## Problem

> Given the `root` of a binary search tree,
> rearrange the tree in in-order
> so that the leftmost node in the tree is now the root of the tree,
> and every node has no left child and only one right child.

## Some questions to ask

* Can the input tree be empty?

## Approach

This is essentially transforming the binary search tree into a singly-linked list,
where the 'next' pointer is represented by the right child of the `TreeNode`.

Take a recursive approach: define a function that performs the transformation
but returns the head and tail of the 'linked list'.
By doing so, we can adjust the `right` pointers accordingly, without having to traverse
the 'list' every time to append to the tail.

```python
def transformIntoSortedList(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
    """Transform binary search tree rooted at the specified 'node' into a
    linked list. Return the head and tail of the linked list.""" 

    if node.left is not None:
        # Transform left child into linked list, and connect the *tail*
        # of that linked list to the current node.
        head, leftTail = transformIntoSortedList(node.left)
        node.left = None
        leftTail.right = node
    else:
        head = node

    if node.right is not None:
        # Transform right child into linked list, and connect the current
        # node to the *head* of that linked list.
        mid, tail = transformIntoSortedList(node.right)
        node.right = mid
    else:
        tail = node

    return head, tail


def increasingBST(root: TreeNode) -> TreeNode:
    """Return linked list representation of the specified 'root' BST."""

    head, _ = transformIntoSortedList(root)
    return head

```

### Complexity
Let n be the number of nodes in `root`.

* O(n) time complexity, from visiting each node once
* O(log(n)) space complexity, i.e. the height of the tree, as the recursive calls go
as deep as the tree

### Other approaches

An iterative solution is possible, and involves a stack to
perform the in-order traversal.

```python
def increasingBST(root: TreeNode) -> TreeNode:
    newRoot = None
    curr = None
    
    stack = [(root, False)]
    while stack:
        
        node, seenLeft = stack.pop()
        
        if not seenLeft:
            stack.append((node, True))
            
            if node.left:
                stack.append((node.left, False))
        else:
            if newRoot is None:
                newRoot = node
                curr = node
                curr.left = None
            else:
                curr.right = node
                curr = node
                curr.left = None
                
            if node.right:
                stack.append((node.right, False))
    
    return newRoot
```
