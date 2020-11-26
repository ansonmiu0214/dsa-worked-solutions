from .solution import longestSubstring
from ..utils import io

print('Enter string:', end=' ')
s = io.get(str)

print('Enter k:', end=' ')
k = io.get(int)

length = longestSubstring(s, k)
print(f'Longest substring matching criteria has length {length}')