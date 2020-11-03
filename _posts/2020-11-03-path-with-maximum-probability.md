---
title: Path with maximum probability
date: 2020-11-03
shortname: path_with_maximum_probability
leetcode: https://leetcode.com/problems/path-with-maximum-probability
tags: [graph, shortest path]
---

## Problem
You are given an undirected weighted graph of `n `nodes (0-indexed),
represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the 
nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`,
find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

## Some questions to ask
* Directed or undirected graph?
* Any parallel arcs?
* Guaranteed to have a path between `start` and `end`?

## Approach
Implement Dijkstra's algorithm for finding the shortest path between nodes,
but adapt the metric of "shortest path" to look for "maximum probability" instead.

Basic idea:
* Begin at `start` node
* Define its neighbours (and their probabilities) as `fringe`
* While `fringe` is not empty:
    * Pick the node in `fringe` with max probability from `start`
    * Either:
        * The node is `end`, which solves the problem; or
        * The node is not `end`, so
            * We expand `fringe` with the neighbours of the current node.
            * For each neighbour:
                * If prob(`start`->`node`->`neighbour`) > prob(`start`->`neighbour`), we use the larger probability in the fringe.
* If `fringe` is empty, that means `end` cannot be reached from start.

```python3
def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    """Return maximum probability from node `start` to node `end`."""

    probFromStart = [int(node == start) for node in range(n)]
    
    # Keep mapping from node to list of neighbours and path probabilities
    neighbours = defaultdict(list)
    for (src, dst), prob in zip(edges, succProb):
        neighbours[src].append((dst, prob))
        neighbours[dst].append((src, prob))
    
    visited = set()

    # Keep priority queue of nodes, with the priority being the
    # *negated* probability from start node. We negate because
    # Python's heap data structure implements a minheap.
    fringe = [(-1, start)]
    while fringe:
        negProbAcc, node = heapq.heappop(fringe)
        probToNode = -negProbAcc
        if node == end:
            return probToNode
        
        visited.add(node)
        for neighbour, nodeToNeighbour in neighbours[node]:
            if neighbour in visited or nodeToNeighbour == 0:
                continue

            viaNeighbour = probToNode * nodeToNeighbour
            if viaNeighbour > probFromStart[neighbour]:
                # More probable path found
                probFromStart[neighbour] = viaNeighbour
                heapq.heappush(fringe, (-viaNeighbour, neighbour))

    # No path found
    return 0
```

### Complexity
Let the number of edges be E.

* O((n + E)log(n)) time complexity, by implementing Dijkstra's algorithm with (min-heap) priority queue
* O(n + E) space complexity, for keeping track of `probFromStart`, `visited` and `neighbours`
