---
title: Find the smallest divisor given a threshold
date: 2020-11-06
shortname: smallest_divisor_given_threshold
leetcode: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
tags: [binary search]
---

## Problem

> Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer divisor
> and divide all the array by it and sum the result of the division.
> Find the __smallest__ divisor such that the result mentioned above is less than or equal to `threshold`.
> 
> Each result of division is rounded to the nearest integer greater than or equal to that element.
> (For example: 7/3 = 3 and 10/2 = 5).

## Some questions to ask

* What to return if there isn't a valid divisor?
* Is empty array valid input?

## Approach

Smallest 'useful' divisor is 1, largest 'useful' divisor is the maximum value in the array.

Find the smallest divisor that satisfies the constraint using binary search, starting with the
range `[1, x]` where `x = max(nums)`.

```python
def smallestDivisor(nums: List[int], threshold: int) -> int:
    """Return smallest divisor such that sum of `nums` normalised
    with respect to the divisor is at most `threshold`."""
    
    lo = 1
    hi = max(nums)

    while lo < hi:
        mid = floor((lo + hi) / 2)
        normalisedSum = sum(ceil(num / mid) for num in nums)

        if normalisedSum <= threshold:
            # Can try smaller threshold, but keep `mid` as candidate
            hi = mid
        else:
            # Sum too large, need bigger divisor
            lo = mid + 1

    return lo
```

### Complexity
Let x be the maximum value in `nums`.

* O(log(x)) time complexity, from binary search
* O(1) space complexity
