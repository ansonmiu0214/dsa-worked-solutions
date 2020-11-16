---
title: Longest mountain in array
date: 2020-11-16
shortname: longest_mountain_in_array
leetcode: https://leetcode.com/problems/longest-mountain-in-array
tags: [array]
---

## Problem

> Let's call any (contiguous) subarray `B` (of `A`) a mountain 
> if the following properties hold:
> 
> * `B.length >= 3`
> * There exists some `0 < i < B.length - 1` such that `B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]`
> 
> (Note that `B` could be any subarray of `A`, 
> including the entire array `A`.)
> 
> Given an array `A` of integers, 
> return the length of the longest mountain. 
> 
> Return `0` if there is no mountain.

## Approach

Iterate over the array, keeping track of the current slope, current mountain length, and longest mountain length.

Recognise the pattern that a mountain is found when you go up a slope then down. Extend the current mountain length for valid input that matches this pattern.

Otherwise, reset the current state.

```python
def longestMountain(arr: List[int]) -> int:
    """Return length of longest mountain in array."""

    UNKNOWN = 0
    UP = 1
    DOWN = 2

    longestLength = 0

    # Keep track of current mountain length, whether a mountain
    # is found at the current iteration, and the current direction.
    currLength = 0

    # We don't know the initial slope.
    direction = UNKNOWN

    first, *rest = arr
    prev = first

    for curr in rest:
        if direction == UNKNOWN:
            if prev < curr:
                # Both 'prev' and 'curr' contribute to upward slope.
                currLength = 2
                direction = UP

        elif direction == UP:
            if prev < curr:
                currLength += 1
            elif prev > curr:
                # 'curr' contributes to downward slope.
                currLength += 1
                direction = DOWN
            else:
                # Flat ground reached, so we reset the current state.
                direction = UNKNOWN
                currLength = 0

        else:
            if prev > curr:
                currLength += 1
            else:
                # Bottom of mountain reached, update global maximum.
                longestLength = max(longestLength, currLength)

                if prev < curr:
                    currLength = 2
                    direction = UP
                else:
                    currLength = 0
                    direction = UNKNOWN

        prev = curr

    # If we end with a downward slope, it is possible that the length
    # of the current mountain is the global maximum.
    return max(longestLength, currLength) if direction == DOWN else longestLength
```

### Complexity
Let n be the length of the array.

* O(n) time complexity, from iterating over the array
* O(1) space complexity, from keeping track of `longestLength`, `currLength` and `direction`
