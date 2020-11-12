from .solution import maximalNetworkRank

print('Enter number of nodes:', end=' ')
n = int(input().strip())

print('Enter roads, e.g. 0,1 1,2 0,3 1,3:', end=' ')
roads = [[int(city) for city in road.split(',')]
         for road in input().strip().split(' ')]

rank = maximalNetworkRank(n, roads)
print(f'Maximal network rank: {rank}')