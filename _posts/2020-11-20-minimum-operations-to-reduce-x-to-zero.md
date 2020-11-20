---
title: Minimum operations to reduce x to zero
date: 2020-11-20
shortname: min_ops_to_reduce_zero
leetcode: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero
tags: [array]
---

## Problem

> You are given an integer array `nums` and an integer `x`.
> In one operation, you can either remove the leftmost 
> or the rightmost element from the array nums 
> and subtract its value from `x`. 
> Note that this modifies the array for future operations.
> 
> Return the minimum number of operations to reduce `x` to exactly 0 
> if it's possible, otherwise, return -1.

## Some questions to ask

* Is the array sorted?
* Can `x` already be 0?

## Approach

Let the `num` array be the concatenation of `left`, `rest` and `right` subarrays.

The goal is to find `left` and `right` such that `sum(left + right) == x` and `len(left) + len(right)` is __minimised__.

This is the equivalent to finding `rest` such that `sum(rest) == sum(num) - x` and `len(rest)` is __maximised__.

We can find the longest subarray sum equal to `sum(num) - x` through computing prefix sums, i.e. finding `i`, `j`, such that `j - i` is maximised and `sum[i..j] == sum(num) - x`, where this range sum can be derived from precomputed prefix sums `prefixSum[i] - prefixSum[j]`.

```python

```

### Complexity
Let n be the length of `nums`.

* O(n) time complexity, from iterating through the array
* O(n) space complexity, from storing the prefix sums