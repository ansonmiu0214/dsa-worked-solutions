from .solution import maxProfit

print('Enter space-separated numbers for inventory:', end=' ')
inventory = list(map(int, input().strip().split(' ')))

print('Enter number of orders:', end=' ')
orders = int(input().strip())

profit = maxProfit(inventory, orders)
print(f'Max profit attainable: {profit}')