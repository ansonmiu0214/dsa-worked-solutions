from collections import deque
from typing import List

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

        # Sliding window for 'nums' begin at index 'k-1', i.e. where
        # the window sees the first 'k' numbers.
        if i >= k - 1:
            maxWindow.append(nums[maxIdxs[0]])

    return maxWindow