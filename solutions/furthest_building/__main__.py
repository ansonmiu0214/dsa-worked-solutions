from .solution import furthestBuilding
from ..utils import io

print('Enter heights, space-separated:', end=' ')
heights = io.get_list(int)

print('Enter number of bricks and number of ladders, space-separated:', end=' ')
[bricks, ladders] = io.get_list(int)

furthest = furthestBuilding(heights, bricks, ladders)
print(f'Furthest reachable building: #{furthest}')