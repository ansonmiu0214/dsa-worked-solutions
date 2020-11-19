---
title: Decode string
date: 2020-11-19
shortname: decode_string
leetcode: https://leetcode.com/problems/decode-string
tags: [monthly challenge, recursion]
---

## Problem

> Given an encoded string, return its decoded string.
> 
> The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.
> Note that `k` is guaranteed to be a positive integer.
> 
> You may assume that the input string is always valid;
> No extra white spaces, square brackets are well-formed, etc.
> 
> Furthermore, you may assume that the original data does not contain any digits 
> and that digits are only for those repeat numbers, `k`. 
> For example, there won't be input like `3a` or `2[4]`.

## Some questions to ask

* Is empty string valid input?

## Approach

Given that the encoded string is defined recursively, we can solve the problem with a recursive approach.

Assume we have a string `k[encoded_string]`. We define a function to decode the scope `encoded_string`,
given that the scope repeats `k` times. When we encounter this pattern inside `encoded_string`, we simply
make a recursive call to decode the inner scope. In order to know where to proceed next, the function should
also return the next index (of the string) to process, along with the decoded string of the inner scope.

To reuse this for the original input string `s` (which does not have to start with a number), we can interpret
`s` as `1[s]`, and invoke the same recursive function, passing `repeat = 1` -- here, we just set it as a default
value.

```python
def decodeString(s: str) -> str:
    """Return decoded string, given encoded string 's'."""
    
    def decodeScope(i: int = 0, repeat: int = 1):
        """Decode the encoding scope beginning at index 'i', given the
        enclosing number of 'repeat's. Returns a tuple of the next index
        to process along with the decoded string for this scope."""

        decoded = []
        while i < len(s):
            if s[i].isdigit():
                # Found 'k[encoded_string]'.
                #        ^
                # Parse numerical value for the repeat of the inner scope.
                nextRepeat = 0
                while s[i] != '[':
                    nextRepeat *= 10
                    nextRepeat += int(s[i])
                    i += 1
                
                # Found 'k[encoded_string]', parsed 'k' as 'nextRepeat'.
                #         ^
                # Inner scope begins at index 'i + 1'.
                i, innerDecoded = decodeScope(i + 1, nextRepeat)
                decoded += innerDecoded
            elif s[i] == ']':
                i += 1
                break
            else:
                decoded.append(s[i])
                i += 1

        return i, (decoded * repeat)

    _, decoded = decodeScope()
    return ''.join(decoded)
```

### Complexity
Let n be the length of the string.

* O(n) time complexity, from traversing the string
* O(n) space complexity, from storing the decoded result

### Other approaches

You can express the solution iteratively by explicitly keeping track of stacks for the `repeat` and `string`,
and pushing onto the respective stacks when you encounter a `[`, and popping the values off on a `]`.