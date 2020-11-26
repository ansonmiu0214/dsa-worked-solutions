from .solution import longestMountain
from ..utils import io

print('Enter space-separated numbers:', end=' ')
arr = io.get_list(int)

length = longestMountain(arr)
print(f'Longest mountain of length {length}')