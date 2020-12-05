from .solution import canPlaceFlowers
from ..utils import io

print('Enter space-separated flower bed:', end=' ')
flowerBed = io.get_list(int)

assert all(0 <= entry <= 1 for entry in flowerBed)

print('Enter n:', end=' ')
n = io.get(int)

canPlace = canPlaceFlowers(flowerBed, n)
print('Can Place' if canPlace else 'Cannot Place')