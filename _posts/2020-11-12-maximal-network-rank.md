---
title: Maximal network rank
date: 2020-11-12
shortname: maximal_network_rank
leetcode: https://leetcode.com/problems/maximal-network-rank
tags: [graph]
---

## Problem

> There is an infrastructure of `n` cities with some number of roads connecting these cities.
> Each `roads[i] = [ai, bi]` indicates that there is a bidirectional road between cities `ai` and `bi`.
> 
> The network rank of two different cities is defined as the total number of directly connected roads to either city.
> If a road is directly connected to both cities, it is only counted once.
> 
> The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
> 
> Given the integer `n` and the array `roads`, return the maximal network rank of the entire infrastructure.

## Some questions to ask

* Any parallel arcs in the graph?
* Is the graph connected?

## Approach

Compute the network rank between all pairs of nodes and return the maximum.

The network rank between a pair of nodes `(x, y)` is the sum of all their unique arcs.
This can be computed from the adjacency matrix, subtracting `matrix[x][y]` to
not double-count the shared arc.

```python
def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    """Return maximal network rank of graph of 'n' nodes
    with arcs defined by 'roads'."""

    arcs = [0] * n
    adjacencyMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for x, y in roads:
        arcs[x] += 1
        arcs[y] += 1
        adjacencyMatrix[x][y] = adjacencyMatrix[y][x] = 1

    # Network rank of `firstCity` and `secondCity` is the number
    # of arcs of both nodes, but minus the one connecting them
    # together (if any) as it is double counted.

    networkRanks = [
        numArcsFirst + numArcsSecond - adjacencyMatrix[firstCity][secondCity]
        for firstCity, numArcsFirst in enumerate(arcs)
        for secondCity, numArcsSecond in enumerate(arcs)
        if firstCity < secondCity
    ]

    return sorted(networkRanks)[-1]
```

### Complexity
As the number of roads is bounded by n(n-1) / 2, i.e. n^2, 

* O(n^2) time complexity, from constructing the adjacency matrix and the nested for-loop
  to compute network rank between all pairs of nodes
* O(n^2) space complexity, for the adjacency matrix
