---
title: Minimum deletions to make string balanced
date: 2020-11-18
shortname: minimum_deletions_balance_string
leetcode: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced
tags: [greedy]
---

## Problem

> You are given a string `s` consisting only of characters `'a'` and `'b'​​​​`.
> 
> You can delete any number of characters in `s` to make `s` balanced. 
> s is balanced if there is no pair of indices `(i,j)`
> such that `i < j` and `s[i] = 'b'` and `s[j] = 'a'`.
> 
> Return the __minimum__ number of deletions needed to make `s` balanced.

## Approach

Take a greedy approach -- only need to delete a character if 'a' is seen after 'b'.

```python
def minimumDeletions(s: str) -> int:
    """Return minimum number of deletions to make 's' balanced, i.e. 
    no 'b' comes before 'a' in string consisting of just 'a's and 'b's."""

    deletions = 0
    countOfBs = 0
    for c in s:
        if c == 'a' and countOfBs > 0:
            # Only need to delete 'a violating character
            # if 'b' comes before an 'a'.
            countOfBs -= 1
            deletions += 1
        elif c == 'b':
            # Keep track of number of 'b's seen.
            countOfBs += 1
    return deletions
```

### Complexity
Let n be the length of the string.

* O(n) time complexity, from traversing the string
* O(1) space complexity, from keeping track of the result and counter for 'b's.