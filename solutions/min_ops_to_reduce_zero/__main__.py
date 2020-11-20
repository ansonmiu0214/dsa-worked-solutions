from .solution import minOperations
from ..utils import printer

print('Enter space-separated nums:', end=' ')
nums = list(map(int, input().strip().split(' ')))

print('Enter x:', end=' ')
x = int(input().strip())

operations = minOperations(nums, x)
if operations != -1:
    print(f'Need at least {printer.pluralise(operation=operations)} to reduce {x} to 0.')
else:
    print('Impossible')