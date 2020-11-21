---
title: Smallest string with a given numeric value
date: 2020-11-21
shortname: smallest_string_given_numeric_value
leetcode: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value
tags: [string, greedy]
---

## Problem

> The __numeric value__ of a lowercase character is defined as its position (1-indexed) in the alphabet, 
> so the numeric value of `a` is `1`, the numeric value of `b` is `2`, the numeric value of `c` is `3`, and so on.
> 
> The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. 
> For example, the numeric value of the string `"abe"` is equal to `1 + 2 + 5 = 8`.
> 
> You are given two integers `n` and `k`. 
> Return the lexicographically smallest string with length equal to `n` and numeric value equal to `k`.
> 
> Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, 
> either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

## Some questions to ask

* What if it is impossible to build such a string? E.g. `n=2` and `k=1`

## Approach

Take a greedy approach and build up to the optimal solution.

Start with a string with length `n` of all `a`s, so the starting value is `n` (i.e. `1 * n`). 

The leftover value to distribute across the characters is `k - n`.
To guarantee the lexicographically smallest string, distribute the leftover value from the least significant position, i.e. right-hand side. 

Each character's value can be at most 26, so if the leftover exceeds the capacity of each character, the excess is propagated over to the next (least) significant position.

```python
def getSmallestString(n: int, k: int) -> str:
    """Return lexiographically smamllest (lower-case) string with
    length equal to 'n' and numeric value equal to 'k'."""

    alphabetSize = len(ascii_lowercase)

    # Start with most optimal string (i.e. all 'a's) and
    # build up from the 'least significant character', i.e. RHS.
    optimalValues = [1] * n

    # Distribute leftover characters from least significant side.
    end = n - 1
    leftover = k - n
    
    while leftover > 0:
        # Value max out at 'alphabetSize', propagate rest to leftover.
        toAdd = min(alphabetSize - optimalValues[end], leftover)
        optimalValues[end] += toAdd
        leftover -= toAdd
        end -= 1

    # Require 'index - 1' to convert 1-index values to 0-index for list.
    return ''.join(ascii_lowercase[index - 1] 
                   for index in optimalValues)
```

### Complexity

* O(n) time complexity, from traversing the array of values representing a string of length n
* O(n) space complexity, from keeping track of the array of values