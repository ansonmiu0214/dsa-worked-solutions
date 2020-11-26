---
title: Longest substring with at least k repeating characters
date: 2020-11-26
shortname: longest_substring_k_repeating
leetcode: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
tags: [string, monthly challenge]
---

## Problem

> Given a string `s` and an integer `k`,
> return the length of the longest substring of `s`
> such that the frequency of each character in this substring is at least `k`.

## Some questions to ask

* What is the alphabet of `s`?
* Is the 'frequency of each character' case sensitive?

## Approach

A candidate substring must have each unique character be repeated (at least) `k` times.

We can iterate over the possible number of unique characters in the substring and solve the problem, keeping track of the longest substring found. The number of unique characters in the substring is upper-bounded by the number of unique characters in `s`, which can be found by collecting all characters of `s` into a set.

In each iteration, we take a sliding window approach: we expand the window when we do not encounter enough unique characters (or when we have the exact number of unique characters but want to maximise the length of the substring), and shrink the window when we have too much unique characters for this iteration.

```python
def longestSubstring(s: str, k: int) -> int:
    """Return the length of the longest substring in 's' such that the
    frequency of each character in this substring is at least 'k'."""

    if len(s) < k:
        # String shorter than k characters cannot possibly have a 
        # substring with characters repeated at least k times.
        return 0

    numUniqueChars = len(set(s))
    longestLength = 0

    for targetCount in range(1, numUniqueChars + 1):
        # Focus on substrings with 'targetCount' number of unique
        # characters that each repeat at least k times.

        counter = Counter()
        countUniqueChars = 0

        numCharsOccurKTimes = 0
        start = end = 0

        while end < len(s):

            if countUniqueChars <= targetCount:
                # Extend window to either find more unique chars, or
                # find a longer substring that matches the criteria.

                if counter[s[end]] == 0:
                    countUniqueChars += 1
                
                counter[s[end]] += 1

                if counter[s[end]] == k:
                    numCharsOccurKTimes += 1
                
                end += 1

            else:
                # Shrink window to reduce number of unique chars.

                if counter[s[start]] == k:
                    numCharsOccurKTimes -= 1
                
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    countUniqueChars -= 1
                
                start += 1

            if countUniqueChars == targetCount == numCharsOccurKTimes:
                # Found a candidate substring s[start:end] which has 'targetCount'
                # unique characters, each occurring at least k times.
                longestLength = max(longestLength, end  - start)

    return longestLength
```

### Complexity
Let n be the length of `s`, and assume `s` has m unique characters.

* O(mn) time complexity, from the nested loops over the range of (number of) unique characters and the input string.
    * Assuming the input is restricted to lower-case ASCII alphabets, m is upper-bounded by 26 (`len(ascii_lowercase)`), which means the time complexity is O(26n) = O(n), i.e. linear with respect to n.
* O(m) space complexity, for keeping track of the character frequency.
    * Again, assuming m is upper-bounded by 26, the space complexity is O(26) = O(1), i.e. constant.

### Other approaches

You could take a divide and conquer approach by scanning the string to find a violating character (i.e. one that occurs less than `k` times in `s`, which means it cannot be part of the substring), and recursively solve the problem in the substrings that do not contain this violating character.