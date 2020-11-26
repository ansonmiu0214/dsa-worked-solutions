from .solution import getSmallestString
from ..utils import io

print('Enter space-separated positive integers for "n" and "k":', end=' ')
n, k = io.get_list(int)

assert 1 <= n <= 10**5, f'"{n}" not between 1 and 10^5, inclusive'
assert n <= k <= 26*n, f'"{k}" not between "n" and "26*n", inclusive'

smallestString = getSmallestString(n, k)
print(f'Smallest string of length {n} and value {k}: {smallestString}')