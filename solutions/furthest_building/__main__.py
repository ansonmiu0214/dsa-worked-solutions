from .solution import furthestBuilding

print('Enter heights, space-separated:', end=' ')
heights = list(map(int, input().strip().split(' ')))

print('Enter number of bricks and number of ladders, space-separated:', end=' ')
[bricks, ladders] = list(map(int, input().strip().split(' ')))

furthest = furthestBuilding(heights, bricks, ladders)
print(f'Furthest reachable building: #{furthest}')