from typing import List

def canReach(arr: List[int], start: int) -> bool:
    """Return true iff you can reach any index in 'arr' with value 0,
    starting from the specified 'start' index."""

    visited = set()
    leftBound = 0
    rightBound = len(arr) - 1

    def canReachViaDFS(curr: int) -> bool:
        """Apply DFS to check whether the zero value in 'arr' can
        be reached given the 'curr' index."""

        if arr[curr] == 0:
            # Found the target.
            return True
        
        visited.add(curr)

        left = curr - arr[curr]
        if left >= leftBound and left not in visited and canReachViaDFS(left):
            return True

        right = curr + arr[curr]
        if right <= rightBound and right not in visited and canReachViaDFS(right):
            return True

        visited.remove(curr)
        return False

    return canReachViaDFS(start)