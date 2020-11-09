---
title: Maximum difference between node and ancestor
date: 2020-11-09
shortname: max_diff_node_ancestor
leetcode: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor
tags: [binary tree, recursion]
---

## Problem

> Given the root of a binary tree,
> find the maximum value `V` for which 
> there exist different nodes `A` and `B`
> where `V = |A.val - B.val|` and `A` is an ancestor of `B`.
>
> A node `A` is an ancestor of `B` if either: any child of `A` is equal to `B`,
> or any child of `A` is an ancestor of `B`.

## Some questions to ask

* What to do for a singleton tree?
* Is the tree a binary __search__ tree (BST)?
  * For BST, simply take `max(abs(leftMost - root), abs(rightMost - root))`

## Approach

A naive approach would be to traverse the tree using DFS
and, for each node, compute _all_ ancestor differences and pick the maximum.

As the question only concerns with the _maximum_ ancestor difference, it
suffices to only keep track of the extreme ancestor values (i.e. maximum and minimum),
and compute the differences with these two ancestors at each node.

```python
def maxAncestorDiff(node: TreeNode,
                    maxAncestor: Optional[int] = None,
                    minAncestor: Optional[int] = None) -> int:
    """Return maximum difference between any node rooted in
    `tree` and its ancestors, given the encountered
    `maxAncestor` and `minAncestor`."""

    if node is None:
        return 0

    if maxAncestor is not None and minAncestor is not None:
        # Compute maximum ancestor difference
        # for current node w.r.t. its ancestors
        currDiff = max(abs(node.val - maxAncestor),
                       abs(node.val - minAncestor))
    else:
        currDiff = 0
    
    # Update (max|min) ancestors for children
    if maxAncestor is None or node.val > maxAncestor:
        maxAncestor = node.val
    
    if minAncestor is None or node.val < minAncestor:
        minAncestor = node.val
    
    maxDiffLeftChild = maxAncestorDiff(node.left,
                                       maxAncestor,
                                       minAncestor)
    maxDiffRightChild = maxAncestorDiff(node.right,
                                        maxAncestor,
                                        minAncestor)

    # Reduce maximum ancestor difference 
    # as found from children
    return max(currDiff, maxDiffLeftChild, maxDiffRightChild)
```

### Complexity
Let n be the number of nodes in the tree.

* O(n) time complexity, for visiting each node exactly once
* O(1) space complexity, if ignoring the recursion overhead