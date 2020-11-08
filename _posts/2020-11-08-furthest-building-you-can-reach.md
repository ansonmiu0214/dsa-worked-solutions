---
title: Furthest building you can reach
date: 2020-11-08
shortname: furthest_building
leetcode: https://leetcode.com/problems/furthest-building-you-can-reach
tags: [greedy]
---

## Problem

> You are given an integer array heights representing the heights of buildings, some bricks,
> and some ladders.
> 
> You start your journey from building 0 and move to the next building 
> by possibly using bricks or ladders.
>
> While moving from building `i` to building `i+1` (0-indexed),
> 
> * If the current building's height is greater than or equal to the next building's height,
>   you do not need a ladder or bricks.
> * If the current building's height is less than the next building's height, you can either use one
>   ladder or (`h[i+1] - h[i]`) bricks.
>
> Return the furthest building index (0-indexed) you can reach
> if you use the given ladders and bricks optimally.

## Approach

Since ladders can cover any height delta, the greedy approach is to use ladders for the
largest height differences, and try to exhaust the bricks on the shortest height differences.

We keep track of the positive height differences (that require either ladder or bricks)
in a min-heap. The idea is these represent the gaps we bridge using a ladder.

Once we bridge more such gaps than we have ladders, we can pop the heap to get
the shortest height gap we've encountered so far, and try to cover this gap using the
available bricks.

When we run out of bricks, we have reached the furthest building possible.

```python
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
```

### Complexity

Let n be the number of buildings, and L be the number of ladders.

* O(n log(L)) time complexity, as min-heap insertion takes logarithmic time, and the heap size is bounded by L
* O(L) space complexity, used by the min-heap

### Other approaches

You could formulate a dynamic programming solution, briefly sketched out below:

* `furthest(i, numBricks, numLadders)` := furthest building reached, when starting on building `i`
  with `numBricks` and `numLadders` remaining.

* `furthest(i, numBricks, numLadders)` = case analysis of below:
    * `heights[i+1] <= heights[i]` ->
        * `furthest(i + 1, numBricks, numLadders)`
    * `heights[i+1] > heights[i]` -> max of the below:
        * `furthest(i + 1, numBricks - (heights[i+1] - heights[i]), numLadders)`
        * `furthest(i + 1, numBricks, numLadders - 1)`
* Base cases:
    * `numBricks < 0` or `numLadders < 0` ->
        * Can't reach bldg `i`; return `i-1`
    * `i == len(heights) - 1` ->
        * Reached the end, return `i`

But memoising this will still be less efficient than the greedy approach.