---
title: Numbers at most n given digit set
date: 2020-11-21
shortname: numbers_at_most_n_given_digits
leetcode: https://leetcode.com/problems/numbers-at-most-n-given-digit-set
tags: [math, monthly challenge]
---

## Problem

> Given an array of `digits`, you can write numbers 
> using each `digits[i]` as many times as we want.  
> For example, if `digits = ['1','3','5']`, we may write numbers 
> such as `'13'`, `'551'`, and `'1351315'`.
> 
> Return the number of positive integers that can be generated 
> that are less than or equal to a given integer `n`.

## Some questions to ask

* What if `digits` is empty?
* Will `digits` contain duplicates?
* Does `digits` include `0`?
* Is `digits` sorted?

## Approach

Let `n` be a `x`-digit number. Assume you have `y` digits in your `digits` set.
Without inspection, you can use all permutations of `digits` to write numbers up to `x-1` digits.

You can write `y ** i` possible numbers for an `i`-digit number, so for numbers
up to `x-1` digits, you can write `(y ** 1) + (y ** 2 ) + ... + (y ** (x - 1))` numbers. This can be computed by the geometric series (first term `y`, common ratio `y`). The special case of `y=1` (where there is one digit in your `digits` set), where it reduces to a arithmetic sequence (with difference `y=1`).

The second half of the problem is to compute how many `x`-digit numbers can be
generated (from the `digits` set) that are less than or equal to `n`.
For each target digit `t` in `n`, derive the number of compatible digits from `digits`, i.e. how many digits `s` in `digits` are less than or equal to `t`.
Then we can proceed as follow, using `digits=[1,3,5,7], n=350` as an example:

1. Consider the first digit. We have 2 compatible candidates (`1,3`), one of which equals the target digit `3`. This means we can take `1` and any permutation of digits for the remaining 2 digits (which is `4*4=16`) to construct a valid number -- `1 * (4*4) = 16` possible ways.

    * i.e. `1xx` and we can fill the `x` with any of the digits in `digits`.

    * If none of the candidates equal the target digit, we can stop here, because we do not need to inspect the later digits since it is guaranteed that the permutation we calculated here covers the rest of the cases.

2. Because the digits match, we need to consider the next digit to filter down the number of matches. Here, we have 3 compatible candidates (`1,3,5`), again one of which equals the target digit `5`. So we take `2` and any permutation of digits for the remaining 1 digit to construct a valid number -- `2 * 4 = 8` possible ways.

3. For the last digit, we do not have a compatible candidate, so we add 0 to the total.

```python
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
```

### Complexity
Let `n` be a `x`-digit number. Assume you have `y` digits in your `digits` set.

* O(x + xy) time complexity, from:
    * iterating through the `x`-digit number to construct the target digits;
    * finding the candidates out of the `y`-sized digit set for
each of the `x` digits in the target number;

* O(x) space complexity, from:
    * storing the target digits;
    * storing the `allPossibilities` suffix product array;
