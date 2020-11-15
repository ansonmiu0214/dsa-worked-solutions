---
title: Sell diminishing valued colored balls
date: 2020-11-15
shortname: sell_colored_balls
leetcode: https://leetcode.com/problems/sell-diminishing-valued-colored-balls
tags: [greedy]
---

## Problem

> You have an `inventory` of different colored balls,
> and there is a customer that wants `orders` balls of any color.
> 
> The customer weirdly values the colored balls.
> Each colored ball's value is the number of balls of that color you currently have in your inventory. 
> For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball.
> After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 
> (i.e., the value of the balls decreases as you sell more to the customer).
> 
> You are given an integer array, `inventory`,
> where `inventory[i]` represents the number of balls of the `i`th color that you initially own.
> You are also given an integer `orders`,
> which represents the total number of balls that the customer wants.
> You can sell the balls in any order.
> 
> Return the maximum total value that you can attain after selling `orders` colored balls.
> As the answer may be too large, return it modulo `10^9 + 7`.

## Some questions to ask

* Is the inventory list of balls sorted by frequency?
* What to return if there are not enough balls in `inventory` to satisfy `order`?

## Approach

Take a greedy approach.

Start with the highest valued ball, and sell it until its value diminishes to the
second-highest valued ball. If you had `a` of the former (valued at `a`) and 
`b` of the latter (valued at `b`), you will now have `a+b` valued at `b`, and this
will use up `a(a-b)` orders. 

Now, `b` is the highest valued ball. 
Continue with the above until the orders have been exhausted.

See inline comments below for more details.

```python
def rangeSum(*, lowIncl, highIncl):
    """Compute sum(range(lowIncl, highIncl + 1))."""

    gap = highIncl - lowIncl + 1
    return (lowIncl + highIncl) * gap // 2

def maxProfit(inventory: List[int], orders: int) -> int:
    """Return maximum total value attainable after selling 'orders'
    colored balls, modulo 10^9 + 7."""

    numBalls = len(inventory)
    if numBalls == 0:
        return 0
    
    inventory.sort()
    profit = 0

    # Keep track of current selling price.
    currMaxVal = inventory[-1]
    for i in reversed(range(numBalls)):
        nextMaxVal = inventory[i-1] if i > 0 else 0

        currMaxCount = numBalls - i

        priceGap = currMaxVal - nextMaxVal

        # Number of orders covered by selling 'currMaxCount' balls
        # priced at 'currMaxVal' to diminish to 'nextMaxVal'.
        numOrders = priceGap * currMaxCount

        if numOrders < orders:
            # Perform 'numOrders', so 'currMaxCount' balls will
            # end up being valued at 'nextMaxVal'.

            avgPrice = rangeSum(lowIncl=nextMaxVal + 1, highIncl=currMaxVal)
            profit += (avgPrice * currMaxCount)
            orders -= numOrders
            currMaxVal = nextMaxVal
        else:
            # Sell as much as possible up to a minPrice > nextMaxVal.
            # Sell the leftovers (if any) at minPrice.

            priceGap, leftovers = divmod(orders, currMaxCount)

            priceGap = orders // currMaxCount
            numOrders = priceGap * currMaxCount
            minPrice = currMaxVal - priceGap

            avgPrice = rangeSum(lowIncl=minPrice + 1, highIncl=currMaxVal)
            profit += (avgPrice * currMaxCount) + (leftovers * minPrice)

            break

    modulo = 10 ** 9 + 7
    return profit % modulo
```
### Complexity
Let n be the number of balls in `inventory`.

* O(n log(n)) time complexity, from sorting the list.
* O(1) space complexity, by sorting in-place.