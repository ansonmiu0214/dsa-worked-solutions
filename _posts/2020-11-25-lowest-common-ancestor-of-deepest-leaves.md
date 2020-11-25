---
title: Lowest common ancestor of deepest leaves
date: 2020-11-25
shortname: lowest_common_ancestor_deepest_leaves
leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
tags: [tree, BFS]
---

## Problem

> Given the `root` of a binary tree, return the __lowest common ancestor__ of its deepest leaves.
> 
> Recall that:
> 
> * The node of a binary tree is a leaf if and only if it has no children
> * The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
> * The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

## Some questions to ask

* Does the tree have unique values?
* Is the tree sorted?
* Is the tree complete?

## Approach

Run BFS to find the deepest leaves and establish the parent relation for each node.

Iteratively reduce the collection of deepest leaves to the lowest common ancestor by
mapping each deepest leaf to its parent and collecting the parents in a set (to remove duplicates).

```python
def lcaDeepestLeaves(root: TreeNode) -> TreeNode:
    """Given the 'root' of a binary tree, return the 
    lowest common ancestor of its deepest leaves."""

    if not root.left and not root.right:
        # Base case, if the root is itself a leaf.
        return root

    deepestLeaves = []
    deepestLevel = 0

    parentOf = {}
    nodeOf = {}

    # Apply BFS and keep track of deepest leaves.
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()

        # Keep track of val -> node mapping, as we return a 'TreeNode'.
        nodeOf[node.val] = node
    
        if node.left or node.right:
            if node.left:
                parentOf[node.left.val] = node.val
                queue.append((node.left, level + 1))
            if node.right:
                parentOf[node.right.val] = node.val
                queue.append((node.right, level + 1))
        else:
            # Found possible deepest leaf candidate.
            # Update 'deepestLevel' if this node is deepest.

            if level > deepestLevel:
                deepestLevel = level
                deepestLeaves = []

            deepestLeaves.append(node.val)
    
    # Map deepest leaves to their parents until they share the same
    # parent -- the set will discard duplicate parents.
    lowestCommonAncestors = set(deepestLeaves)
    while len(lowestCommonAncestors) > 1:
        lowestCommonAncestors = set(parentOf[node]
                                    for node in lowestCommonAncestors)

    lowestCommonAncestor = next(iter(lowestCommonAncestors))
    return nodeOf[lowestCommonAncestor]
```

Note that we won't need the `nodeOf` mapping if `TreeNode` were hashable.

### Complexity
Let n be the number of nodes in the tree specified by `root`.

* O(n) time complexity, from traversing the tree
* O(n) space complexity, from keeping track of `nodeOf` and `parentOf`
