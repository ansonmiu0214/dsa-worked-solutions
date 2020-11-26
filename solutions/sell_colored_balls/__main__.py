from .solution import maxProfit
from ..utils import io

print('Enter space-separated numbers for inventory:', end=' ')
inventory = io.get_list(int)

print('Enter number of orders:', end=' ')
orders = io.get(int)

profit = maxProfit(inventory, orders)
print(f'Max profit attainable: {profit}')