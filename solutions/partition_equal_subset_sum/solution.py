from typing import List

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