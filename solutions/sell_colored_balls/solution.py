from typing import List

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