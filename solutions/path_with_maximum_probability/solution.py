from collections import defaultdict
import heapq
from typing import List

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