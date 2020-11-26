from math import ceil
from .solution import smallestDivisor
from ..utils import io

print('Enter space-separated nums:', end=' ')
nums = io.get_list(int)

print('Threshold:', end=' ')
threshold = io.get(int)

divisor = smallestDivisor(nums, threshold)
print(f'Smallest divisor is {divisor}, '
      f'which yields sum of {sum(ceil(num / divisor) for num in nums)}')