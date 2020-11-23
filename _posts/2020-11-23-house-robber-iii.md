---
title: House robber iii
date: 2020-11-23
shortname: house_robber_iii
leetcode: https://leetcode.com/problems/house-robber-iii
tags: [tree, monthly challenge, DFS]
---

## Problem

> The thief has found himself a new place for his thievery again.
> There is only one entrance to this area, called the "root".
> Besides the root, each house has one and only one parent house.
> After a tour, the smart thief realized that "all houses in this place forms a binary tree".
> It will automatically contact the police if two directly-linked houses were broken into on the same night.
> 
> Determine the maximum amount of money the thief can rob tonight without alerting the police.

## Some questions to ask

* Is the tree of houses 'sorted' according to value?

## Approach

Devise a recursive solution, given the recursive nature of trees.
Each node presents an optimisation decision -- to rob or to skip,
so we can embed this in the recursive solution, which will propagate the
optimal value up to the root.

We solve the problem in terms of a function that, given a `node`, returns
the maximum robbery amount for two cases: rob `node` or skip `node`.

By case analysis,

* By robbing `node`, we must skip `node.left` and `node.right`
* By skipping `node`, the maximum robbery amount is the maximum out of:
    * Robbing `node.left` and `node.right` (children)
    * Robbing `node.left` and skipping `node.right` (maybe grandchild is more valuable)
    * Robbing `node.right` and skipping `node.left` (as per above)
    * Skipping `node.left` and skipping `node.right` (maybe sum of grandchildren is more valuable)

```python
def amountIfRobOrSkip(node: Optional[TreeNode]) -> Tuple[int, int]:
    """Given the constraint of not robbing adjacent houses, return
    a tuple of:
    
    o max robbery amount from place rooted at 'node' that *includes* robbing 'node'
    o max robbery amount from place rooted at 'node' that *does not include*
      robbing 'node'."""

    if node is None:
        return 0, 0
    
    amountIfRobLeft, amountIfSkipLeft = amountIfRobOrSkip(node.left)
    amountIfRobRight, amountIfSkipRight = amountIfRobOrSkip(node.right)

    # If robbing 'node', must only rob the 'grandchildren' houses.
    amountIfRob = node.val + amountIfSkipLeft + amountIfSkipRight

    # Maximise from all combinations of skipping 'node' .
    amountIfSkip = max(amountIfRobLeft + amountIfRobRight,
                       amountIfRobLeft + amountIfSkipRight,
                       amountIfSkipLeft + amountIfRobRight,
                       amountIfSkipLeft + amountIfSkipRight)

    return amountIfRob, amountIfSkip

def rob(root: TreeNode) -> int:
    """Return maximum amount the thief can rob from town rooted at 'root'
    without alerting the police."""

    return max(amountIfRobOrSkip(root))
```

### Complexity
Let n be the number of nodes in the binary tree.

* O(n) time complexity, from traversing all nodes of the tree
* O(1) space complexity, ignoring recursive stack overhead
