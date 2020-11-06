from math import ceil, floor
from typing import List

def smallestDivisor(nums: List[int], threshold: int) -> int:
    """Return smallest divisor such that sum of `nums` normalised
    with respect to the divisor is at most `threshold`."""
    
    lo = 1
    hi = max(nums)

    while lo < hi:
        mid = floor((lo + hi) / 2)
        normalisedSum = sum(ceil(num / mid) for num in nums)

        if normalisedSum <= threshold:
            # Can try smaller threshold, but keep `mid` as candidate
            hi = mid
        else:
            # Sum too large, need bigger divisor
            lo = mid + 1

    return lo