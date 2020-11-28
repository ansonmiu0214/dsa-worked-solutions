from .solution import maxSlidingWindow
from ..utils import io

print('Enter space-separated numbers:', end=' ')
nums = io.get_list(int)

print('Enter k:', end=' ')
k = io.get(int)

assert 1 <= k <= len(nums), f'1 <= {k} <= {len(nums)} not satisfied'

maxWindow = maxSlidingWindow(nums, k)
print('Max window:', maxWindow)