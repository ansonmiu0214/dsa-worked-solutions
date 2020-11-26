from .solution import findMinHeightTrees
from ..utils import io

print('Enter number of nodes:', end=' ')
n = io.get(int)

print('Enter space-separated edges (e.g. 1,2 1,0):', end=' ')
edges = [[int(node) for node in edge.split(',')] for edge in io.get_list(str)]

roots = findMinHeightTrees(n, edges)
print(f'Min height tree(s) are rooted at: {roots}')