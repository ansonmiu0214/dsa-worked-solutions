from .solution import longestMountain

print('Enter space-separated numbers:', end=' ')
arr = list(map(int, input().strip().split(' ')))

length = longestMountain(arr)
print(f'Longest mountain of length {length}')