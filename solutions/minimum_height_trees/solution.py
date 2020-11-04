from collections import defaultdict, deque
from typing import List

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """Return list of node indices which can be the root of a min-height tree."""

    adjacencyMatrix = defaultdict(list)
    for x, y in edges:
        adjacencyMatrix[x].append(y)
        adjacencyMatrix[y].append(x)
    
    parentOf = [-1 for _ in range(n)]

    def furthestNodeFrom(start: int, *, computeParent: bool):
        """Return node furthest from `start`. Optionally populates
        the outer `parentOf` mapping to allow for backtracking."""

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