from math import ceil

from .solution import smallestDivisor

print('Enter space-separated nums:', end=' ')
nums = list(map(int, input().strip().split(' ')))

print('Threshold:', end=' ')
threshold = int(input().strip())

divisor = smallestDivisor(nums, threshold)
print(f'Smallest divisor is {divisor}, '
      f'which yields sum of {sum(ceil(num / divisor) for num in nums)}')