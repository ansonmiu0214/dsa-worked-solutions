---
title: Partition equal subset sum
date: 2020-11-27
shortname: partition_equal_subset_sum
leetcode: https://leetcode.com/problems/partition-equal-subset-sum
tags: [monthly challenge, DFS, dynamic programming]
---

## Problem

> Given a non-empty array `nums` containing only positive integers,
> find if the array can be partitioned into two subsets
> such that the sum of elements in both subsets is equal.

## Some questions to ask

* Is the array sorted?

## Approach

To partition an _integer_ array into two equal-sum subsets rules out two situations:

* Singleton and empty arrays
* Arrays with odd-sum -- cannot achieve floating point sums in partitions comprised of integer values

This reduces the problem into, finding a subset of the array that sums up to the target sum of `sum(nums) / 2`.

Because the partition is a subset of the array rather than a subarray, a greedy approach of sorting + sliding window will not cover all cases.

We form a subset by considering each element of the array and deciding whether to select (to contribute to the target sum) or skip.
We apply DFS to cover all cases, and use a 2D array to cache results to avoid re-computing overlapping subproblems.

```python
def canPartition(nums: List[int]) -> bool:
    """Return true iff the specified 'nums' can be
    partitioned into two equal-sum subsets."""

    totalCount = len(nums)

    if totalCount < 2:
        # Cannot partition empty or singleton lists.
        return False

    targetSubsetSum, cannotPartition = divmod(sum(nums), 2)
    if cannotPartition:
        # Cannot partition 'nums' with odd sum into two equal-sum subsets.
        return False

    # Cache the results from DFS.
    cache = [[None for _ in range(targetSubsetSum + 1)]
             for _ in range(totalCount + 1)]
    
    def containsSum(startIndex: int, targetSum: int) -> bool:
        """Return true iff `nums[startIndex:]` contains a subsequence
        that sums to 'targetSum'."""

        if targetSum == 0:
            return True
        
        if startIndex == totalCount or targetSum < 0:
            return False

        if cache[startIndex][targetSum] is None:
            # Explore the two options: either select 'nums[startIndex]'
            # in subsequence, or skip this index.

            ifSelect = containsSum(startIndex + 1, targetSum - nums[startIndex])
            ifSkip = containsSum(startIndex + 1, targetSum)

            cache[startIndex][targetSum] = ifSelect or ifSkip

        return cache[startIndex][targetSum]

    return containsSum(0, targetSubsetSum)
```

### Complexity

Let n be the length of `nums`, and m be the sum of `nums`.

* O(nm) time complexity, inferred from the dimensions of `cache`
* O(nm) space complexity, inferred from the dimensions of `cache`

### Other approaches

You can fill the `cache` memoisation array bottom-up, with the same time and space complexity.
