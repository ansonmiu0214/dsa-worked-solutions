from solutions.utils.io import get_list
from .solution import maximalNetworkRank
from ..utils import io

print('Enter number of nodes:', end=' ')
n = io.get(int)

print('Enter roads, e.g. 0,1 1,2 0,3 1,3:', end=' ')
roads = [[int(city) for city in road.split(',')]
         for road in io.get_list(str)]

rank = maximalNetworkRank(n, roads)
print(f'Maximal network rank: {rank}')