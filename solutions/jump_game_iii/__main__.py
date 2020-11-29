from .solution import canReach
from ..utils import io

print('Enter space-separated numbers:', end=' ')
nums = io.get_list(int)

print('Can Reach' if canReach(nums) else 'Can Not Reach')