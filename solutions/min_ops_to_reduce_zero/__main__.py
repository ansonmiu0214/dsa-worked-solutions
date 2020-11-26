from .solution import minOperations
from ..utils import io, printer

print('Enter space-separated nums:', end=' ')
nums = io.get_list(int)

print('Enter x:', end=' ')
x = io.get(int)

operations = minOperations(nums, x)
if operations != -1:
    print(f'Need at least {printer.pluralise(operation=operations)} to reduce {x} to 0.')
else:
    print('Impossible')