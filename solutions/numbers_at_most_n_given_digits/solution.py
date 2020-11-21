from collections import deque
from typing import List

def geometricSeries(*, u_1: int, r: int, n: int) -> int:
    """Compute geometric series up to 'n', given initial value
    'u_1' and common ratio 'r'."""

    return (u_1 * n) if r == 1 else (u_1 * (u_1 ** n - 1) / (r - 1))

def atMostNGivenDigitSet(digits: List[int], n: int) -> int:
    """Return the number of positive integers that can be generated
    from 'digits' that are less than or equal to 'n'."""

    numDigits = len(digits)

    # Construct target digits
    targetDigits = deque()
    while n > 0:
        n, targetDigit = divmod(n, 10)
        targetDigits.appendleft(targetDigit)
    numTargetDigits = len(targetDigits)

    # First compute number of positive integers that have
    # ('numTargetDigits' - 1) digits.
    possibilities = geometricSeries(u_1=numDigits,
                                    r=numDigits,
                                    n=numTargetDigits - 1)

    # Precompute array 'allPossibilities' such that
    # 'allPossibilies[i]' := number of positive integers with 
    # 'numTargetDigits' - 'i' digits.
    allPossibilities = deque()
    product = 1
    for _ in range(numTargetDigits):
        product *= numDigits
        allPossibilities.appendleft(product)

    for i, targetDigit in enumerate(targetDigits):
        # Find candidates from 'digits' for 'i'th digit in target number.
        candidates = set(digit for digit in digits if digit <= targetDigit)
        numCandidates = len(candidates)

        if i + 1 == numTargetDigits:
            # Last digit, so take all candidates.
            possibilities += numCandidates
        elif targetDigit in candidates:
            # Only take 'numCandidates - 1' of all possibilities from this
            # index onwards; the remaining one depends on the candidates for
            # the next digit.
            possibilities += ((numCandidates - 1) * allPossibilities[i+1])
        else:
            # Any combination of digits for later digits will be guaranteed
            # to be less than 'n', so take all and return early.
            possibilities += (numCandidates * allPossibilities[i+1])
            break
    
    return possibilities