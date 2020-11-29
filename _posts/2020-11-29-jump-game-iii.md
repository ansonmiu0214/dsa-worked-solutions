---
title: Jump game iii
date: 2020-11-29
shortname: jump_game_iii
leetcode: https://leetcode.com/problems/jump-game-iii
tags: [DFS, monthly challenge]
---

## Problem

> Given an array of non-negative integers `arr`,
> you are initially positioned at `start` index of the array.
> When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`,
> check if you can reach to any index with value `0`.
> 
> Notice that you can not jump outside of the array at any time.

## Some questions to ask

* Is there guaranteed to be a 0 in `arr`?

## Approach

Apply depth-first search from the start index to explore the possible jumps,
avoiding loops by keeping a `visited` set of the encountered array indices.

```python
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

        return False

    return canReachViaDFS(start)
```

### Complexity

Let n be the length of `arr`.

* O(n) time complexity, from traversing each index at most once
* O(n) space complexity, from the `visited` set and the recursion overhead