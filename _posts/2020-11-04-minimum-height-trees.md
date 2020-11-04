---
title: Minimum height trees
date: 2020-11-04
shortname: minimum_height_trees
leetcode: https://leetcode.com/problems/minimum-height-trees
tags: [graph, BFS, tree]
---

## Problem

> Given a tree of n nodes labelled from `0` to `n - 1`,
> and an array of `n - 1` edges where `edges[i] = [ai, bi]` indicates that there is an undirected edge
> between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root. 
> When you select a node `x` as the root, the result tree has height `h`. 
> Among all possible rooted trees, those with minimum height (i.e. `min(h)`)  are called **minimum height trees** (MHTs).
> 
> Return a list of all MHTs' root labels. You can return the answer in any order.
> 
> The **height** of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## Some questions to ask
* Are there parallel edges?

## Approach
Find the _diameter_ of the tree, and the MHTs' root labels can be derived from
the midpoint of the diameter.

The diameter of a tree is the distance between the two nodes furthest away from each other.
We can take an arbitrary node (`start`) and apply breadth-first search (BFS) to find the furthest
node from (`start`) -- let's denote this as `first`.
Then we run BFS again to find the furthest node from `first` -- let's denote this as `second`.

The path from `second` to `first` defines the diameter, and we can take the midpoint
of the path as the root of the MHT.

```python
def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """Return list of node indices which can be the root of a min-height tree."""

    adjacencyMatrix = defaultdict(list)
    for x, y in edges:
        adjacencyMatrix[x].append(y)
        adjacencyMatrix[y].append(x)
    
    parentOf = [-1 for _ in range(n)]

    def furthestNodeFrom(start: int, *, computeParent: bool):
        """Return node furthest from `start` using BFS (breadth-first search)
         Optionally populates the outer `parentOf` mapping to allow for backtracking."""

        furthestNode = None
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            furthestNode = node
            visited.add(node)

            for neighbour in adjacencyMatrix[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    if computeParent:
                        parentOf[neighbour] = node

        return furthestNode

    # Compute diameter by finding the two nodes
    # furthest away from each other.
    firstNode = furthestNodeFrom(0, computeParent=False)
    secondNode = furthestNodeFrom(firstNode, computeParent=True)

    # Backtrack path from the two furthest nodes.
    path = []
    while secondNode != firstNode:
        path.append(secondNode)
        secondNode = parentOf[secondNode]
    path.append(firstNode)

    diameter = len(path)
    midpoint = diameter // 2
    if diameter % 2 == 0:
        # Even diameter, so both `midpoints` are acceptable
        return [path[midpoint-1], path[midpoint]]
    else:
        # Odd diameter, so there is an unique answer
        return [path[midpoint]]
```

### Complexity
Let m be the number of edges.

* O(m + n) time complexity, from O(m) construction of adjacency matrix and O(n) from BFS
* O(m + n) space complexity, from O(m adjacency matrix and O(n) parent mapping