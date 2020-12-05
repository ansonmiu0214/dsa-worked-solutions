---
title: Can place flowers
date: 2020-12-05
shortname: can_place_flowers
leetcode: https://leetcode.com/problems/can-place-flowers
tags: [greedy, monthly challenge, array]
---

## Problem

> You have a long `flowerbed` in which some of the plots are planted, and some are not.
> However, flowers cannot be planted in adjacent plots.
> 
> Given an integer array `flowerbed` containing `0`'s and `1`'s,
> where `0` means empty and `1` means not empty, and an integer `n`,
> return if `n` new flowers can be planted in the `flowerbed`
> without violating the no-adjacent-flowers rule.

## Some questions to ask

* What if the flower bed is empty, i.e. zero-length?
* Can we modify the input array?

## Approach

Assuming we cannot modify the input array,
we can compute the maximum number of new flowers that can be added to 
`flowerBed`, and check that `n` is bounded by this.

```python
def canPlaceFlowers(flowerBed: List[int], n: int) -> bool:
    """Return true iff 'n' new flowers can be added to the 'flowerBed'."""

    length = len(flowerBed)

    # Memoise results from 'maximumNewFlowers' function.
    cache = {}

    def maximumNewFlowers(index: int = 0):
        """Return maximum number of new flowers that can be placed in the
        'flowerBed', starting at the specified 'index'."""

        if index in cache:
            return cache[index]

        if index >= length:
            # Out of bounds.
            cache[index] = 0
        
        elif index + 1 == length:
            # Place flower here if current position is empty.
            cache[index] = 1 - flowerBed[index]

        elif flowerBed[index] == 1:
            # Current position is not empty.
            cache[index] = maximumNewFlowers(index + 2)

        elif flowerBed[index + 1] == 0:
            # Next position is empty -- place flower here.
            cache[index] = 1 + maximumNewFlowers(index + 2)

        else:
            # Next position is not empty.
            cache[index] = maximumNewFlowers(index + 1)

        return cache[index]

    return n <= maximumNewFlowers()
```

### Complexity

Let m be the length of `flowerBed`.

* O(m) time complexity, from memoisation
* O(m) space complexity, from memoisation

### Other approaches

If we *can* modify the input array, we can simply iterate
over `flowerBed` and toggle the entry to `1` if the empty slot can be
replaced by a flower. This ensures that future decisions are made based on
the new flowers added in the previous slots.

```python
def canPlaceFlowers(flowerBed: List[int], n: int) -> bool:
    length = len(flowerBed)
    newFlowers = 0
    for i, entry in enumerate(flowerBed):
        if entry == 1:
            continue

        if i > 0 and flowerBed[i-1] == 1:
            continue
    
        if i + 1 < length and flower[i+1] == 1:
            continue

        flowerBed[i] = 1
        newFlowers += 1

        if newFlowers == n:
            break

    return n <= newFlowers
```