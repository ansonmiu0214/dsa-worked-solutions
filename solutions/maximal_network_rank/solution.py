from typing import List

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