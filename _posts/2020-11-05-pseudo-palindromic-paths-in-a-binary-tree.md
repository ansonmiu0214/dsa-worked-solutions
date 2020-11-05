---
title: Pseudo palindromic paths in a binary tree
date: 2020-11-05
shortname: pseudo_palindromic_path_in_binary_tree
leetcode: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree
tags: [tree, DFS]
---

## Problem

> Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic 
> if at least one permutation of the node values in the path is a palindrome.
> 
> Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

## Some questions to ask

* Empty tree allowed?

## Approach
Break down what it means to be a pseudo-palindromic path:
* For even-length paths, all values along the path must have even-parity frequency.
* For odd-length paths, exactly one value along the path must have odd-parity frequency (to be the middle), and all other values must have even-parity frequency.

The idea is to apply depth-first search (DFS) to explore all root-to-leaf paths,
and keep track of the values along the path, and conclude whether we found a
pseudo-palindromic path when we reach each leaf.

Because we are only concerned with the parity of the frequency of each visited value,
we don't need to keep a counter -- instead, we can use a set to keep track of the
odd-parity nodes: when we visit a node, if its value is not in the set, we add it in;
otherwise, we remove it from the set.

Using this interpretation with respect to the definition of pseudo-palindromic paths:
* For even-length paths, the set should be empty
* For odd-length paths, the set should be a singleton (of the value that will be the midpoint)

```python
def pseudoPalindromicPaths (root: TreeNode) -> int:
    """Return number of pseudo-palindromic paths in tree rooted at `root`."""

    nodesWithOddOccurrences = set()

    def flip(val: int):
        """Flip membership of `val` in `nodesWithOddOccurrences`."""
        if val in nodesWithOddOccurrences:
            nodesWithOddOccurrences.remove(val)
        else:
            nodesWithOddOccurrences.add(val)

    def countPathsFromDFS(node: TreeNode, pathSoFar: int = 0):
        if node is None:
            return 0
        
        # Increment count of `node.val` in "visited"
        flip(node.val)
        pathSoFar += 1
        if node.left is None and node.right is None:
            # For even-length paths, all values must have even-parity occurrences to be palindrome.
            # For odd-length paths, exactly one value must have odd-parity occurrence.
            count = int(pathSoFar % 2 == len(nodesWithOddOccurrences))
        else:
            count = countPathsFromDFS(node.left, pathSoFar) + countPathsFromDFS(node.right, pathSoFar)
        
        # Decrement count of `node.val` in "visited"
        flip(node.val)
        return count
    
    return countPathsFromDFS(root)
```

### Complexity
Let the tree have `n` nodes.

* O(n) time complexity, as each node is visited exactly once.
* O(log(n)) space complexity, as the `nodesWithOddOccurrences` set can grow to be at most the height of the tree, if a path is defined by strictly unique values.

