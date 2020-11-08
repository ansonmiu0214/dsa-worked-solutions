import heapq
from typing import List

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    """Return index of furthest building reachable."""
    
    heightDiffsForLadder = []
    
    currHeight = None
    for nextBldg, nextHeight in enumerate(heights):
        if nextBldg == 0 or nextHeight <= currHeight:
            currHeight = nextHeight
            continue
        
        heightDiff = nextHeight - currHeight
        heapq.heappush(heightDiffsForLadder, heightDiff)
        if len(heightDiffsForLadder) > ladders:
            # Exhausted ladders, try replace shortest height-gap
            # with bricks instead.

            shortestDiff = heapq.heappop(heightDiffsForLadder)
            bricks -= shortestDiff
            
            if bricks < 0:
                # Ran out of bricks.
                return nextBldg - 1
    
        currHeight = nextHeight

    return nextBldg