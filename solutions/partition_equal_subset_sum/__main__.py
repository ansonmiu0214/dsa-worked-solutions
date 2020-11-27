from .solution import canPartition
from ..utils import io

print('Enter space-separated numbers:', end=' ')
nums = io.get_list(int)

print('Can Partition' if canPartition(nums) else 'Cannot Partition')