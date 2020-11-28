---
title: Sliding window maximum
date: 2020-11-28
shortname: sliding_window_maximum
leetcode: https://leetcode.com/problems/sliding-window-maximum
tags: [monthly challenge, array]
---

## Problem

> You are given an array of integers `nums`.
> There is a sliding window of size `k` which is moving from the very left of the array to the very right.
> You can only see the `k` numbers in the window.
> Each time the sliding window moves right by one position.
> 
> Return the _max sliding window_.

## Some questions to ask

* Is the array sorted?
* What if the sliding window is larger than the input array?

## Approach

Need a way to keep track of:

1. Candidates for the maximum in the window
2. Whether the candidates are in scope of the sliding window's current position

Assume we keep the maximum candidates in a list.
Point #1 means that the list is always in decreasing order.
For example, `[3,1,2]` won't be a valid candidate list, because `1` is not a maximum with `2` in scope.
Assume `[3,1]` was our candidate list: when we encounter `2`, the candidate list should be `[3,2]` instead;
this means that we pop elements off the list that are less than the current element, i.e. the elements that are
no longer candidates for the maximum, given that the new element is greater.

Point #2 means that we need to keep track of the indices of the maximum candidates,
so we know whether any of them becomes out of scope. Because the list is populated as we traverse the array,
we need to pop the head off the list when the head element is no longer in scope of the window.

This motivates the use of a queue. The queue will keep track of the _indices_ of the maximum candidates.
When we move the sliding window across the array, we will:

1. Pop off candidates from the front of the queue which are out of scope
2. Pop off candidates from the back of the queue which are smaller than the current element
3. Keep track of the current head of the queue, which represents the index of the maximum for the sliding window's current position

```python
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """Return the max sliding window of size 'k' on 'nums'."""

    maxWindow = []

    # Keep track of the indices of the 'max' candidates.
    # Elements are guaranteed to be in decreasing order.
    maxIdxs = deque([0])

    for i, num in enumerate(nums):

        leftBoundary = i - k
        while maxIdxs and maxIdxs[0] <= leftBoundary:
            # Discard any maximum values not in scope of the window.
            maxIdxs.popleft()

        while maxIdxs and num >= nums[maxIdxs[-1]]:
            # Discard any values smaller than 'num', as they won't be
            # considered 'max candidates since 'num' is larger and also
            # in the same window scope.
            maxIdxs.pop()

        maxIdxs.append(i)
        maxWindow.append(nums[maxIdxs[0]])

    # Sliding window for 'nums' begin at index 'k-1', i.e. where
    # the window sees the first 'k' numbers.
    return maxWindow[k-1:]
```

### Complexity

Let n be the length of `nums`.

* O(n) time complexity, as each element is pushed onto the queue exactly one and popped off at most once
* O(`k`) space complexity, as the size of `maxIdxs` is bounded by `k`