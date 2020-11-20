from typing import List

def minOperations(nums: List[int], x: int) -> int:
    """Return minimum operations to reduce 'x' to zero."""

    target = sum(nums) - x
    if target < 0:
        # 'x' is greater than sum of 'nums', impossible to reduce to 0.
        return -1

    n = len(nums)
    if target == 0:
        # 'x' is exactly the sum of 'nums', need to remove all elements.
        return n
    
    prefixSumAtIndex = {}
    runningSum = 0
    maxLength = 0
    for i, num in enumerate(nums):
        runningSum += num

        targetPrefixSum = runningSum - target
        if targetPrefixSum == 0:
            # Need exactly this prefix, plus one to convert 0-index to length.
            maxLength = max(maxLength, i + 1)
        else:
            j = prefixSumAtIndex.get(targetPrefixSum, None)
            if j is not None:
                maxLength = max(maxLength, i - j)

        prefixSumAtIndex[runningSum] = i

    return -1 if maxLength == 0 else (n - maxLength)